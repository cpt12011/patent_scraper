# Selection and output of google patent data to excel file
import pandas as pd

#Write the path to your python script here. You can do this by checking the directory location of your python script.
#Make sure to move all csv files to the same folder as the py script is in
mypath=r'YOUR PATH HERE'
from os import listdir
from os.path import isfile, join

csv_files = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith('.csv')]
for f in csv_files:
    print(f)

columns = ['title', 'assignee', 'inventor/author', 'priority date',
       'filing/creation date', 'publication date', 'grant date', 'result link',
       'representative figure link']

# Have all searches you want to scrape exported as csvs in the same folder as this file
dfs = []
for f in csv_files:
    df = pd.read_csv(f, skiprows=[0], index_col='id')
    dfs.append(df)

df_master = pd.concat(dfs)

df_master['assignee'].drop_duplicates()


# Write the name of your output file in the form of 'my_file_name.xlsx'
# If you already have a file of the same name open, protection
df_master.to_excel('OUTPUT-FILE-NAME.xlsx')