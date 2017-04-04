from urllib.request import urlopen
import json
import requests
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
start_date=input()
end_date=input()
api_key='0nWQLQhOaaFnh0Vd61mPLXLvg9FVdTxh4ZTMUUOS'
url='/neo/rest/v1/feed?start_date='+start_date+'&end_date='+end_date+'&api_key='+api_key
try:
    conn = http.client.HTTPSConnection('api.nasa.gov')
    conn.request('Get',url)
    response = conn.getresponse().read()
    json_data=json.loads(response.decode("UTF-8"))
    dic=json.dumps(json_data)
    a=json_data['near_earth_objects']['1994-07-23']
    j=0 
    q=[]
    l=float(input())
    u=float(input())
    count=0
    for i in a:
        q.append(i.get('estimated_diameter'))
        if q[j]['meters']['estimated_diameter_min']>=l and  q[j]['meters']['estimated_diameter_max']<=u:
            count+=1
        j+=1
    print(count)    
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

