#製作一個猜數字遊戲#
import random
ans = random.randint(1, 100)
while True:
  try:
    guess = int(input('1-100中猜一個數字:'))
    if guess == 0:
      print('再見')
      break

    if ans == guess:
      print('猜對了')
      break
    elif ans > guess:
      print('猜大一點')
    else:
      print('猜小一點')

  except ValueError:
      print('輸入的要是整數喔')