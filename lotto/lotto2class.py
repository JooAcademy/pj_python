import tkinter as tk
from tkinter import messagebox
import random

class RandomNumberGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title('랜덤 번호 생성기')

        self.start_label = tk.Label(self.window, text='시작 번호 ')
        self.start_label.grid(row=0, column=0)
        self.start_entry = tk.Entry(self.window)
        self.start_entry.grid(row=0, column=1)

        self.end_label = tk.Label(self.window, text='끝 번호 ')
        self.end_label.grid(row=1, column=0)
        self.end_entry = tk.Entry(self.window)
        self.end_entry.grid(row=1, column=1)

        self.select_label = tk.Label(self.window, text='뽑을 갯수 ')
        self.select_label.grid(row=2, column=0)
        self.select_entry = tk.Entry(self.window)
        self.select_entry.grid(row=2, column=1)

        self.generate_button = tk.Button(self.window, text='생성', command=self.get_input)
        self.generate_button.grid(row=3, column=0, columnspan=2)

        self.result_label = tk.Label(self.window, font=('Arial', 14))
        self.result_label.grid(row=4, column=0, columnspan=2)

    def get_input(self):        
        startnum = self.start_entry.get()
        endnum = self.end_entry.get()
        selectnum = self.select_entry.get()
        
        try:    
            startnum = int(startnum)
            endnum = int(endnum)
            selectnum = int(selectnum)  
            
            if endnum > 99:
                messagebox.showerror("에러", "끝 번호는 99보다 작아야 합니다.")
                return
            elif startnum > endnum:
                messagebox.showerror("에러", "시작 번호는 끝 번호보다 작아야 합니다.")
                return
            elif selectnum > (endnum - startnum + 1):
                messagebox.showerror("에러", "뽑을 갯수는 시작 번호와 끝 번호 사이의 숫자보다 작아야 합니다.")
                return

            resultnum = random.sample(range(startnum, endnum+1), selectnum)
            resultnum = sorted(resultnum)
            
            self.result_label.config(text=' '.join(map(str, resultnum)))

        except ValueError:
            messagebox.showerror("에러", "시작 번호, 끝 번호, 뽑을 갯수는 정수여야 합니다.")


window = tk.Tk()
window.geometry("230x115")  # widthxheight
window.minsize(230,115)
app = RandomNumberGenerator(window)
window.mainloop()