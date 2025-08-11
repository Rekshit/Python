'''
import matplotlib.pyplot as plt 
fruits = ['Apples', 'Mangoes', 'Bananas', 'Grapes', 'Cherries']  
sales= [400, 150, 300, 500, 250] 
plt.bar(fruits, sales, color=['blue', 'yellow', 'green', 'red', 'yellow'], width=0.6) 
plt.xlabel('FRUIT TYPES') 
plt.ylabel('SALES FIGURES') 
plt.title('FRUIT SALES DATA') 
plt.show()
'''
'''
import matplotlib.pyplot as plt 
fruits = ['Apples', 'Mangoes', 'Bananas', 'Grapes', 'Cherries']  
sales= [450, 350, 300, 500, 375] 
plt.plot(fruits, sales, linestyle=':', color='green') 
plt.xlabel('FRUIT TYPES') 
plt.ylabel('SALES FIGURES') 
plt.title('FRUIT SALES DATA') 
plt.show()
'''
'''
import matplotlib.pyplot as plt 
data= [1,2,2,2,2,3,3,3,4,4,4,4,4,4,5,5,6,6,7,7,7] 
plt.hist(data, bins='auto', color='lightgreen',edgecolor='black') 
plt.xlabel('MARKS') 
plt.ylabel('NO OF STUDENTS') 
plt.title('MARKS DISTRIBUTION') 
plt.show()
'''
import matplotlib.pyplot as plt 
age = ['3', '4', '5', '6', '7', '8', '9']  
height= [2, 2.5, 3, 3.9, 4, 4.5, 5] 
plt.scatter(age, height, color='green') 
plt.xlabel('AGE (in years)') 
plt.ylabel('HEIGHT (in feet)') 
plt.title('AGE vs Height OF CHILDREN') 
plt.show()