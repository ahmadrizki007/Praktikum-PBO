import tkinter as tk
import random
from tkinter import messagebox

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5

def check_number():
    global attempts

    try:
        guess = int(guess_entry.get())
        attempts += 1

        if guess == secret_number:
            messagebox.showinfo("Tebakan Benar", f"Selamat! Anda menebak angka {secret_number} dengan benar.")
            window.destroy()
        elif attempts >= max_attempts:
            messagebox.showinfo("Game Over", f"Anda tidak berhasil menebak angka {secret_number}. Permainan berakhir.")
            window.destroy()
        else:
            if guess < secret_number:
                result_label.config(text="Tebakan terlalu rendah.")
            else:
                result_label.config(text="Tebakan terlalu tinggi.")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid.")

window = tk.Tk()
window.title("Tebak Angka")

guess_label = tk.Label(window, text="Tebakan Anda:")
guess_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

submit_button = tk.Button(window, text="Submit", command=check_number)
submit_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
