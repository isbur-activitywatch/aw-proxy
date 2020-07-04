import json
import time
import zmq


from AW import AW


print('Starting to listen...')
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

while True:

    r = socket.recv_json()
    print("We are going to handle:")
    print(r)
    
    result = getattr(AW, r[0]).__call__(*r[1:-1], **r[-1])

    print("Result:")
    print(result)

    socket.send_json(result)
    time.sleep(1)