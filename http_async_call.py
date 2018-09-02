#Making the necessary imports
import requests
import asyncio

#Function for making http calls to webhook using asynchronous technique and returning the date parameter
def webhook():
    r=loop1.run_in_executor(None,requests.get,'https://webhook.site/#/10c68a23-5b6a-4f00-938a-a74d8d4a653a')
    result= yield from r
    return result.headers['Date']
    
#Function for printing the received dates
async def main(routine):
    for futures in asyncio.as_completed(routine):
        print(await futures)

#Generating event loops using asyncio library for asynchrounous jobs, running the loops and finally closing them
routine=[webhook() for i in range (0,3)]
loop = asyncio.get_event_loop()
loop1 = asyncio.get_event_loop()
loop.run_until_complete(main(routine))
loop.close()
loop1.close()
