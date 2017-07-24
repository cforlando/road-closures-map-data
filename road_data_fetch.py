"""
Script to pull all current road closure information
Michael duPont - michael@mdupont.com - @mdupont (Slack)

Requires requests library:
pip install requests
"""

import json
import requests

LAYERS = [
    'Special Events',
    'Road Closures',
    'Road Blocks',
    'Detour Northbound',
    'Detour Southbound',
    'Detour Westbound',
    'Detour Eastbound',
    'Detour Arrows',
    'Event Staging',
    'Projects'
]

URL = """http://www2.cityoforlando.net/arcgis/rest/services/Traffic_Control/Road_Closures/MapServer/{}/query?geometry=%7B%0D%0A%22xmin%22%3A+519066.9112086431%2C%0D%0A%22ymin%22%3A+1520502.1260502483%2C%0D%0A%22xmax%22%3A+556428.0223197542%2C%0D%0A%22ymax%22%3A+1541668.7927169148%0D%0A%7D&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects&returnGeometry=true&returnIdsOnly=false&returnCountOnly=false&returnDistinctValues=false&f=pjson"""

DATA = {item: json.loads(requests.get(URL.format(i)).text)['features'] for i, item in enumerate(LAYERS)}

json.dump(DATA, open('road_data.json', 'w'))
