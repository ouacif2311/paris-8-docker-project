import numpy as np
import math as m
import pandas as pd
import numpy.random as rand
from sqlalchemy import create_engine
import os
import subprocess
from algorithmes import Kmeans
import utilsFunctions


subprocess.call("/home/kmeans/wait-for-it.sh db:5432",shell=True)

res = pd.read_sql_table('iris', 'postgresql+psycopg2://kmeans_project_user:kmeans_project_user_password@db:5432/database')  

algoKmeans = Kmeans(3)

table=res.iloc[:,:-1].to_numpy()

clusters = algoKmeans.implementation(table)

classes = res.iloc[:,5].map(lambda x : utilsFunctions.convert_iris_data_class (x)).tolist()
clusters = clusters.reshape(150,).tolist()
d = {'Cluster': clusters, 'Class': classes}
df = pd.DataFrame(data=d)


engine = create_engine('postgresql+psycopg2://kmeans_project_user:kmeans_project_user_password@db:5432/database')
df.to_sql('output', engine,if_exists="replace")

