###判斷成績的級距###

while True:
    x = int(input('成績(0-100):'))

    if 101> x >=90:
            print('excellent')
    elif 90 > x >=60:
            print('great')
    elif 60 > x >=0:
            print('bad')
    else:
        print('bye')
        break