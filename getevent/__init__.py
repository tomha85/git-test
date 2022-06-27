import azure.functions as func
from azure.cosmos import CosmosClient
import os
import json
from bson.json_util import dumps
import azure.cosmos.cosmos_client as cosmos_client

def main(req: func.HttpRequest, outdoc:func.DocumentList) -> func.HttpResponse:
    
    #logging.info('Python HTTP trigger function processed a request.')
    id = req.params.get('id')
    if id:
        try:       
            data_json = []

            for user in outdoc:
                if id == user["id"]:
                    utility_json = {
                    "id": user['id'],
                    "utility": user['utility'],
                    "ver": user['ver'],
                    "kind": user['kind'],
                    "ovgipsignalid": user['ovgipsignalid'],
                    "data": user['data']           
                    }
                    data_json.append(utility_json)
        
            result=json.dumps(data_json)     

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except ConnectionError as e:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)