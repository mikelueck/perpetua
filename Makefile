.PHONY: run

CREDS="Downloads/perpetua-309819-490675f81f96.json"

all:
	docker build . -t app:latest

run:
  export GOOGLE_APPLICATION_CREDENTIALS="$(CREDS)" &
	docker run --log-driver=gcplogs -it -p 8000:8000 app:latest
