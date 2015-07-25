print('TASK 1')
import pylab as p


#parameters
n=n_partitions=1000
mu=0.1
sigma=0.26
S0=39
n_path=1000

#create path
t=p.linspace(0,3,n+1)
dB=p.randn(n_path,n+1)/p.sqrt(n)
dB[:,0]=0
B=dB.cumsum(axis=1)

#calculate stock price
nu=mu-sigma*sigma/2.0
S=p.zeros_like(B)  #create a zero matrix with same size as B
S[:,0]=S0    #assign e1st input as S0
S[:,1:]=S0*p.exp(nu*t[1:]+sigma*B[:,1:])   # generate the equation
S_5line=S[0:5] #simulate the first five run and show on plot

p.plot(t,S_5line.transpose())
#label
label = 'Time ' ; p.xlabel(label)
label = 'Stock prices ' ; p.ylabel(label)
p.title('GBM of ' + label + ' ,mu=0.1 ' + ' and sigma=0.26  ' )
p.show()        

#expectation at S3
ST=S[:,1:]
S3=ST[:,-1]
S3_mean=p.mean(S3)
S3_variance=p.var(S3)
print('E(S3) = '+str(S3_mean))

#variance at S3
print('Var(S3) = ' + str(S3_variance))

S3_exceed = S3 > 39
number_exceed = sum (S3_exceed) #number of price exceed 39
print ('number [S(3)>39] = ' + str(number_exceed))

#prob.of exceed 39
print ('(P[S(3)>39]) = ' + str(number_exceed/n_path))

#matrix with end price exceed 39
S3_exceed_price = S3_exceed*S3

#sum of values that exceeded and divide by number of exceeded to get a mean.
print('E[S(3)|S(3)>39] = ' + str(sum(S3_exceed_price)/number_exceed))




