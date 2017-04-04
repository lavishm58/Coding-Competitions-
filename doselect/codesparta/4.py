import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
n=int(input())
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '03f7a70c30104f77969992d960eb1ae1',
}
for i in range(n):
    a=input()
    params = json.dumps({"url": a})

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request('POST', '/emotion/v1.0/recognize?%s',params, headers)
        response = conn.getresponse()
        decoded_response = response.read().decode("UTF-8")
        jsonResponse=json.loads(decoded_response)
    #sprint(jsonResponse)
    
        for item in jsonResponse:
            name = item.get("scores")
            a=[None]*8
            a[0]=name.get('sadness')
            a[1]=name.get('neutral')
            a[2]=name.get('contempt')
            a[3]=name.get('disgust')
            a[4]=name.get('anger')
            a[5]=name.get('surprise')
            a[6]=name.get('fear')
            a[7]=name.get('happiness')
            x=max(a)
            if a[0]==x:
                print('sadness')
            elif a[1]==x:
                print('neutral')
            elif a[2]==x:
                print('contempt')
            elif a[3]==x:
                print('disgust')
            elif a[4]==x:
                print('anger')
            elif a[5]==x:
                print('surprise')
            elif a[6]==x:
                print('fear')
            elif a[7]==x:
                print('happiness')        
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))