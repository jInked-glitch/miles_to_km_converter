from tkinter import *

def button_clicked():
    miles = float(input.get())
    km = miles * 1.609
    # km = round(miles * 1.609)
    result_value_label.config(text = f"{km}")

window = Tk()
window.title("Miles to Km Converter")

# ウィンドウの余白を設定
window.config(padx=30, pady=30)

#Entry
input = Entry(width=10)
# print(input.get())
input.grid(column=1, row=0)

#Label
my_label_0 = Label(text="Miles")
my_label_1 = Label(text="is equal to", font=("Arial", 14))
my_label_2 = Label(text="Km", font=("Arial", 14))

my_label_0.grid(column=3, row=0)
my_label_1.grid(column=0, row=1)
my_label_2.grid(column=3, row=1)
# ラベルの余白を設定するときは
# my_label.config(padx=50, pady=50)

# result
result_value_label = Label(text="0")
result_value_label.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()
