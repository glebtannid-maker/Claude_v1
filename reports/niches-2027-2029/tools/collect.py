import json,glob,os,sys
base='/root/.claude/projects/-home-user-Claude-v1/c29411ef-8e32-52db-9f99-175754ba018c/subagents/workflows'
S='/tmp/claude-0/-home-user-Claude-v1/c29411ef-8e32-52db-9f99-175754ba018c/scratchpad'
def results():
    for j in sorted(glob.glob(base+'/*/journal.jsonl'), key=os.path.getmtime):
        for line in open(j):
            try: e=json.loads(line)
            except: continue
            if e.get('type')=='result' and isinstance(e.get('result'),dict):
                yield e['result']
what=sys.argv[1]
if what=='map':
    order=['gen_ai','motion_industry','adobe_platforms','agents_mcp','dooh_3d','consumer_apps','seo_utilities','ai_dev_economics']
    got={}
    for r in results():
        if 'scenarios' in r and 'domain_key' in r: got[r['domain_key']]=r  # later wins
    out=[got[k] for k in order if k in got]
    json.dump(out,open(S+'/data/market_map.json','w'),ensure_ascii=False,indent=1)
    print('map domains:',[d['domain_key'] for d in out])
elif what=='cards':
    got={}
    for r in results():
        if 'scores' in r and 'mvp' in r and 'id' in r: got[r['id']]=r
    json.dump(list(got.values()),open(S+'/data/cards.json','w'),ensure_ascii=False,indent=1)
    print('cards:',len(got))
elif what=='skeptic':
    got={}
    for r in results():
        if 'new_scores' in r and 'id' in r and 'verdict' in r: got[r['id']]=r
    json.dump(list(got.values()),open(S+'/data/skeptic.json','w'),ensure_ascii=False,indent=1)
    print('skeptic:',len(got))
elif what=='ideation':
    out=[r for r in results() if 'shortlist' in r and 'lens' in r]
    json.dump(out,open(S+'/data/ideation.json','w'),ensure_ascii=False,indent=1)
    print('lenses:',[r['lens'] for r in out])
