import openpyxl
from openpyxl import Workbook
from datetime import datetime
import os

def get_user_input(prompt):
    return input(prompt)

def save_data_to_excel(data, filename):
    if not os.path.exists(filename):
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(['Client House', 'Start Time', 'End Time', 'Date', 'Total Amount', 'Miles Driven', 'Taxes on Driving'])
    else:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
    
    sheet.append(data)
    workbook.save(filename)

def main():
    filename = 'personal_care_assistant_data.xlsx'
    
    client_house = get_user_input("Enter the client's house you worked at: ")
    start_time = get_user_input("Enter the start time (HH:MM format): ")
    end_time = get_user_input("Enter the end time (HH:MM format): ")
    date = get_user_input("Enter the date (YYYY-MM-DD format): ")
    total_amount = float(get_user_input("Enter the total amount made: "))
    miles_driven = float(get_user_input("Enter the miles driven: "))
    taxes_on_driving = float(get_user_input("Enter the taxes on driving: "))
    
    data = [client_house, start_time, end_time, date, total_amount, miles_driven, taxes_on_driving]
    save_data_to_excel(data, filename)
    print("Data saved to '{}'".format(filename))

if __name__ == "__main__":
    main()
