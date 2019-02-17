#!/usr/bin/python3 
#Author - Ravi Ainampudi 

import os
import re

path_location = input("Please provide location path for files in mount point. (Ex: /var/www/ ):") #Files location

try:
    for dirname, subdirs, filelist in os.walk(path_location): #Parsing files in that location recursively
        for fname in filelist:
            if fname.endswith(".html"): #Checking HTML files only
                fpath = os.path.join(dirname,fname)
                match = None
                with open(fpath, "r") as file_data: #Reading each HTML file
                    file_data = file_data.read()
                    pattern = r'1?800[\s.-]?(?:438|GET)[\s.-]?(?:4357|HELP)' #Regular expression to find phone number or its letter Mnemonics
                    match = re.sub(pattern, r'202-456-1414' , file_data, flags=re.IGNORECASE) #Phone number substitution
                
                if match: #Change original file only if substitution is made. 
                    with open(fpath, 'w') as file_write: #Writing the substituted string to original file.
                        file_write.write(match)

except Exception as error:
    print(error)
                    
