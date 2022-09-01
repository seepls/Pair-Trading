# CAN-RSA trading strategy signal 
fint2.insert(len(fint2.columns), 'fintz2', fintz2)
fint2.insert(len(fint2.columns), 'fintz2(-1)', fintz2.shift(1))
fint2.insert(len(fint2.columns), 'fintz2(-2)', fintz2.shift(2))
fintsig2 = 0.0
fintsig2a = []

for i in fint2.index:
    if fint2.at[i, 'fintz2(-2)'] > -2 and fint2.at[i, 'fintz2(-1)'] < -2:
        fintsig2 = -2.0
    elif fint2.at[i, 'fintz2(-2)'] < -1 and fint2.at[i, 'fintz2(-1)'] > -1:
        fintsig2 = -1.0
    elif fint2.at[i, 'fintz2(-2)'] < 2 and fint2.at[i, 'fintz2(-1)'] > 2:
        fintsig2 = 2.0
    elif fint2.at[i, 'fintz2(-2)'] > 1 and fint2.at[i, 'fintz2(-1)'] < 1:
        fintsig2 = 1.0
    else:
        fintsig2 = 0.0
    fintsig2a.append(fintsig2)

fint2.insert(len(fint2.columns), 'fintsig2', fintsig2a)

# CAN-RSA trading strategy position
fintpos2 = 0.0
fintpos2a = []

for i in fint2.index:
    if fint2.at[i, 'fintsig2'] == -2.0:
        fintpos2 = 1.0
    elif fint2.at[i, 'fintsig2'] == -1.0:
        fintpos2 = 0.0
    elif fint2.at[i, 'fintsig2'] == 2.0:
        fintpos2 = -1.0
    elif fint2.at[i, 'fintsig2'] == 1.0:
        fintpos2 = 0.0
    else:
        fintpos2 = None
    fintpos2a.append(fintpos2)
fint2.insert(len(fint2.columns), 'fintpos2', fintpos2a)
fint2 = fint2.fillna(method='ffill')

print('== CAN-RSA Trading Strategy Position ==')
print('')
print(fint2.loc['2015-02-01':, ['fintz2', 'fintsig2', 'fintpos2']])
print('')

