from matplotlib.pyplot import *
from numpy import *

#simple function graphic 

def straight_line():
	plt.plot([1,2,3,4])#values
	plt.show()



first_value_for_linspace = int(input())
second_value_for_linspace = int(input())
third_value_for_linspace = int(input())
x = linspace(first_value_for_linspace,second_value_for_linspace,third_value_for_linspace)
y= x**2
plot(x,y)
show()
