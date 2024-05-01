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

from sklearn.linear_model import LinearRegression

from tqdm import tqdm

import seaborn as sns

# -------------------------------------------------
def find_df_name(df):
    """
    Finds the variable name associated with a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame for which to find the variable name.

    Returns:
        str: The variable name.
    """
    for name, obj in globals().items():
        if obj is df:
            return name
    return None  # If not found

# -------------------------------------------------------------
def show_info_about_column(df, col):
    """
    Show some standard information for a Dataframe all together 

    Args:
        df (pd.DataFrame): The DataFrame to analyze
        col (): The column of the DataFrame to analyze

    Returns:
        a bunch of printed output
    """
    print(f"----- {find_df_name(df)} -- {col} -----------------------------------")
    print(f"{df[col].describe(include='all') = } \n")  
    print(f"----- {find_df_name(df)} -- {col} -----------------------------------")
    print(f"{df[col].nunique(dropna=True) = } \n ")    
    print(f"----- {find_df_name(df)} -- {col} -----------------------------------")
    print(f"{df[col].value_counts() = } \n ")    
    print(f"----- end of query --------------------------------------------------")

    return
