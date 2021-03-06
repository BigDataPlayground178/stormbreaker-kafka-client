docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=localhost --env ADVERTISED_PORT=9092 spotify/kafka
export KAFKA=localhost:9092
kafka-console-producer.sh --broker-list $KAFKA --topic topic
export ZOOKEEPER=localhost:2181
kafka-console-consumer.sh --zookeeper $ZOOKEEPER --topic topic