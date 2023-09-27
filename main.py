import pandas as pd
import numpy as np

from classes.KAnonymizer import KAnonymizer



ds = pd.read_csv(filepath_or_buffer='Artists-Pseudo-02.csv',sep=',')

sensitivity_features = [i  for i in ds.columns if i not in ['Region','BeginDate','Income ($)']] 

print(sensitivity_features)
print(ds)


ano = KAnonymizer(ds,sensitivity_features)




