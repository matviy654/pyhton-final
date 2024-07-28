import tkinter as tk


responses = {
    "Привіт"   : "Привіт! Вам потрібно допомогти?",
    "привіт"   : "Привіт! Вам потрібно допомогти?",
    "Дарова"   : "Привіт! Вам потрібно допомогти?",
    "дарова"   : "Привіт! Вам потрібно допомогти?",
    "як справи?": "норм",
    "Як справи?": "чудово",
    "Що ти вмієш?": "Я можу відповідати на прості запитання, та написати код",
    "що ти вмієш?": "Я можу відповідати на прості запитання, та написати код",
    "До побачення"  : "До побачення! Гарного дня вам!",
    "до побачення"  : "До побачення! Гарного дня вам!",
    "напиши код": "ха-ха-ха-ха, НІ!",
    "Напиши код": "ха-ха-ха-ха, НІ!",
    "чому?":"Тому що це важко :(",
    "Чому?":"Тому що це важко :(",

}

def get_response(user_input):
    return responses.get(user_input,"Вибачте,але в моєму сховищі немає відповіді.")

def send_message(event=None):
    user_input = user_entry.get()
    if user_input.strip():
        chat_window.config()
        chat_window.insert(tk.END, f"Ви: {user_input}\n")
        response = get_response(user_input)
        chat_window.insert(tk.END, f"Бот228: {response}\n")
        chat_window.config()
        chat_window.yview(tk.END)
    user_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Чат-Бот від Кравця Матвія")

chat_window = tk.Text(root,   height=20, width=50)
chat_window.pack(pady=10, padx=10)

user_entry = tk.Entry(root, font=("Helvetica", 14))
user_entry.pack(pady=10, padx=10, fill=tk.X)
user_entry.bind("<Return>", send_message)

send_button = tk.Button(root, text="Надіслатити", command=send_message)
send_button.pack(pady=5)

root.mainloop()
