from firebase_admin import credentials, firestore, initialize_app


from datetime import datetime
import json

# ---------------------------------------------------------------------------------------------------------------------------------------------
class Firebase:
    # ---------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, path_credentials):
        self.cred = credentials.Certificate(path_credentials)
        self.app=initialize_app(self.cred)
        self.firestore_client = firestore.client()
        
    def get_json_collection(self,collection,date_from=None,date_to=None):
        _date_from=None
        _date_to=None
        if(date_from!=None):
            _date_from=datetime.strptime(date_from, "%d/%m/%Y").timestamp() * 1000
        if(date_to!=None):
            _date_to=datetime.strptime(date_to, "%d/%m/%Y").timestamp() * 1000  
        dict=[]
        if _date_from!=None and _date_to!=None:
            docs = self.firestore_client.collection(collection)\
                .where(filter=firestore.FieldFilter("timestamp", ">=", _date_from))\
                .where(filter=firestore.FieldFilter("timestamp", "<=", _date_to)).stream()
        else:
            docs = self.firestore_client.collection(collection).stream()
        for doc in docs:
          doc_data = doc.to_dict()
          filtered_data = {key: doc_data[key] for key in ['date', 'timestamp','devEUI'] if key in doc_data}
        dict.append(filtered_data)
        valores = {'total': len(dict), 'devices': dict}  
        return  json.dumps(valores, indent=4)
