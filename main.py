import customtkinter as ctk
import random

#* Notable runtime and API

VERISON = '0.1.0'
placeholdertext = [
    'Once upon a time...', 
    'In my imagination...',
    'Just a reminder...',
    'Wanted to say...',
    'I would like to know…',
    'FYI...',
    'A promise I have...'
    ]


#* Define application size and information
app = ctk.CTk()
app.title('Notable')
app.geometry("700x700")

tabview = ctk.CTkTabview(master=app, width=700, height=700)
tabview.pack()

tabview.add("Note")
tabview.add("Settings")

#? Set default tab for application
tabview.set("Note")

# Widgets
NoteEntry = ctk.CTkEntry(
    master=tabview.tab("Note"), 
    placeholder_text=random.choice(placeholdertext),
    corner_radius=20,
    width=700,
    height=600,
    )
NoteEntry.pack()

#* Run Application
if '__main__' == __name__:
    app.mainloop()