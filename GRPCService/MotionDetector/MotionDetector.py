import cv2
#from ...LoggerService import LoggerService
from .IMotionDetector import IMotionDetector
import asyncio

class MotionDetector(IMotionDetector):
    def __init__(self): #, logger : LoggerService):
        #self.logger = logger
        self.backSub = cv2.createBackgroundSubtractorKNN(history = 10,
                                                         dist2Threshold = 2000)

    def warmup(self, frames: list):
        for frame in frames:
            self.backSub.apply(frame)

    async def findMotionBoxes(self, frame):

        #Experiment with and add image transformations like erosion, dilation etc.
        fgMask = self.backSub.apply(frame)
        contours, hier = cv2.findContours(fgMask, 
                                          cv2.RETR_TREE, 
                                          cv2.CHAIN_APPROX_TC89_KCOS)

        motionBoxes = []
        for c in contours:
            if cv2.contourArea(c) > 70:
                (x,y,w,h) = cv2.boundingRect(c)
                motionBoxes.append([x,y,x+w,y+h])
        return motionBoxes

    async def findMotionBoxesSequence(self, frames):
        motionBoxes = []
        for frame in frames:
            frameBoxes = await self.findMotionBoxes(frame)
            motionBoxes.append(frameBoxes)
        return motionBoxes
