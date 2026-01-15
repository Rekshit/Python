from tkinter import *
import tkinter as tk
import statistics
import math

# Create main window
root = Tk()
root.title("Project-1: Measure of Central Tendency and Dispersion")
root.minsize(500, 500)
root.maxsize(1200, 988)

# Title and Author
title_label = Label(root, text='Title: Measure of Central Tendency and Dispersion', font=('Arial', 16))
title_label.pack(pady=10)

author_label = Label(root, text='Author Details:', font=('Arial', 12))
author_label.pack()

# Input area
number_label = Label(root, text='Enter List of Numbers:', font=('Arial', 10))
number_label.place(x=10, y=75)

number_text = Text(root, height=1, width=30)
number_text.place(x=180, y=75)

# Central Tendency Section
ctLabel = Label(root, text='Measure of Central Tendency', font=('Arial', 12))
ctLabel.place(x=10, y=130)

var = IntVar()

r1_ct = Radiobutton(root, text="Arithmetic Mean", variable=var, value=1)
r1_ct.place(x=10, y=160)

r2_ct = Radiobutton(root, text="Harmonic Mean", variable=var, value=2)
r2_ct.place(x=10, y=180)

r3_ct = Radiobutton(root, text="Geometric Mean", variable=var, value=3)
r3_ct.place(x=10, y=200)

r4_ct = Radiobutton(root, text="Mode", variable=var, value=4)
r4_ct.place(x=10, y=220)

r5_ct = Radiobutton(root, text="Median", variable=var, value=5)
r5_ct.place(x=10, y=240)

# Output label
result_label = Label(root, text="", font=('Arial', 12), fg='blue')
result_label.place(x=10, y=350)

# Function to calculate result
def calculate():
    try:
        # Get the list of numbers entered
        raw_text = number_text.get("1.0", "end-1c")
        nums = [float(x) for x in raw_text.replace(',', ' ').split()]

        choice = var.get()
        result = None

        if choice == 1:
            result = sum(nums) / len(nums)
            label = "Arithmetic Mean"
        elif choice == 2:
            result = len(nums) / sum(1/x for x in nums)
            label = "Harmonic Mean"
        elif choice == 3:
            product = math.prod(nums)
            result = product ** (1/len(nums))
            label = "Geometric Mean"
        elif choice == 4:
            result = statistics.mode(nums)
            label = "Mode"
        elif choice == 5:
            result = statistics.median(nums)
            label = "Median"
        else:
            result_label.config(text="Please select an option.")
            return

        result_label.config(text=f"{label}: {round(result, 3)}")

    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Calculate Button
calcButton = Button(root, text='Calculate', command=calculate)
calcButton.place(x=10, y=310)

# Quit button
quitButton = Button(root, text='Quit from System', command=root.destroy)
quitButton.pack(padx=5, pady=20, side=tk.BOTTOM)

# Run window
root.mainloop()
