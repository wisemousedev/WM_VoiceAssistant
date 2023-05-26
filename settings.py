import os
import dotenv

dotenv.load_dotenv('.env')

HA_API_KEY = os.environ['HA_API_KEY']
OpenAI_API_KEY = os.environ['OpenAI_API_KEY']

RU_MODEL = os.environ['RU_MODEL']
UA_MODEL = os.environ['UA_MODEL']
