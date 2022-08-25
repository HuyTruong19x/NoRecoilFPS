import win32api;
import win32con;
import keyboard;
import mouse;

recoil = (1,2,-3,-1,2,-1,-2,3,0,-1,1,0)
i = 0
currentWeapon = ""
while 1 :
    if keyboard.is_pressed("shift") and win32api.GetAsyncKeyState(0x01):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,recoil[i],1,0,0)
        i = i + 1
        i = i % len(recoil)
    # print("xc")
    if keyboard.is_pressed("ctrl+f1") and currentWeapon != "M4A1":
        print("switch to M4A1")
        currentWeapon = "M4A1"
        recoil = (1,2,-3,-1,2,-1,-2,3,0,-1,1,0)
    if keyboard.is_pressed("ctrl+f2") and currentWeapon != "AK":
        print("switch to AK")
        currentWeapon = "AK"
        recoil = (5,2,-6,-2,4,-2,-3,5,0,-2,5,0)
    if keyboard.is_pressed("ctrl+f3"):
        print("switch to Berry")
    if keyboard.is_pressed("ctrl+f4"):
        print("switch to K2")
    if keyboard.is_pressed("ctrl+f5"):
        print("switch to ACE32")
    if keyboard.is_pressed("esc"):
        break