import random

class Model:

    def __init__(self):
        pass

    def predict(self, payload: dict):
        
        if payload['capital.gain'] > 10000:

            return {
                'status' : 'success',
                'prediction_raw' : 0.99,
                'predicted_income_class' : '>50k',
            }
        
        elif payload['capital.loss'] < 2000:

            return {
                'status' : 'success',
                'prediction_raw' : 0.01,
                'predicted_income_class' : '<=50k',
            }

        else:
            pred_raw = random.random()
            pred_income = '<=50k'

            if pred_raw > 0.5:
                pred_income = '>50k'

            return {
                'status' : 'success',
                'prediction_raw' : 0.01,
                'predicted_income_class' : '<=50k',
            }
        



