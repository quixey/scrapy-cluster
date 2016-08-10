
FROM orca.quixey.com/python27

MAINTAINER Don Bennett <don@quixey.com>

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libxml2 libxslt1-dev libffi-dev libssl-dev
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY scrapy.cfg scrapy.cfg
COPY crawling crawling

ENTRYPOINT ["scrapy", "runspider"]
CMD ["crawling/spiders/link_spider.py"]
