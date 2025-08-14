init:
	python -m venv .venv && (. .venv/bin/activate || .venv\Scripts\activate) && pip install -r requirements.txt

lint:
	ruff check .
	black --check .

fmt:
	black .

test:
	pytest -q

run:
	python -m src.bot.main
