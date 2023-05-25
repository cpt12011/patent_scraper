# patent_scraper

This code reads any number of csv files with patent data downloaded from google patents from the same folder in the path of this code file, deletes duplicates, and concactenates all searches into one xlsx file such that you can aggregate multiple keyword searches.

First, create a new folder containing a copy of this code file.

Then, run as many keyword searches as you want. Use '("KEYWORD1") AND ("MULTI KEYWORD2")' if you want to run and/or searches with specific search terms of single or multiple words. For each search, click the download arrow and 'Download (CSV)' and make sure to download it in the same folder as the patent scraper ipnyb file.

Then add your folder path to the 'mypath' variable in the python code and your desired excel output file name and run the code.

You will need to install:
Anaconda: https://docs.anaconda.com/free/anaconda/install/windows/

And Pandas: https://docs.anaconda.com/free/navigator/tutorials/pandas/

Or if you have pandas installed on an alternative IDE, feel free to use the .py file instead
