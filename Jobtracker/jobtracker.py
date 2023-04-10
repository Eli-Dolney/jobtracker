import os
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = "D:\job tracker\jobtracker-382104-8b3c34d48a56.json"

def get_google_sheets_service():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    return service

def save_data_to_google_sheets(sheet_id, data):
    service = get_google_sheets_service()
    body = {
        'range': 'A1',
        'values': [data],
        'majorDimension': 'ROWS'
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range='A1',
        valueInputOption='RAW',
        insertDataOption='INSERT_ROWS',
        body=body).execute()

def submit_data():
    sheet_id = '1WyWTHTaItze8sX4njt1jSn81oLRM_pnlrm7JbBBpCfw' # Replace this with your Google Sheet ID
    
    client_house = client_house_entry.get()
    total_hours_worked = float(total_hours_worked_entry.get())
    date = date_entry.get()
    money_made = float(money_made_entry.get())
    miles_driven = float(miles_driven_entry.get())

    data = [client_house, total_hours_worked, date, money_made, miles_driven]
    save_data_to_google_sheets(sheet_id, data)
    result_label.config(text="Data saved to Google Sheets")

root = tk.Tk()
root.title("Job Tracker")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=3)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)

default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=12)

label_font = tkfont.Font(size=12, weight="bold")

client_house_entry = ttk.Entry(mainframe, font=default_font)
client_house_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
ttk.Label(mainframe, text="Client's house:", font=label_font).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

total_hours_worked_entry = ttk.Entry(mainframe, font=default_font)
total_hours_worked_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
ttk.Label(mainframe, text="Total hours worked:", font=label_font).grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

date_entry = ttk.Entry(mainframe, font=default_font)
date_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
ttk.Label(mainframe, text="Date (YYYY-MM-DD):", font=label_font).grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

money_made_entry = ttk.Entry(mainframe, font=default_font)
money_made_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
ttk.Label(mainframe, text="Money made:", font=label_font).grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

miles_driven_entry = ttk.Entry(mainframe, font=default_font)
miles_driven_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
ttk.Label(mainframe, text="Miles driven:", font=label_font).grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

submit_button = ttk.Button(mainframe, text="Submit", command=submit_data, style='Submit.TButton')
submit_button.grid(row=5, column=1, pady=10)

result_label = ttk.Label(mainframe, text="", font=default_font)
result_label.grid(row=6, column=0, columnspan=2)

# Button style
style = ttk.Style()
style.configure('Submit.TButton', font=default_font)

root.mainloop()

