import pyautogui
import time
import threading
import tkinter as tk

CLICK_STATUS: bool = False
PRESSING_FREQ: int = 60  ## U can change this option


def click_every_minute():
    """
    Activate clicking
    """
    global CLICK_STATUS
    while CLICK_STATUS:
        x, y = pyautogui.position()
        pyautogui.click(x, y)
        time.sleep(PRESSING_FREQ)


def start_clicking(status_label, start_button, stop_button):
    global CLICK_STATUS
    if not CLICK_STATUS:
        CLICK_STATUS: bool = True
        threading.Thread(target=click_every_minute, daemon=True).start()
        update_status_label(status_label, start_button, stop_button)


def stop_clicking(status_label, start_button, stop_button):
    global CLICK_STATUS
    if CLICK_STATUS:
        CLICK_STATUS = False
        update_status_label(status_label, start_button, stop_button)


def update_status_label(status_label, start_button, stop_button):
    if CLICK_STATUS:
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
