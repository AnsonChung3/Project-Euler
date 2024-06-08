import math

def demo_helper():
    return 200

def gen_primes():
    D = {}
    q = 2
    
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1  

def find_lcm():
    greater, smaller= 2, 1
    while True:
        if (greater % smaller) == 0:
            # greater number is the lcm and yield
            pass
        else:
            gcd = math.gcd(greater, smaller)
            if gcd == 1:
                # no common denominator, lcm is product of the two numbers
                # lcm is calculated and instantly replced as the greater number and yield
                greater = (greater * smaller)
            else:
                multiplier = int((greater / math.gcd(greater, smaller)))
                greater = (smaller * multiplier)
                
        # yield and smaller are moved out of if-else statement for cleaner look
        # calculation are done inside the statement
        # variable smaller is to keep track of the number checked against for LCM
        # all it does is increment by 1
        yield greater
        smaller += 1