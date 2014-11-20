__author__ = 'daviz'

import pykka, logging

logger = logging.getLogger("dpype-activity")

class Activity(pykka.ThreadingActor):
    """
    Base class for all Activities

    """
    __cin = None
    __cout = None

    def __init__(self, cin, cout):
        super(Activity, self).__init__()
        self.__cin = cin
        self.__cin.register(self)
        self.__cout = cout


    def __do(self, message):

        return self.do(message.payload)


    def __process(self, message):

        self.channelOut.send(self.__do(message))

    def do(self, payload):
        pass




