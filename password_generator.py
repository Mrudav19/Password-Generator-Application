import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title('Password Generator')
        master.geometry('250x200')
        master.resizable(0, 0)

        self.label = tk.Label(master, text="Password Length")
        self.label.pack(pady=10)

        self.string_pass = tk.StringVar()
        self.txt = tk.Entry(master, textvariable=self.string_pass)
        self.txt.pack()

        self.btn = tk.Button(master, text="Generate", command=self.process)
        self.btn.pack(pady=10)

    def process(self):
        length = self.get_password_length()

        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        special = '@#$%&*'
        all_chars = lower + upper + digits + special

        if length <= 0:
            messagebox.showerror('Error', 'Password length should be a positive integer')
            return

        if length < 6:
            messagebox.showwarning('Warning', 'Password length is too short, it may not be secure.')

        password = ''.join(random.sample(all_chars, length))
        self.show_result(password)

    def get_password_length(self):
        try:
            length = int(self.string_pass.get())
        except ValueError:
            length = 0
        return length

    def show_result(self, password):
        messagebox.showinfo('Result', f'Your password: {password}\n\nPassword copied to clipboard.')
        pyperclip.copy(password)

def main():
    gui = tk.Tk()
    app = PasswordGeneratorApp(gui)
    gui.mainloop()

if __name__ == "__main__":
    main()
