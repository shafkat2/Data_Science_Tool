from flask_restful import Resource
import logging as logger

class getLayout(Resource):

    def get(self):
        # get the values from boto3      
        return {'message': 'inside get method layout'},200

    def post(self):        
        logger.debug("inside post method")
        return {'message': 'inside POST method'},200

    def put(self):        
        logger.debug("inside put method")
        return {'message': 'inside PUT method'},200
    
    def delete(self):
        logger.debug("inside delete method")
        return {'message': 'inside DELETE method'},200

class getLayout2(Resource):

    def get(self):
        # get the values from boto3
        return {'message': 'inside get method layout2'},200

    def post(self):        
        logger.debug("inside post method")
        return {'message': 'inside POST method'},200

    def put(self):        
        logger.debug("inside put method")
        return {'message': 'inside PUT method'},200
    
    def delete(self):
        logger.debug("inside delete method")
        return {'message': 'inside DELETE method'},200
