import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    return weight / (height * height)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def on_calculate():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    if weight <= 0 or height <= 0:
        messagebox.showerror("Error", "Weight and height must be positive numbers.")
        return

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")

# GUI setup
root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate BMI", command=on_calculate)
calculate_button.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
