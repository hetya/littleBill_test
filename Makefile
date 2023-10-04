all : start

build :
	docker-compose -f project/docker-compose.yml --env-file .env build

create : build
	docker-compose -f project/docker-compose.yml --env-file .env create

start : create
	docker-compose -f project/docker-compose.yml --env-file .env start


database db:
	docker-compose -f project/docker-compose.yml --env-file .env up -d db

backend back : db
	docker-compose -f project/docker-compose.yml --env-file .env build back
	docker-compose -f project/docker-compose.yml --env-file .env up -d back

stop :
	docker-compose -f project/docker-compose.yml --env-file .env down

clean purge: stop
	docker system prune -af
	docker volume prune -f

re : clean all

.SILENT : build create start all stop clean
.PHONY : build create start all stop clean