import pyautogui,math
pyautogui.FAILSAFE=True
Radius = 250
Speed=8
pyautogui.hotkey('alt', 'tab')
(X,Y)=pyautogui.locateCenterOnScreen('circle.png')
X+=1
Y+=1
pyautogui.moveTo(X+Radius,Y)
pyautogui.mouseDown()
for i in range(370):
    if i%Speed==0:
       pyautogui.moveTo(X+Radius*math.cos(math.radians(i)),Y+Radius*math.sin(math.radians(i)))
pyautogui.mouseUp() 