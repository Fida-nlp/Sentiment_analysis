.PHONY: build run push

build:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt
	docker build -t sentiment-analysis-api .

run:
	if [ ! -d ".venv" ]; then \
		python3 -m venv .venv; \
		. .venv/bin/activate && pip install -r requirements.txt; \
	fi; \
	. .venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --port 8000

push:
	docker tag sentiment-analysis-api <aws_account_id>.dkr.ecr.<region>.amazonaws.com/sentiment-analysis-api
	docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/sentiment-analysis-api