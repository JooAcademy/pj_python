'''
win32설치하기
윈도우 커맨드cmd 또는 파이썬 터미널 창에

pip install pypiwin32 

'''


import win32com.client as win32
import os
from tkinter import*

hwp = win32.Dispatch("HWPFrame.HwpObject") # 한컴
hwp.XHwpWindows.Item(0).Visible = True

path = os.getcwd() # 현재 폴더

hwp.Open(path + "/abc.hwp", "HWP", None)
#hwp.Open(path + "/abc.hwpx", "HWPX", None)

def text_input():
    hwpaction = hwp.CreateAction("InsertText")
    hwpset = hwpaction.CreateSet()
    hwpaction.GetDefault(hwpset)
    txt = 2024
    hwpset.SetItem("Text", f"안녕하세요! 한컴{txt}") 
    hwpaction.Execute(hwpset)
    
def temp_def(txt):
    hwpaction = hwp.CreateAction("InsertText")
    hwpset = hwpaction.CreateSet()
    hwpaction.GetDefault(hwpset)    
    hwpset.SetItem("Text", txt) 
    hwpaction.Execute(hwpset)   
    
def 글자크기3증가():
    hwp.HAction.Run("CharShapeHeightIncrease")    

popwin = Tk()
popwin.title = "한컴 테스트 창"
#newBtn = Button(popwin, text="버튼입니다.", command=lambda:글자크기3증가())
newbutton1 = Button(popwin, text="자체 로컬변수", command=lambda:text_input())
newbutton1.place(x=0, y=0)
newbutton2 = Button(popwin, text="매개변수넘기기", command=lambda:temp_def("한컴오피스 자동화"))
newbutton2.place(x=100, y=0)

popwin.mainloop()
    
