import random
from tarotcard import *
import tkinter as tk
import customtkinter


# Function which randomly select a card
def pickcard():
    random_key = random.choice(list(majorarcana.keys()))
    output.delete("1.0", tk.END)  
    output.insert(tk.END, majorarcana[random_key])



root = customtkinter.CTk()
root.title("Tarot card reader")
root.geometry("500x300")

label = customtkinter.CTkLabel(root, text="Tarot card reader", height=50, width=50, fg_color="transparent", font=("Arial", 20))
label.pack()

# The button for pick a card
get_input_button = customtkinter.CTkButton(root, text='Pick a Card', width=50, command=pickcard)
get_input_button.pack(padx=5, pady=5)

# Show the result
output = customtkinter.CTkTextbox(root, height=150, width=400, font=("Arial", 20))
output.pack()


root.mainloop()