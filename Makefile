.PHONY: run

all:
	docker build . -t app:latest

run:
	docker run -it -p 8000:8000 app:latest
