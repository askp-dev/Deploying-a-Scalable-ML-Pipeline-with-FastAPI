import pytest
from sklearn.model_selection import train_test_split
import os
import pandas as pd
from ml.data import process_data
from ml.model import train_model
from train_model import cat_features
from sklearn.ensemble import RandomForestClassifier

"""
# Setup: Prepared a small dataset for testing, stored in data/testdata.csv

def setup_training_data():
    project_path = "../Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
    data_path = os.path.join(project_path, "data", "census.csv")
    test_path = os.path.join(project_path, "data", "testdata.csv")
    data = pd.read_csv(data_path)
    ds = data.sample(5)  # small sample for testing
    ds.to_csv(test_path, encoding='utf-8', index=False)


setup_training_data()  # Ran once to create the test data

"""

# Prepare training data for tests
project_path = "../Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
test_path = os.path.join(project_path, "data", "testdata.csv")
data = pd.read_csv(test_path)
train, test = train_test_split(data, test_size=0.2, random_state=42)

X_train, y_train, encoder, lb = process_data(
    train,
    categorical_features=cat_features,
    label="salary",
    training=True
)


def test_correct_algorithm():
    """
    # Test to ensure the correct algorithm is used
    """
    model = train_model(X_train, y_train)
    assert isinstance(
        model, RandomForestClassifier), "Model uses incorrect algorithm; Expected a RandomForestClassifier"
    print("test_ml.py::test_correct_algorithm PASSED")


# TODO: If the training and test datasets have the expected size or data type.
def test_correct_test_training_size():
    """
    # Test to Ensure the training and test datasets have the expected size.
    """
    assert train.shape[0] == 4, "Unexpected training data size"
    assert 4 * test.shape[0] == train.shape[0], "Incorrect relative data sizes"
    print("test_ml.py::test_correct_test_training_size PASSED")


def test_correct_feature_names():
    """
    # Test to Ensure the training and test datasets have the expected feature names.
    """
    expected_features = cat_features

    assert all(
        col in train.columns for col in expected_features), "Training data is missing expected features"
    assert all(
        col in test.columns for col in expected_features), "Test data is missing expected features"
    print("test_ml.py::test_correct_feature_names PASSED")
