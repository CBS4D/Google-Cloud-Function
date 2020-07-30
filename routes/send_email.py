import requests

from flask import current_app, request
from flask_restful import Resource
from marshmallow import ValidationError

from schemas.payloads import InputSchema

# Schema Object Declarations:
input_schema = InputSchema()


class SendEmail(Resource):
    '''
    '''

    def __init__(self):
        self.resp = {
            "status": "failed",
            "message": "Api execution not successful",
            "details": ""
        }

    def post(self):
        '''
        '''
        try:
            json_data = request.get_json()

            data = input_schema.load(json_data)

            headers = {
                "Content-Type": "application/json"
            }

            google_url = current_app.config.get('GOOGLE_CLOUD_FUNCTION_URL')
            if not google_url:
                self.resp['details'] = "Please provide google cloud \
                function url in config"
                return self.resp, 422

            json_data['password'] = current_app.config['GOOGLE_ACCOUNT_PASSWORD']

            response = requests.post(
                google_url, json=json_data, headers=headers)

            if response.status_code != 200:
                self.resp['details'] = "error while executing google \
                cloud function"
                return self.resp, response.status_code

            return {
                "status": "success",
                "message": "Api execution is successful",
                "details": "mail sent, please check your inbox"
            }, 202

        except ValidationError as v_err:
            resp = {"error": []}
            return v_err.messages, 400

        except Exception as e:
            print(e)
            self.resp['details'] = "Internal server Error"
            return self.resp, 500
