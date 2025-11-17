import tkinter as tk
from tkinter import ttk
from utils.resource_path import get_resource_path
from config import FAVICON, CURRENT_YEAR

def get_message_box(title, message, auto_close_time=0):
    # Aktuelle Zeile im Grid
    rowNumber = 0

    # Style-Objekt erstellen
    style = ttk.Style()

    # Verschiedene Styles konfigurieren
    style.configure("Red.TLabel", foreground="red")
    style.configure("Green.TLabel", foreground="green")
    style.configure("Yellow.TLabel", foreground="yellow")
    style.configure("Blue.TLabel", foreground="blue")
    style.configure("Black.TLabel", foreground="black")
    style.configure("Countdown.TLabel", foreground="gray", font=("Arial", 10))

    # Neues Fenster erstellen
    window = tk.Toplevel()
    window.title(title)
    window.resizable(False, False)
    window.focus()
    window.iconbitmap(get_resource_path(FAVICON))

    # Spalten- und Zeilenkonfiguration
    for i in range(6):
        window.grid_columnconfigure(i, weight=1)
    window.grid_rowconfigure(2, weight=1)

    # Titel-Style wählen
    if title == "Success":
        style_name = "Green.TLabel"
    elif title == "Hint":
        style_name = "Yellow.TLabel"
    elif title == "Error":
        style_name = "Red.TLabel"
    elif title == "Info":
        style_name = "Black.TLabel"
    else:
        style_name = "Blue.TLabel"

    # Titel-Label
    title_label = ttk.Label(
        window,
        text=title,
        font=("Arial", 25),
        anchor="center",
        wraplength=400,
        style=style_name
    )
    title_label.grid(row=rowNumber, column=0, columnspan=6, sticky="nsew", padx=10, pady=10)

    #Eine Reihe erhöhen
    rowNumber += 1

    # Nachrichten-Label
    message_label = ttk.Label(
        window,
        text=message,
        font=("Arial", 15),
        anchor="center",
        wraplength=400
    )
    message_label.grid(row=rowNumber, column=0, columnspan=6, sticky="nsew", padx=10, pady=10)


    # Optionales Countdown-Label
    if auto_close_time > 0:
        #Eine Reihe erhöhen
        rowNumber += 1
        countdown_var = tk.StringVar()
        countdown_var.set(f"Schließt automatisch in {auto_close_time} Sekunden …")

        countdown_label = ttk.Label(
            window,
            textvariable=countdown_var,
            style="Countdown.TLabel"
        )
        countdown_label.grid(row=rowNumber, column=0, columnspan=6, sticky="nsew", padx=10, pady=(0, 10))
        rowNumber += 1
    else:
        countdown_var = None

    #Eine Reihe erhöhen
    rowNumber += 1
    # Stretchzeile
    #Eine Reihe erhöhen
    rowNumber += 1

    # Footer
    copyright_label = ttk.Label(
        window,
        text=f"© {CURRENT_YEAR} Andreas Huning"
    )
    copyright_label.grid(row=rowNumber, column=0, columnspan=3, sticky="w", padx=(10, 0), pady=10)

    # Fenster schließen
    def close_window():
        window.destroy()

    close_button = ttk.Button(window, text="Close", command=close_window)
    close_button.grid(row=rowNumber, column=3, columnspan=3, sticky="e", padx=(0, 10), pady=10)

    # Fenster positionieren
    window.update_idletasks()
    width = window.winfo_reqwidth()
    height = window.winfo_reqheight()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

    # Fokus auf das neue Fenster legen
    window.grab_set()

    # Countdown starten, wenn nötig
    if auto_close_time > 0 and countdown_var is not None:
        def update_countdown(seconds_left):
            if seconds_left > 0:
                countdown_var.set(f"Schließt automatisch in {seconds_left} Sekunden …")
                window.after(1000, update_countdown, seconds_left - 1)
            else:
                close_window()

        update_countdown(auto_close_time)

    # Warten bis das Fenster geschlossen wird
    window.wait_window()
