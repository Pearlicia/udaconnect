import grpc
import data_pb2
import data_pb2_grpc


print("Sending sample payload...")

channelL = grpc.insecure_channel("localhost:5005")
stub = data_pb2_grpc.LocationServiceStub(channelL)

location_id = data_pb2.Location(id=20)

response = stub.Get(location_id)
print(response)


channelP = grpc.insecure_channel("localhost:5005")
stub = data_pb2_grpc.PersonServiceStub(channelP)

person_id = data_pb2.Person(id=21)

response = stub.Get(person_id)
print(response)

