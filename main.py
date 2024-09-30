import pyautogui
import time
import threading
import tkinter as tk

clicking = False


def click_every_minute():
    global clicking
    while clicking:
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        time.sleep(60)


def start_clicking(status_label, start_button, stop_button):
    global clicking
    if not clicking:
        clicking = True
        threading.Thread(target=click_every_minute, daemon=True).start()
        update_status_label(status_label, start_button, stop_button)


def stop_clicking(status_label, start_button, stop_button):
    global clicking
    if clicking:
        clicking = False
        update_status_label(status_label, start_button, stop_button)


def update_status_label(status_label, start_button, stop_button):
    if clicking:
        status_label.config(text="Статус: включен", fg="green")
        start_button.config(state="disabled")
        stop_button.config(state="normal")
    else:
        status_label.config(text="Статус: выключен", fg="red")
        start_button.config(state="normal")
        stop_button.config(state="disabled")


def create_status_window():
    root = tk.Tk()
    root.title("Автокликер")

    status_label = tk.Label(root, text="Статус: выключен", font=("Helvetica", 16), fg="red")
    status_label.pack(pady=20)
    start_button = tk.Button(root, text="Включить автокликер", font=("Helvetica", 14),
                             command=lambda: start_clicking(status_label, start_button, stop_button))
    start_button.pack(pady=10)
    stop_button = tk.Button(root, text="Отключить автокликер", font=("Helvetica", 14),
                            command=lambda: stop_clicking(status_label, start_button, stop_button))
    stop_button.pack(pady=10)
    stop_button.config(state="disabled")
    root.mainloop()


create_status_window()
