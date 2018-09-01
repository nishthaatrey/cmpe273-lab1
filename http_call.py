import requests

for n in range(0,3):
    r=requests.get('https://webhook.site/#/10c68a23-5b6a-4f00-938a-a74d8d4a653a')
    print(r.headers['date'])