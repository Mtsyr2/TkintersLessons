from tkinter import *

colors = {'красный': '#ff0000',
          'оранжевый': '#ff7d00',
          'желтый': '#ffff00',
          'зеленый': '#00ff00',
          'голубой': '#007dff',
          'синий': '#0000ff',
          'фиолетовый': '#7d00ff'}


class Color_Button:
    def __init__(self, color):
        self.but = Button(width=3, height=1, padx=3, bg=colors[color], command=self.press_action)
        self.operator = color
        # self.color = color
        self.bg = colors[color]
        self.but.pack(side=LEFT)

    def press_action(self):
        color_ent.delete(0, END)
        color_ent.insert(0, self.operator)
        color_lab['text'] = self.bg


root = Tk()
color_ent = Entry(width=20, justify=CENTER)
color_ent.pack()
color_lab = Label(width=20)
color_lab.pack()

but1 = Color_Button('красный')
but2 = Color_Button('оранжевый')
but3 = Color_Button('желтый')
but4 = Color_Button('зеленый')
but5 = Color_Button('голубой')
but6 = Color_Button('синий')
but7 = Color_Button('фиолетовый')

root.mainloop()
