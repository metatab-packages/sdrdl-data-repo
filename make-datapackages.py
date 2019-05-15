
import json
from metapack import MetapackDoc, open_package
from os import getenv
from os.path import expanduser
from metapack.util import datetime_now
from metapack.util import make_metatab_file, slugify
"""
Create datapackages for CKAN datasets that were not created with Metatab
"""

from pathlib import Path


def make_package(md):

    name = md['name']

    root = Path('packages').joinpath(name)


    root.mkdir(parents=True, exist_ok=True)

    print(json.dumps(md, indent=4))

    if md['notes']:
        root.joinpath('README.md').write_text(md['notes'])
 
    doc = make_metatab_file('metatab_template.csv')
    doc['Root']['Created'] = datetime_now()
    
    doc['Documentation'].new_term('Root.Documentation', 'file:README.md', title='README')
    
    doc.ensure_identifier()
    doc.update_name(create_term=True)
    
    for r in md['resources']:
        
        doc['Resources'].new_term('Root.Datafile',
                                  r['url'],
                                  name=slugify(r['name']),
                                  description=r['description'] or r['name'],
                                  )
        
    if md.get('organization'):
        doc['Root'].find_first('Root.Origin').value = md['organization']['name'].replace('-','.')
        
    doc['Root'].find_first('Root.Title').value = md['title']
    
    doc.write_csv(str(root.joinpath('metadata.csv')))
    
    return doc

def update_package(md):
    
    name = md['name']

    root = Path('packages').joinpath(name)

    if not root.exists():
        return 
        
    doc = MetapackDoc(str(root.joinpath('metadata.csv')))
    
    print(doc.name, doc.ref)

    for t in md['tags']:
        t = doc['Root'].new_term('Root.Tag', t['name'])
        print(t)

    #print(json.dumps(md, indent=4))

    doc.write()

with Path('datasets.jsonl').open() as f:
     for l in f:
         md = json.loads(l)
        
         ex = { e['key']: e['value'] for e in md.get('extras') }
    
         name = ex.get('root.name', ex.get('name',''))
        
         if not name:
             update_package(md)
        
    