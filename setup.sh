# setup the repo basic structure

# create python virtual environment
python -m venv .venv

# create folders
mkdir -p data
mkdir -p notebooks
mkdir -p src
mkdir -p models
mkdir -p app
mkdir -p tests

# copy input csv (original data) to data folder
cp 'input/telco_customer_churn_data 1.csv' data/telco_customer_churn_data.csv


# ... fill README
# ... fill requirements.txt

# activate virtual environment
source .venv/Scripts/activate

# install requirements
pip install -r requirements.txt






# deactivate virtual environment
deactivate
