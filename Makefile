S3_FILE=docker-compose/s3_storages.yaml

.PHONY:

up_s3:
	docker-compose --env-file .env -f ${S3_FILE} up --build
down_s3:
	docker-compose --env-file .env -f ${S3_FILE} down
