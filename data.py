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

"""
to extract values from worksheets

"""
easy = SHEET.worksheet('easy')
data = easy.get_all_values()
easy =[]
x = [item for item in easy.col_values(1) if item]

print (list(x))

normal = SHEET.worksheet('normal')
data1 = normal.get_all_records()
# print(data1)
hard = SHEET.worksheet('hard')
data2 = hard.get_all_records()

# print(data2)

# val = easy.acell('A2').value
def sheet_value():
    
    x = [item for item in normal.col_values(1) if item]
    return list(x)

word = random.choice(sheet_value())
print(word)

levels = [easy, normal, hard]

# def get_level_data(level):
#     """
#     Get level input from the user.
#     """
#     print("\n Choose from Levels: Easy , normal, Hard")

#     level = input("\n Please enter level:  ").upper()
#     print(f"\n The level you chose is {level}")
#     return level

# result = get_level_data(levels)
# print(result)

