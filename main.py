import pandas as pd
import numpy as np

from classes.KAnonymizer import KAnonymizer



ds = pd.read_csv(filepath_or_buffer='Artists-Pseudo-02.csv',sep=',')

sensitivity_features = [i  for i in ds.columns if i not in ['Region','BeginDate','Income ($)']] 
anonymizer = KAnonymizer(ds,sensitivity_features)

while True:

    print("Niveis de Generalização para Atributo BeginDate {0,1,2}:")
    beginDate_level = int(input("Selecione o nível de Generalização de BeginDate"))
    
    print("Niveis de Generalização para Atributo Region {0,1,2,4}:")
    region_level = int(input("Digite o nível de generalizacao para Region:"))
    
    anonymizer.setGeneralizationFeatureLevel({'BeginData':beginDate_level,
                                              'Region':region_level})
    
    
    k_values =anonymizer.getKValues()
    
    print(f'Valores possíveis para K: {k_values}')
    
    for k in k_values:
        
        anonymizer.anonymizerK(k)
        anonymizer.saveAnonymizedData(f'{k}AnonArtists.csv')
        
        
    again = str("Deseja continuar? [y/n]").strip().lower()[0]
    
    if again =='n':
        break
        
    
    




