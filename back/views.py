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
        if prime < limit and (val % prime) == 0:
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
                if product > val:
                    val = product

    return web.Response(text=str(val))

async def PE_question_5(request):
    answer = 0
    counter = 0
    for n in helpers.find_lcm():
        counter += 1
        if counter == 20:
            answer = n
            break

    return web.Response(text=str(answer))

async def PE_question_6(request):
    sum_of_number = 0
    sum_of_squares = 0

    for i in range(1, 101):
        sum_of_number += i
        sum_of_squares += (i * i)

    return web.Response(text=str(sum_of_number * sum_of_number - sum_of_squares))

async def PE_question_7(request):
    counter = 0
    for prime in helpers.gen_primes():
        counter += 1
        if counter == 10001:
            return web.Response(text=str(prime))

async def PE_question_8(request):
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
        if val > answer:
            answer = val
        index += 1
        val = 1
    
    return web.Response(text=str(answer))

async def PE_question_10(request):
    answer = 0
    for prime in helpers.gen_primes():
        if prime >= 2000000:
            break
        answer += prime
    return web.Response(text=str(answer))

async def PE_question_11(request):
    problem = helpers.Q11_problem
    answer = 0

    for row in range(len(problem)):
        for col in range(len(problem)-3):
            horizontal = (problem[row][col] * problem[row][col+1] * problem[row][col+2] * problem[row][col+3])
            if horizontal > answer:
                answer = horizontal
                
    for row in range(len(problem)-3):
        for col in range(len(problem)):
            vertical = (problem[row][col] * problem[row+1][col] * problem[row+2][col] * problem[row+3][col])
            if vertical > answer:
                answer = vertical

    for row in range(len(problem)-3):
        for col in range(len(problem)-3):
            top_left = (problem[row][col] * problem[row+1][col+1] * problem[row+2][col+2] * problem[row+3][col+3])
            if top_left > answer:
                answer = top_left
                
    for row in range(len(problem)-3):
        for col in range(3, len(problem)):
            top_right = (problem[row][col] * problem[row+1][col-1] * problem[row+2][col-2] * problem[row+3][col-3])
            if top_right > answer:
                answer = top_right
    
    return web.Response(text=str(answer))

async def PE_question_12(request):
    def triangle_gen():
        add_on = 11
        sum = 55
        while True:
            sum += add_on
            yield sum
            add_on += 1
    
    divisor_count = 0

    for i in triangle_gen():
        for k in range(2, math.isqrt(i)+1):
            if (i % k == 0):
                divisor_count += 1
            if (divisor_count >= 249):
                return web.Response(text=str(i))
        divisor_count = 0  

async def PE_question_13(request):
    sum = 0
    for n in helpers.Q13_problem:
        sum += n

    return web.Response(text=str(sum)[0:10])

async def PE_question_14(request):
    def collatz_chain_count(START):
        n = START
        
        while n != 1:
            if n % 2 == 0:
                new = n / 2
            else:
                new = n * 3 + 1
            yield new
            n = new

    answer, chain = 0, 0

    for i in range (1, 1000000):
        if len(list(collatz_chain_count(i))) > chain:
            answer, chain = i, len(list(collatz_chain_count(i)))
    
    return web.Response(text=str(answer))