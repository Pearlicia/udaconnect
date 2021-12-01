import os
from app.udaconnect.models import Location
from app.udaconnect.schemas import (
    LocationSchema,
)
from app.udaconnect.services import LocationService
from flask import request, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from kafka import KafkaProducer
from json import dumps

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("location-service", description="Connections via geolocation.")  # noqa


KAFKA_TOPIC = "location"
KAFKA_SERVER = "kafka:9092"
producer = KafkaProducer(bootstrap_servers=[f'{KAFKA_SERVER}'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

 
@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    def post(self):
        try:
            request_data = request.get_json()
            creation_time = request_data["creation_time"]
            creation_time = creation_time.isoformat()
            request_value = {
                "id": request_data["id"],
                "person_id": request_data["person_id"],
                "longitude": request_data["longitude"],
                "latitude": request_data["latitude"],
                "creation_time": creation_time,
            }
            producer.send(KAFKA_TOPIC, request_value)
            producer.flush()
            return request_value
        except Exception as e:
            return {"error": str(e)}, 400

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location