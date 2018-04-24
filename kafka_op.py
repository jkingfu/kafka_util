#!/usr/bin/env python
#encoding=utf-8
import sys
import json
import time
import traceback
import log
from confluent_kafka import Consumer, KafkaError, KafkaException, TopicPartition

KAFKA_SERVER_HOSTS = "kafka01:9092"
class KafkaConsumer(object):
    def __init__(self,group_id,topic):
        self.client = Consumer({'bootstrap.servers':KAFKA_SERVER_HOSTS,'group.id':group_id,'session.timeout.ms': 6000,'default.topic.config':{'auto.offset.reset':'smallest'}})
        self.topic= topic
    def query_kafka(self, max_part):
        for p_id in range(0, max_part):
            tp = TopicPartition(self.topic, p_id)
            committed = self.client.committed([tp])
            watermark_offsets = self.client.get_watermark_offsets(tp)
            c_offset=committed[0].offset
            partition=committed[0].partition
            min_offset=watermark_offsets[0]
            max_offset=watermark_offsets[1]
            print ("%d %d %d %d %d" % (partition,min_offset, c_offset, max_offset,max_offset-c_offset))
    def reset_kafka(self, tps):
        for tp in tps:
            self.client.assign([tp])
            print(tp)
            self.client.poll()
    def close(self):
        self.client.close()
