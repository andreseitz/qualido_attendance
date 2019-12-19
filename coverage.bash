#! /bin/bash

coverage3 run -m unittest discover -v
coverage html
firefox --new-instance --new-window htmlcov/index.html
rm -rf htmlcov
rm .coverage
