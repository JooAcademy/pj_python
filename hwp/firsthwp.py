'''
win32설치하기
윈도우 커맨드cmd 또는 파이썬 터미널 창에

pip install pypiwin32 

'''


import win32com.client as win32
import os

hwp = win32.Dispatch("HWPFrame.HwpObject")
hwp.XHwpWindows.Item(0).Visible = True

path = os.getcwd() # 현재 폴더

hwp.Open(path + "/abc.hwp", "HWP", None)
hwp.Open(path + "/abc.hwpx", "HWPX", None)

