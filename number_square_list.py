def squares(n):
    squared_numbers = [i**2 for i in range(1, n+1) if i in range(1, n+1)]

    return squared_numbers

try:
    n = float(input("請輸入一個數字："))
    n = int(n)
    result = squares(n)
    print(result)
except ValueError:
    print('輸入正整數')