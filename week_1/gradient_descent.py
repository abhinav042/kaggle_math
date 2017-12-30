# import modules 
import numpy as np 
import pandas as pd
import matplotlib as mpl 
import random
import os
from mpl_toolkits.mplot3d import Axes3D

# extract data
FILE = "kc_house_data.csv"

def get_data(FILE):
    train_df = pd.read_csv(FILE)

def check_file(FILE):
    if not os.path.isfile(FILE):
        print('this file doesnt exist')
        quit()

if __name__ == '__main__':
    check_file(FILE)
    
