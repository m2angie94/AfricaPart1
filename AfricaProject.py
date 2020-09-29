import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('africa.csv')
print(list(df.columns))

print("\nThe first five rows of the data ")
print(df.head())
#print(df)

df.sort_values(by = ['Country Name', 'Region'])
west_africa = df[df.Region == 'West Africa']
north_africa = df[df.Region == 'North Africa']
southern_africa = df[df.Region == 'Southern Africa']
east_africa = df[df.Region == 'East Africa']
print("\n----------West African Countries---------------")
print(west_africa)
print(west_africa.count())

print("\n----------North African Countries---------------")
print(north_africa)

print("\n----------Southern African Countries---------------")
print(southern_africa)

print("\n----------East African Countries---------------")
print(east_africa)

#df2 = pd.read_csv('africa.csv', index_col = 'Region')
#print(df2)
# print(df.iloc['Population'])
#new_col = []

#for row in df2['Population']:
#   row1 = row.replace(',', '')
#    row2 = int(row1)
#    new_col.append(row2)

#df2['Population'] = new_col
#print(df2.head())

# df2['Population'] = df2['Population'].astype(float)

# I WANT TO PULL THE DATA FROM EACH REGION AND PLOT IT WITH POPULATION ON THE Y AXIS AN THE COUNTRY ON THE X AXIS
# WANT TO CREATE 4 BAR CHARTS AND PIE CHARTS FOR WEST, NORTH SOUTH AND EAST
#df2 =df2.astype(float)
# df2 = pd.DataFrame(west_africa)

#west africa
new_col = []

for row in west_africa['Population']:
    #this gets rid of the commmas that make the population a string and thus being able to convert it to a int to graph
    row1 = row.replace(',', '')
    row2 = int(row1)
    new_col.append(row2)

west_africa['Population'] = new_col
print(west_africa.head())
west_africa.plot(kind = 'bar' , x = 'Country Name', y = 'Population', color = 'green')
west_africa.sort_values(by = ['Population'], ascending = True)[['Country Name', 'Population']]
plt.title("West African Countries")
plt.xlabel("Country")
plt.ylabel("InMilliions")
plt.show()

west_africa.plot(kind = 'pie', y = 'Population', labels= west_africa['Country Name'])
plt.title("Population")
plt.tight_layout()
plt.show

#west_africa.pie('Population', explode=explode, labels='Country Name', autopct='%1.1f%%',
#        shadow=True, startangle=90)
#plt.show()
#north africa
new_col = []

for row in southern_africa['Population']:
    row1 = row.replace(',', '')
    row2 = int(row1)
    new_col.append(row2)

southern_africa['Population'] = new_col
print(southern_africa.head())
southern_africa.plot(kind = 'bar' , x = 'Country Name', y = 'Population', color = 'red')
southern_africa.sort_values(by = ['Population'], ascending = True)[['Country Name', 'Population']]
plt.title("Southern African Countries")
plt.xlabel("Country")
plt.ylabel("InMilliions")
plt.show()

#southern africa
new_col = []

for row in north_africa['Population']:
    row1 = row.replace(',', '')
    row2 = int(row1)
    new_col.append(row2)

north_africa['Population'] = new_col
print(north_africa.head())
north_africa.plot(kind = 'bar' , x = 'Country Name', y = 'Population', color = 'yellow')
north_africa.sort_values(by = ['Population'], ascending = True)[['Country Name', 'Population']]
plt.title("North African Countries")
plt.xlabel("Country")
plt.ylabel("InMilliions")
plt.show()

#west africa
new_col = []

for row in east_africa['Population']:
    row1 = row.replace(',', '')
    row2 = int(row1)
    new_col.append(row2)

east_africa['Population'] = new_col
print(east_africa.head())
east_africa.plot(kind = 'bar' , x = 'Country Name', y = 'Population', color = 'cyan')
east_africa.sort_values(by = ['Population'], ascending = True)[['Country Name', 'Population']]
plt.title("East African Countries")
plt.xlabel("Country")
plt.ylabel("InMilliions")
plt.show()


#TRIED TO MAKE A FUNCTION FOR THE COUNTRY DATAFRAME 
#AND PLOT
#def main():
#    convert(west_africa)
#    convert(north_africa)
#    convert(southern_africa)
#    convert(east_africa)
    
#west_africa['Population'] = new_col
#print(west_africa.head())
#west_africa.plot(kind = 'bar' , x = 'Country Name', y = 'Population')
#west_africa.sort_values(by = ['Population'], ascending = True)[['Country Name', 'Population']]
#plt.title("West African Countries")
#plt.xlabel("Country")
#plt.ylabel("InMilliions")
#plt.show()
    
#def convert(dataframe):
#    new_col = []

#    for row in dataframe['Population']:
#        row1 = row.replace(',', '')
#        row2 = int(row1)
#        new_col.append(row2)

#    dataframe['Population'] = new_col
    
#def plot_graph(dataframe):
#    dataframe.plot(kind = 'bar' , x = 'Country Name', y = 'Population')
#    dataframe.sort_values(by = ['Population'], ascending = True)[['Country Name', 'Population']]
#    plt.title("West African Countries")
#    plt.xlabel("Country")
#    plt.ylabel("InMilliions")
#    plt.show()