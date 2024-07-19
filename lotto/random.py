import tkinter as tk
import random

# 랜덤으로 숫자를 생성하는 함수
def generate_random_numbers():
    num_of_numbers = int(entry_num.get())
    simsa_num = num_of_numbers * 3 # 예비심사위원 숫자 3배수 지정           
    numbers = random.sample(range(1, simsa_num+1), num_of_numbers)
    label_result.config(text=', '.join(map(str, numbers)))

# GUI 생성
root = tk.Tk()
root.title("심사위원 랜덤 번호 뽑기")
root.geometry("250x80")

# 입력창 생성
rnm_num = tk.Label(root, text="심사위원은 몇 명 입니까?")
rnm_num.pack()

entry_num = tk.Entry(root)
entry_num.pack()

# 버튼 생성
button_generate = tk.Button(root, text="생성", command=generate_random_numbers)
button_generate.pack()

# 결과 출력창 생성
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()