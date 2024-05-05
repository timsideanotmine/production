# -------------------------------------------------------------
# standaard in python
import os 
import datetime
import sys
import random
import calendar
import gzip
import json

# -------------------------------------------------------------
# te installeren packages en modules
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

from scipy.stats import weibull_min
from scipy.stats import skewnorm
from scipy.stats import norm
from scipy.stats import pareto
from scipy.stats import beta

from scipy import stats as st

from sklearn.linear_model import LinearRegression

from tqdm import tqdm

import seaborn as sns

def bereken_percentiel_voor_rang(prijs_rang, rijen):
    """
    bereken in welk percentieel de prijs van een merk ligt.

    Args:
        prijs_rang (int): de rang in de gesorteerde dataframe
        rijen (int): totaal_aantal rijen van de dataframe 

    Returns:
        float: het percentage percentiel
    """
    percentiel = (prijs_rang / rijen) * 100
    return percentiel
