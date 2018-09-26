all: clean
	@gunicorn --pythonpath featuren app:app --bind=0.0.0.0:8000 --reload

clean:
	@find . -name "*.pyc" -delete
	@find . -name "*__pycache__" -delete
	@find . -name ".coverage" -delete

tests: clean fmt lint
	@PYTHONPATH=featuren pytest --cov=featuren tests/

lint:
	@pycodestyle --ignore=E501 .

fmt:
	@black .

deps:
	@pip install -r requirements.txt

migrate:
	@orator -n migrate -c featuren/settings.py -p featuren/migrations -f

reset:
	@orator migrate:reset -c featuren/settings.py -p featuren/migrations

serve:
	@mkdocs serve

add-user:
	@python cli.py add-user
