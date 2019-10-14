import json
from iotfunctions.db import Database


with open('credentials_as.json', encoding='utf-8') as F:
    credentials = json.loads(F.read())
db_schema = None
db = Database(credentials=credentials)

from custom.multiply_by_factor import MultiplyByFactor

db.register_functions([MultiplyByFunction])