import streamlit as st
import random

class ValentineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Валентинка")
        self.root.geometry("600x400")
        self.root.configure(bg="#ffc0cb")

        # Створення полотна для анімації сердечок
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="#ffc0cb", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Масив сердечок
        self.hearts = []
        self.create_hearts()

        # Перша сцена
        self.first_label = tk.Label(
            root, 
            text="Віриш в кохання з першого погляду чи мені пройти ще раз?",
            font=("Arial", 14),
            bg="#ffc0cb"
        )
        self.first_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.yes_button1 = tk.Button(
            root, text="Вірю", command=self.second_scene,
            bg="#ffb6c1", font=("Arial", 12)
        )
        self.yes_button1.place(relx=0.35, rely=0.5, anchor=tk.CENTER)

        self.no_button1 = tk.Button(
            root, text="Не вірю", command=self.second_scene,
            bg="#ffb6c1", font=("Arial", 12)
        )
        self.no_button1.place(relx=0.65, rely=0.5, anchor=tk.CENTER)

        self.animate_hearts()

    def create_hearts(self):
        """Створити сердечки на полотні"""
        for _ in range(20):
            x = random.randint(0, 600)
            y = random.randint(0, 400)
            size = random.randint(10, 30)
            heart = self.canvas.create_text(x, y, text="❤", font=("Arial", size), fill="red")
            speed_x = random.uniform(-1, 1)
            speed_y = random.uniform(1, 3)
            self.hearts.append((heart, speed_x, speed_y))

    def animate_hearts(self):
        """Анімація руху сердечок"""
        for i, (heart, speed_x, speed_y) in enumerate(self.hearts):
            self.canvas.move(heart, speed_x, speed_y)
            x, y = self.canvas.coords(heart)

            # Переміщення сердечок при виході за межі
            if x < 0 or x > 600:
                speed_x *= -1
            if y > 400:
                y = 0
            self.hearts[i] = (heart, speed_x, speed_y)
            self.canvas.coords(heart, x, y)

        self.root.after(50, self.animate_hearts)

    def second_scene(self):
        # Очистити першу сцену
        self.first_label.place_forget()
        self.yes_button1.place_forget()
        self.no_button1.place_forget()

        # Друга сцена
        self.second_label = tk.Label(
            self.root, 
            text="Ти станеш моєю валентинкою? (Дашка шо за крінж)", 
            font=("Arial", 14),
            bg="#ffc0cb"
        )
        self.second_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.yes_button2 = tk.Button(
            self.root, text="Так", command=self.yes_choice,
            bg="#ffb6c1", font=("Arial", 12)
        )
        self.yes_button2.place(relx=0.35, rely=0.5, anchor=tk.CENTER)

        self.no_button2 = tk.Button(
            self.root, text="Ні", command=self.no_choice,
            bg="#ffb6c1", font=("Arial", 12)
        )
        self.no_button2.place(relx=0.65, rely=0.5, anchor=tk.CENTER)

    def yes_choice(self):
        # Очистити другу сцену
        self.second_label.place_forget()
        self.yes_button2.place_forget()
        self.no_button2.place_forget()

        # Відповідь "Так"
        tk.messagebox.showinfo(
            "Результат", 
            "Лох згадав що треба жінку любить. Лох молодець. І я тебе також любить (При зустрічі руки поцілую, бо знаю, що ти це не обереш)))"
        )

    def no_choice(self):
        # Очистити другу сцену
        self.second_label.place_forget()
        self.yes_button2.place_forget()
        self.no_button2.place_forget()

        # Фон чорний, текст "Venom"
        self.root.configure(bg="black")
        self.canvas.pack_forget()

        venom_label = tk.Label(
            self.root, 
            text="Venom", 
            font=("Arial", 55, "bold"), 
            bg="black", fg="white"
        )
        venom_label.pack(pady=20)

        you_lose_label = tk.Label(
            self.root, 
            text="Ю луз", 
            font=("Arial", 20), 
            bg="black", fg="red"
        )
        you_lose_label.pack()

        final_label = tk.Label(
            self.root, 
            text="Вітаю, у вас закохався веном і вирішив вас з'їсти, щоб цю красу більше ніхто не бачив) Він ревнує ж! Цьом",
            font=("Arial", 12), 
            bg="black", fg="white"
        )
        final_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = ValentineApp(root)
    root.mainloop()
