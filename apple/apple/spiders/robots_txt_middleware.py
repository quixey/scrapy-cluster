import scrapy
import logging
import sys,os
from scrapy.downloadermiddlewares.robotstxt import RobotsTxtMiddleware 


class   robots_txt_middleware(RobotsTxtMiddleware):
    
    def process_request(self, request, spider):

        if spider.obey_robotstxt == False:
            spider.logger.info("Ignoring robots.txt")
            return None
        super(robots_txt_middleware,self).process_request(request,spider)
