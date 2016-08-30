#proxy.py
import scrapy
import base64
import re
import random

class RandomProxy():

	proxy_address = ""
	user_pass = ""

	def __init__(self, *args, **kwargs):
		self.proxy_address = ""
		self.user_pass = ""

	def generateRandomProxy(self):


		fin = open('../../proxy_list.txt')
		proxies = {}
		partsCompile = re.compile('(\w+://)(\w+:\w+@)?(.+)')

		for line in fin.readlines():
		    partsMatch = partsCompile.match(line)
		    if not partsMatch:
		        if(not line.startswith("http://")):
		            line = "http://"+line.strip()
		        self.user_pass = "quixey2".strip() + ":" + "fg34gdsf85gdw".strip()
		        proxies[line] = self.user_pass
		    else:
		        # Cut trailing @
		        if partsMatch.group(2):
		            self.user_pass = partsMatch.group(2)[:-1]
		        else:
		            self.user_pass = ''
		        proxies[(partsMatch.group(1) + partsMatch.group(3)).strip()] = self.user_pass


		self.proxy_address = random.choice(proxies.keys())