# views are what you call the endpoints
# these are only backend urls you'd want
from aiohttp import web
import helpers
import math

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

async def PE_question_2(request):
    def fib_generator(LIMIT):
        a, b = 1, 2
        while a < LIMIT:
            yield a
            a, b = b, a + b
    sum = 0
    for fib in fib_generator(4000000):
        if fib % 2 == 0:
            sum += fib
    return web.Response(text=str(sum))

async def PE_question_3(request):
    val = 600851475143
    limit = math.isqrt(val)
    answer = 0

    for prime in helpers.gen_primes():
        if (prime < limit) and (val % prime) == 0:
            answer = prime
        if prime > limit:
            break
    
    return web.Response(text=str(answer))

async def PE_question_4(request):
    val = 0

    for i in range(999, 99, -1):
        for j in range(i-1, 99, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if (product > val):
                    val = product

    return web.Response(text=str(val))

async def PE_question_5(request):
    answer = 0
    counter = 0
    for n in helpers.find_lcm():
        counter += 1
        if (counter == 20):
            answer = n
            break

    return web.Response(text=str(answer))

async def PE_question_6(request):
    sum_of_number = 0
    sum_of_squares = 0

    for i in range (1, 101):
        sum_of_number += i
        sum_of_squares += (i * i)

    return web.Response(text=str(sum_of_number * sum_of_number - sum_of_squares))

async def PE_question_7 (request):
    counter = 0
    for prime in helpers.gen_primes():
        counter += 1
        if (counter == 10001):
            return web.Response(text=str(prime))

async def PE_question_8 (request):
    index = 0
    val= 1
    answer = 0
    while index < 986:
        # slicing [a:a+13] because a+13 itself is excluded
        selection = helpers.Q8_problem[index:index+13]
        for i in range(13):
            # numbers can't be sliced
            # therefore it needs to be transfored back to int to do maths
            val = val * int(selection[i])
        if (val > answer):
            answer = val
        index += 1
        val = 1
    
    return web.Response(text=str(answer))