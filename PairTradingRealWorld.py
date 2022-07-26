# the prices of two assets diverge and converge over time. the fact that spread deviations return to their mean. 
# find a good pair for trading, optimal entry/exit and a stop loss as an additional risk management component.
#The co-integration test identifies scenarios where two non-stationary time series are integrated together in
# a way that they cannot deviate from equilibrium in the long term.
# tests for co-integration are Johansen Test (12 timeseries) and the Augmented Dickey-Fuller (ADF) test(2 timeseries).

import numpy as np
import pandas as pd
import statsmodels.api as sm
from johansen import coint_johansen

data = pd.read_csv("http://web.pdx.edu/~crkl/ceR/data/usyc87.txt",index_col='YEAR',sep='\s+',nrows=66)
y = data['Y']
c = data['C']
 
from statsmodels.tsa.vector_ar.vecm import coint_johansen
 
"""
    Johansen cointegration test of the cointegration rank of a VECM
 
    Parameters
    ----------
    endog : array_like (nobs_tot x neqs)
        Data to test
    det_order : int
        * -1 - no deterministic terms - model1
        * 0 - constant term - model3
        * 1 - linear trend
    k_ar_diff : int, nonnegative
        Number of lagged differences in the model.
"""
 
def joh_output(res):
    output = pd.DataFrame([res.lr2,res.lr1],
                          index=['max_eig_stat',"trace_stat"])
    print(output.T,'\n')
    print("Critical values(90%, 95%, 99%) of max_eig_stat\n",res.cvm,'\n')
    print("Critical values(90%, 95%, 99%) of trace_stat\n",res.cvt,'\n')
 
 
# Model 3 (2 lag-difference used = 3 lags VAR or VAR(3) model)
# with constant/trend (deterministc) term
joh_model3 = coint_johansen(data,0,2) # k_ar_diff +1 = K
joh_output(joh_model3)
 
# Model 2: with linear trend only
joh_model2 = coint_johansen(data,1,2) # k_ar_diff +1 = K
joh_output(joh_model2)
 
# Model 1: no constant/trend (deterministc) term
joh_model1 = coint_johansen(data,-1,2) # k_ar_diff +1 = K
joh_output(joh_model1)


#The z-score is calculated from raw data points of our distribution so that the new 
# distribution is a normal distribution with mean 0 and standard deviation of 1.
# With this distribution we can create threshold levels such as 2 sigma, 3 sigma, and so on.


# When Z-score crosses upper threshold:

# Short asset A // Long asset B

# When Z-score crosses lower threshold:

# Long asset A // Short asset 

