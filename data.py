import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
def load_and_explore_dataset():
    # Load Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], 
                      columns=iris['feature_names'] + ['target'])
    
    # Map target numbers to species names
    target_names = iris['target_names']
    df['species'] = df['target'].map(dict(enumerate(target_names)))
    
    print("Dataset Overview:")
    # Display first few rows
    print(df.head())
    
    # Check data types
    print("\nData Types:")
    print(df.dtypes)
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    return df

# Task 2: Basic Data Analysis
def perform_data_analysis(df):
    # Compute basic statistics
    print("\nBasic Statistics:")
    print(df.describe())
    
    # Group by species and compute mean of numerical features
    print("\nMean Features by Species:")
    grouped_stats = df.groupby('species')[['sepal length (cm)', 'sepal width (cm)', 
                                            'petal length (cm)', 'petal width (cm)']].mean()
    print(grouped_stats)
    
    return grouped_stats

# Task 3: Data Visualization
def create_visualizations(df):
    # Set up a 2x2 grid of plots
    plt.figure(figsize=(16, 12))
    plt.suptitle('Iris Dataset Analysis', fontsize=16)
    
    # 1. Line Chart (Average Feature Trends by Species)
    plt.subplot(2, 2, 1)
    df.groupby('species')[['sepal length (cm)', 'petal length (cm)']].mean().T.plot(kind='line', ax=plt.gca())
    plt.title('Average Sepal and Petal Lengths by Species')
    plt.xlabel('Feature')
    plt.ylabel('Length (cm)')
    plt.legend(title='Species')
    
    # 2. Bar Chart (Petal Width by Species)
    plt.subplot(2, 2, 2)
    df.groupby('species')['petal width (cm)'].mean().plot(kind='bar', ax=plt.gca())
    plt.title('Average Petal Width by Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Width (cm)')
    plt.xticks(rotation=45)
    
    # 3. Histogram (Sepal Length Distribution)
    plt.subplot(2, 2, 3)
    df['sepal length (cm)'].hist(bins=20, ax=plt.gca())
    plt.title('Distribution of Sepal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency')
    
    # 4. Scatter Plot (Sepal Length vs Petal Length)
    plt.subplot(2, 2, 4)
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', ax=plt.gca())
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    
    plt.tight_layout()
    plt.show()

# Main Execution
def main():
    try:
        # Load and explore dataset
        df = load_and_explore_dataset()
        
        # Perform data analysis
        grouped_stats = perform_data_analysis(df)
        
        # Create visualizations
        create_visualizations(df)
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the analysis
if __name__ == "__main__":
    main()
