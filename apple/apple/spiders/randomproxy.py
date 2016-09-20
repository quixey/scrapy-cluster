#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2013 by Aivars Kalvans <aivars.kalvans@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import re
import random
import base64
import logging
import scrapy
from config.config import get_config_parser


class RandomProxy(scrapy.Spider):

	def __init__(self, settings):
		self.logger.info("RandomProxy initiated !")
		self.proxy_list = settings.get('PROXY_LIST')
		self.proxies = {}
		self.enable_proxy = None
		try:
			fin = open(self.proxy_list)
		except :
			self.logger.info("Reading File failed. No proxies")
			return

		config = get_config_parser()
#BC		self.enable_proxy = 0
                self.enable_proxy = 1

		try:
			self.enable_proxy = config.getint('ProxyManagement',
					'enable')
		except:
#BC			self.logger.info('Error reading Configs for http_proxy, defaulting')
                        self.enable_proxy = 1

		for line in fin.readlines():
			parts = re.match('(\w+://)(\w+:\w+@)?(.+)', line)
			if not parts:
				if(not line.startswith("http://")):
					line = "http://"+line.strip()
				user_pass = settings.get("PROXY_USER_KEY").strip()+":"+settings.get("PROXY_USER_PASS").strip()
				self.proxies[line] = user_pass
			else:
				# Cut trailing @
				if parts.group(2):
					user_pass = parts.group(2)[:-1]
				else:
					user_pass = ''
				self.proxies[(parts.group(1) + parts.group(3)).strip()] = user_pass

		self.logger.info(self.proxies)
		fin.close()

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings)

	def process_request(self, request, spider):

		# Don't overwrite with a random one (server-side state for IP)

		if 'proxy' in request.meta or self.enable_proxy == None or self.enable_proxy == 0:
			return

		proxy_address = random.choice(self.proxies.keys())
		proxy_user_pass = self.proxies[proxy_address]

		if self.enable_proxy == 1:
			request.meta['proxy'] = proxy_address
		self.logger.info('Using Proxy %s' % proxy_address)
		if proxy_user_pass:
			basic_auth = 'Basic ' + base64.encodestring(proxy_user_pass)
			request.headers['Proxy-Authorization'] = basic_auth

	def process_exception(self, request, exception, spider):
		if self.enable_proxy != None:
			if self.enable_proxy == 1:
                                try :
				    proxy = request.meta['proxy']
				    self.logger.info('proxy Failed <%s>' % proxy)
                                except:
                                    pass

		# log.msg('Removing failed proxy <%s>, %d proxies left' % (
		#			proxy, len(self.proxies)))
		# try:
		#	del self.proxies[proxy]
		# except ValueError:

		pass

