import tkinter as tk
from tkinter import ttk

depvar = 86475
conversion_history = []

def deposit_money():
    global depvar
    depvar += round(float(money_entry.get()))
    show_balance()

def withdraw_money():
    global depvar
    withdrawal_amount = round(float(money_entry.get()))
    if withdrawal_amount <= depvar:
        depvar -= withdrawal_amount
        show_balance()
    else:
        result_label.config(text="Insufficient funds")

def authenticate_pin():
    entered_pin = pin_entry.get()
    if entered_pin == "0077":
        show_balance()
    else:
        result_label.config(text="Incorrect PIN")

def show_balance():
    balance_label.config(text=f"Your bank balance is: {depvar}")

def convert_currency():
    global depvar
    currency_from = from_var.get()
    currency_to = to_var.get()
    amount = round(float(amount_entry.get()))
   
    conversion_rate = get_conversion_rate(currency_from, currency_to)
    total = round(amount * conversion_rate)
    if total <= depvar:
        depvar -= total
        result_label.config(text=f"{amount} {currency_from} is equal to {total} {currency_to}.")
        show_balance()
        conversion_history.append(f"{amount} {currency_from} -> {total} {currency_to}")
    else:
        result_label.config(text="Insufficient funds")

def get_conversion_rate(currency, conversion):
    rates = {
        'GBP': {'USD': 1.27, 'EUR': 1.17, 'AED': 4.68, 'INR': 105.86},
        'USD': {'GBP': 0.79, 'EUR': 0.92, 'AED': 3.67, 'INR': 83.12},
        'EUR': {'USD': 1.09, 'GBP': 0.86, 'AED': 4.00, 'INR': 90.53},
        'AED': {'USD': 0.27, 'EUR': 0.25, 'GBP': 0.21, 'INR': 22.63},
        'INR': {'USD': 0.012, 'EUR': 0.011, 'AED': 0.044, 'GBP': 0.009}
    }
    return rates[currency][conversion]

def show_conversion_history():
    history_window = tk.Toplevel(root)
    history_window.title("Conversion History")
    history_label = tk.Label(history_window, text="Conversion History:")
    history_label.pack()
    for conversion in conversion_history:
        conversion_label = tk.Label(history_window, text=conversion)
        conversion_label.pack()

root = tk.Tk()
root.title("Currency Converter")

pin_label = ttk.Label(root, text="Enter PIN:")
pin_label.grid(row=0, column=0, padx=5, pady=5)

pin_entry = ttk.Entry(root, show="*")
pin_entry.grid(row=0, column=1, padx=5, pady=5)

authenticate_button = ttk.Button(root, text="Check", command=authenticate_pin)
authenticate_button.grid(row=0, column=2, padx=5, pady=5)

from_var = ttk.Combobox(root, values=["GBP", "USD", "EUR", "AED", "INR"], state="readonly")
from_var.grid(row=1, column=1, padx=5, pady=5)
from_var.current(0)

to_var = ttk.Combobox(root, values=["GBP", "USD", "EUR", "AED", "INR"], state="readonly")
to_var.grid(row=2, column=1, padx=5, pady=5)
to_var.current(1)

amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=3, column=0, padx=5, pady=5)

amount_entry = ttk.Entry(root)
amount_entry.grid(row=3, column=1, padx=5, pady=5)

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

money_label = ttk.Label(root, text="Deposit/Withdraw Money:")
money_label.grid(row=5, column=0, padx=5, pady=5)

money_entry = ttk.Entry(root)
money_entry.grid(row=5, column=1, padx=5, pady=5)

deposit_button = ttk.Button(root, text="Deposit", command=deposit_money)
deposit_button.grid(row=6, column=0, padx=5, pady=5)

withdraw_button = ttk.Button(root, text="Withdraw", command=withdraw_money)
withdraw_button.grid(row=6, column=1, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

balance_label = ttk.Label(root, text="")
balance_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

history_button = ttk.Button(root, text="Show Conversion History", command=show_conversion_history)
history_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
