__author__ = 'daviz'

import logging,pykka, pika

logger = logging.getLogger("dpype-channels")

class Channel(pykka.ThreadingActor):

    def __init__(self, config):
        super(Channel,self).__init__()
        self.__config = config
        self.__initialize()


    def __initalize(self):
        pass


    def register(self,activity):
        self.__activity = activity


    def stop(self):
        pass

class RabbitMQChannel(Channel):


    def __initialize(self):
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.__config.host, port=self.__config.port))

        self.__channel = connection.channel()
        self.__channel.declare(queue=self.__config.channelName)

        #TODO Configurable no_ack parameter
        self.__channel.basic_consume(self.callback,queue=self.__config.channelName,no_ack=True)

        self.__channel.start_consuming()

    def callback(self,ch, method, properties, body):
        print "Received %r" % (body)


    def stop(self):

        self.__channel.stop_consuming()