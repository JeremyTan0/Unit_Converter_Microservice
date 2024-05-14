import zmq

context = zmq.Context()

print("Connection in progress…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:7777")
print("Connection established")

pack_json = {
    "convert_type": "lbs",
    "values": 2
}
socket.send_json(pack_json)
print(f"Sent JSON: {pack_json}")

convert_json = socket.recv_json()
print(f"Received JSON: {convert_json}")