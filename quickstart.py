from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1RNPpdQKnt6Y9FTbYA6B7yXQzqXarkxLt-SYnzazz0gY'
SAMPLE_RANGE_NAME = 'Sheet1!A2:E2'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    spreadsheet_id = '1RNPpdQKnt6Y9FTbYA6B7yXQzqXarkxLt-SYnzazz0gY'
    range_name = 'Sheet1!E2:E2'
    values = [
        [
            "TRUE"
        ],
        # Additional rows ...
    ]
    body = {
        'values': values
    }
    result = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_name,
                                                    valueInputOption='USER_ENTERED', body=body).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s' % (row[0]))


if __name__ == '__main__':
    main()
