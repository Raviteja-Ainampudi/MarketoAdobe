# MarketoAdobe Homework Projects. 

:key: Each Question folder has their code to solve those problem statements. 

:key: Each answer has been provided with execution procedure to explain the approach of using those code files. 

:key: Caching Web API has been developed in a MVC style.  

# Question 1:
   Reads files from Sys args and Copies useful data to output file. :sunglasses:
   
     * Used Python3 for data handling. 
     * Program can work on argument pairs of 32 bit unsigned IP addresses and Subnet.
     * Program can also read 32 bit unsigned IP addresses and Subnet pairs from an inputfile and results 
       were written In an useful fashion to an outputfile, when both specified on through the STDIN.  
     * Has a couple of default Unit Test cases present when no system arguments passed. 

# Question 2:
  * Developed two solutions to implement this Phone number / Letter Nmemonics replacement in HTML files. :sweat_smile:
    #### Bash Style:
         * Single Pipeline of Linux Commands to solve the problem Statement. 
         * Also provided a solution to retain original HTML data as backup files. 
         * Used regular expressions. 
    
    #### Python3 Style:
         * Code recursively searches for data in HTML files in the directory path provided as input. 
         * Used regular expressions. 

# Question 3:
   *  Developed Caching Web API using **Python**, **Flask**, **Jinja2** and **HTML**. :sparkles: :sparkles:
   *  API considers float values for latitude in range of (-90, 90) and for longitude in range(-180, 180).
      And return a random number generated as URL. 
   *  Diagnostic API calls with Cache Hit and Miss counters has been implemented. 
   *  Execution time for LRU cache features of Hit, Miss when full and Miss when not full has been implemented. 
   *  This application can run on both Python2 and Python3 platforms. 
   
      #### Caching:
            * For Python2, desgined independent code for LRU caching operations. 
            * For For Python3, Used LRU Cache tool from Functools library. 
            * A Python dictionary is used for caching purposes. Dict has an average time complexity 
              of O(1) for dictionary operations like Get, Set and Delete. 
            * Comment out lines 8,9 or 12,13 in app.py file while switching between Python2 and Python3 environments. 
            
      #### Files:
            * static - Has Multimedia files
            * templates - Has HTML code with Jinja2 templating embedded. 
            * app.py - Primary application file. 
            * cache_hitter27.py - Cache Manager when application is running on Python2 environment.
            * cache_hitter36.py - Cache Manager when application is running on Python3 environment.
            
      #### Diagnostic API Calls: 
         ###### Homepage:
         ![alt text](https://github.com/Raviteja-Ainampudi/MarketoAdobe/blob/master/Question3/API_Screenshots/API%20HomePage.PNG "Logo 1")
  
         ###### Cache Miss When Not Full:
         ![alt text](https://github.com/Raviteja-Ainampudi/MarketoAdobe/blob/master/Question3/API_Screenshots/API%20Cache%20Value%20Miss.PNG "Logo 2")
         
         ###### Cache Hit:
         ![alt text](https://github.com/Raviteja-Ainampudi/MarketoAdobe/blob/master/Question3/API_Screenshots/API%20Cache%20Value%20Hit.PNG "Logo 3")
         
         ###### Cache Clear:
         ![alt text](https://github.com/Raviteja-Ainampudi/MarketoAdobe/blob/master/Question3/API_Screenshots/API%20Cache%20Clear.PNG "Logo 4")
         
      #### URLS: 
            * Homepage: http://127.0.0.1:5000/home/
            * Latitude and Longitude Diagnostic Response: http://127.0.0.1:5000/latlong/ 
              (This View is valid only after Homepage has appropiate inputs.)
            * Clear Cache Info - http://127.0.0.1:5000/clearcache/
            
      #### Screencasted Video for API Working Process:    
      [API Video in Google Drive](https://drive.google.com/drive/folders/1nkfsuycR6jeogg0X5VfLXiDt-VOZ1Mj_)

      [API Video in Github](https://github.com/Raviteja-Ainampudi/MarketoAdobe/tree/master/Question3/API_Screen_Video)



:v: :us: :+1:
