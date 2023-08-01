def squares(n):
    for i in range(1, n+1):
        n = i **2
    return(n)
while True:
    try:
        n = int(input("輸入一個正整數(輸入0結束):"))


        if n == 0:
            break
        else:
            print(squares(n))
    except ValueError:
        print('輸入一個正整數')