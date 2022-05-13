import random
from tkinter import *
from single_player import guess_single, try_count

number = random.randint(1, 100)


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        # Нужно привязать счетчик к кнопке "Ввод"
        # self.counts = "Попытка № 1"
        # self.lbl_counts = Label(text=self.counts, font=("Times New Roman", 16, "bold"),
        #                         bg="#000", foreground="#FFF")
        # self.lbl_counts.place(x=11, y=20)

        self.result = "Введите число:"
        self.lbl_result = Label(text=self.result, font=("Times New Roman", 16, "bold"),
                                bg="#000", foreground="#FFF")
        self.lbl_result.place(x=11, y=60)

        self.action = "0"
        self.lbl_number = Label(text=self.action, font=("Times New Roman", 21, "bold"),
                                bg="#000", foreground="#FFF")
        self.lbl_number.place(x=11, y=100)

        btns = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            "Сброс", "0", "Стереть цифру"
        ]
        x = 10
        y = 170
        for bt in btns:
            com = lambda x=bt: self.button_logic(x)
            Button(text=bt, bg="#FFF", font=("Times New Roman", 15),
                   command=com).place(x=x, y=y, width=150, height=65)
            x += 160
            if x > 400:
                x = 10
                y += 75

        Button(text="Ввод", bg="#FFF", font=("Times New Roman", 15),
               command=lambda x="Ввод": self.button_logic(x)).place(x=10, y=470, width=470, height=65)

    def button_logic(self, operation):
        if operation == "Сброс":
            self.action = ""
        elif operation == "Стереть цифру":
            self.action = self.action[0:-1]
        elif operation == "Ввод":
            self.result = guess_single(self.action, number)
            # self.counts = try_count(count)
            # self.lbl_counts.configure(text=self.counts)
            self.lbl_result.configure(text=self.result)
            self.action = "0"
        else:
            if self.action == "0":
                self.action = ""
            self.action += operation
        self.update()

    def update(self):
        if self.action == "":
            self.action = "0"
        self.lbl_number.configure(text=self.action)


root = Tk()
root["bg"] = "#000"
root.geometry("490x550+200+200")
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
