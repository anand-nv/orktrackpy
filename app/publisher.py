from kombu import Connection, Consumer, Exchange, Producer, Queue
from kombu.asynchronous import Hub


class Publisher:
    def __init__(self, amqp_url='amqp://guest:guest@localhost:5672/'):
        self.exchange_cfg = {
            'rabbit_url': amqp_url,
            'name': 'oreka.fanout',
            'type': 'fanout',
            'routing_key': 'oreka',
        }
        self.conn = Connection(amqp_url)
        self.oreka_exchange = Exchange(self.exchange_cfg['name'], self.exchange_cfg['type'], durable=True)

        self.db_queue = Queue('db', exchange=self.oreka_exchange, routing_key='oreka.db')
        self.live_queue = Queue('live', exchange=self.oreka_exchange, routing_key='oreka.live')
        self.producer = Producer(self.conn)

    def publish(self, msg):
        self.producer.publish(msg,
                              exchange=self.oreka_exchange,
                              routing_key='oreka.*',
                              serializer='json',
                              )




publisher = Publisher()
