# Parse inventory export
#  Open file
#  Use list of augs to search, return true or false
# Compare aug_list to parse
# Return all augs not found in parse
import os
import glob

local_dir = "C:\\Users\\jcarl\\AppData\\Local\\VirtualStore\\Program Files (x86)\\Everquest\\"

augs = "Kerafyrm's Final Word", "Eye of the Sleeper", "Xegony's Final Word", "Cazic's Command", "Cazic's Order", \
       "Cazic's Wish", "Cazic's Word", "Stone of Dragons", "Stone of Drakes", "Stone of Racnars",\
       "Stone of Elder Magic", "Stone of Elder Endurance", "Stone of Elder Health", "Aviak Talon", "Aviak Feather", \
       "Aviak Eye", "Kodiak Eye", "Kodiak Fur Hair", "Kodiak Claw", "Shark Eye", "Bloodthirsty Shark Skin", \
       "Shark Tooth"

# Sets inv_files to be a list of filename.txt
inv_files = [os.path.basename(x) for x in glob.glob(
    "C:\\Users\\jcarl\\AppData\\Local\\VirtualStore\\Program Files (x86)\\Everquest\\*_inv.txt")]

# For loop that calls a function for each file
for inv_file in inv_files:
    print('\n' + inv_file.replace('_inv.txt', ''))
    file = open(local_dir + inv_file, "r")
    file_string = file.read()
    for aug in augs:
        if aug not in file_string:
            print(aug)
    file.close()


# Define main comparison functionality
# def compare(x):
#     pass


# file = open(filename, "r")
#
# if "Eye of the Sleeper" in file.read():
#     print("true")
#
#
#
# for i in augs:
