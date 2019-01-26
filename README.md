# Everquest Unique Aug Tool
Script to identify missing unique augments for numerous charecters in Everquest

## Motivation
Playing on the emulated Everquest server, The Hidden Forest, I found myself having trouble managing so many unique augments across multiple characters.
I wanted a way to cleanly visualize which characters had these augs without manually going through each inventory.
Therefore, I decided to create a script to scrape all augs out of inventory dump files, cross reference the augs with a list in Google sheets and finally organize.

I consider myself a novice Python developer so any and all criticism to the approach, code, and documentation is welcome.
Please feel free to email me at JCarlee@gmail.com with suggestions or ideas.
 
## Dependencies
* Python 3
* gspread
* oauth2client.service_account
* glob

```
pip install gspread
```

## Google Sheets Personal Library Setup
* [Create Copy of Template](https://docs.google.com/spreadsheets/d/1X95ZZVY5w94Pm0p9duMocIzvdu8OPTQ9iFitJcsGivA/edit#gid=542426973)
* You need two sheets from this workbook: `AugList` and `Python`
* Modify Character names and Augments to your liking

[OAuth2 setup](https://gspread.readthedocs.io/en/latest/oauth2.html)  
To be named `THF Augs-442548b249e7.json`  

## Inventory dumps

## Author

* **John Carlee** - JCarlee@gmail.com
