from email import header
import logging

import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    query = req.params.get('query')
    if not query:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            query = req_body.get('query')

    if query:
        return func.HttpResponse(json.dumps([{
            "command":"copy",
            "line":10
        },{
            "command":"paste",
            "line":52
        }]) ,
             status_code=200
        )
    else:
        return func.HttpResponse(
             json.dumps({"error":"Please provide a query"}) ,
             status_code=400
        )
