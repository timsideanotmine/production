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
def simulatie(days_to_simulate, data_points, dagelijkse_productie, use_random_seed):
    """
    What:
        function will take production numbers (zero and non-zero)
        for a factory and will 
        calculate the chance p_zero 

    Args:
        days_to_simulate : integer, obligated
                requested number of days to simulate
        data_points : integer, obligated
                used number of linspace intervals to draw the PDF function 
                for given dagelijke_productie parameter
        dagelijkse_productie : ndarray, obligated
                in this exercise the column ['production'] from given dataset
        use_random_seed : string, obligated
                any value <> 'random' will not set the seed value for np.linspace
        
    Returns:
        plotdata_enkel_productie : ndarray 
            plot data with non-zero values only to be used for 
            histogram live production data
            against computed simulation plot data
        x : ndarray
            evaluation base fr pdf
        pdf : ndarray
            Probability density function evaluated at x
        plotdata_simulatie : ndarray
            plot data with non-zero data included, result of simulation
        mu : float64
            derived mu value from norm.fit(plotdata_enkel_productie) 
        sigma : float64
            derived sigma value from norm.fit(plotdata_enkel_productie) 
        p_zero : float
            chance on zero production value

    """    
    if use_random_seed == 'random':
        np.random.seed()
    else:
        np.random.seed(42)
    
    dagelijkse_productie_zonder_productie = dagelijkse_productie[dagelijkse_productie == 0]
    dagelijkse_productie_enkel_productie = dagelijkse_productie[dagelijkse_productie != 0]
    
    p_zero = len(dagelijkse_productie_zonder_productie) / len(dagelijkse_productie) 
    
    plotdata_enkel_productie = dagelijkse_productie_enkel_productie.to_numpy()
    mu, sigma = norm.fit(plotdata_enkel_productie)

    x = np.linspace(min(dagelijkse_productie_enkel_productie), max(dagelijkse_productie_enkel_productie), data_points)
    pdf = norm.pdf(x, mu, sigma)

    zero_production_simulated = np.zeros(int(p_zero * days_to_simulate))
    positive_production_simulated = np.random.normal(mu, sigma, days_to_simulate - len(zero_production_simulated))
    daily_production_simulated = np.concatenate((zero_production_simulated, positive_production_simulated))
    daily_production_integer_simulated = np.round(daily_production_simulated).astype(int)
        
    return plotdata_enkel_productie, x, pdf, daily_production_integer_simulated, mu, sigma, p_zero
