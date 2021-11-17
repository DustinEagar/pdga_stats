# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import time
from datetime import datetime
import os

import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

style.use("fivethirtyeight")

df = pd.read_csv("./pdga_player_stats_05_11_21_01-48-08.csv")

df["Rating"].plot()
