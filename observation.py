# --coding:utf-8--
from glob import glob
import os
import pandas as pd

path_loc = os.path.join(os.getcwd(),'dataTrainComplete')
train_path_list = glob(os.path.join(path_loc ,"[1-9]*.txt"))
keyword_chem = pd.read_excel(os.path.join(os.getcwd() ,'Keywords','02chem.list.xlsx') ,header=None)
keyword_chem_1 = pd.read_excel(os.path.join(os.getcwd() ,'Keywords','02chem.list_1.xlsx') ,header=None)
pd.testing.assert_frame_equal(keyword_chem, keyword_chem_1)

keyword_crop = pd.read_excel(os.path.join(os.getcwd() ,'Keywords','02crop.list.xlsx') ,header=None)
keyword_crop_1 = pd.read_excel(os.path.join(os.getcwd() ,'Keywords','02crop.list_1.xlsx') ,header=None)
pd.testing.assert_frame_equal(keyword_crop, keyword_crop_1)

keyword_pest = pd.read_excel(os.path.join(os.getcwd() ,'Keywords','02pest.list.xlsx') ,header=None)
keyword_pest_1 = pd.read_excel(os.path.join(os.getcwd() ,'Keywords','02pest.list_1.xlsx') ,header=None)
pd.testing.assert_frame_equal(keyword_pest, keyword_pest_1)

data = {}
for path in train_path_list:
    with open(path ,encoding = 'utf-8-sig') as file:
        text = file.read()
        data[path[42:-4]] = text
label = pd.read_csv('TrainLabel.csv')