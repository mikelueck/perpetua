.PHONY: run

PROJECT_ID=perpetua-309819
TAG=1.0
CREDS=Downloads/perpetua-309819-490675f81f96.json

all:
	docker build . -t app:latest

run:
	export GOOGLE_APPLICATION_CREDENTIALS="$(CREDS)" &
	docker run --log-driver=gcplogs -it -p 8000:8000 app:latest

run_local:
	docker pull gcr.io/$(PROJECT_ID)/app:$(TAG)
	docker run --log-driver=gcplogs -it -p 8000:8000 gcr.io/$(PROJECT_ID)/app:$(TAG)
	
repo:
	docker tag app:latest gcr.io/$(PROJECT_ID)/app:$(TAG)
	docker push gcr.io/$(PROJECT_ID)/app:$(TAG)

