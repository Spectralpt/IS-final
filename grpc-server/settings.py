import os

#Server config
#Default value '50051'

GRPC_SERVER_PORT = os.getenv('GRPC_SERVER_PORT', '50051')
MAX_WORKERS = int(os.getenv('MAX_WORKERS', '10'))

#Media files

MEDIA_PATH = os.getenv('MEDIA_PATH',f'{os.getcwd()}/app/csv')

#DB settings
DBNAME = os.getenv('DBNAME', 'myDatabase')
DBUSERNAME = os.getenv('DBUSERNAME ', 'myUser')
DBPASSWORD = os.getenv('DBPASSWORD ', 'myPassword')
DBHOST = os.getenv('DBHOST ', 'localhost')
DBPORT = os.getenv('DBPORT ', '5432')

