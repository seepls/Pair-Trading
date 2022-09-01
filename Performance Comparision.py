# CAN-RSA Strategy Spread Returns
rfcan = fcan.pct_change(1).dropna()
rfrsa = frsa.pct_change(1).dropna()
rfintsp2 = rfcan - rg.OLS(tcan, trsa).fit().params[0] * rfrsa

# CAN-RSA Strategy Without Trading Commissions Returns
rfint2 = rfintsp2 * fint2['fintpos2']

# CAN-RSA Strategy With Trading Commissions Returns (0.1% Per Trade)
fint2.insert(len(fint2.columns), 'fintpos2(-1)', fint2['fintpos2'].shift(1))
finttc2 = 0.0
finttc2a = []

for i in fint2.index:
    if (fint2.at[i, 'fintsig2'] == -2.0 or fint2.at[i, 'fintsig2'] == -1.0 or fint2.at[i, 'fintsig2'] == 2.0
        or fint2.at[i, 'fintsig2'] == 1.0) and fint2.at[i, 'fintpos2'] != fint2.at[i, 'fintpos2(-1)']:
        finttc2 = 0.001
    else:
        finttc2 = 0.000
    finttc2a.append(finttc2)
fint2.insert(len(fint2.columns), 'finttc2', finttc2a)
rfint2c = rfint2 - fint2['finttc2']

# 6.2. CAN-RSA Strategy Cumulative Annualized Returns

# CAN-RSA Strategy Cumulative Annualized Returns Calculation
rfintcuma2 = np.cumprod(rfint2 + 1) ** (252 / len(fint2)) - 1
rfintcuma2c = np.cumprod(rfint2c + 1) ** (252 / len(fint2)) - 1
rfcancuma = np.cumprod(rfcan + 1) ** (252 / len(fint2)) - 1
rfrsacuma = np.cumprod(rfrsa + 1) ** (252 / len(fint2)) - 1

# CAN-RSA Strategy Cumulative Annualized Returns Chart
plt.plot(rfintcuma2, label='rfintcuma2')
plt.plot(rfintcuma2c, label='rfintcuma2c')
plt.plot(rfcancuma, label='rfcancuma')
plt.plot(rfrsacuma, label='rfrsacuma')
plt.title('CAN-RSA Trading Strategy Cumulative Returns')
plt.legend(loc='upper left')
plt.show()

# 6.3. CAN-RSA Strategy Performance Summary
results2 = [{'0': 'Annualized:', '1': 'rfint2', '2': 'rfint2c', '3': 'rfcan', '4': 'rfrsa'},
        {'0': 'Return', '1': np.round(rfintcuma2[-1], 4),
         '2':np.round(rfintcuma2c[-1], 4),
         '3': np.round(rfcancuma[-1], 4),
         '4': np.round(rfrsacuma[-1], 4)},
        {'0': 'Standard Deviation', '1': np.round(np.std(rfint2) * np.sqrt(252), 4),
         '2': np.round(np.std(rfint2c) * np.sqrt(252), 4),
         '3': np.round(np.std(rfcan) * np.sqrt(252), 4),
         '4': np.round(np.std(rfrsa) * np.sqrt(252), 4)},
        {'0': 'Sharpe Ratio (Rf=0%)', '1': np.round(rfintcuma2[-1] / (np.std(rfint2) * np.sqrt(252)), 4),
         '2': np.round(rfintcuma2c[-1] / (np.std(rfint2c) * np.sqrt(252)), 4),
         '3': np.round(rfcancuma[-1] / (np.std(rfcan) * np.sqrt(252)), 4),
         '4': np.round(rfrsacuma[-1] / (np.std(rfrsa) * np.sqrt(252)), 4)}]
table2 = pd.DataFrame(results2)
print('')
print('== CAN-RSA Strategy Performace Summary ==')
print('')
print(table2)

