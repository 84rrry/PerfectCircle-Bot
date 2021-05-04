import pyautogui,math
#Drag mouse to top left corner to stop the automation 
pyautogui.FAILSAFE=True
#define radius
Radius = 250
#define speed
Speed=8
#to change the window
pyautogui.hotkey('alt', 'tab')
#locate the center 
(X,Y)=pyautogui.locateCenterOnScreen('circle.png')
X+=1
Y+=1
#move to the right initial position
pyautogui.moveTo(X+Radius,Y)
#draw the circle 
pyautogui.mouseDown()
for i in range(370):
    if i%Speed==0:
       pyautogui.moveTo(X+Radius*math.cos(math.radians(i)),Y+Radius*math.sin(math.radians(i)))
pyautogui.mouseUp() 
