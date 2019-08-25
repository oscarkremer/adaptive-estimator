#################################################################################
# GLOBALS                                                                       #
#################################################################################
.DEFAULT_GOAL := check
PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BUCKET = [OPTIONAL] your-bucket-for-syncing-data (do not include 's3://')
PROFILE = default
EPOCHS = 30
NETWORK_ID = 1
PROJECT_NAME = cerberus-garten
PYTHON_INTERPRETER = python3

################################################################################
# COMMANDS                                                                     #
# TO SHOW OUTPUT USE LOGGER=stdout                                             #
################################################################################


model:
	@echo "---> Test - Estimation"
	@$(PYTHON_INTERPRETER) src/api/model_parameters.py


evaluate:
	@echo "---> Starting evaluation"
	@$(PYTHON_INTERPRETER) src/api/evaluate.py


setup: check_environment
	@echo "---> Running setup.."
	@conda env create -f environment.yml
	@cp -n .env.example .env
	@echo "---> To complete setup please run \n---> source activate cerberus"


install:
	@echo "---> Installing dependencies"
	@conda env update -f environment.yml


imag_proc:
	@echo "---> Image Segmentation"
	@$(PYTHON_INTERPRETER) src/api/image_process.py

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

train:
	@echo "---> Load and prepare files, for training and testing"
	@echo "---> This may take a few minutes, depending on the number of epochs"
	@$(PYTHON_INTERPRETER) src/api/classifier_fit.py --epochs $(EPOCHS) --network-id $(NETWORK_ID)


validate:
	@echo "---> Start validation of convolutional networks"
	@$(PYTHON_INTERPRETER) src/api/validate.py 


download: dirs
	aws s3 cp s3://thrive-cea/processed/sales.csv data/processed/ --quiet
	aws s3 cp s3://thrive-cea/processed/stock.csv data/processed/ --quiet


lint:
	flake8 src


predict:
	@$(PYTHON_INTERPRETER) src/api/predict.py


check_environment:
	@echo "---> Checking environment.."
	$(PYTHON_INTERPRETER) test_environment.py


autocorrect:
	@echo "---> Processing autocorrect"
	@autopep8 --in-place --aggressive --aggressive --global-config .flake8 $(shell find . -name '*.py')


console:
	@$(PYTHON_INTERPRETER)
