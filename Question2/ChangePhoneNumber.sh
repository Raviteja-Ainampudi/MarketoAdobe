#!/bin/bash
#Author - Ravi Ainampudi

#Bash file has commands to change phone number with or without creating backupup data for HTML files.

#Single Pipeline of linux Commands to change phonenumber in HTML file WITHOUT backup HTML data.

find '/var/www/' -name "*.html" -fstype nfs -type f | xargs sed -r -i 's/\(?\<1?800[-) .]?(438|GET)[ -.]?(4357|HELP)\>/202\-456\-1414/gI';

#OR

#Single Pipeline of linux Commands to change phonenumber in HTML file with backup HTML data.

find '/var/www/' -name "*.html" -fstype nfs -type f | xargs sed -r -i.bak 's/\(?\<1?800[-) .]?(438|GET)[ -.]?(4357|HELP)\>/202\-456\-1414/gI';
