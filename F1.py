import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
constructors_df = pd.read_csv('constructors.csv')
constructor_standings_df = pd.read_csv('constructor_standings.csv')
constructor_results_df = pd.read_csv('constructor_results.csv')
circuits_df = pd.read_csv('circuits.csv')

#print(constructor_results_df.columns)
# Example of merging datasets
# This is just illustrative; adjust based on your analysis needs
merged_df = pd.merge(constructor_results_df, constructors_df, on='constructorId', how='left')

print(merged_df)

'''
# Example: Count wins by constructor
constructor_results_df['position'] = pd.to_numeric(constructor_results_df.get('position', pd.Series()), errors='coerce')
wins_by_constructor = constructor_results_df[constructor_results_df['position'] == 1].groupby('constructorId')['raceId'].count()

wins_by_constructor = pd.merge(wins_by_constructor.reset_index(), constructors_df[['constructorId', 'name']], on='constructorId', how='left')

print(wins_by_constructor)


# Visualization: Wins by Constructor
sns.barplot(x=wins_by_constructor['name'], y=wins_by_constructor['raceId'])
plt.title('Wins by Constructor')
plt.xticks(rotation=45)
plt.ylabel('Number of Wins')
plt.xlabel('Constructor Name')
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()




# Quick data inspection
#print(constructors_df.head())
#print(constructor_standings_df.head())
#print(constructor_results_df.head())
#print(circuits_df.head()) '''
