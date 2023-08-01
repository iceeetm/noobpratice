####開啟作業網站####

import pyautogui, time

pyautogui.press('win')
pyautogui.typewrite('edge')
pyautogui.press('enter')
pyautogui.typewrite('https://www.geogebra.org/classic?lang=zh_TW')
pyautogui.press('enter')
time.sleep(1)
pyautogui.PAUSE = 2

####執行畫圖####
##第一種方式###

import time
pyautogui.PAUSE = 0.1
pyautogui.click(2713, 169)
pyautogui.click(2856, 284)
pyautogui.click(3000, 450)
pyautogui.typewrite('1')
pyautogui.press('enter')


##第二種方式##

import pyautogui
pyautogui.PAUSE = 0.5

pyautogui.click(2713, 169)
pyautogui.click(2856, 284)

def draw_ichi(x, y):
    pyautogui.click(x, y)  # 移動到座標 (x, y) 並點擊
    pyautogui.typewrite('1')  # 輸入 '1'
    pyautogui.press('enter')  # 按下 Enter 鍵

for x in [3000, 3100]:
    for y in [500, 600]:
        draw_ichi(x, y)

pyautogui.click(2658, 159)
pyautogui.click(2728, 286)

def draw_ichi(x, y):
   
    pyautogui.click(x + 20, y - 20)
    pyautogui.click(x - 20, y - 20)

    pyautogui.press('enter')    
    

for x in [3000, 3100]:
    for y in [500, 600]:
        draw_ichi(x, y)
