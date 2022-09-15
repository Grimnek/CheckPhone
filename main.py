import tkinter
from tkinter import messagebox, StringVar, VERTICAL, Button, Scrollbar, Menu, Tk, Text, END
import phonenumbers
from phonenumbers import geocoder, carrier

width = 400
height = 200

root = Tk()
root.title("CheckPhoneNumberPy")
root.geometry(f"{width}x{height}+700+250")
root.minsize(width, height)
root.maxsize(width, height)
main_menu = Menu()


def number():
    try:
        data = text.get('1.0', tkinter.END)
        phoneNumber = phonenumbers.parse(data)
        Carrier = carrier.name_for_number(phoneNumber, 'en')
        Region = geocoder.description_for_number(phoneNumber, 'en')
        valid = phonenumbers.is_valid_number(phoneNumber)
        if bool(valid) == True:
            valid = "Так"
        else:
            valid = "Нi"
        phone_answer = f"Оператор: {Carrier}\nКраїна: {Region}\nДійсний номер: {valid}"
        text.delete('1.0', END)
        text.insert('1.0', phone_answer)
    except Exception as e:
        messagebox.showerror("Помилка", "Введіть номер телефону.")


def help():
    messagebox.showinfo("Інформація",
                        """Вписуємо номер телефону та перевіряємо його на оператора, країну та дійсність номера.""")


message = StringVar()

message_button = Button(text="Перевірити", padx="20", pady="15", background="#555", foreground="#fff", command=number)
message_button.place(relx=.5, rely=.7, anchor="center")

text = Text(root, width=400, height=400, wrap="word")
text.place(relx=.5, rely=.3, anchor="center", width="350", height="80")
scrollb = Scrollbar(text, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

main_menu.add_cascade(label="Інформація", command=help)

root.config(menu=main_menu)
root.mainloop()
