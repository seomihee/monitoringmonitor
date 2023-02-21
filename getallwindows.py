import pyautogui
import win32gui

#print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))

#for win in pyautogui.getAllWindows():
#    print(win)

#w = win32gui.GetWindowText(win32gui.GetForegroundWindow())

#print(w)

#print ()
#win32gui.GetWindowText()

# 현재 화면의 스크린 사이즈 가져오기
size = pyautogui.size()
print(size)

# size[0] == width
# size[1] == height

for win in pyautogui.getAllWindows():
    if (win.isActive == True and win.isMaximized == True) : # 창이 최대화 상태일 때
        print("full window : "+win32gui.GetWindowText(win._hWnd))
        #print(win32gui.GetWindowText(win._hWnd))
        break
        #print(win)
    elif (win.isActive == True and win.isMaximized == False) : # 창이 최대화 상태는 아니지만 포커스가 있어서 제일 상단에 위치(가리는 다른 창 존재)
        print("activated window : "+win32gui.GetWindowText(win._hWnd))
        #win = pyautogui.getWindowsWithTitle(win32gui.GetWindowText(win._hWnd))[0]
    elif (win.isActive == False and win.isMinimized == False) : # 창에 포커스가 간 것은 아니지만 포커스를 가진 창이 최대화 상태가 아니라 보임(가리는 창)
        if (win.isActive == False and win.isMaximized == True ) : # 창에 포커스가 있는 것은 아니지만 최대화 상태임
            print("background window : "+win32gui.GetWindowText(win._hWnd))
            break
        else :
            print("overlapped windows : "+win32gui.GetWindowText(win._hWnd))
        #print(win)
    #elif (win.isActive == False and win.isMaximized == True ) : # 창에 포커스가 있는 것은 아니지만 최대화 상태임
     #   print("background window : "+win32gui.GetWindowText(win._hWnd))
    


#win = pyautogui.getActiveWindow()
#print(win.title)