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

from tkinter import *
from win32com.client import Dispatch

def setup_hancom():
    hancom = Dispatch("HWPFrame.HwpObject")
    hancom.XHwpWindows.Item(0).Visible = True
    return hancom

def insert_text(hancom, text):
    action = hancom.CreateAction("InsertText")
    action_set = action.CreateSet()
    action_set.SetItem("Text", text)
    action.Execute(action_set)

def create_button(parent, text, command, x, y):
    button = Button(parent, text=text, command=command)
    button.place(x=x, y=y)
    return button

def main():
    hancom = setup_hancom()

    newwin = Tk()
    newwin.title("한컴 테스트")

    create_button(newwin, "버튼입니다", lambda: insert_text(hancom, "내용입니다 "), 0, 0)
    create_button(newwin, "버튼입니다", lambda: insert_text(hancom, "인자 "), 0, 20)
    create_button(newwin, "버튼입니다", lambda: insert_text(hancom, "언젠가 성공하기를... "), 0, 40)

    newwin.mainloop()

if __name__ == "__main__":
    main()
