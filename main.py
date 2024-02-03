# importing Flask and other modules
from flask import Flask, request, render_template 
from FirebaseClass import *
from ToolsClass import *
import os
import sys

# Obtener la ruta completa del script
script_path = os.path.abspath(sys.argv[0])
# Extraer el directorio del script
script_dir = os.path.dirname(script_path)
# Cambiar el directorio de trabajo actual al directorio del script
os.chdir(script_dir)
# Flask constructor
PATH_JSON='./firebase/crispdevicestool-firebase-adminsdk-adahh-2106b4e801.json'
tools=Tools()
fb=Firebase(PATH_JSON)
app = Flask(__name__,
            template_folder='templates',  # Name of html file folder
            static_folder='static'  # Name of directory for static files
           )   

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
      startDate = request.form.get("startDate")
       # getting input with name = lname in HTML form 
      endDate = request.form.get("endDate") 
      ABPFirestore=fb.get_json_collection('ABPDevices',startDate,endDate)
      return render_template("index1.html", data=ABPFirestore)
    return render_template("index1.html", data=None)

if __name__=='__main__':
   app.run(
     debug=True,
     host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
     port=7000 
   )

