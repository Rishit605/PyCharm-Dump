import os
import pandas as pd
import numpy as np


def importDataInfo(path):
    columns = ['Center', 'Left', 'Right', 'Stearing', 'Throttle', 'Brake', 'Speed']
    data = pd.read_csv(os.path.join(path, 'driving_log.csv'), names=columns)
    print(data.head())
