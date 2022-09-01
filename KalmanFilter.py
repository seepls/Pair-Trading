# Kalman filter the distribution is given by gaussian( mean, sigma sqaure)
# Vairance is a measure of Gaussian spread 
# Gaussian function 

def f(mu,sigma2,x):
    coefficient = 1.0 /sqrt(2.0*pi*sigma2)
    exponential = exp(-0.5*(x-mu)**2 / sigma2)
    return coefficient * exponential 
  

# kalman filter iterates measurements 
# Updates : new mean, Mu prime, is the weighted sum of the old means.
# variance term is unaffected by the actual means, it just uses the previous variances.

def update(mean1,var1,mean2,var2):
    new_mean = (var2*mean1 + var1*mean2)/(var2 + var1)
    new_var = 1/(1/var2 + 1/var1)
    return [new_mean, new_var]
  
def predict(mean1,var1,mean2,var2):
    new_mean = mean1 + mean2
    new_var = var2 + var1
    return [new_mean, new_var]  
  
# iteration 
for n in range(len(measurements)):
    mu,sig = update(mu,sig,measurements[n], measurement_sig)
    print('Update': [{},{}].format(mu,sig))
    mu, sig = predict(mu,sig, motions[n], motion_sig)
    print('Predict: [{}, {}]'.format(mu,sig))
