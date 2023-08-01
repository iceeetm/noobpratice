#使用者輸入條件練習#
#使用者名稱不得超過20個字元、限用英文、不得輸入空格、不得輸入數字、不分大小寫
#使用者輸入電話格式為0000-000000，輸入錯誤則請重新輸入
#使用者輸入之電子信箱格式要有"@"及"."才符合格式
#顯示"歡迎 + 使用者名稱(第一個字母大寫)"，第二行顯示"電話號碼"第三行為"電子信箱"

username ='iceACE'
phone = '0911-222333'
mail = 'aaa@gmail.com'


if len(username) > 20:
    print('使用者名稱不能超過20個字元。')
elif " " in username:
    space_pos = username.find(' ')
    print(f'您的空格在{space_pos}個字元，不能輸入空格。')
elif not username.isalpha():  #僅英文回傳True(不含空格或其他符號)
    print("使用者名稱只能包含英文字母，不能使用其他字元。")
elif "-" not in phone or len(phone) != 11 or phone[4] != '-':
    print('電話格式錯誤，請重新輸入。')
elif "@" not in mail or 'com' not in mail:
    print('電子信箱格式錯誤，請重新輸入。')


else:
    username = username.capitalize() #字首大寫其他小寫
    print(f'歡迎，{username}\n您的註冊電話為{phone}\n您的註冊信箱為{mail}')

