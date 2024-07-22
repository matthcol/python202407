# Project magicsquareproject

## Unit testing with pytest
### CLI mode (cmd dos, powershell, unix/linux shell)
```
pytest

# verbose mode
pytest -v

# only  package tests
pytest -v tests

# only file test\test_magicalsquare.py
pytest -v tests\test_magicalsquare.py

# with filter
pytest -v -k square_ok
pytest -v -k square_ko
```
