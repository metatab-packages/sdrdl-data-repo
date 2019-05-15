from ckanapi import RemoteCKAN
import json

"""
Get a list of all of the metatab s3 packages on https://data.sandiegodata.org
"""

c = RemoteCKAN('https://data.sandiegodata.org')
packages = c.action.current_package_list_with_resources()

for package_name in c.action.package_list():
    
    md = c.action.package_show(id=package_name)
    
    d = { e['key']: e['value'] for e in md.get('extras') }
    
    name = d.get('root.name', d.get('name',''))
    
    for r in md.get('resources',[]):
        if r['name'] == name+'.csv':
            print(r['url'])
    
