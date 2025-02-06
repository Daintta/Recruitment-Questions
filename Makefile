ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

install:
	pip3 install -r requirements.txt

run:
	python3.12 src/__init__.py

open:
	open ${ROOT_DIR}/src/generated/index.html

ro: run open