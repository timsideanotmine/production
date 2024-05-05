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

def bereken_confidence_interval(nr_of_executions,
                                use_random_seed,
                                used_data_set,
                                used_data_set_column,
                                sample_size_factor,
                                ci_interval):
    
    """
    What:
        function will calulate the confidence interval and will
        return the mean values used for it

    Args:
        nr_of_executions : integer, obligated
                requested number of executing the mean calculation
                based on sample size
        use_random_seed : string, obligated
                any value <> 'random' will not set the seed value for np.linspace
        used_data_set : data frame to be used, obligated
                must contain used_data_set_column
        used_data_set_column : obligated, column with values to be used to 
                calculate the mean() value over
        sample_size_factor : float, obligated
                factor > 0.0 and <= 1.0
                will reduce the sample size with given factor        
        ci_interval : list, obligated [value 1, value 2]
                [2.5, 97.5], 
                value 1 > 0.0 and < value 2 
                value 2 < 100.0 and > value 1                        
        
    Returns:
        confidence_interval : ndarray 
            2 values, being the lower and the upper value for the interval
        all_the_means_calculated : ndarray
            calculated data set of all means, with length nr_of_executions

    """    
    
    # array for storing bootsstrapped calculated means
    all_the_means_calculated = np.empty(nr_of_executions)
    
    # picking randmness
    if use_random_seed == 'random':
        np.random.seed()
    else:
        np.random.seed(42)
    
    #  dloing all the bootsstrapping
    for i in range(nr_of_executions):
        picked_samples = np.random.choice(used_data_set[used_data_set_column], 
                                           size=int(len(used_data_set)
                                                    *sample_size_factor), 
                                           replace=True)
        all_the_means_calculated[i] = picked_samples.mean()

    #  calculating the reqested interval
    confidence_interval = np.percentile(all_the_means_calculated, ci_interval)

    return confidence_interval, all_the_means_calculated 