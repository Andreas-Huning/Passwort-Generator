import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import random

#Variablen
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
specials = '!"§$%&_.,:;'
mathSymbols = "+-*/"
brackets= "(){}[]"

def resource_path(relative_path):
    """ Gibt Pfad zur Datei, auch im PyInstaller-Build """
    try:
        # PyInstaller erstellt einen temporären Pfad _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Funktion zum Beenden
def close_tool():
    root.destroy()   

# Funktion zum erstellen des Passwortes
def generate_password():
    # Alle Checkboxen in einer Liste zur einfacheren Prüfung
    options = [
        (letterUppercase.get(), letters.upper()),
        (letterLowercase.get(), letters),
        (number.get(), numbers),
        (specialChar.get(), specials),
        (mathSymbol.get(), mathSymbols),
        (bracket.get(), brackets)
    ]

    # Prüfen, ob mindestens eine Option gewählt wurde
    if not any(opt[0] for opt in options):
        infoLabel.config(text="Please select at least one character type")
        return
    else:
        infoLabel.config(text="")

    # Länge des Passwortes holen und prüfen
    try:
        passwordLength = int(numberInput.get())
    except ValueError:
        infoLabel.config(text="Please enter an integer")
        return

    # Alle ausgewählten Zeichengruppen zusammenfügen
    chars = ''.join(group for selected, group in options if selected)

    # Liste aus Zeichen machen, mischen und wieder zusammenfügen
    char_list = list(chars)
    random.shuffle(char_list)
    chars = ''.join(char_list)

    # Passwort generieren
    password = ''#.join(random.choice(chars) for x in range(passwordLength))
    for i in range(passwordLength):
        password += random.choice(chars)
        try:
            separatorLenght = int(numberInputSeparator.get())
            if separatorLenght > 0 :
                if ( i + 1 ) % separatorLenght == 0 and ( i + 1 ) != passwordLength:
                    password += '-'
        except ValueError:
            print("Fehler")

        
    # Passwort anzeigen
    output_Password.delete(0, tk.END)
    output_Password.insert(0, password)



def copy_to_clipboard():
    password = output_Password.get()
    if password:
        root.clipboard_clear()            # Zwischenablage leeren
        root.clipboard_append(password)   # Text in Zwischenablage kopieren
        root.update()                     # Damit es direkt übernommen wird (Wichtig!)
        infoLabel.config(text="Password copied to clipboard")  # Feedback für den Nutzer
    else:
        infoLabel.config(text="No password to copy")


#Gui erstellen
root = tk.Tk()

# Variablen
letterUppercase = tk.IntVar(value=0)  # Startwert: 0 = nicht ausgewählt  / 1 = ausgewählt
letterLowercase = tk.IntVar(value=0)
number = tk.IntVar(value=0)
specialChar = tk.IntVar(value=0)
mathSymbol = tk.IntVar(value=0)
bracket = tk.IntVar(value=0)
spin_var = tk.StringVar(value="16")
spin_var2 = tk.StringVar(value="0")

#Titelleiste
root.title("Generate Password") 

#Standardgröße setzen Breite x Höhe          
root.geometry("450x320")

#Deaktiviere das Skalieren (weder in Breite noch in Höhe)                 
root.resizable(False, False)           

# Icon oben links & in Taskleiste
root.iconbitmap(resource_path("assets/favicon.ico"))

#Fenster aktivieren (in den Vordergrund setzen)
root.focus()                            


# Spalten 0–5 konfigurieren, damit sie sich mitvergrößern
for i in range(6):
    root.grid_columnconfigure(i, weight=1)

# Grid-Zeilen konfigurieren
# Zeile 0 = Titel
# Zeile 1-7 = Inhalt
# Zeile 9 = Stretch-Zeile (füllt alles dazwischen)
# Zeile 10 = Button & Copyright
root.grid_rowconfigure(8, weight=1)  # Hauptinhalt stretchbar

#Label erstellen
title_label = ttk.Label(root,text="Generate your Password",font=("Arial",25),anchor="center")
title_label.grid(column=0, row=0, columnspan=6, sticky="nsew")

# Frame für Label + Entry
input_frame = ttk.Frame(root)
input_frame.grid(column=0, row=1, columnspan=6, sticky="w", padx=20, pady=(10, 0))

