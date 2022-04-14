import gspread

from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Jordan_palace")


def get_sales_data():
    """
    Request input of trainer name and sales figures for the year from user.
    """
    while True:
        print("Please enter trainer name")
        name_str = input("Enter the name here: ")
        print(f"The name provided is {name_str}\n")
        print("Please enter sales figures for the year.")
        print("Data should be twelve numbers, seperated by commas.")
        print("Example: 1,2,3,4,5,6,7,8,9,10,11,12\n")

        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data 
       

def validate_data(values):
    """
    Converts string values into integers.
    Raises value error if string values can not be converted into integers,
    or if there are not exactly 12 values. 
    """
    try:
        [int(value) for value in values]
        if len(values) != 12:
            raise ValueError(
                f"Exactly 12 values are required, however you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False 

    return True


def update_sales_worksheet(data):
    """
    Update sales worksheet. Add new column with the list data provided. 
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("monthly_sales")
    sales_worksheet.update('G2:G13')
    print("Sales worksheet updated successfully.\n")


data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)


