
VENV_PIP = .venv/bin/pip

install:
	python3 -m venv .venv
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install pytest

test:
	PYTHONPATH=. .venv/bin/pytest test/ -v

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +

.PHONY: install test clean