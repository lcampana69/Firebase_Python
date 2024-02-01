from datetime import datetime
import time
import os
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv, find_dotenv

class Tools:
    downloads_path = str(Path.home() / "Downloads")
    # ---------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        _ = load_dotenv(find_dotenv()) # read local .env file
        
   	# ---------------------------------------------------------------------------------------------------------------------------------------------
    def get_env_var(var):
        return os.environ[var]
   
   	# ---------------------------------------------------------------------------------------------------------------------------------------------
    def timestamp_to_string(self, ts,format='%d/%m/%Y %H:%M:%S'):
        f = "%Y-%m-%dT%H:%M:%S.%f%z"
        last = 0
        if isinstance(ts, str):
                    last = time.mktime(datetime.strptime(ts, f).timetuple())
        else:
                    last=ts
        return datetime.fromtimestamp(last).strftime(format)
   	# ---------------------------------------------------------------------------------------------------------------------------------------------
    def timestamp_to_datetime(self, ts,format='%d/%m/%Y %H:%M:%S'):
        f = "%Y-%m-%dT%H:%M:%S.%f%z"
        last = 0
        if isinstance(ts, str):
                    last = time.mktime(datetime.strptime(ts, f).timetuple())
        else:
                    last=ts
        return datetime.fromtimestamp(last)       
    
   	# ---------------------------------------------------------------------------------------------------------------------------------------------
    def fwrite(self,file, txt,append=False):
        if append==True:
            fichero = open(file, "a")
            fichero.write(txt+"\n")
            fichero.close()
        else:
            fichero = open(file, "w")
            fichero.write(txt+"\n")
            fichero.close()
            
   	# ---------------------------------------------------------------------------------------------------------------------------------------------
    def fread_csv(self,file):
        return pd.read_csv(file)
        
        
    #----------------------------------------------------------------------------------------------------------------------------------------------
    def delay(self, sec=1):
        time.sleep(sec)
        
        