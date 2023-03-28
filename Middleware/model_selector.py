
import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

class LifeCycle:
    def __init__(self, path):
        self.model = joblib.load(path+'/lifecycle_qboost.pkl')
        self.data = pd.read_pickle(path+'/test_data.pkl')
    
    def former(self, result):
        prodCode = list(self.data.prodcode)
        result_dict = dict()
        for i in range(len(prodCode)):
            result_dict[prodCode[i]] = result[i]
        return result_dict


    def predict(self):
        result = self.model.predict(self.data[['sellPriceAvg', 'prodSex', 'prodNeckMeanQty', 'prodSexMeanQty', 'prodMfYearMeanQty', 'max_basePrice', 'prop2MeanQty',
                                     'min_basePrice', 'prodDsgn', 'prodSexMeanLifeW', 'prodCount', 'prop2', 'saleInitDay', 'prodMfYearMeanLifeW','initYearMeanLifeW', 'prodDsgnMeanQty',
                                     'fromStartSaleDiffW','cv', 'adi']])
        return self.former(result)
    

selected = LifeCycle('/Users/iseong-won/model-assistant-chatgpt/models')

print(selected.predict())
    
        

