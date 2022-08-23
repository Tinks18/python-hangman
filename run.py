import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_hangman')

easy = SHEET.worksheet('easy')

intermediate = SHEET.worksheet('intermediate')
hard = SHEET.worksheet('hard')
data = easy.get_all_records()

# val = easy.acell('A2').value
def sheet_value():
    x = [item for item in intermediate.col_values(1) if item]
    return list(x)

secret = random.choice(sheet_value())
print(secret)




# list_of_dicts = worksheet.get_all_records()
# data1 = intermediate.get_all_values()
# data2 = hard.get_all_values()
# print(data)
# print(val)
# print(data1)
# print(data2)

def get_level_data():
    """
    Get level input from the user.
    """
    print("Choose from Levels: Easy , Intermediate, Hard")

    data_str = input("Please enter level:  ").upper()
    print(f"The level you chose is {data_str}")

# use_sheet = get_level_data()

# def sheet_value():
#     x = [item for item in use_sheet.col_values(1) if item]
#     return list(x)

# secret = random.choice(sheet_value())
# print(secret)
