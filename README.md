# Nodal Analysis Circuit Solver

A python program that solves electrical circuits.

## Usage

### Web Application

Run these commands to open the web app:

```bash
git clone https://github.com/daniyalmarofi/NACS.git
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then access the web applocation from `http://127.0.0.1:8000/`.

### Command Line

To run the app from command line, run `cli_version.py` file.

Here is commands to use the app:

| Functionality        | Command                               | Example   |
| -------------------- | ------------------------------------- | --------- |
| Add a Resistor       | R {leftNode} {rightNode} {resistance} | R 0 1 10  |
| Add a Voltage Source | IV {posTerm} {negTerm} {voltage}      | IV 0 1 24 |
| Add a Current Source | IC {comeIn} {comeOut} {current}       | IC 1 0 5  |
| Solve Circuit        | calculate                             | calculate |

## Screenshot

![Screenshot](.\screenshot.png)
