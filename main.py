# Parse inventory export
#  Open file
#  Use list of augs to search, return true or false
# Compare aug_list to parse
# Return all augs not found in parse
import os
import glob
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('THF Augs-442548b249e7.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('THFInformation').worksheet("AugList")

# wks.update_acell('B1', 'Value')

local_dir = "C:\\Users\\jcarl\\AppData\\Local\\VirtualStore\\Program Files (x86)\\Everquest\\"

augs = "Kerafyrm's Final Word", "Eye of the Sleeper", "Xegony's Final Word", "Cazic's Command", "Cazic's Order", \
       "Cazic's Wish", "Cazic's Word", "Stone of Dragons", "Stone of Drakes", "Stone of Racnars",\
       "Stone of Elder Magic", "Stone of Elder Endurance", "Stone of Elder Health", "Aviak Talon", "Aviak Feather", \
       "Aviak Eye", "Kodiak Eye", "Kodiak Fur Hair", "Kodiak Claw", "Shark Eye", "Bloodthirsty Shark Skin", \
       "Shark Tooth"

# Sets inv_files to be a list of filename.txt
inv_files = [os.path.basename(x) for x in glob.glob(
    "C:\\Users\\jcarl\\AppData\\Local\\VirtualStore\\Program Files (x86)\\Everquest\\*_inv.txt")]

char_names = ['Apoth', 'Vwar', 'Takn', 'Guvian', 'Crit', 'Calleagh', 'Topson', 'Euvian']
col_list = ['D', 'E', 'F', 'G', 'H', 'I', 'J' 'K']

# For loop that calls a function for each file

for inv_file, no in zip(inv_files, range(6, 14)):
    # print('\n' + inv_file.replace('_inv.txt', ''))
    file = open(local_dir + inv_file, "r")
    file_string = file.read()
    cell_list = wks.range('B' + str(no) + ':W' + str(no))
    for aug, cell in zip(augs, cell_list):
        if aug not in file_string:
            #print("FALSE")
            cell.value = 'FALSE'
        else:
            #print("TRUE")
            cell.value = 'TRUE'
    wks.update_cells(cell_list)
    file.close()
