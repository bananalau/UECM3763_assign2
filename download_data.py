from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pylab as p
import numpy as np

start = dt(2012,6, 1)
end = dt(2015, 5,31)
data1 = DR("6947.KL", 'yahoo', start, end) #digi.com

#input data into array
data=p.array(data1)
#taking out closing price
close_price = data[:,-1]
sumprice = close_price.cumsum()

avg_day=5

#make a zero matrix with 2 row , from day1 to last 4 days and from 1st day 
#to the fifth day from the last day.
matrix = np.zeros((2,(len(sumprice)-avg_day+1)))
matrix[0,:] = sumprice[(avg_day-1):] #sum value from 5th to last day
matrix[1,1:] = sumprice[:-(avg_day)] #sum value from 1st to the last 5th day

moving_avg = (matrix[0] - matrix[1]) / avg_day

p.plot(moving_avg)
#label
label = 'Days ' ; p.xlabel(label)
label = '5 days average ' ; p.ylabel(label)
p.title('5 days moving average of Digi from 1st June 2012 till 31 May 2015 ' )
p.show()   

#downlaod KLSE data
#combining both data together
combine_data = ["6947.KL","^KLSE"] 
#retrieve information from yahoo with same duration , 
#get only adjusted close price
data2 = DR(combine_data,'yahoo',start,end)['Adj Close']

#compute into a array
combine = p.array(data2)
#calcualte correlation for both Digi and KLSE
correlation=data2.corr()
print('Correlation =\n',correlation)