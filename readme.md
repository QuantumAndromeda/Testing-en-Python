To set up the environment execute:
```
python -m venv .venv
.venv\Scripts\activate
pip install -r ./requirements.txt
```
To run tests execute (first command only if not in venv yet):
```
.venv\Scripts\activate
python -m unittest -v ./test/calculator_test.py
```