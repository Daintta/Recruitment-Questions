ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

install:
	pip3 install -r requirements.txt

encrypt:
	staticrypt src/generated/index.html -p ${STATICRYPT_PASSWORD} \
		--template-color-primary "#172738" \
		--template-title "Daintta SWE - Recruitment Q&A" \
		--template-color-secondary "#0BB3AD" \
		--template-error "Incorect password."

run:
	python3.12 src/__init__.py
	$(MAKE) encrypt

open:
	open ${ROOT_DIR}/encrypted/index.html

ro: run open
