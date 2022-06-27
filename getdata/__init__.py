
import azure.functions as func
from azure.cosmos import CosmosClient
import os
import json
from bson.json_util import dumps
import azure.cosmos.cosmos_client as cosmos_client


def main(req: func.HttpRequest, outdoc:func.DocumentList) -> func.HttpResponse:
    
    #logging.info('Python HTTP trigger function processed a request.')
 
    try:        
        
        data_json = []

        for user in outdoc:
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
    except ConnectionError:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)
