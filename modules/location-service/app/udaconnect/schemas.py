from app.udaconnect.models import Location
from marshmallow import Schema, fields, pre_load
from datetime import datetime

class LocationSchema(Schema):
    id = fields.Integer()
    person_id = fields.Integer()
    longitude = fields.String(attribute="longitude")
    latitude = fields.String(attribute="latitude")
    creation_time = fields.DateTime()

    class Meta:
        model = Location
        datetimeformat = '%Y-%m-%dT%H:%M:%S'

   
