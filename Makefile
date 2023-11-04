SHELL:=/bin/bash
.venv:
	python -m venv .venv
	# source ./.venv/bin/activate

setup:
	source ./.venv/bin/activate && pip install -q --upgrade pip && pip install -q -r requirements.txt