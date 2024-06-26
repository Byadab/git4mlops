import pathlib
import os
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT,"datasets")

TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'

MODEL_NAME = 'classification.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,'trained_models')

TARGET = 'Loan_Status'

#Final features used in the model
FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

CAT_FEATURES = ['Gender',
 'Married',
 'Dependents',
 'Education',
 'Self_Employed',
 'Credit_History',
 'Property_Area']

# in our case it is same as Categorical features
FEATURES_TO_ENCODE = ['Gender',
 'Married',
 'Dependents',
 'Education',
 'Self_Employed',
 'Credit_History',
 'Property_Area']

FEATURE_TO_MODIFY = ['ApplicantIncome']
FEATURE_TO_ADD = 'CoapplicantIncome'

DROP_FEATURES = ['CoapplicantIncome']

LOG_FEATURES = ['ApplicantIncome', 'LoanAmount'] # taking log of numerical columns








'''#importing important libraries
import pathlib
import os
import prediction_model

#pachage.__file__ --> points to the specific pachage path
#getting the folder location for prediction_model folder
PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'

MODEL_NAME = 'classification.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, "trainded_models")

TAREGT = 'Loan_Status'

#final features used in the model
FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
            'ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term','Credit_History',
            'Property_Area']

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                'Credit_History', 'Property_Area']


#inour casse same as cat_features
FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                'Credit_History', 'Property_Area']

FEATURE_TO_MODIFY = ['ApplicantIncome']
FEATURE_TO_ADD = 'CoapplicantIncome'

DROP_FEATURES = ['CoapplicantIncome']

#Log of numerical columns
LOG_FEATURES = ['ApplicantIncome', 'LoanAmount'] '''