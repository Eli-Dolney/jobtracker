import os
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = '/Users/elidolney/Desktop/jobtracker/jobtracker-382104-0bafcd7aed9a.json'

def get_user_input(prompt):
    return input(prompt)

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

def main():
    sheet_id = '1WyWTHTaItze8sX4njt1jSn81oLRM_pnlrm7JbBBpCfw' # Replace this with your Google Sheet ID
    
    client_house = get_user_input("Enter the client's house you worked at: ")
    total_hours_worked = float(get_user_input("Enter the total hours worked for the day: "))
    date = get_user_input("Enter the date (YYYY-MM-DD format): ")
    money_made = float(get_user_input("Enter the amount of money made: "))
    miles_driven = float(get_user_input("Enter the miles driven: "))

    data = [client_house, total_hours_worked, date, money_made, miles_driven]
    save_data_to_google_sheets(sheet_id, data)
    print("Data saved to Google Sheets")

if __name__ == "__main__":
    main()

