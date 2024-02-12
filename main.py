import customtkinter as ctk
import random
import os

# * Preload runtime information

VERISON = "0.2.0 (CANARY.2122024.020.B1)"
placeholderText = [
    "Once upon a time...",
    "In my imagination...",
    "Just a reminder...",
    "Wanted to say...",
    "I would like to know…",
    "FYI...",
    "A promise I have...",
]

placeholderTitle = [
    "Business meeting",
    "Construction notes",
    "Biology notes",
    "Algebra notes",
    "Reading notes",
    "Informational notes",
    "Awesome notepad",
]

saveDirectory = os.path.expanduser("~/Documents")


# Tab widget
class Menu(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create `tab` objects
        self.add("Note")
        self.add("Settings")

        # ? Set default tab for application
        self.set("Note")

        # Widgets - Note tab

        NoteTitle = ctk.CTkTextbox(
            master=self.tab("Note"),
            corner_radius=15,
            width=700,
            height=50,
        )
        NoteTitle.pack(pady=10)
        NoteTitle.insert("0.0", random.choice(placeholderTitle))

        NoteEntry = ctk.CTkTextbox(
            master=self.tab("Note"),
            corner_radius=20,
            width=700,
            height=530,
            activate_scrollbars=True,
        )
        NoteEntry.pack()
        NoteEntry.insert("0.0", random.choice(placeholderText))

        # Widgets - Settings tab

        AppInfo = ctk.CTkFrame(
            master=self.tab("Settings"), width=200, height=200, corner_radius=5
        )
        AppInfo.pack(pady=10)

        VersionInformation = ctk.CTkLabel(
            master=AppInfo, text=f"Noteable verison: {VERISON}"
        )
        VersionInformation.pack()

        def save_file():
            title = NoteTitle.get("0.0", "end")
            text = NoteEntry.get("0.0", "end")

            with open(
                os.path.join(saveDirectory, f"{title}.txt".replace("\n", "")), "w"
            ) as f:
                f.write(text)

        SaveButton = ctk.CTkButton(
            master=self.tab("Note"), text="Save note to computer", command=save_file
        )

        SaveButton.pack(pady=10)


# * Define application size and information
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(f"Notable - {VERISON}")
        self.geometry("700x700")
        self.resizable(False, False)

        self.tab_view = Menu(master=self, width=700, height=700)
        self.tab_view.pack()


# * Run Application
if "__main__" == __name__:
    ctk.set_default_color_theme("app\green.json")
    app = App()
    app.mainloop()
