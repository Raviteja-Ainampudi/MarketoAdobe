#!/usr/bin/python3
#Author - Ravi Ainampudi

from flask import Flask, request, render_template, redirect, url_for, flash, session
import time
import sys

import cache_hitter36 as cachehitter
flag = False

#If you want to run Python2 uncoment below 2 lines and comment above 2 lines
#import cache_hitter27 as cachehitter27
#flag = True


app = Flask(__name__)

@app.route("/home/")
def func_home():
    """Homepage View"""
    return render_template("home.html")

@app.route("/latlong/", methods=["GET","POST"])
def func_inp_floats():
    """View used to access inputs by users."""
    if request.method == "POST":
        result = request.form
        try:
            lat_value = float(result['lati_value'])
            long_value = float(result['longi_value'])
        except Exception as error:
            flash("ERROR!!: Please provide only integers or float values.") #Flash error message on screen. 
            return redirect(url_for('func_home'))
         
        if (lat_value < -90.0 or lat_value > 90.0 ) or (long_value < -180.0 or long_value > 180.0 ): #Check for valid lati and longi values.
            flash("ERROR!!: Please makesure that Latitude lies between -90 to +90 and Longitude lies between -180 to +180.")
            return redirect(url_for('func_home'))
        else:
            if not flag:
                initial_cache_info = list(cachehitter.find_image_url.cache_info())
                start_time = time.time()
                url_obtained = cachehitter.find_image_url(lat_value, long_value)
                total_exec_time = float(time.time() - start_time)
                fin_cache_info = list(cachehitter.find_image_url.cache_info())
                if  fin_cache_info[0] > initial_cache_info [0]:
                    hit_miss = "Hit"
                else:
                    if fin_cache_info[-1] == 3000:
                        hit_miss = "Miss When Full"
                    else:
                        hit_miss = "Miss When Not Full"
                return render_template("results.html", lat_val=lat_value, lon_val=long_value, URL_Value = url_obtained, hit_miss=hit_miss, total_exec_time = total_exec_time, func_out=cachehitter.find_image_url, flag=flag)
            
            else:
                initial_cache_info = cachehitter27.info_cache()
                start_time = time.time()
                url_obtained = cachehitter27.find_image_url(lat_value, long_value)[0]
                total_exec_time = float(time.time() - start_time)
                fin_cache_info = cachehitter27.info_cache()
                if  fin_cache_info[0] > initial_cache_info [0]:
                    hit_miss = "Hit"
                else:
                    if fin_cache_info[-2] == 3000:
                        hit_miss = "Miss When Full"
                    else:
                        hit_miss = "Miss When Not Full"
                        
            return render_template("results.html", lat_val=lat_value, lon_val=long_value, URL_Value = url_obtained, hit_miss=hit_miss, total_exec_time = total_exec_time, func_out=cachehitter27.info_cache(), flag=flag)

    else:
        flash("ERROR!!: Please makesure that Latitude lies between -90 to +90 and Longitude lies between -180 to +180.")
        return redirect(url_for('func_home'))
        
@app.route("/clearcache/")        
def func_clear_cache():
    """This View is used to clear the cache information of the API."""
    if not flag:
        return render_template("clearcache.html", flag=flag, func_out=cachehitter.find_image_url)
    else:
        return render_template("clearcache.html", flag=flag, func_out=cachehitter27)
    

if __name__ == "__main__":
    app.secret_key = "SECRET_MESSAGE_ADOBE_MARKETO"
    app.run(host="0.0.0.0", port=5000, debug=True)

