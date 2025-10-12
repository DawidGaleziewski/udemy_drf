# basic python flow

python3 -m venv .venv
source .venv/bin/activate
pip3 freeze
python -m pip install Django
pip3 freeze > requirements.txt

# vs code extenstions
tabnine

# django setup
add new app to settings.py, migrate dbs, create superuser