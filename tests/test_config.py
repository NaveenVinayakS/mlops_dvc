# we execute this test by using "pytest -v"

# configtest.py is a dependency file for this

import pytest
import json
import logging
import os
import joblib
from prediction_service.prediction import form_response,api_response
import prediction_service

# function name must start with TEST
    # assert -> assertion return true(PASSED) if test case PASS.
    # individually we can run this file "pytest -v"
    # we can run this file using tox command also

    # what tox does is it will create a python virtual enviorment using tox ini file and requirements are
    # collected from -rrequirements.txt , command is "tox" if any changes in requirement the "tox -r"

# for testing purpose this is the input data that we are giving for model
input_data = {
    "incorrect_range":
    {"fixed_acidity": 7897897,
    "volatile_acidity": 555,
    "citric_acid": 99,
    "residual_sugar": 99,
    "chlorides": 12,
    "free_sulfur_dioxide": 789,
    "total_sulfur_dioxide": 75,
    "density": 2,
    "pH": 33,
    "sulphates": 9,
    "alcohol": 9
    },

    "correct_range":
    {"fixed_acidity": 5,
    "volatile_acidity": 1,
    "citric_acid": 0.5,
    "residual_sugar": 10,
    "chlorides": 0.5,
    "free_sulfur_dioxide": 3,
    "total_sulfur_dioxide": 75,
    "density": 1,
    "pH": 3,
    "sulphates": 1,
    "alcohol": 9
    },

    "incorrect_col":
    {"fixed acidity": 5,
    "volatile acidity": 1,
    "citric acid": 0.5,
    "residual sugar": 10,
    "chlorides": 0.5,
    "free sulfur dioxide": 3,
    "total_sulfur dioxide": 75,
    "density": 1,
    "pH": 3,
    "sulphates": 1,
    "alcohol": 9
    }
}

TARGET_range = {
    "min": 3.0,
    "max": 8.0
}


# we pass the input data to form_response and api_response , we check the output range and name of columns
# and number of columns

def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert  TARGET_range["min"] <= res <= TARGET_range["max"]

def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert  TARGET_range["min"] <= res["response"] <= TARGET_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message
