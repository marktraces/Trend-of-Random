import random
from matplotlib import pyplot as plt
import collections
import numpy as np

num_of_generation = int(input('Number of generation \n \t --> '))

data = []
for j in range (0,num_of_generation):
    randata = random.randint(45,100)
    data.append(randata)

print(data)

data.sort()

print(data)

frequency = collections.Counter(data)

x_axis = list(frequency.keys())
y_axis = list(frequency.values())

#Calculation Of Modal Class
modal_fix = len(y_axis)
modal_num = 0
modal_class = []
for i in range(0,modal_fix):
    if y_axis[i] > modal_num:
        modal_num = y_axis[i]
        modal_class = []
        modal_class.append(x_axis[i])
        print(modal_class)
    elif y_axis[i] == modal_num:
        modal_class.append(x_axis[i])
        print(modal_class)
        
print ('The modal class is :')
print(modal_class)

#Calculation Of Mean
Summation = 0
for randata in data:
    Summation = Summation + randata
Mean = Summation/num_of_generation
print ('The mean is ' + str(Mean))

#Calculation Of Median
midval = (num_of_generation)/2
i = 0
medianth = 0
while medianth != midval :
    medianth = medianth + y_axis[i]
    i = i + 1
median = x_axis[i]
print ('The median is ' + str(median))
    
#Best Measure
Best_Measure = 'For individual datas that have limit of skewness, the mean is the best measure.'
print(Best_Measure + str(Mean))



#Plotting the datas in a graph

plt.style.use('ggplot')

plt.tight_layout()

plt.plot(x_axis,y_axis,color = '#444444',linestyle = '--',label ='Random datas')

plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.title('Trends of Randomness')

plt.legend()

plt.show()