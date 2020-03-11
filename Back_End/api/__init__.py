from flask_restful import Api
from app import flaskAppInstance
from .Task import getLayout2
from .Task import getLayout
from .TaskById import TaskById

restServer = Api(flaskAppInstance)

restServer.add_resource(getLayout,'/','/api/v1.0/task/layout2/')
restServer.add_resource(TaskById,'/api/v1.0/task/<string:taskId>')