# Label im Frame
inputLabel = ttk.Label(input_frame, text="Password length: ")
inputLabel.grid(column=0, row=0, sticky="w")

# Entry im Frame
#numberInput = ttk.Entry(input_frame, width=10)
numberInput = ttk.Spinbox(input_frame, from_=1, to=100, increment=1, width=10, textvariable=spin_var)
numberInput.grid(column=1, row=0, sticky="w")

# Info Label im Frame
input_frame.grid_columnconfigure(3, weight=1)  # Label soll mitwachsen
infoLabel = ttk.Label(input_frame, text="")
infoLabel.grid(column=3, columnspan=4, row=0, sticky="ew")


#Checkbox
chkbtn1 = ttk.Checkbutton(root, text ='Uppercase ( A-Z )',variable=letterUppercase, takefocus = 1)
chkbtn2 = ttk.Checkbutton(root, text ='Lowercase ( a-z )',variable=letterLowercase, takefocus = 1)
chkbtn3 = ttk.Checkbutton(root, text ='Numbers ( 0-9 )',variable=number, takefocus = 1)
chkbtn4 = ttk.Checkbutton(root, text ='Specials ( !"§$%&_.,:; )',variable=specialChar, takefocus = 1)
chkbtn5 = ttk.Checkbutton(root, text ='Math symbols ( +-*/ )',variable=mathSymbol, takefocus = 1)
chkbtn6 = ttk.Checkbutton(root, text ='Brackets ( (){}[] )',variable=bracket, takefocus = 1)

chkbtn1.grid(column=0, row=2, columnspan=2, sticky="w", pady=(10,0), padx=20)
chkbtn2.grid(column=0, row=3, columnspan=2, sticky="w", padx=20)
chkbtn3.grid(column=0, row=4, columnspan=2, sticky="w", padx=20)
chkbtn4.grid(column=3, row=2, columnspan=2, sticky="w", pady=(10,0),padx=20)
chkbtn5.grid(column=3, row=3, columnspan=2, sticky="w", padx=20)
chkbtn6.grid(column=3, row=4, columnspan=2, sticky="w", padx=20)

# Trennzeichen einfügen für zum Beispiel Seriennummern
# Frame für Label + Entry
input_frame_separator = ttk.Frame(root)
input_frame_separator.grid(column=0, row=5, columnspan=6, sticky="w", padx=20, pady=(10, 0))

# Label im Frame
inputLabelSeparator = ttk.Label(input_frame_separator, text="Separator '-' every x characters ")
inputLabelSeparator.grid(column=0, row=0, sticky="w")

# Entry im Frame
#numberInput = ttk.Entry(input_frame, width=10)
numberInputSeparator = ttk.Spinbox(input_frame_separator, from_=0, to=100, increment=1, width=5, textvariable=spin_var2)
numberInputSeparator.grid(column=1, row=0, sticky="w", padx=10)

# Frame für Label + Entry
output_frame = ttk.Frame(root)
output_frame.grid(column=0, row=6, columnspan=6, sticky="nsew", padx=20, pady=(10, 0))

# Konfiguriere die Spalte im Frame, damit sie sich ausdehnt
output_frame.grid_columnconfigure(0, weight=1)

# Label im Frame
outputLabel = ttk.Label(output_frame, text="Your Password: ")
outputLabel.grid(column=0, row=0, sticky="w")

# Entry im Frame
output_Password = ttk.Entry(output_frame, width=10,font=("Arial",15))
output_Password.grid(column=0, columnspan=6, row=1, sticky="nsew")

# starte das Programm
startButton = ttk.Button(root, text="start",command=generate_password)
startButton.grid(column=0, row=7, padx=(20,0), pady=(10,10), sticky="w")

# Kopieren in die Zwischenablage
copy_button = ttk.Button(root, text="copy", command=copy_to_clipboard)
copy_button.grid(column=1, row=7, padx=(0,0), pady=(10,10), sticky="w")

# Beendet das Programm
close_button = ttk.Button(root, text="close",command=close_tool)
close_button.grid(column=5, row=9, padx=(0,10), pady=(0,10), sticky="e")

# Copyright
copyright_label = ttk.Label(root, text="© 2025 Andreas Huning")
copyright_label.grid(column=0, row=9, columnspan=2, sticky="w", padx=(10,0), pady=(0,10))

#öffnet das Fenster und hält es offen
root.mainloop() 