"""
This is the main of the client ingesting events into Kafka to power 
the Stormbreak Flink datastream processing platform 
"""
from constants import KAFKA_BOOTSTRAP_SERVER, KAFKA_MAX_QUEUE, SOURCES
from datareader import combiningEventSources

from confluent_kafka import Producer

producer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVER,
        'queue.buffering.max.messages': KAFKA_MAX_QUEUE, 
        'queue.buffering.max.ms' : 100
}

def deliveryCallback(err, msg):
        if err:
            print("[ERROR] message failed delivery: {}".format(err))
        else:
            print("[PRODUCER LOG] message delivered {} - partition {} with offset {}".format(msg.topic(), msg.partition(), msg.offset()))
        
def producingEvent(timestamps, records):
    # instantiating producer
    producer = Producer(producer_config)

    # producing sequential events
    counter = 0
    print("[PRODUCER] STARTING PRODUCER")
    for ts in timestamps:
        for record in records[ts]:
            record_topic = record[0]
            record_key   = "{}:{}".format(record[0],record[1])
            record_val   = record[2]
            producer.produce(record_topic, record_val, record_key, callback=deliveryCallback)
            producer.poll(0)
            counter += 1

    producer.flush()
    print("[PRODUCER] PRODUCED {} MSG".format(counter))

if __name__ == "__main__":
    data = combiningEventSources(SOURCES)
    producingEvent(data[0], data[1])
