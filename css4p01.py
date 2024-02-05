#!/bin/env python 3


import pandas as pd


#>> Data Cleaning and Pre-processing

# We address missing data by filling the missing values in 'Revenue (Millions)' 
# with the median to minimize the impact of outliers and by using the median for 
# 'Metascore' after converting to integers to maintain data consistency.

# Read the data
df = pd.read_csv("movie_dataset.csv") 

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# Generate a summary of the DataFrame
print(df.info())

# Generate descriptive statistics of the DataFrame
print(df.describe())

# Verify the current column names in the DataFrame
print(df.columns.tolist())

# Rename columns
df.columns = df.columns.str.replace(' ', '_')

# Renamed columns
print(df.columns.tolist())

# Fill missing values for 'Revenue_(Millions)' with the median
revenue_median = df['Revenue_(Millions)'].median()
# df['Revenue_(Millions)'].fillna(revenue_median, inplace=True)
df['Revenue_(Millions)'] = df['Revenue_(Millions)'].fillna(revenue_median)

# Convert 'Metascore' to integers and fill missing values with the median
metascore_median = df['Metascore'].median()
df['Metascore'] = df['Metascore'].fillna(metascore_median).astype(int)

# Generate a summary of the DataFrame again
print(df.info())

# Generate descriptive statistics of the DataFrame again
print(df.describe())

#>> Answering the questions

# A1. To find the highest-rated movie in the dataset, we will look for the row 
# with the maximum value in the 'Rating' column 

highest_rated_movie = df.loc[df['Rating'].idxmax()]

print(highest_rated_movie) 

# A2. The average revenue of all movies in the dataset

average_revenue = df['Revenue_(Millions)'].mean()

print(average_revenue)

# A3. The average revenue of movies from 2015 to 2017 in the dataset

# Filter the DataFrame for movies released from 2015 to 2017
movies_2015_to_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate the average revenue for this filtered dataset
average_revenue_2015_to_2017 = movies_2015_to_2017['Revenue_(Millions)'].mean()

print(average_revenue_2015_to_2017)

# A4. Number of movies released in 2016

# Count the number of movies released in 2016
movies_2016_count = df[df['Year'] == 2016].shape[0]

print(movies_2016_count)

# A5. Number of movies directed by Christopher Nolan

# Count the number of movies directed by Christopher Nolan
nolan_movies_count = df[df['Director'] == 'Christopher Nolan'].shape[0]

print(nolan_movies_count)

# A6. Number of movies with a rating of at least 8.0

# Count the number of movies with a rating of at least 8.0
rated_movies_count = df[df['Rating'] >= 8.0].shape[0]

print(rated_movies_count)

# A7. Median rating of movies directed by Christopher Nolan

# Calculate the median rating of movies directed by Christopher Nolan
nolan_median_rating = df[df['Director'] == 'Christopher Nolan']['Rating'].median()

print(nolan_median_rating)

# A8. Year with the highest average rating

# Group the data by 'Year' and calculate the average rating for each year
average_rating_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()

print(year_highest_average_rating)

# A9. Percentage increase in number of movies made between 2006 and 2016

# Get 'Year' column data type to ensure correct filtering for 2006 and 2016
year_data_type = df['Year'].dtype

# Count movies in 2006 and 2016 ensuring correct data type usage
movies_2006 = df.loc[df['Year'] == 2006, 'Title'].count() if year_data_type != 'object' else df.loc[df['Year'] == '2006', 'Title'].count()
movies_2016 = df.loc[df['Year'] == 2016, 'Title'].count() if year_data_type != 'object' else df.loc[df['Year'] == '2016', 'Title'].count()

# Calculate the percentage increase if both counts are non-zero to avoid division by zero
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100 if movies_2006 > 0 else "N/A"

print(percentage_increase)

# A10. The most common actor in all the movies

# Split the 'Actors' column into lists, explode to separate rows, and count occurrences
most_common_actor = df['Actors'].str.split(',').explode().str.strip().value_counts().idxmax()

# Find the count for the most common actor
most_common_actor_count = df['Actors'].str.split(',').explode().str.strip().value_counts().max()

print((most_common_actor, most_common_actor_count))

# A11. Number of unique genres that are there in the dataset

# Split the 'Genre' column into individual genres, explode to separate rows, and count unique genres
unique_genres_count = df['Genre'].str.split(',').explode().nunique()

print(unique_genres_count)

# A12. Correlation of the numerical features

# Calculate the correlation matrix of the numerical features in the dataset
correlation_matrix = df.select_dtypes(include=['int64', 'float64']).corr()

print(correlation_matrix)

# 1. Five insights that I can deduce

# 1.1. A strong positive correlation exists between 'Votes' and 'Revenue_(Millions)', approximately 0.64, suggesting movies with more votes tend to generate higher revenue.
    
# 1.2. There is a high positive correlation between 'Rating' and 'Metascore', approximately 0.60, indicating that audience ratings are in agreement with critical scores.
    
# 1.3. 'Runtime_(Minutes)' shows a positive correlation with both 'Rating', approximately 0.39, and 'Votes', approximately 0.41, implying that longer films might be better received and more engaged with by audiences.
    
# 1.4. 'Year' has a negative correlation with 'Votes', approximately -0.41, which could suggest that newer movies have had less time to accumulate votes compared to older ones.
    
# 1.5. 'Rank' has a negative correlation with 'Votes', approximately -0.28, and 'Revenue_(Millions)', approximately -0.26, indicating that movies with a better rank (lower numerical value) tend to have more votes and revenue.
    
# 2. Advice for directors:

# 2.1. Since 'Votes' correlate strongly with 'Revenue', directors should focus on audience engagement, as popular movies are also high-grossing.
    
# 2.2. The strong correlation between 'Rating' and 'Metascore' suggests that high-quality movies that please both audiences and critics can achieve better success.
    
# 2.3. Given the positive correlation with 'Rating' and 'Votes', the runtime should be sufficient to develop the story, but not so long that it disengages viewers.
    
# 2.4. The negative correlation of 'Year' with 'Votes' hints that movies that remain relevant and continue to engage audiences over time might maintain or increase their popularity.
    
# 2.5. The correlation between 'Rank' and other features like 'Votes' and 'Revenue' suggests that tracking performance metrics can provide valuable feedback for improvement.












