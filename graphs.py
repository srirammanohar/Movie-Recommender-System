__author__ = 'Rudra'
import numpy
import matplotlib.pyplot as plt
Normalized = [0.0792333530923,0.141043397969,0.222117794486, 0.285024154589,0.330415754923,0.409722222222,0.425,0.37037037037]
Non_Normalized = [0.0837779095041,0.143351800554,0.221804511278,0.278260869565,0.324580598104,0.388888888889,0.425,0.37037037037]
Baseline=[0.0806164789567,0.0911819021237,0.113721804511,0.180676328502,0.241429613421,0.238425925926,0.341666666667,0.296296296296]
x= [i for i in range(2,10)]
plt.plot(x,Normalized)
plt.plot(x,Non_Normalized)
plt.plot(x,Baseline)

#plt.hist(Non_Normalized, x, alpha=0.5, label='y')
plt.legend(loc='upper right')
'''
colors = ['red', 'blue']
plt.hist(Normalized,x, normed=1, histtype='bar', color=colors, label=colors)
plt.legend(prop={'size': 10})
'''
plt.show()