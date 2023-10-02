import pandas as pd
import numpy as np

from classes.KAnonymizer import KAnonymizer

ds = pd.read_csv(filepath_or_buffer='Artists-Pseudo-02.csv',sep=',')

sensitivity_features = [i  for i in ds.columns if i not in ['Region','BeginDate','Income ($)']] 
anonymizer = KAnonymizer(ds,['Region','BeginDate'],sensitivity_features)

anonymizer.setK(2)
anonymizer.plotHistogram('2-anonimato.png')
anonymizer.setK(4)
anonymizer.plotHistogram('4-anonimato.png')
anonymizer.setK(8)
anonymizer.plotHistogram('8-anonimato.png')

#print(anonymizer.getValuesOfGeneralization(2,3))

anonymizer.plotHistogram()
""" while True:

    print("Niveis de Generalização para Atributo BeginDate {0,1,2}:")
    beginDate_level = int(input("Selecione o nível de Generalização de BeginDate"))
    
    print("Niveis de Generalização para Atributo Region {0,1,2,3}:")
    region_level = int(input("Digite o nível de generalizacao para Region:"))
    
    anonymizer.getValuesOfGeneralization(beginDate_level,region_level)
    

    again = str("Deseja continuar? [y/n]").strip().lower()[0]
    
    if again =='n':
        break  """