.PHONY: init test


init:
	virtualenv env; \
	. env/bin/activate; \
	pip3 install -r requirements.txt --index-url https://pypi.org/simple;

test:
	. env/bin/activate; \
	PYTHONPATH=. pytest;
