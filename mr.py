print('TASK 2')
import pylab as p


#set parameter
n=n_partitions=1000
n_path=1000
alpha = 1
theta = 0.064
sigma = 0.27
R0 = 3
time =1 
dT = time/n
#dRT = alpha(theta - RT)dT + sigma dBT

#create path
t=p.linspace(0,1,n+1)[:-1]
dB=p.randn(n_path,n+1)/p.sqrt(n)
dB[:,0]=0
B=dB.cumsum(axis=1)
R=p.zeros_like(B)  #create a R matrix with all zeros and size similar to B
R[:,0]=R0  #initiate the first initial at R0

for step in range(n):
    R[:,step+1] = R[:,step] + (theta- R[:,step])*dT + sigma*R[:,step]*dB[:,step+1]

#pick 5 plot
RT=R[0:5:,:-1]

p.plot(t,RT.transpose())

#label
label = 'Time , ' ; p.xlabel(label)
label = 'R(T), ' ; p.ylabel(label)
p.title('5 runs of Mean reversal process of ' + label + 'alpha =1 , theta = 0.064 and sigma = 0.27')
p.show() 

#last prices of 5 sample
R1=R[:,-1]

#Expected price
E_R1=sum(R1) / len(R1)  #find mean or expected value
print('Expected value of R(1) = ' + str(E_R1))

#P[R(1)> 2]

exceed_R1 = R1 > 2  # create a matrix that find the path that exceed 2 at the end R(1)
num_exceed = sum(exceed_R1) #number of path that exceed 2
prob = num_exceed / len(R1)

print( ' P[R(1)> 2] = ' +  str(prob))
