import pyautogui
import time

# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

pyautogui.FAILSAFE = True

pyautogui.PAUSE = 1

pyautogui.moveTo(1919, 1060)
pyautogui.click()

pyautogui.moveTo(122, 850)
pyautogui.doubleClick()

time.sleep(5)

pyautogui.moveTo(1687, 146)
pyautogui.doubleClick()

pyautogui.typewrite("main#1")
pyautogui.hotkey('Enter')