# views are what you call the endpoints
# these are only backend urls you'd want
from aiohttp import web
import helpers
import math
import itertools

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

async def PE_question_15(request):
    # generate empty 21 x 21 grid view
    # grid_view[0][0] will be the top left corner, and [19][19] be the bottom right corner
    grid_view = []
    for row in range(21):
        grid_view.append([*range(21)])

    for index in range(21):
        # assigning value = 1 to the top row
        grid_view[0][index] = 1
        # assigning value = 1 to the left column
        grid_view[index][0] = 1
    
    for row in range (1, 21):
        for i in range(1, 21):
            # value to each point/node is the sum of the one above and the one to the right
            # https://youtu.be/UplqE9mm490?si=rVliLbK4860C_QHg&t=232
            # this is the illustration of this method
            grid_view[row][i] = grid_view[row-1][i] + grid_view[row][i-1]
    
    return web.Response(text=str(grid_view[20][20]))

async def PE_question_16(request):
    num = str(2**1000)
    answer = 0

    for i in num:
        answer += int(i)

    return web.Response(text=str(answer))

async def PE_question_17(request):
    len_of_digit = { 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 0: 0}
    len_of_tenth = { 1: 3, 2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6, 0: 0}
    teen_exceptions = [4, 6, 7, 9]
    hundreds = [100, 200, 300, 400, 500, 600, 700, 800, 900]

    # answer starts at 11 for "one thousand"
    answer = 11

    for num in range(1, 1000):
        str_num = list(str(num)[::-1])
        if num < 100:
            str_num.append('0')
            # take off the extra addition of "hundred and"
            # see more details in the hundreds' block
            answer -= 10
        if num < 10:
            str_num.append('0')

        # adding digiits
        answer += len_of_digit[int(str_num[0])]

        # adding tenths
        if int(str_num[1]) == 1 and int(str_num[0]) in teen_exceptions:
            answer += 1
        answer += len_of_tenth[int(str_num[1])]

        # adding hundreds
        # the +10 is for "hundred and"
        # extra addition for < 100 is alraedy taken in the previous logic block
        answer += len_of_digit[int(str_num[2])] + 10
        if num in hundreds:
            # -3 for the "and"
            answer -= 3

    return web.Response(text=str(answer))

async def PE_question_18(request):
    answer = helpers.max_sum_triangle(helpers.Q18_problem)
    return web.Response(text=str(answer))

async def PE_question_67(request):
    answer = helpers.max_sum_triangle(helpers.Q67_problem)
    return web.Response(text=str(answer))

async def PE_question_20(request):
    product = 1
    for i in range(2, 101):
        product = i * product
    
    answer = 0
    for num in str(product):
        answer += int(num)
    
    return web.Response(text=str(answer))

async def PE_question_22(request):
    answer = 0
    
    sorted_names = sorted(helpers.Q22_problem)
    for i in range(len(sorted_names)):
        name = sorted_names[i]
        name_value = 0
        for alphabet in name:
            # the value for "A" is 65, so the value here is -64
            name_value += ord(alphabet)-64
        answer += name_value * (i + 1)

    return web.Response(text=str(answer))

async def PE_question_28(request):
    answer = 1
    for i in range(3, 1002, +2):
        # top right corner
        top_right = i ** 2
        answer += top_right
        # top lef corner
        answer += top_right - (i - 1)
        # bottom left corner
        answer += top_right - (i - 1) * 2
        # bottom right corner
        answer += top_right - (i - 1) * 3

    return web.Response(text=str(answer))

async def PE_question_36(request):
    answer = 0
    bin = "{0:b}"
    for i in range(1, 1000000):
        ten_str = str(i)
        if ten_str == ten_str[::-1]:
            bin_str = bin.format(i)
            if bin_str == bin_str[::-1]:
                answer += i
    print(answer)
    return web.Response(text=str(answer))

async def PE_question_41(request):
    digits = [str(i) for i in range(9, 0, -1)]

    for i in range(0, 6):
        for num in itertools.permutations(digits[i:]):
            answer = "".join(num)
            if (helpers.isPrime(int(answer))):
                return web.Response(text=answer)

async def PE_question_81(request):
    # this solution starts from the top left corner(0, 0), then moves in layers towards the bottom right corner
    Q81 = helpers.Q81_problem
    # variable set up for readability
    MAX = len(Q81)

    # range for row is set so the function will never loop through the point (0, 0),
    # which the function should skip
    # this eliminates the boolean check for (0, 0) which is only useful for a single time
    for row in range(1, MAX):
        # the range setting avoids the diagonal points
        for col in range(row):
            if col == 0:
                # this is for all numbers on the left edge
                Q81[row][col] += Q81[row-1][col]
                # this is for all numbers on the top edge
                Q81[col][row] += Q81[col][row-1]
            else:
                Q81[row][col] += min(Q81[row-1][col], Q81[row][col-1])
                Q81[col][row] += min(Q81[col-1][row], Q81[col][row-1])
        # bottom right corner is handled after both right and bottom edged are done looping
        Q81[row][row] += min(Q81[row-1][row], Q81[row][row-1]) 

    return web.Response(text=str(Q81[MAX-1][MAX-1]))

# async def PE_question_357(request):    
#     answer = 0

#     # the solution starts by making a full list of primes under 10^8
#     # it is for both quick check up and first filter for numbers
#     list_of_primes = list(helpers.gen_primes_with_limit(10**8))
    
#     # since n+1 has to be prime, all n must be prime-1
#     list_of_answers = [prime - 1 for prime in list_of_primes]
#     # remove the first prime(2)
#     del list_of_answers[0]
#     # multiples of 4 means 2 x 2 x something, which makes the combo an even number
#     # hence it's filtered out
#     # this brings the numbers being tested to <3% of 10^8
#     list_filtered_out_divisible_by_4 = [n for n in list_of_answers if not n % 4 == 0]

#     def test_w_prime(n, primes):
#         test_limit = int(n ** 0.5)
        
#         for i in range(2, test_limit+1): 
#             if n % i == 0 and not (i + n/i) in primes:
#                 return False
#         # print(f"{n} is adding")
#         answer += n
    
#     for n in list_filtered_out_divisible_by_4:
#         test_w_prime(n)
    
#     # due to a mix of performance issue from docker, python, and my own computer
#     # there is no way for my machine to run this code in a reasonable time
#     # posisbly docker can only use so much resources
#     # posisbly pyhton is single thread or something to do with garabage collection
#     # possibly my laptop is too old(8+years) to run it

#     # I tried to break up the massive lists into smaller ones to see if that helps
#     # it's proved, with a smaller max value 10^6, it runs 1/3 quicker
#     # but unfortunately when it comes to 10^8 it doesn't finish within 48 hours

#     # since the code should work but can't be run, this solution is commented out

#     return web.Response(text=str(answer))