import customtkinter as ctk
import random
import os

#* Preload runtime information

VERISON = '0.1.0'
placeholderText = [
    'Once upon a time...', 
    'In my imagination...',
    'Just a reminder...',
    'Wanted to say...',
    'I would like to know…',
    'FYI...',
    'A promise I have...'
    ]

placeholderTitle = [
    'Business meeting',
    'Construction notes',
    'Biology notes',
    'Algebra notes',
    'Reading notes',
    'Informational notes',
    'Awesome notepad'
    ]

saveDirectory = os.path.expanduser("~/Documents")


#* Define application size and information
app = ctk.CTk()
app.title('Notable')
app.geometry("700x700")
app.resizable(False, False)

tabview = ctk.CTkTabview(master=app, width=700, height=700)
tabview.pack()

tabview.add("Note")
tabview.add("Settings")

#? Set default tab for application
tabview.set("Note")

# Widgets - Note tab
NoteTitle = ctk.CTkTextbox(
    master=tabview.tab("Note"),
    corner_radius=15,
    width=700,
    height=50,
)
NoteTitle.pack(pady=10)
NoteTitle.insert("0.0", random.choice(placeholderTitle))

NoteEntry = ctk.CTkTextbox(
    master=tabview.tab("Note"),
    corner_radius=20,
    width=700,
    height=530,
    activate_scrollbars=True
)
NoteEntry.pack()
NoteEntry.insert("0.0", random.choice(placeholderText))

# Widgets - Settings tab

AppInfo = ctk.CTkFrame(
    master=tabview.tab("Settings"), 
    width=200, 
    height=200, 
    corner_radius=5
)
AppInfo.pack(pady=10)

VersionInformation = ctk.CTkLabel(
    master=AppInfo,
    text=f'Noteable verison: {VERISON}'
)
VersionInformation.pack()

#* Noteable API and funcutionality

def save_file():
    title = NoteTitle.get("0.0", "end")
    text = NoteEntry.get("0.0", "end")

    with open(os.path.join(saveDirectory, f'{title}.txt'.replace("\n", "")), 'w') as f:
        f.write(text)


# Widget - Save function
SaveButton = ctk.CTkButton(
    master=tabview.tab("Note"),
    text="Save note to computer",
    command=save_file
)

SaveButton.pack(pady=10)

#* Run Application
if '__main__' == __name__:
    app.mainloop()