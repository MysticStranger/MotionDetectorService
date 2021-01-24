from abc import ABCMeta, abstractmethod

class IMotionDetector(metaclass=ABCMeta):

    '''
    
    Class holding and providing functionality for a motiondetector.
    Starts from either cv2.createBackgroundSubtractorKNN() or
    cv2.createBackgroundSubtractorMOG(). 
    
    Additional custom processing such as dilation or erosion etc
    can be added as a part of the detect() method.

    __init__ should contain atleast a backgroundsubtractor as an attribute,
    self.backSub = cv2.createBackgroundSubtractorKNN(...).
    
    '''

    @abstractmethod
    def warmup(self, frames: list) -> None:
        '''

        Takes in a list of frames and calls backSub.Apply(frame) over frames
        to ensure that the background subtractor starts from a good averaged
        subtraction.

        input: fgMask : object

        returns: None

        See MotionDetector.py for an example implementation.

        '''
        pass
        
    @abstractmethod
    async def findMotionBoxes(self, frame : object) -> list:

        '''
        
        Takes a frame/image and computes the foregroundmask fgMask and
        finds the enclosing bounding boxes of regions of detected 
        motion in the foreground mask.

        Each bounding box is of the format list(xmin, ymin, xmax, ymax)

        input: frame/image : object

        returns: motionBoxes: [[xmin,ymin,xmax,ymax], ...]

        '''
        pass

    @abstractmethod
    async def findMotionBoxesSequence(self, frames : list) -> list:
        pass

