#Making the necessary imports
import requests
import asyncio

#Function for making http calls to webhook using asynchronous technique and returning the date parameter
def webhook():
    r=loop.run_in_executor(None,requests.get,url)
    result= yield from r
    return result.headers['Date']
    
#Function for printing the received dates
async def main(routine):
    for date in asyncio.as_completed(routine):
        print(await date)

#Generating event loop using asyncio library for asynchrounous jobs, running the loop and finally closing it
routine=[webhook() for i in range (0,3)]
url='https://webhook.site/#/10c68a23-5b6a-4f00-938a-a74d8d4a653a'

loop = asyncio.get_event_loop()
loop.run_until_complete(main(routine))
loop.close()
