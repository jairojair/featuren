
## Install from scratch!

Firstly, install requirements down below:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Git](https://git-scm.com) 

##### Git clone

	git clone https://github.com/jairojair/featuren.git

##### Setup

	cd featuren

	docker-compose build
	docker-compose run app make migrate

##### Add new user

	docker-compose run app make add-user

##### Run

	docker-compose up

Access: [http://0.0.0.0:8000](http://0.0.0.0:8000) and your browser will show the message below: 

```bash
{
	"message":"Welcome to Featuren!",
	"documentation":"https://jairojair.github.io/featuren/"
}
```
