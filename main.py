import tkinter as tk
from tkinter import ttk, messagebox
from base_conversion import *


def base_to_base():
    user_val = convert_val.get()
    user_val = [int(i) for i in user_val]
    user_base = from_base.get()
    to_option_choice = bases.get()

    convert_start = BaseConversion(int(user_base), user_val)
    temp_val = convert_start.to_decimal()
    convert_end = BaseConversion(int(to_option_choice), int(temp_val))
    temp_val = convert_end.from_decimal()
    result = temp_val
    result_entry.insert(0, result)


def convert_base():
    user_val = convert_val.get()
    user_base = from_base.get()
    to_option_choice = bases.get()

    # Clear Previous Result
    result_entry.delete(0, tk.END)

    # Check Empty Input
    if convert_val.get() == '' or from_base.get() == '':
        messagebox.showerror('Empty Fields', 'Please enter the required fields.')
        return

    if to_option_choice == '2':
        if user_base == '10':
            conversion = BaseConversion(int(to_option_choice), int(user_val))
            result = conversion.from_decimal()
            result_entry.insert(0, result)
        base_to_base()

    if to_option_choice == '8':
        if user_base == '10':
            conversion = BaseConversion(int(to_option_choice), int(user_val))
            result = conversion.from_decimal()
            result_entry.insert(0, result)
        base_to_base()

    if to_option_choice == '10':
        if user_base == '16':
            conversion = BaseConversion(int(user_base), int(user_val))
            result = conversion.hex_to_decimal()
            result_entry.insert(0, result)

        user_val = [int(i) for i in user_val]
        conversion = BaseConversion(int(user_base), user_val)
        result = conversion.to_decimal()
        result_entry.insert(0, result)

    if to_option_choice == '16':
        if user_base == '10':
            conversion = BaseConversion(int(to_option_choice), int(user_val))
            result = conversion.from_decimal()
            result_entry.insert(0, result)
        base_to_base()


# Window Setup
root = tk.Tk()
root.title('Numeric Base Conversion')
root.geometry('560x220')
root.resizable(width=False, height=False)

# Convert Value
convert_val = tk.StringVar()
val_label = tk.Label(root, text='Value', font='Helvetica 14 bold', pady=10)
val_label.grid(row=0, column=0)
val_entry = tk.Entry(root, textvariable=convert_val)
val_entry.grid(row=1, column=0, padx=30)

# From Base
from_base = tk.StringVar()
from_base_label = tk.Label(root, text='From Base', font='Helvetica 14 bold', pady=10)
from_base_label.grid(row=3, column=0)
from_base_entry = tk.Entry(root, textvariable=from_base)
from_base_entry.grid(row=4, column=0, padx=30)

# Dropdown Selection
to_base = tk.StringVar()
selection_label = tk.Label(root, text='To Base', font='Helvetica 14 bold', pady=15)
selection_label.grid(row=0, column=1)
bases = ttk.Combobox(root, width=25, textvariable=to_base, state='readonly')

bases['values'] = (
    '2',
    '8',
    '10',
    '16'
)

bases.grid(row=1, column=1)
bases.current(2)

# Result
result_label = tk.Label(root, text='Result', font='Helvetica 14 bold')
result_label.grid(row=3, column=1)
result_entry = tk.Entry(root)
result_entry.grid(row=4, column=1)
convert_btn = tk.Button(root, text='Convert', width=12, command=lambda: convert_base())
convert_btn.grid(row=5, column=1, pady=10)

# Start Program
root.mainloop()
