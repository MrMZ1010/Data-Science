import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Load the dataset
foods = pd.read_csv('food_nutrients.csv')

# Select relevant columns
nutrient_columns = ['calories', 'protein', 'fat', 'carbohydrates', 'fiber', 'sugar']
foods = foods[['food_name'] + nutrient_columns]

# Fill missing values for nutrient columns with the mean
foods[nutrient_columns] = foods[nutrient_columns].fillna(foods[nutrient_columns].mean())

# Scale the nutrient data
scaler = StandardScaler()
scaled_nutrients = scaler.fit_transform(foods[nutrient_columns])

# Create a DataFrame with scaled nutrients
scaled_foods = pd.DataFrame(scaled_nutrients, columns=nutrient_columns)
scaled_foods['food_name'] = foods['food_name']

# Plotting the results
def plot_all_foods_nutrients(foods, nutrient_columns):
    sns.set(style="whitegrid")
    
    # Melt the DataFrame for better plotting
    melted_foods = pd.melt(foods, id_vars=['food_name'], value_vars=nutrient_columns, 
                           var_name='Nutrient', value_name='Value')
    
    # Create the bar plot
    plt.figure(figsize=(14, 10))
    ax = sns.barplot(x='food_name', y='Value', hue='Nutrient', data=melted_foods, palette='viridis')
    
    # Set the title and labels
    ax.set_title('Nutrient Comparison Across Foods', fontsize=16)
    ax.set_xlabel('Food Name', fontsize=14)
    ax.set_ylabel('Nutrient Value (Standardized)', fontsize=14)
    
    # Rotate the x labels for better readability
    plt.xticks(rotation=90, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    
    # Show the plot
    plt.legend(title='Nutrient', fontsize=12)
    plt.tight_layout()
    plt.show()

# Plot all foods and their nutrients
plot_all_foods_nutrients(scaled_foods, nutrient_columns)
