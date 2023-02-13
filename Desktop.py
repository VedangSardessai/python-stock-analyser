import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("10800*10800")


def choose_stock_and_indicator():
    print('Test')


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand='true')

label = customtkinter.CTkLabel(master=frame, text="Analyze Stock")
label.pack(pady=12, padx=10)

stockDropdownLabel = customtkinter.CTkLabel(master=frame, text="Choose a Company you want to analyze")
stockDropdownLabel.pack(pady=12, padx=10)

stockChosen = ""
indicatorChosen = ""


def stock_menu_callback(choice):
    stockChosen = choice
    print("Stock Chosen:", stockChosen)


def indicator_menu_callback(choice):
    indicator = choice
    print("Indicator Chosen:", stockChosen)


stockDropdown = customtkinter.CTkOptionMenu(master=frame,
                                            values=['ADANIPORTS', 'APOLLOHOSP', 'ASIANPAINT', 'AXISBANK',
                                                    'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 'BHARTIARTL',
                                                    'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB',
                                                    'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFC',
                                                    'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO',
                                                    'HINDUNILVR', 'ICICIBANK', 'INDUSINDBK', 'INFY',
                                                    'ITC', 'JSWSTEEL', 'KOTAKBANK', 'LT',
                                                    'M&M', 'MARUTI', 'NESTLEIND', 'NTPC',
                                                    'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE',
                                                    'SBIN', 'SHREECEM', 'SUNPHARMA', 'TATACONSUM',
                                                    'TATAMOTORS', 'TATASTEEL', 'TCS', 'TECHM',
                                                    'TITAN', 'ULTRACEMCO', 'UPL', 'WIPRO'],
                                            command=stock_menu_callback)

stockDropdown.pack(padx=20, pady=10)
stockDropdown.set("Choose a Stock")  # set initial value

indicatorDropDownLabel = customtkinter.CTkLabel(master=frame, text='Choose Indicator to apply for your analysis')
indicatorDropDownLabel.pack(pady=12, padx=10)

indicatorDropDown = customtkinter.CTkOptionMenu(master=frame,
                                                values=['SMA-5', 'SMA-7', 'SMA-9', 'SMA-12', 'SMA-21', 'SMA-50',
                                                        'SMA-100', 'SMA-200', 'EMA-5', 'EMA-7', 'EMA-9', 'EMA-12',
                                                        'EMA-21', 'EMA-50', 'EMA-100', 'EMA-200'],
                                                command=stock_menu_callback)

indicatorDropDown.pack(padx=20, pady=10)
indicatorDropDown.set("Choose an indicator")  # set initial value

root.mainloop()

