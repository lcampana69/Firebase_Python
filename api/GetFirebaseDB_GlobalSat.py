from FirebaseClass import *
from ToolsClass import *
#import argparse
import os
import sys

# Obtener la ruta completa del script
script_path = os.path.abspath(sys.argv[0])

# Extraer el directorio del script
script_dir = os.path.dirname(script_path)

# Cambiar el directorio de trabajo actual al directorio del script
os.chdir(script_dir)


PATH_JSON='./firebase/crispdevicestool-firebase-adminsdk-adahh-2106b4e801.json'

tools=Tools()
fb=Firebase(PATH_JSON)

#parser = argparse.ArgumentParser(description="python GetFirebaseDB_GlobalSat.py desde hasta")
#parser.add_argument("desde", type=str, help="desde en formato <dd/mm/aaaa>", default=None)
#parser.add_argument("hasta", type=str, help="hasta en formato <dd/mm/aaaa>",default=None)

#args = parser.parse_args()

#ABPFirestore=fb.get_json_collection('ABPDevices',args.desde,args.hasta)

#print(ABPFirestore)
