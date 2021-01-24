from concurrent import futures
import grpc
import cv2
import MotionDetectionService_pb2
import MotionDetectionService_pb2_grpc
import base64
import asyncio
import time

'''

message MotionDetectionRequest {
    repeated bytes files = 1;
    string file_format = 2;
}

'''

cap = cv2.VideoCapture('../171-Truck_Moving.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
def run():
    channel = grpc.insecure_channel('192.168.10.134:5002')
    stub = MotionDetectionService_pb2_grpc.MotionDetectionServiceStub(channel)
    req = MotionDetectionService_pb2.MotionDetectionRequest()
    count = 0
    try:
        while True:
            ret, frame = cap.read()
            if ret != 1:
                break

            ret, frame = cv2.imencode('.jpg', frame)
            req.files.append(frame.tobytes())
            req.file_format = 'jpg'
            count += 1
            if count % 8 == 0:
                break

        responses = stub.Analyze(req)
        print(responses)
    except grpc.RpcError as e:
        print(e.details())
        
if __name__ == '__main__':
    now = time.time()
    run()
    print(time.time() - now)

