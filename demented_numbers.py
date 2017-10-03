# Solution for: https://webcache.googleusercontent.com/search?q=cache:7lhnzUkjAKsJ:https://www.codechef.com/MN18R022/problems/MU51+&cd=3&hl=en&ct=clnk&gl=in

def sumSquareOfDigits(num):
    return sum([int(x)**2 for x in str(num)])

def find(a, b):
    nonDemented = set()
    demented = set()
    for num in range(a, b+1):
        
        seen = set()
        s = num
        while s != 1 and s not in seen and s not in nonDemented:
            #print(s)
            seen.add(s)
            s = sumSquareOfDigits(s)
            
        if s != 1:
            nonDemented.add(num)
            nonDemented.add(s)
        else:
            demented.add(num)

    print(len(demented))

    
find(1, 10)
find(100, 150)
find(1000, 1099)