# CAN-RSA rolling spread Z- score calculations 
fcan = fint2['fcan']
frsa = fint2['frsa']
fintsp2 = fcan - rg.OLS(tcan, trsa).fit().params[0] * frsa
fintz2 = (fintsp2 - fintsp2.rolling(window=21).mean()) / fintsp2.rolling(window=21).std()

#CAN-RSA rolling spread Z-Score chart 
fig3, ax = plt.subplots()
ax.plot(fintz2, label='fintz2')
ax.axhline((-2), color='green')
ax.axhline((-1), color='green', linestyle='--')
ax.axhline((2), color='red')
ax.axhline((1), color='red', linestyle='--')
ax.legend(loc='upper left')
plt.suptitle('CAN-RSA Rolling Spread Z-Score')
plt.show()

