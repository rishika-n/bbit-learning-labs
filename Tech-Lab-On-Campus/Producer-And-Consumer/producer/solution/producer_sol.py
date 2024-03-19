
from producer_interface import mqProducerInterface
class mqProducer(mqProducerInterface):
    def __init__(self, routing_key, exchange_name) -> None: 
        # body of constructor
        self.routing_key = routing_key
        self.exchange_name = exchange_name

        self.setupRMQConnection() 
    
    def bark(self) -> None:
        # Print {name of dog} is barking!
        print(self.name, "is barking!")

    