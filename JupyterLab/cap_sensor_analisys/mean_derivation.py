import cv2
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import pandas as pd
from tqdm import tqdm
import os
import csv
from glob import glob
from pathlib import Path

#ファイルのパスは各データ群に統一
#例えば，Cap sensorのEcoflex 1Wt%のサーマルエクスパンジョンなら，
#Ecoflex 1%で，荷重 vs 平均電気容量，分散，変化率のdfを出力.

def ave_dri(Target_path):
    df1 = pd.read_table(Target_path, sep="\s+",header=1, usecols=['Cp'])
    n_low = len(df1)
    ave_Cp = df1.mean(numeric_only=True)
    deri_Cp = df1.std(numeric_only=True)
    return df1,n_low, ave_Cp, deri_Cp

# 重さは同期できないので，sortしたデータを順番に表示していく．
def weightdep(Target_path):
    dataList = glob.glob(path=TargetPath)
    
    return dataList

print((r"C:\Users\tagawa\Desktop\JupyterLab\cap_sensor_analisys\original_data\*"))