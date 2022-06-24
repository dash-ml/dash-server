.PHONY: build
# shell option to use extended glob from from https://stackoverflow.com/a/6922447/1560241
SHELL:=/bin/bash -O extglob

VERSION=`< VERSION`

author=$(Ge Yang)
author_email=$(yangge1987@gmail.com)

# notes on python packaging: http://python-packaging.readthedocs.io/en/latest/minimal.html
default: publish release
build:
	rm -rf dist
	python setup.py sdist
dev:
	make build
	pip install --ignore-installed dist/ml_dash*.whl
convert-rst:
	pandoc -s README.md -o README --to=rst
	sed -i '' 's/code/code-block/g' README
	sed -i '' 's/\.\. code-block:: log/.. code-block:: text/g' README
	sed -i '' 's/\.\//https\:\/\/github\.com\/episodeyang\/ml_logger\/tree\/master\/ml-dash-server\//g' README
	perl -p -i -e 's/\.(jpg|png|gif)/.$$1?raw=true/' README
	rst-lint README
resize: # from https://stackoverflow.com/a/28221795/1560241
	echo ./figures/!(*resized).jpg
	convert ./figures/!(*resized).jpg -resize 888x1000 -set filename:f '%t' ./figures/'%[filename:f]_resized.jpg'
update-doc: convert-rst
	python setup.py sdist upload
release:
	git tag v$(VERSION) -m '$(msg)'
	git push origin --tags
publish: convert-rst
	make test
	make build
	twine upload dist/*
publish-no-test: convert-rst
	make build
	twine upload dist/*
start: # dev start: use sanic to bootstrap.
	source activate playground && python -m ml_dash.main --host=0.0.0.0 --port=8081 --workers=4 --logdir="tests/runs"
test:
	python -m pytest dash_server_specs/test_ml_dash.py --capture=no
