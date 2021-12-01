import grpc
import data_pb2
import data_pb2_grpc
from datetime import datetime
from data_pb2 import PersonMessage, LocationMessage


print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = data_pb2_grpc.LocationServiceStub(channel)

location = data_pb2.LocationMessage(
    id=1,
    person_id= 1,
    longitude= "37.5534409999999994",
    latitude= "-122.2905240000000049",
    creation_time=datetime.now().isoformat(),
)

result = stub.Create(location)
print(result)


channel = grpc.insecure_channel('localhost:5005')
stub = data_pb2_grpc.PersonServiceStub(channel)

person = data_pb2.PersonMessage(
    first_name="Felicia", 
    last_name="Ebikon", 
    company_name="Pearlicia"
)

result = stub.Create(person)
print(result)
