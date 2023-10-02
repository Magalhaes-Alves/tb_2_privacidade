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



while True:

    print("Niveis de Generalização para Atributo BeginDate {0 = Ano, 1 = Decada, 2=Seculo}:")
    beginDate_level = int(input("Selecione o nível de Generalização de BeginDate: "))
    
    print("Niveis de Generalização para Atributo Region {0 = Cidade, 1 = País, 2= Sub-Região,3 = Região}:")
    region_level = int(input("Digite o nível de generalizacao para Region: "))
    
    v_date,v_region =anonymizer.getValuesOfGeneralization(beginDate_level,region_level)

    print(f"Valores possíveis para essa generalização de nível {beginDate_level} para feature BeginDate:")
    print(v_date)

    print(f"Valores possíveis para essa generalização de nível {region_level} para feature Region:")
    print(v_region)


    again = str(input("Deseja continuar? [y/n]")).strip().lower()[0]
    
    if again =='n':
        break