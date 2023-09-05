def change():
    while True:
        try:
            print(
                """
這是一個重量換算小程式，請輸入公斤重量，查詢其他單位換算後的重量。
可以查詢的單位有:噸、公斤、公克、毫克、台斤、兩、台錢、磅、盎司"
            """
            )

            a = float(input("請輸入公斤重:"))

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
            for x, y in changeDict.items():
                ans = a * y
                print(f"{a}公斤 等於{ans:.2f}{x}")

        except ValueError:
            print("輸入的數值無效喔~請重新輸入")


change()
