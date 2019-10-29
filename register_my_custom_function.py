import json
from iotfunctions.db import Database


with open('credentials_as.json', encoding='utf-8') as F:
    credentials = json.loads(F.read())
db_schema = None
db = Database(credentials=credentials)

from rawkintrevo_tutorial2.divbyfactor import RawkintrevosDivByFactor
from rawkintrevo_tutorial2.LegitRequest import ExternalModel

db.register_functions([RawkintrevosDivByFactor, ExternalModel])

db.unregister_functions(["ExternalModel"])

import rawkintrevo_tutorial2
db.register_module(rawkintrevo_tutorial2)

import rawkintrevo_tutorial2.LegitRequest
db.register_module(rawkintrevo_tutorial2.LegitRequest)