test:
	@pytest -v

lint:
	@flakehell lint

black:
	@black fizzbuzz/ tests/
