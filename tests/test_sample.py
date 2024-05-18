# tests/test_app.py
from sample import intro

def test_sample():
    assert intro() == "Hello, World!"
