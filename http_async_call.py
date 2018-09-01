import requests
import threading

def async_call():
    r=requests.get('https://webhook.site/#/10c68a23-5b6a-4f00-938a-a74d8d4a653a')
    print(r.headers['date'])
   

t1=threading.Thread(target=async_call)
t2=threading.Thread(target=async_call)
t3=threading.Thread(target=async_call)

t1.start()
t2.start()
t3.start()

