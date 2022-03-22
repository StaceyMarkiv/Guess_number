from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"),
                         bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            "Сброс", "0", "Стереть цифру"
        ]
        x = 10
        y = 180
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=150,
                                      height=80)
            x += 160
            if x > 400:
                x = 10
                y += 90

    def logicalc(self, operation):
        if operation == "Сброс":
            self.formula = ""
        elif operation == "Стереть цифру":
            self.formula = self.formula[0:-1]
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


root = Tk()
root["bg"] = "#000"
root.geometry("485x550+200+200")
root.title("Угадай число")
root.resizable(False, False)
app = Main(root)
app.pack()
root.mainloop()


# def Hello(event):
#     print("Yet another hello world")
#
# btn = Button(root,                  #родительское окно
#              text="Click me",       #надпись на кнопке
#              width=30,height=5,     #ширина и высота
#              bg="white",fg="black") #цвет фона и надписи
# btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
# btn.pack()                          #расположить кнопку на главном окне
# root.mainloop()