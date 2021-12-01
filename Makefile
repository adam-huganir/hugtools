SHELL := /bin/bash
VERSION_NUMBER = ` grep -P "^version = " pyproject.toml | cut -d\" -f2 `
PACKAGE_NAME=hugtools

build-publish-docs: build-docs publish-docs
build-publish: build publish

build-docs: UPDATE_API = false
build-docs:
	@rm -rvf ./docs/_build
	@if [[ -e "./docs" ]]; then \
  		if [[ ${UPDATE_API} == true ]]; then \
			sphinx-apidoc --force --no-toc --extensions "sphinx.ext.napoleon" \
							--extension "sphinx.ext.autosummary"  -o docs . ; \
		fi \
	else \
		sphinx-apidoc --full --force --no-toc --extensions "sphinx.ext.napoleon" \
						--extension "sphinx.ext.autosummary"  -o docs . ; \
	fi
	@cd ./docs && make html && make singlehtml && cd ..
	@echo "View documentation (locally) at file:///`pwd`/docs/_build/html/index.html"

version:
	echo ${PACKAGE_VERSION}

build:
	@rm -rf ./dist ; poetry build -f sdist

doc-server:
	python -m http.server -b localhost -d ./docs/_build/html

github-pages:
	@rm -rf html && cd docs && make html && cp -r _build/html ../html