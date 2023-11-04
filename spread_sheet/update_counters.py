from spread_sheet.validate_google_credentials import validate_credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# The ID and range of the spreadsheet.
SAMPLE_SPREADSHEET_ID = '1ViSZFxvUxX6CGu7EO-4dAMzEGZ_ACX7tK09YeZ6_tuo'
SAMPLE_RANGE_NAME = 'A1:C6'

def update_applyment(company: str) -> bool:
    creds = validate_credentials()

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        #something went wrong
        if not values:
            print('No data found.')
            return False
        
        #update the row
        print(values)
        for index, row in enumerate(values):
            if company in row:
                print(f"the current row is {row}")
                new_value = int(row[1]) + 1
                row[1] = str(new_value)
                
                update_values = [row]
                body = {'values': update_values}
                result = sheet.values().update(
                    spreadsheetId=SAMPLE_SPREADSHEET_ID,
                    range=f"{index+1}:{index+1}",
                    valueInputOption='RAW',
                    body=body).execute()
                return True
        
    except HttpError as err:
        print(err)

    return False

"""
HEADERS_RANGE = '1:1'

def get_action_index(sheet, action: str) -> int:
    headers = sheet.values().get(spreadsheetId = SAMPLE_SPREADSHEET_ID,
                                range = HEADERS_RANGE)
    for index, header in enumerate(headers):
        if header == action:
            return index + 1
    return 0
"""