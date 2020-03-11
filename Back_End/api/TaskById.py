from flask_restful import Resource
import logging as logger

class TaskById(Resource):

    def get(self,taskId):
        logger.debug("inside get method of task by ID")
        return { 'message': 'inside get method, Task by ID {}'.format(taskId) },200

    def post(self,taskId):        
        logger.debug( "inside post method" )
        return { 'message': 'inside post method, Task by ID {}'.format(taskId) },200

    def put(self,taskId):        
        logger.debug("inside put method")
        return { 'message': 'inside put method, Task by ID {}'.format(taskId) },200
    
    def delete(self,taskId):
        logger.debug("inside delete method")
        return { 'message': 'inside delete method, Task by ID {}'.format(taskId) },200