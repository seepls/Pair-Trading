#### Pair trading strategy

Why Pairs trading project choice ?   
Long term capital management (LTCM) built by ex Lehman brother founder and other Nobel price winners i.e Fischer Black.  
The hedge fund was able to make 40% profit yoy, with such market neutral trading Statistical Arbitrage strategies.    

Example : ICICI and IDBI bank , PEPSI and Coca Cola 
  
Pair trading is a market neutral trading strategy (mean reverting) enabling traders to profit from virtually any market conditions: uptrend, downtrend, or sideways movement. The strategy monitors performance of two historically correlated securities. When the correlation between the two securities temporarily weakens, i.e. one stock moves up while the other moves down, the pairs trade would be to short the outperforming stock and to long the underperforming one, betting that the "spread" between the two would eventually converge. The divergence within a pair can be caused by temporary supply/demand changes, large buy/sell orders for one security, reaction for important news about one of the companies, and so on. 
  
While it is commonly agreed that individual stock prices are difficult to forecast, there is evidence suggesting that it may be possible to forecast the spread series—of certain stock portfolios.  


Steps : 
1. pair identification / Estimation  : select two assets  (Asset A, Asset B) likely to have a stationary spread.                                              Stationary process :  Joint probability distribution does not change with time. 
   Test for stationarity : ADF (Augmented Dickey Fuller test ), Philips peron .


2. Pair short term statistical relationship : prices return correlation

3. Single pairs spread co-integration : long - term statistical relationship 
	Co-integration test : Johansen Test( for upto 12 series ) and the Augmented Dickey-Fuller (ADF) test (for only 2 series ), Philips Perron test 
  Engle- granger test : Series non-stationary, difference stationary and Spread is stationary. Prices move together in long term = stationary spread.

co-integrated pairs spreads trading strategies calculations entry-exit trading signals and associated long/short trading positions are generated based on paired assets rolling spread normalized time series / z-score crossing certain bands thresholds. :               
Use of  Kalman Filter is an efficient optimal estimator for mu +- Z sigma 

			from statsmodels.tsa.stattools import coint 
			coint(PriceA, PriceB)
			import statsmodels.tsa.stattools as ts
			ts.adfuller()
			For mean reversion check : Ornstein–Uhlenbeck

4. Performance evaluation (accuracy ) :  Backtesting using historical data. Sharpe ratio, Returns, PnL. Drawdown. 
