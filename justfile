run:
    streamlit run sedlec/app/app.py

compile-requirements:
    pip-compile requirements.in -o requirements.txt --no-emit-index-url --no-emit-find-links  --no-allow-unsafe --no-header --resolver=backtracking

add PACKAGE:
    @echo {{PACKAGE}} >> requirements.in
    just --justfile {{justfile()}} compile-requirements
    just --justfile {{justfile()}} install

install-dev:
    pip install -Ur requirements-dev.txt 

install:
    pip install -Ur requirements.txt 

install-all: install install-dev
