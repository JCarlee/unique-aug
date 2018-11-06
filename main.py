import os
import glob
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('THF Augs-442548b249e7.json', scope)
gc = gspread.authorize(credentials)
aug_sheet = gc.open('THFInformation').worksheet("AugList")
info_sheet = gc.open('THFInformation').worksheet("Python")

# CHANGE based on your directory storing exported files
local_dir = "C:\\Users\\jcarl\\AppData\\Local\\VirtualStore\\Program Files (x86)\\Everquest\\"

# Create this list from spreadsheet, instead of hard coding
augs = ["Kerafyrm's Final Word", "Eye of the Sleeper", "Xegony's Final Word", "Cazic's Command", "Cazic's Order",
        "Cazic's Wish", "Cazic's Word", "Stone of Dragons", "Stone of Drakes", "Stone of Racnars",
        "Stone of Elder Magic", "Stone of Elder Endurance", "Stone of Elder Health", "Aviak Talon", "Aviak Feather",
        "Aviak Eye", "Kodiak Eye", "Kodiak Fur Hair", "Kodiak Claw", "Shark Eye", "Bloodthirsty Shark Skin",
        "Shark Tooth"]

# Sets inv_files to be a list of filename.txt
inv_files = [os.path.basename(x) for x in glob.glob(local_dir + "*_inv.txt")]

aug_start_col = info_sheet.acell('A2').value
aug_end_col = info_sheet.acell('B2').value
char_row_start = info_sheet.acell('C2').value
char_row_end = info_sheet.acell('D2').value

for inv_file, column in zip(inv_files, range(char_row_start, (char_row_end+1))):
    file = open(local_dir + inv_file, "r")  # Open inv file, read
    file_string = file.read()  # Save inv file contents to a temporary string
    cell_list = aug_sheet.range(aug_start_col + str(column) + ':' + aug_end_col + str(column))
    for aug, cell in zip(augs, cell_list):
        if aug not in file_string:
            cell.value = 'FALSE'
        else:
            cell.value = 'TRUE'
    aug_sheet.update_cells(cell_list)
    file.close()
