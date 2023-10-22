
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[22]:


# Assuming the data is in a CSV file named 'covid_data.csv'
df = pd.read_csv("C:/Users/soumi/Downloads/covid-data.csv")


# In[23]:


df.head()


# In[25]:


df.info()


# In[26]:


df.describe()


# In[27]:


total_cases_by_country = df.groupby('location')['total_cases'].max()
total_deaths_by_country = df.groupby('location')['total_deaths'].max()


# In[28]:


country_with_highest_cases = total_cases_by_country.idxmax()
country_with_highest_deaths = total_deaths_by_country.idxmax()


# In[40]:


# Filter the data to exclude non-country entities and sort by total cases
filtered_cases = total_cases_by_country.drop(['High income', 'Upper middle income', 'Lower middle income', 'Low income']).nlargest(10)

# Create a bar plot for the top 10 countries
plt.figure(figsize=(10, 6))
sns.barplot(x=filtered_cases.index, y=filtered_cases.values)
plt.xticks(rotation=90)
plt.title("Total Cases by Country (Top 10, Excluding Non-Country Entities)")
plt.show()


# In[41]:


# Filter the data to exclude non-country entities and sort by total deaths
filtered_data = total_deaths_by_country.drop(['High income', 'Upper middle income', 'Lower middle income', 'Low income']).nlargest(10)

# Create a bar plot for the top 10 countries
plt.figure(figsize=(10, 6))
sns.barplot(x=filtered_data.index, y=filtered_data.values)
plt.xticks(rotation=90)
plt.title("Total Deaths by Country (Top 10, Excluding Non-Country Entities)")
plt.show()


# In[37]:


import geopandas as gpd
# Load the world map shapefile
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge the shapefile with your COVID-19 data using the ISO country codes
merged_data = world.merge(df, left_on='iso_a3', right_on='iso_code')

# Create a map showing total cases per million people
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='total_cases_per_million', cmap='coolwarm', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title('Total COVID-19 Cases per Million People')
plt.show()


# In[48]:


# Pairplot for a visual overview of relationships
sns.pairplot(df[['total_cases', 'total_deaths', 'total_tests', 'population']])
plt.show()


# In[49]:


# Correlation matrix to quantify relationships
correlation_matrix = df[['total_cases', 'total_deaths', 'total_tests', 'population']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()


# In[50]:


# Box plots to visualize distributions
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.boxplot(data=df, x='continent', y='total_cases')
plt.xticks(rotation=90)
plt.title("Total Cases by Continent")

plt.subplot(2, 2, 2)
sns.boxplot(data=df, x='continent', y='total_deaths')
plt.xticks(rotation=90)
plt.title("Total Deaths by Continent")

plt.subplot(2, 2, 3)
sns.boxplot(data=df, x='continent', y='total_tests')
plt.xticks(rotation=90)
plt.title("Total Tests by Continent")

plt.subplot(2, 2, 4)
sns.boxplot(data=df, x='continent', y='population')
plt.xticks(rotation=90)
plt.title("Population by Continent")

plt.tight_layout()
plt.show()


# In[52]:


# Bar plot for total cases by continent
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='continent', y='total_cases', errorbar=None)
plt.xticks(rotation=45)
plt.title("Total Cases by Continent")
plt.show()


# In[53]:


# Bar plot for total deaths by continent
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='continent', y='total_deaths', errorbar=None)
plt.xticks(rotation=45)
plt.title("Total Deaths by Continent")
plt.show()

