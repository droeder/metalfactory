python -m venv venv
. ./venv/bin/activate

pip install autopep8 bandit pylint mypy
python3 -m pip install --upgrade pip
pip install -r dev_requirements.txt