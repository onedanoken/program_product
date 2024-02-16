from sqrt import square_root, complex_square_root
import tkinter as tk
from tkinter import ttk

def counter():
    res_entry.delete(0, tk.END)
    num = num_entry.get()
    precision = pres_entry.get()
    precision = precision if len(precision) else None
    if len(num) and num[-1] == 'i':
        try:
            numri = complex(num.replace(" ", "")[:-1] + "j")
            numre, numim = numri.real, numri.imag
            res_entry.insert(0, complex_square_root(numre, numim, precision))
        except:
            res_entry.insert(0, err_mess[curr_lang[0]])
    else:
        a = square_root(num, precision)
        if a != err_mess["russian"]:
            res_entry.insert(0, a)
        else:
            try:
                res_entry.insert(0, str(complex_square_root(float(num), 0.0, precision)).replace("j", "i"))
            except:
                res_entry.insert(0, err_mess[curr_lang[0]])


def russian_lang():
    label_num["text"] = russian[0]
    label_pres["text"] = russian[1]
    label_res["text"] = russian[2]
    button["text"] = russian[3]
    curr_lang[0] = "russian"


def english_lang():
    label_num["text"] = english[0]
    label_pres["text"] = english[1]
    label_res["text"] = english[2]
    button["text"] = english[3]
    curr_lang[0] = "english"


def chinese_lang():
    label_num["text"] = chinese[0]
    label_pres["text"] = chinese[1]
    label_res["text"] = chinese[2]
    button["text"] = chinese[3]
    curr_lang[0] = "chinese"


russian = ["Введите число:", "Введите точность:", "Результат:", "Считать"]
english = ["Input number:", "Input precision:", "Result:", "Calculate"]
chinese = ["输入数字:","输入精度:", "结果:", "计算:"]
curr_lang = ["russian"]
err_mess = {"russian": "Некорректный ввод данных.", "english": "Incorrect data input", "chinese": "数据输入不正确"}

root = tk.Tk()
root.geometry("360x160")
root.title('Square root calc')
root.resizable(0, 0)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=1)

label_num = ttk.Label(root, text="Введите число:")
label_num.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
num_entry = ttk.Entry(root)
num_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
label_pres = ttk.Label(root, text="Введите точность:")
label_pres.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
pres_entry = ttk.Entry(root)
pres_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
label_res = ttk.Label(root, text="Результат:")
label_res.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
res_entry = ttk.Entry(root)
res_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
button = ttk.Button(root, text="Считать", command=counter)
button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

intvar = tk.IntVar()
intvar.set(0)
ttk.Radiobutton(text="Русский", command=russian_lang, variable=intvar, value=0).grid(column=3, row=1, sticky=tk.W, padx=15, pady=5)
ttk.Radiobutton(text="English", command=english_lang, variable=intvar, value=1).grid(column=3, row=2, sticky=tk.W, padx=15, pady=5)
ttk.Radiobutton(text="中文", command=chinese_lang, variable=intvar, value=2).grid(column=3, row=3, sticky=tk.W, padx=15, pady=5)
root.mainloop()
