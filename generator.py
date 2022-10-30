import random
from matplotlib import pyplot as plt
import collections

x = input("What is the left most limit of your trend: \n \t -->")
y = input("What is the right most limit of your trend: \n \t -->")
z = input("How many times do you want to generate random numbers: \n \t -->")

data = []
for j in range (1,z):
    randata = random.randint(x,y)
    data.append(randata)
data.sort()

frequency = collections.Counter(data)

x_axis = list(frequency.keys())
y_axis = list(frequency.values())

plt.style.use('ggplot')

plt.plot(x_axis,y_axis,color = '#444444',linestyle = '--',label ='Random datas')

plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.title('Trends of Randomness')

plt.legend()

plt.tight_layout()

plt.show()
