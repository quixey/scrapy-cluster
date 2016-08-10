# -*- Makefile -*-

default: image

requirements.txt: ../requirements.txt
	cp $^ .

image: requirements.txt
	docker build --rm=true --tag="crawlers" -f Dockerfile .
