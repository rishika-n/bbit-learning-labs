import pika
import os
from producer_interface import mqProducerInterface
class mqProducer(mqProducerInterface):

    def __init__(self, routing_key, exchange_name) -> None: 
        # body of constructor
        self.routing_key = routing_key
        self.exchange_name = exchange_name

        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)
        self.channel = self.connection.channel()

        

        self.setupRMQConnection() 

    
    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        # con_params = pika.URLParameters(os.environ["AMQP_URL"])
        # connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        # channel = connection.channel()

        # Create the exchange if not already present
        # exchange = self.channel.exchange_declare(exchange=self.exchange_name)
        self.channel.exchange_declare(
            exchange=self.exchange_name, exchange_type="topic"
        )
        


    def publishOrder(self, message: str) -> None:

        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message,
        )

        # Send serialized message or String

        # Print Confirmation
        print("Hurray! You produced successfully")

        # Close channel and connection
        self.channel.close()
        self.connection.close()

    