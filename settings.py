import os
import dotenv

dotenv.load_dotenv('.env')

HA_API_KEY = os.environ['HA_API_KEY']
OpenAI_API_KEY = os.environ['OpenAI_API_KEY']
