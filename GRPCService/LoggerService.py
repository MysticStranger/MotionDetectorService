import logging
import os
import datetime

class LoggerService:
    
    '''
    
    The service for logging. Configured to log messages to a text file with the format: '(Date) log.txt'.
    Creates a new file if no file with the specific name was found.
    Attributes
    ----------
    logger: module
        The underlying logging module.
    
    '''

    def __init__(self):
        self.logger = logging

        LOGNAME = datetime.datetime.now().strftime("%Y-%m-%d") + ' log.txt'
        LOGFILE = os.path.join(os.getcwd() + '/logs', LOGNAME)
        FORMAT = '%(asctime)s [%(levelname)s] <%(process)d> - %(message)s'
        LEVEL = logging.INFO
        self.logger.basicConfig(filename=LOGFILE, level=LEVEL, format=FORMAT)

    def logDebug(self, message):
        '''
        Writes the specified message to the logging file with a 'DEBUG'-prefix.
        Parameters
        ----------
        message: 
        
            The specified message to log.
            
        '''
        self.logger.debug(message)

    def logError(self, message):
        '''
        Writes the specified message to the logging file with a 'ERROR'-prefix.
        Parameters
        ----------
        message: 
        
            The specified message to log.
            
        '''
        self.logger.error(message)

    def logInfo(self, message):
        '''
        Writes the specified message to the logging file with a 'INFO'-prefix.
        Parameters
        ----------
        message: 
        
            The specified message to log
            
        '''
        self.logger.info(message)

    def logWarning(self, message):
        '''
        Writes the specified message to the logging file with a 'WARN'-prefix.
        Parameters
        ----------
        message: 
        
            The specified message to log.
            
        '''
        self.logger.warn(message)