build:
	docker build -t sentiment-analysis-api .

run:
	docker run -p 8000:8000 sentiment-analysis-api

push:
	docker tag sentiment-analysis-api <aws_account_id>.dkr.ecr.<region>.amazonaws.com/sentiment-analysis-api
	docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/sentiment-analysis-api