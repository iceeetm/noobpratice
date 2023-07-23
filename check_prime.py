#檢測一個數字是不是質數，輸入0結束#
def is_prime(num):
  if num < 2:
   return False
  for i in range(2, int(num**0.5) + 1):
   if num % i == 0:
    print(i, '乘以', (num // i), '是', num)
    return False
  return True



while True:
  try:
    n = int(input('輸入一個正整數（輸入0結束）:'))
    if n == 0:
        print('再見')
        break

    if is_prime(n):
          print(n, '是質數')
    else:
          print(n, '不是質數')


  except ValueError:
    print('請輸入一個正整數')