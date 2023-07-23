#檢測一個數字為奇數或偶數，輸入0結束#
def is_even(num):
   if num % 2 ==0:
       return True
   else:
       return False

while True:
  try:
    num = int(input('enter a number(enter 0 to end):'))
    if num == 0:
      print('end')
      break

    if is_even(num):
        print(num, 'is 偶數')
    else:
        print(num, 'is 奇數')



  except ValueError:
    print('請重新輸入一個整數')