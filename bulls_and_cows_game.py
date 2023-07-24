##猜數字(幾A幾B) Bulls & Cows###

import random
import itertools


ans =''.join(random.sample('0123456789',4))

def valid(n):
    if len(n) !=4:
        return False
    if any( x not in '0123456789' for x in n):
        return False
    if any(x==y for x,y in itertools.combinations(n,2)):
        return False
    return True
def tip(ans, num):
    A, B = 0, 0
    for i in range(4):
        if num[i] == ans[i]:
            A = A+1
        elif num[i] in ans:
            B = B+1
    return '{}A{}B'.format(A,B)  

while True:
    try:
        num = input('輸入一個四位數字(輸入0結束):')
        if num =='0':
            print('再見')
            break
        if num==ans:
            print('答對')
            break
        if not valid(num):
            print(num, '不合法的數字，請重新輸入一個四位數')
            continue
        if tip(ans,num):
            print(tip(ans,num))
            
    except ValueError:
        print('請重新輸入一個四位數')

    
    