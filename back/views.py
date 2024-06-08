# views are what you call the endpoints
# these are only backend urls you'd want
from aiohttp import web
import helpers

# these fucntions are handling requests
# and if you look into routes.py, they are assigned a endpoint
async def test(request):
    print ("getting into index")
    return web.Response(text='Hello Aiohttp!')

async def test_demo_helper(request):
    print ('test demo helper')
    val = helpers.demo_helper()
    return web.Response(text=str(val))

async def PE_question_1(request):
    result = 0
    for n in range(1000):
        if n % 3 == 0 or n % 5 == 0:
            result += n
    return web.Response(text=str(result))