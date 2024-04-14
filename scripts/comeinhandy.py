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

# -------------------------------------------------------------
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

# -------------------------------------------------------------
def laad_msr_gegevens_in_dataframe(loc):
    """
    What:
        Loads the MSR values, given the specific format of the json file, into a dataframe
        note : it is expected there is ALWAYS a file with correctly json formatted data

    Args:
        loc : a location where to find the *.json file 
        
    Returns:
        df (pd.DataFrame): the DataFrame to create with the location and MSR numbers
    """
    # load jsn file with MSR values
    loc = "../data/raw/productiemodel/data_productie/master_data.json"
    with open(loc, 'r') as file:
        msr_file = json.load(file)

    # convert the json data to a suitable dictionary format to be loaded into a dataframe
    msr_expanded = list()
    for msr_description, msr_value in msr_file.items():
        #  make a dictionary each time
        dict_msr = {'factory':msr_description[:3], 
                    'msr_description': msr_description,
                    'msr_value':msr_value
                   }
        msr_expanded.append(dict_msr)

    # load the list of data dictionaries into the dataframe for a MSR value per location
    df_msr = pd.DataFrame(msr_expanded)
        
    return df_msr

# -------------------------------------------------------------
def laad_dagelijkse_productie_in_dataframe(fact, loc):
    """
    What:
        Loads the available JSON files, given the specific format of the json file, into a dataframe
        note : it is expected there is ALWAYS correctly json formatted data

    Args:
        fact : name of factory for which daily production data is loaded
        loc  : a location where to find the *.json file(s)
        
    Returns:
        df (pd.DataFrame): the DataFrame to be create with daimy production for a specific factory
    """

    # load all the json files into a list of json files
    daily_production_files = list()

    # loop over files in folder
    for file in os.listdir(loc):

        if file.endswith('.json'):
            json_file_path = os.path.join(loc, file)
            
            
            # json_files.append(os.path.join(loc, filename))
            # print(json_file_path)
            with open(json_file_path, 'r') as json_file:
                json_data = json.load(json_file)

            #  add factory identification to the dictionary
            json_data['factory'] = fact
            
            daily_production_files.append(json_data)


    # convert the list to a single data frame
    df_production = pd.DataFrame(daily_production_files)
    
    return df_production

# -------------------------------------------------------------

# -------------------------------------------------------------

# -------------------------------------------------------------
