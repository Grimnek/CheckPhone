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
        Valid = phonenumbers.is_valid_number(phoneNumber)
        if bool(Valid) == True:
            Valid = "Так"
        else:
            Valid = "Нi"
        phone_answer = f"Operator: {Carrier}\nCountry: {Region}\nValid number: {Valid}"
        text.delete('1.0', END)
        text.insert('1.0', phone_answer)
    except Exception as e:
        messagebox.showerror("Error", "Enter a phone number with phone code.")


def help():
    messagebox.showinfo("Info",
                        """We enter the phone number with phone code and check it for the operator, country and validity of the number.""")


message = StringVar()

message_button = Button(text="Check", padx="20", pady="15", background="#555", foreground="#fff", command=number)
message_button.place(relx=.5, rely=.7, anchor="center")

text = Text(root, width=400, height=400, wrap="word")
text.place(relx=.5, rely=.3, anchor="center", width="350", height="80")
scrollb = Scrollbar(text, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

main_menu.add_cascade(label="Info", command=help)

root.config(menu=main_menu)
root.mainloop()
