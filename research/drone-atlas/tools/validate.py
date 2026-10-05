#!/usr/bin/env python3
"""Offline integrity checks for the AER Drone Atlas; not source-truth validation."""
import csv,json,math,re
from pathlib import Path
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def check(condition,message):
 if not condition: errors.append(message)
def readcsv(name,key):
 with (ROOT/'data'/name).open(newline='',encoding='utf-8') as f:
  rows=list(csv.DictReader(f))
 ids=[r[key] for r in rows]
 check(len(ids)==len(set(ids)),f'{name}: duplicate ID')
 for r in rows: check(None not in r and all(v is not None for v in r.values()),f'{name}: malformed row')
 return rows
sources=readcsv('sources.csv','source_id'); source_ids={r['source_id'] for r in sources}
def refs(value,label):
 ids=value if isinstance(value,list) else value.split(';') if value else []
 for sid in ids: check(sid in source_ids,f'{label}: undefined source {sid}')
for s in sources:
 check(s['url'].startswith('https://'),f"{s['source_id']}: invalid URL")
 check(s['retrieval'] in {'full_text','search_excerpt','failed'},f"{s['source_id']}: invalid retrieval")
 check(s['access_date']=='2026-10-05',f"{s['source_id']}: review date drift")
 check(s['publication_date']=='unknown' or re.fullmatch(r'\d{4}(-\d{2})?(-\d{2})?',s['publication_date']),f"{s['source_id']}: invalid date")
data=json.loads((ROOT/'data/platforms.json').read_text()); platforms=data['platforms']
pids={p['platform_id'] for p in platforms}
check(len(pids)==len(platforms),'duplicate platform ID')
for p in platforms:
 refs(p['source_ids'],p['platform_id'])
 check(p['maturity'] in {'announced','prototype','demonstrated','commercial','operational'},f"{p['platform_id']}: invalid maturity")
 for k in ['payload_kg','endurance_s','speed_m_s']:
  check(p[k] is None or isinstance(p[k],(int,float)) and p[k]>=0,f"{p['platform_id']}: invalid {k}")
 if p['takeoff_mass_kg']:
  check(p['takeoff_mass_kg']['value']>0 and p['takeoff_mass_kg']['operator'] in {'=','<','<='},f"{p['platform_id']}: invalid mass")
obs=readcsv('observations.csv','observation_id')
units={'flight_time':'s','hover_time':'s','battery_energy':'J','link_range':'m','recommended_payload':'kg','cruise_speed':'m/s','electrical_power':'W','demonstrated_duration':'s'}
for o in obs:
 refs(o['source_ids'],o['observation_id'])
 check(o['platform_id'] in pids,f"{o['observation_id']}: invalid platform")
 check(o['metric'] in units and units.get(o['metric'])==o['unit'],f"{o['observation_id']}: invalid unit")
 try: check(math.isfinite(float(o['value'])) and float(o['value'])>=0,f"{o['observation_id']}: invalid value")
 except ValueError: errors.append(f"{o['observation_id']}: nonnumeric value")
 check(o['evidence'] in {'M','F','E','I','A','S'},f"{o['observation_id']}: evidence label")
for p in platforms:
 if p['endurance_s'] is not None:
  check(any(o['platform_id']==p['platform_id'] and o['metric']=='flight_time' and float(o['value'])==p['endurance_s'] for o in obs),f"{p['platform_id']}: missing matching endurance observation")
suppliers=readcsv('suppliers.csv','supplier_id')
for s in suppliers:
 refs(s['source_ids'],s['supplier_id'])
 if s['price']!='unknown':
  check(float(s['price'])>0 and all(s[k]!='unknown' for k in ['currency','market','price_date']),f"{s['supplier_id']}: price provenance missing")
coverage=readcsv('coverage.csv','coverage_id')
for c in coverage:
 refs(c['source_ids'],c['coverage_id'])
 check((ROOT/c['path']).is_file(),f"{c['coverage_id']}: missing path {c['path']}")
 check(c['depth'] in {'open','candidate','partial','deep'},f"{c['coverage_id']}: invalid depth")
 check(bool(c['remaining_gap']),f"{c['coverage_id']}: no gap declared")
media=readcsv('media.csv','media_id')
for m in media:
 refs(m['source_ids'],m['media_id'])
 check(bool(m['reuse_status']),f"{m['media_id']}: no rights status")
 if 'not_played' in m['inspection'] or 'failed' in m['inspection']:
  check(m['useful_timestamps']=='unknown',f"{m['media_id']}: uninspected timestamps")
def anchors(path):
 out=set()
 for heading in re.findall(r'^#{1,6}\s+(.+)$',path.read_text(),re.M):
  slug=re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-');out.add(slug)
 return out
nlinks=0
for path in ROOT.rglob('*.md'):
 for link in re.findall(r'\[[^\]]*\]\(([^\s]+?)\)',path.read_text()):
  if re.match(r'\w+://',link) or link.startswith('mailto:'): continue
  nlinks+=1
  target,_,anchor=unquote(link).partition('#');dest=(path.parent/target).resolve() if target else path
  check(dest.exists(),f'{path.relative_to(ROOT)}: broken link {link}')
  if anchor and dest.exists() and dest.suffix=='.md':check(anchor in anchors(dest),f'{path.relative_to(ROOT)}: missing anchor {link}')
area=4*math.pi*(.254/2)**2
power=9.81**1.5/math.sqrt(2*1.225*area)
check(abs(power-43.6)<.1,'hover example arithmetic')
check(67*86400+6*3600+52*60==5813520,'Zephyr time conversion')
check(abs(18.96/(34/60)-33.46)<.01,'Mini energy example')
check(.5*.01*60**2==18,'inertial drift example')
check(18.96*3600==68256,'battery J conversion')
if errors:
 print('\n'.join(errors));raise SystemExit(1)
print(f'PASS: {len(platforms)} platforms, {len(obs)} observations, {len(sources)} sources, {len(suppliers)} suppliers, {len(coverage)} coverage rows, {len(media)} media references; {nlinks} local links/anchors; example arithmetic.')
print('Limits: no remote URL, source-truth, stock, certification, flight or video validation.')
