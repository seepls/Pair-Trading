# Import  libraries 
!pip install arch
import warnings
import numpy as np
import pandas as pd
from pandas_datareader import data 
import datetime as dt
import matplotlib.pyplot as plt 
import statsmodels.regression.linear_model as rg
import statsmodels.tsa.api as sm #or as ts. The package now includes various advances, 
#such as Value at Risk, Vector Autoregression, Vector Error Correction
from scipy import optimize
from IPython.display import Image
import arch.unitroot as at
import warnings
 
# Data reading , similar economies and commodities sector : Australian and Canadian  
data = pd.read_csv('Pairs-Trading-Analysis-Data.txt',index_col='Date',parse_dates=True)
intl = data.loc[:,['aus','can']]

# training and test set 
tintl = intl[:'2014-12-31']
tintl.columns=['taus','tcan']
fintl=intl['2015-01-02':]
fintl.columns = ['faus','fcan']

# return calculation
taus = tintl['taus']
tcan = tintl['tcan']
rtaus = taus.diff().fillna(0)
rtcan = tcan.diff().fillna(0)

# correlation coefficient : measures degree to which paired assets price returns move together taking into 
# account std. deviation.
print(np.round(pd.DataFrame(rtaus).join(rtcan).corr(),4))


# Price chart 
figl,ax1 = plt.subplots()
ax1.plot(taus)
ax1.legend(loc='lower left')
ax2 = ax1.twinx()
ax2.plot(tcan, color='orange')
ax2.legend(loc='lower right')
plt.suptitle('AUS-CAN Prices')
plt.show()

#Return Chart 
figl,ax1 = plt.subplots()
ax1.plot(rtaus)
ax1.legend(loc='lower left')
ax2 = ax1.twinx()
ax2.plot(rtcan, color='orange')
ax2.legend(loc='lower right')
plt.suptitle('AUS-CAN Returns')
plt.show()

#AUS-CAN non-stationary prices check 
print('=== AUS Prices Augumented Dickey-Fuller Test ===')
print('')
print(at.ADF(taus, trend='ct'))
print('')
print('=== CAN Prices Augmented Dickey-Fuller Test === ')
print(at.ADF(tcan, trend='ct'))
print('')

# check for stationary once diffrenciated

print('=== AUS Prices Differences Augumented Dickey-Fuller Test ===')
print('')
print(at.ADF(taus.diff(1).dropna(), trend='ct'))
print('')
print('=== CAN Prices Differences Augmented Dickey-Fuller Test === ')
print(at.ADF(tcan.diff(1).dropna(), trend='ct'))
print('')

#AUS -CAN Pair spread calculation : consists of paired assets linear regression residuals or forecasting errors.
#It corresponds to being long or buying one asset and being short or selling another one depending on their
#co-integration relationship
tintsp = taus - rg.OLS(taus, tcan).fit().params[0] * tcan
# beta_hat = np.matmul(np.matmul(np.array(tcan).transpose(), np.array(tcan)),tcan.transpose(), taus)
# beta_hat
# spread chart 
fig2, ax = plt.subplots()
ax.plot(tintsp, label='tintsp')
ax.axhline(tintsp.mean(), color = 'orange')
ax.legend(loc='upper left')
plt.suptitle('AUS-CAN Spread')
plt.show()

#AUS-CAN Spread co-integration test 
print('=== AUS-CAN spread Augumented Dickey-Fuller Co-Integration Test ===')
print('')
print(at.ADF(tintsp, trend='ct'))
print('')
print('=== AUS-CAN spread Phillips-Perron Co-Integration Test === ')
print(at.PhillipsPerron(tintsp, trend='ct',test_type='rho'))
print('') 

