import tkinter as tk
from tkinter import messagebox
import random

class RandomNumberGeneratorApp:
    def __init__(self, window):
        self.window = window
        self.window.title('랜덤 번호 생성기')
        self.init_ui()

    def init_ui(self):
        self.entries = self.create_input_widgets(['시작 번호', '끝 번호', '뽑을 갯수'])
        self.create_generate_button()
        self.result_label = tk.Label(self.window, font=('Arial', 14))
        self.result_label.grid(row=4, column=0, columnspan=2)

    def create_input_widgets(self, labels):
        entries = []
        for i, label_text in enumerate(labels):
            tk.Label(self.window, text=label_text).grid(row=i, column=0)
            entry = tk.Entry(self.window)
            entry.grid(row=i, column=1)
            entries.append(entry)
        return entries

    def create_generate_button(self):
        tk.Button(self.window, text='생성', command=self.generate_numbers).grid(row=3, column=0, columnspan=2)

    def generate_numbers(self):
        try:
            start, end, count = (int(entry.get()) for entry in self.entries)
            self.validate_input(start, end, count)
            result = sorted(random.sample(range(start, end + 1), count))
            self.result_label.config(text=' '.join(map(str, result)))
        except ValueError:
            messagebox.showerror("에러", "모든 입력은 정수여야 합니다.")
        except Exception as e:
            messagebox.showerror("에러", str(e))

    def validate_input(self, start, end, count):
        if end > 99:
            raise ValueError("끝 번호는 99보다 작아야 합니다.")
        elif start > end:
            raise ValueError("시작 번호는 끝 번호보다 작아야 합니다.")
        elif count > (end - start + 1):
            raise ValueError("뽑을 갯수는 시작 번호와 끝 번호 사이의 숫자보다 작아야 합니다.")

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("230x115")
    app = RandomNumberGeneratorApp(window)
    window.mainloop()
