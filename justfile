run:
    streamlit run sedlec/app.py

compile-requirements:
    pip-compile requirements.in -o requirements.txt --no-emit-index-url --no-emit-find-links  --no-allow-unsafe --no-header --resolver=backtracking

add PACKAGE:
    @echo {{PACKAGE}} >> requirements.in
    : compile-requirements
    : install

install-dev:
    pip install -Ur requirements-dev.txt 

install:
    pip install -Ur requirements.txt 

install-all: install install-dev
