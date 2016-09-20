
# PREFIX *must* be customized for the crawler so different crawlers don't
# go dumping stuff in each others kafka queues!

PREFIX = "apple-2"

MESSAGE_BUS = 'frontera.contrib.messagebus.kafkabus.MessageBus'
KAFKA_LOCATION = 'kafka.scrapy.quixey.com'

FRONTIER_GROUP = "{}".format(PREFIX)
INCOMING_TOPIC = "{}-done".format(PREFIX)
OUTGOING_TOPIC = "{}-todo".format(PREFIX)

SCORING_GROUP = "{}-strategy".format(PREFIX)
SCORING_TOPIC = "{}-strategy".format(PREFIX)
