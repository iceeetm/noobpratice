def userEnter():
    while True:
        try:
            changeDict = {
                "噸": 0.001,
                "公斤": 1,
                "公克": 1000,
                "毫克": 100000,
                "台斤": 1.667,
                "兩": 26.667,
                "台錢": 266.667,
                "磅": 2.20462,
                "盎司": 35.27396,
            }

            a = float(input("輸入公斤重量:"))
            b = str(change())

            ans = a * changeDict[b]
            print(f"{a}公斤 等於 {ans}{b}")

        except ValueError:
            print("輸入錯誤請重新輸入")


def change():
    changeList = ["噸", "公斤", "公克", "毫克", "台斤", "兩", "台錢", "磅", "盎司"]

    print("1.噸\n2.公斤\n3.公克\n4.毫克\n5.台斤\n6.兩\n7.台錢\n8.磅\n9.盎司")

    b = int(input("輸入你要轉換的重量單位的代號:"))
    print(changeList[b - 1])
    return changeList[b - 1]


userEnter()
