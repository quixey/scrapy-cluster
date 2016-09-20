# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.exporters import JsonLinesItemExporter

class ApplePipeline(object):

    def __init__(self):
        self.item_count = 0
        self.file_name = "apps.json"
        self.file_pointer = None

    def process_item(self, item, spider):

        self.lock.acquire()        
        self.item_count = self.item_count + 1
        if self.file_pointer == None:
            self.file_pointer = open(self.file_name, 'a+')
        self.lock.release()
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        if self.file_pointer != None
            self.file_pointer.close()

