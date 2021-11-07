from tkinter import *


class ButtonMath:
    def __init__(self, action):
        self.but = Button(text=action, width=20, command=self.math)
        self.operator = action
        self.but.pack()

    def math(self):
        try:
            n1 = float(ent_n1.get())
            n2 = float(ent_n2.get())
        except ValueError:
            lab_result['text'] = 'Ошибка ввода'
        else:
            if self.operator == '+':
                lab_result['text'] = n1 + n2
            elif self.operator == '-':
                lab_result['text'] = round(n1 - n2, 2)
            elif self.operator == '*':
                lab_result['text'] = round(n1 * n2, 2)
            elif self.operator == '/':
                if n2 != 0:
                    lab_result['text'] = round(n1 / n2, 2)
                else:
                    lab_result['text'] = 'Деление на ноль!'


root = Tk()

ent_n1 = Entry(width=10)
ent_n1.pack()
ent_n2 = Entry(width=10)
ent_n2.pack()

but_summa = ButtonMath('+')
but_diff = ButtonMath('-')
but_prod = ButtonMath('*')
but_div = ButtonMath('/')

lab_result = Label(width=20)
lab_result.pack()

if __name__ == '__main__':
    root.mainloop()
