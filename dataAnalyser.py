import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# importing covid19 dataset
corona_dataset_csv = pd.read_csv('Dataset/covid19_Confirmed_dataset.csv')
print(corona_dataset_csv.head(10))
print(corona_dataset_csv.shape)
# Delete the useless columns
corona_dataset_csv.drop(['Lat','Long'],axis=1,inplace=True)
print(corona_dataset_csv.head(10))
# Aggregating the rows by the country
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
print(corona_dataset_aggregated.head(10))
print(corona_dataset_aggregated.shape)
# Visualizing data related to a country for example China
corona_dataset_aggregated.loc['China'].plot()
corona_dataset_aggregated.loc['Italy'].plot()
corona_dataset_aggregated.loc['Spain'].plot()
plt.legend()
plt.show()
# Calculating a good measure
corona_dataset_aggregated.loc['China'].plot()
plt.show()
# caculating the first derivative of the curve
corona_dataset_aggregated.loc['China'].diff().plot()
plt.show()
#  find maxmimum infection rate for China
print(corona_dataset_aggregated.loc['China'].diff().max())
print(corona_dataset_aggregated.loc['Italy'].diff().max())
print(corona_dataset_aggregated.loc['Spain'].diff().max())
#  find maximum infection rate for all of the countries.
countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for country in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[country].diff().max())
corona_dataset_aggregated['max infection rate'] = max_infection_rates
corona_dataset_aggregated.head()
#  create a new dataframe with only needed column
corona_data = pd.DataFrame(corona_dataset_aggregated['max infection rate'])
print(corona_data.head())
# Importing the WorldHappinessReport.csv dataset
# selecting needed columns for our analysis
# join the datasets
# calculate the correlations as the result of our analysis
# importing the dataset
world_happiness_report = pd.read_csv("Dataset/worldwide_happiness_report.csv")
world_happiness_report.head()
print(world_happiness_report.shape)
#  let's drop the useless columns
columns_to_dropped = ['Overall rank','Score','Generosity','Perceptions of corruption']
world_happiness_report.drop(columns_to_dropped,axis=1 , inplace=True)
world_happiness_report.head()
# changing the indices of the dataframe
world_happiness_report.set_index(['Country or region'],inplace=True)
world_happiness_report.head()
#  now let's join two dataset we have prepared
print(corona_data.head())
# wolrd happiness report Dataset :
print(world_happiness_report.head())
data = world_happiness_report.join(corona_data).copy()
print(data.head())
# correlation matrix
print(data.corr()) # it is representing the correlation between every two columns of our dataset
# Visualization of the results
print(data.head())
# Plotting GDP vs maximum Infection rate
x = data['GDP per capita']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
plt.show()
sns.regplot(x,np.log(y))
plt.show()
# Plotting Social support vs maximum Infection rate
x = data['Social support']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
plt.show()
sns.regplot(x,np.log(y))
plt.show()
# Plotting Healthy life expectancy vs maximum Infection rate
x = data['Healthy life expectancy']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
plt.show()
sns.regplot(x,np.log(y))
plt.show()
# Plotting Freedom to make life choices vs maximum Infection rate¶
x = data['Freedom to make life choices']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))
plt.show()
sns.regplot(x,np.log(y))
plt.show()