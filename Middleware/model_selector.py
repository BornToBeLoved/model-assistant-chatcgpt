
import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# 제품 생애 총 판매량 예측 모델
class LifeCycle:
    def __init__(self, path):
        self.model = joblib.load('/Users/iseong-won/model-assistant-chatgpt/models/lifecycle_qboost.pkl')
        self.data = pd.read_pickle(path)
    
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
    

# selected = LifeCycle('/Users/iseong-won/model-assistant-chatgpt/models')

# print(selected.predict())
    
        

