from concurrent import futures
import cv2
import grpc
from grpc.experimental import aio
import base64
import MotionDetectionService_pb2
import MotionDetectionService_pb2_grpc
import time
import numpy as np
import asyncio
from MotionDetector.MotionDetector import MotionDetector
from MotionDetector.get_iou import get_iou
import json
import sys
from LoggerService import LoggerService

image_extensions = {
    'jpg',
    'png'
}

video_extensions = {
    'mp4',
    'mkv',
    'avi',
    'asf'
}

class MotionDetectionService(MotionDetectionService_pb2_grpc.MotionDetectionServiceServicer):
    def __init__(self):
        self.motion_detector = MotionDetector()
        self.logger = LoggerService()

    async def motion_detection(self, frames):
        self.motion_detector.warmup(frames)
        return await self.motion_detector.findMotionBoxesSequence(frames)

    def build_response(self, async_results):
        response = MotionDetectionService_pb2.MotionDetectionResponse()
        for frame_result in async_results:
            response_frame = MotionDetectionService_pb2.MotionDetectionFrame()
            print(frame_result)
            for res in frame_result:
                response_frame.detections.append(MotionDetectionService_pb2.MotionDetection(xmin=res[0],
                                                                                            ymin=res[1],
                                                                                            xmax=res[2],
                                                                                            ymax=res[3]))
            response.frames.append(response_frame)
        return response

    async def Analyze(self, request, context):
        frames = []
        classes = []
        tracked_classes = []

        response = {
            'Analyzed' : False,
            'Results' : [],
            'Message' : ''
        }
        
        try:
            for f in request.files:
                #b64d = base64.b64decode(frame.frame)
                dBuf = np.frombuffer(f, dtype = np.uint8)
                dst = cv2.imdecode(dBuf, -1)
                frames.append(dst)

            self.logger.logInfo('Frames extracted for motiondetection gRPC service.')

            mot = await self.motion_detection(frames)
            response = self.build_response(mot)
            response.analyzed = True

            self.logger.logInfo('Content analyzed successfully')

            return response

        except Exception as e:
            self.logger.logError(e)
            return response

    async def serve(self):
        MAX_MESSAGE_LENGTH = 10000000

        server = aio.server(futures.ThreadPoolExecutor(max_workers=10), 
                            options=[
                                ("grpc.max_receive_message_length", MAX_MESSAGE_LENGTH), 
                                ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
                                ])
        MotionDetectionService_pb2_grpc.add_MotionDetectionServiceServicer_to_server(MotionDetectionService(), server)
        server.add_insecure_port('0.0.0.0:50051')
        await server.start()
        self.logger.logInfo('Server running...')
        await server.wait_for_termination()
        self.logger.logInfo('Server stopped.')



if __name__ == '__main__':
    curr_server = MotionDetectionService()
    asyncio.run(curr_server.serve())
