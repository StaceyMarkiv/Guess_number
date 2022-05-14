import random
from tkinter import *
from game_logic import guess_single, try_count

number = random.randint(1, 100)
max_count = 4  # Максимальное число ходов


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.count = 0
        self.try_counts = "Try No. 0"
        self.lbl_counts = Label(text="Count label")
        self.result = "Some result"
        self.lbl_result = Label(text="Result label")
        self.action = "Button press"
        self.lbl_number = Label(text="Number label")
        self.build()

    def build(self):
        # Вывод результата
        self.result = "Введите число:"
        self.lbl_result = Label(text=self.result, font=("Times New Roman", 16, "bold"),
                                bg="#00008B", foreground="#FFF")
        self.lbl_result.place(x=11, y=20)

        # Счетчик попыток
        self.count = 1
        self.try_counts = f"Попытка № {self.count}"
        self.lbl_counts = Label(text=self.try_counts, font=("Times New Roman", 16, "bold"),
                                bg="#00008B", foreground="#FFF")
        self.lbl_counts.place(x=11, y=60)

        # Ввод числа игроком
        self.action = "0"
        self.lbl_number = Label(text=self.action, font=("Times New Roman", 21, "bold"),
                                bg="#00008B", foreground="#FFF")
        self.lbl_number.place(x=11, y=100)

        # Кнопки на панели
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
            Button(text=bt, bg="#87CEFA", foreground="#00008B", font=("Times New Roman", 16, "bold"),
                   command=com).place(x=x, y=y, width=150, height=65)
            x += 160
            if x > 400:
                x = 10
                y += 75

        Button(text="Ввод", bg="#87CEFA", foreground="#00008B", font=("Times New Roman", 24, "bold"),
               command=lambda x="Ввод": self.button_logic(x)).place(x=10, y=470, width=470, height=65)

        # Перезапуск игры
        # Button(text="Начать сначала", bg="#87CEFA", foreground="#00008B", font=("Times New Roman", 12, "bold"),
        #        command=lambda x="Ввод": self.button_logic(x)).place(x=330, y=10, width=150, height=25)

    def button_logic(self, operation):
        if operation == "Сброс":
            self.action = ""
        elif operation == "Стереть цифру":
            self.action = self.action[0:-1]
        elif operation == "Ввод":
            self.count += 1
            self.try_counts, endgame = try_count(self.count, max_count)  # Проверка номера попытки
            if endgame:  # Превышено число попыток
                self.result = endgame
                self.action = f"Правильный ответ: {number}"
            else:
                self.lbl_counts.configure(text=self.try_counts)  # Обновление вывода номера попытки
                self.result, win_number = guess_single(self.action, number)  # Определение результата
                if win_number:  # Игрок угадал число
                    self.action = win_number
                else:
                    self.action = "0"
            self.lbl_result.configure(text=self.result)  # Обновление вывода результата
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
root["bg"] = "#00008B"
root.geometry("490x550+400+100")
root.title("Угадай число")
root.resizable(False, False)
app = Main(root)
app.pack()
root.mainloop()
