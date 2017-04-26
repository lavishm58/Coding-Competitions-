from urllib.request import urlopen
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import requests

from datetime import timedelta, date

star_date=input()
en_date=input()
l=float(input())
u=float(input())
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)
sy=int(star_date[0:4])
sm=int(star_date[5:7])
sd=int(star_date[8:10])
api_key='0nWQLQhOaaFnh0Vd61mPLXLvg9FVdTxh4ZTMUUOS'
url='/neo/rest/v1/feed?start_date='+star_date+'&end_date='+en_date+'&api_key='+api_key
ey=int(en_date[0:4])
em=int(en_date[5:7])
ed=int(en_date[8:10])
s_date = date(sy,sm,sd)
e_date = date(ey,em,ed+1)
try:
    conn = http.client.HTTPSConnection('api.nasa.gov')
    conn.request('Get',url)
    response = conn.getresponse().read()
    json_data=json.loads(response.decode("UTF-8"))
    dic=json.dumps(json_data)
    count=0
    for single_date in daterange(s_date,e_date):
        a=json_data['near_earth_objects'][str(single_date.strftime("%Y-%m-%d"))]
        q=[]
    
        for i in a:
            q.append(i.get('estimated_diameter'))
        for i in range(len(q)):
            if q[i]['meters']['estimated_diameter_min']>l and  q[i]['meters']['estimated_diameter_max']<u:
                count+=1
    print(count)    
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

