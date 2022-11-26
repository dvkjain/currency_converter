import requests
from bs4 import BeautifulSoup
import tkinter as tk

root = tk.Tk()
root.geometry ("500x500")
root.configure (bg = "#A4A6D6")
root.title ("Prices")

class App:

    def __init__ (self, master):

        self.master = master

        self.variable = tk.StringVar(master)
        self.variable.set ("USD")
        self.currency_options = ["USD", "CAD", "EUR", "BRL", "MXN", "JPY", "AUD", "INR", "TWD"]
        self.options_menu = tk.OptionMenu (master, self.variable, *self.currency_options)

        self.second_variable = tk.StringVar(master)
        self.second_variable.set ("USD")
        self.second_options_menu = tk.OptionMenu (master, self.second_variable, *self.currency_options)


        self.user_input = tk.Entry (master)
        self.to_label = tk.Label (master, text = "to", bg = "#A4A6D6")
        self.final_result = tk.Label (master, bg = "#A4A6D6", borderwidth = 0, highlightthickness = 0, font = "Arial")
        self.convert_btn = tk.Button (master, text = "Convert", width = 10, command = self.convert_currency)

        self.options_menu.grid (row = 2, column = 1, columnspan = 3, pady = 10, padx = 10)
        self.second_options_menu.grid (row = 2, column = 10, pady = 10, padx = 10)
        self.user_input.grid (row = 4, column = 1, rowspan = 4, padx = 10)
        self.to_label.grid (row = 4, column = 6, padx = 20)
        self.final_result.grid (row = 4, column = 8, padx = 20, columnspan = 4)
        self.convert_btn.grid (row = 40, column = 6, pady = 30)

        self.master.bind('<Return>', self.convert_currency)

    def enter_url (self):

        self.currency_to_convert_from = self.variable.get()
        self.final_currency = self.second_variable.get()
        self.amount = self.user_input.get()

        self.url = f"https://www.x-rates.com/calculator/?from={self.currency_to_convert_from}&to={self.final_currency}&amount={self.amount}"
        print (self.url)

        self.response = requests.get(self.url)
        self.content = self.response.content
        self.site = BeautifulSoup(self.content, "html.parser")
        self.price = self.site.find(attrs = {"class": "ccOutputRslt"})

        self.current_price = self.price.text
        self.final_result.configure (text = self.current_price)

    def convert_currency (self):

        self.enter_url()

if __name__ == "__main__":

    App (root)
    root.resizable (False, False)
    root.mainloop()
