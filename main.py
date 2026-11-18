
# import tkinter as tk
# from tkinter import *
# from textblob import TextBlob
# import requests

# root = Tk()
# root.title("Auto corrector and Translator")
# root.geometry("700x400")
# root.config(background="#dae6f6")


# def check_spelling_app():
#     if hasattr(root, 'translation_widgets'):
#         for widget in root.translation_widgets:
#             widget.place_forget()

#     def check_spelling():
#         word = enter_text.get()
#         a = TextBlob(word)
#         right = str(a.correct())
#         spell.config(text="Correct text is: " + right)

#     heading = Label(root, text="Enter a word:",
#                     font=("Trebuchet MS", 30, "bold"),
#                     bg="#dae6f6", fg="black")
#     heading.place(x=170, y=35)

#     check_button = Button(root, text="Check",
#                           font=("Arial", 20, "bold"),
#                           fg="white", bg="orange",
#                           command=check_spelling)
#     check_button.place(x=260, y=105)

#     enter_text = Entry(root, justify="center", width=30,
#                        font=("Poppins", 20),
#                        bg="white", border=2)
#     enter_text.place(x=100, y=170)
#     enter_text.focus()

#     spell = Label(root, text="Correct text is:",
#                   font=("Poppins", 20),
#                   bg="#dae6f6", fg="black")
#     spell.place(x=100, y=240)

#     root.spelling_widgets = [
#         heading, check_button, enter_text, spell
#     ]


# def translation_app():
#     if hasattr(root, 'spelling_widgets'):
#         for widget in root.spelling_widgets:
#             widget.place_forget()

#     def translate_text():
#         text = entry.get()

#         try:
#             url = "https://api.mymemory.translated.net/get"
#             params = {
#                 "q": text,
#                 "langpair": "en|hi"
#             }

#             response = requests.get(url, params=params, timeout=15)
#             response.raise_for_status()

#             data = response.json()
#             translated = data["responseData"]["translatedText"]

#             output_var.config(text=translated)

#         except Exception as e:
#             output_var.config(text="Translation error: " + str(e))

#     label = Label(root, text="Enter Text in English:",
#                   font=("Trebuchet MS", 25, "bold"),
#                   bg="#dae6f6", fg="black")
#     label.place(x=100, y=35)

#     translate_button = Button(root, text="Translate",
#                               font=("Arial", 20, "bold"),
#                               fg="white", bg="orange",
#                               command=translate_text)
#     translate_button.place(x=260, y=105)

#     entry = Entry(root, justify="center", width=30,
#                   font=("Poppins", 20),
#                   bg="white", border=2)
#     entry.place(x=100, y=170)

#     output_var = Label(root, text="Translated Text in Hindi:",
#                        font=("Poppins", 20),
#                        bg="#dae6f6", fg="black",
#                        wraplength=600)
#     output_var.place(x=50, y=240)

#     root.translation_widgets = [
#         label, translate_button, entry, output_var
#     ]


# Sbutton = Button(root, text="Auto Correct",
#                  font=("Arial", 20, "bold"),
#                  fg="white", bg="purple",
#                  command=check_spelling_app)
# Sbutton.place(x=80, y=320)

# Tbutton = Button(root, text="Translator",
#                  font=("Arial", 20, "bold"),
#                  fg="white", bg="purple",
#                  command=translation_app)
# Tbutton.place(x=400, y=320)

# root.mainloop()



import tkinter as tk
from tkinter import *
from textblob import TextBlob
import requests

root = Tk()
root.title("Auto corrector and Translator")
root.geometry("700x400")
root.config(background="#dae6f6")


def check_spelling_app():

    if hasattr(root, 'translation_widgets'):
        for widget in root.translation_widgets:
            widget.place_forget()

    def check_spelling():
        word = enter_text.get()
        a = TextBlob(word)
        right = str(a.correct())
        spell.config(text="Correct text is: " + right)

    heading = Label(
        root,
        text="Enter a word:",
        font=("Trebuchet MS", 30, "bold"),
        bg="#dae6f6",
        fg="black"
    )
    heading.place(x=170, y=25)

    enter_text = Entry(
        root,
        justify="center",
        width=30,
        font=("Poppins", 20),
        bg="white",
        border=2
    )
    enter_text.place(x=100, y=100)

    check_button = Button(
        root,
        text="Check",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="orange",
        command=check_spelling
    )
    check_button.place(x=260, y=165)

    spell = Label(
        root,
        text="Correct text is:",
        font=("Poppins", 20),
        bg="#dae6f6",
        fg="black"
    )
    spell.place(x=100, y=235)

    root.spelling_widgets = [
        heading, enter_text, check_button, spell
    ]


def translation_app():

    if hasattr(root, 'spelling_widgets'):
        for widget in root.spelling_widgets:
            widget.place_forget()

    def translate_text():
        text = entry.get()

        try:
            url = "https://api.mymemory.translated.net/get"

            params = {
                "q": text,
                "langpair": "en|hi"
            }

            response = requests.get(
                url, params=params, timeout=15
            )
            response.raise_for_status()

            data = response.json()
            translated = data["responseData"]["translatedText"]

            output_var.config(text=translated)

        except Exception as e:
            output_var.config(text="Translation error: " + str(e))

    label = Label(
        root,
        text="Enter Text in English:",
        font=("Trebuchet MS", 25, "bold"),
        bg="#dae6f6",
        fg="black"
    )
    label.place(x=100, y=25)

    entry = Entry(
        root,
        justify="center",
        width=30,
        font=("Poppins", 20),
        bg="white",
        border=2
    )
    entry.place(x=100, y=100)

    translate_button = Button(
        root,
        text="Translate",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="orange",
        command=translate_text
    )
    translate_button.place(x=260, y=165)

    output_var = Label(
        root,
        text="Translated Text in Hindi:",
        font=("Poppins", 20),
        bg="#dae6f6",
        fg="black",
        wraplength=600
    )
    output_var.place(x=50, y=235)

    root.translation_widgets = [
        label, entry, translate_button, output_var
    ]


Sbutton = Button(
    root,
    text="Auto Correct",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="purple",
    command=check_spelling_app
)
Sbutton.place(x=80, y=320)

Tbutton = Button(
    root,
    text="Translator",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="purple",
    command=translation_app
)
Tbutton.place(x=400, y=320)

root.mainloop()
