A simple python program for placing incoming freshman into floors

### To Get Started

1. Clone this repo in your preferred directory and enter the repo:
    ```
    git clone git@github.com:mrkwanzaa/roominNzoomin.git
    ```

2. Setup a virtual environment and install all requirements:
    Install (or upgrade) virtualenv:
    ```
    python3 -m pip install --upgrade virtualenv
    ```
    Create your virtualenv named `venv`:
    ```
    python3 -m virtualenv venv
    ```
    Activate your virtual environment on Unix (Mac or Linux):
    ```
    source venv/bin/activate
    ```
    Install all requirements for development:
    ```
    pip install -r requirements.txt
    ```
3. Run `python main.py` to see results.
    Note that this uses `students.csv` and `floors.csv` both of which have included examples.

TODO:
    Implement survey value adjustment in `students.py`
    Auto group staple groups