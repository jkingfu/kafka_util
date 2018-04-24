#!/usr/bin/env python
#encoding=utf-8
import sys
import json
import time
import traceback
import log
import kafka_op
#form kafka_op import KafkaConsumer
from confluent_kafka import Consumer, KafkaError, KafkaException, TopicPartition

def main():
    group_id = sys.argv[1]
    topic = sys.argv[2]
    max_part = int(sys.argv[3])
    kafka_consumer = kafka_op.KafkaConsumer(group_id,topic)
    kafka_consumer.query_kafka(max_part)
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("input para err: group_id topic max_part")
        sys.exit(1)
    main()
