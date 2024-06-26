import pandas as pd
import numpy as np
import joblib
from pathlib import Path
import os
import sys

##add bellow PATH TO avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))


from prediction_model.config import config
from prediction_model.processing.data_handeling import load_pipeline
# import prediction_model.processing.preprocessing as pp
# import prediction_model.pipeline as pipe


classification_pipeline = load_pipeline(config.MODEL_NAME)

def generate_predictions(data_input):
    data = pd.DataFrame(data_input)
    pred = classification_pipeline.predict(data[config.FEATURES])
    output = np.where(pred==1,'Y','N')
    result = {'prediction':output}
    return result


# def generate_predictions():
#     test_data = load_dataset(config.TEST_FILE)
#     pred = classification_pipeline.predict(test_data[config.FEATURES])
#     output = np.where(predictions==1,'Y','N')
#     print(output)
#     # result = {'predictions':output}
#     return output

if '__name__' == '__main__':
    generate_predictions()
    
    