"""
Constants of the Kafka producer client
"""

# topic 
TOPIC_FRIENDSHIP = "friendships"
TOPIC_POSTS      = "posts"
TOPIC_COMMENTS   = "comments"

# datasets
DATASET_FRIENDSHIP = "./datasets/friendships.dat"
DATASET_POSTS      = "./datasets/posts.dat"
DATASET_COMMENTS   = "./datasets/comments.dat"
SOURCES            = [(DATASET_FRIENDSHIP, TOPIC_FRIENDSHIP), (DATASET_POSTS, TOPIC_POSTS), (DATASET_COMMENTS, TOPIC_COMMENTS)]

# Kafka server configuration (assuming default port configuration)
KAFKA_BOOTSTRAP_SERVER = "localhost:9092"
KAFKA_MAX_QUEUE        = 100000

# datetime format
DATETIME_FORMAT  = "%Y-%m-%dT%H:%M:%S.%f"