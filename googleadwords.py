""" Created on Tue Jan 15 19:49:00 2019
By: Dahiana Jimenez

DataCamp - Project
Generating Keywords for Google Adwords
"""

import pandas as pd

# List of words to pair with products
words = ['buy','price','cost','promo','sale','discount']

# Combine the words with the product names
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

# Create an empty list
keywords_list = []

# Loop through products
for product in products:
    # Loop through words
    for word in words:
        # Append combinations
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])
        
# Inspect keyword list
from pprint import pprint
pprint(keywords_list)

# Turn list into DataFrame
keywords_df = pd.DataFrame(keywords_list)

# Explore DataFrame
keywords_df.head()

# Rename the columns of the DataFrame
keywords_df.rename(columns={0:'Ad Group', 1:'Keyword'}, inplace=True)

# Add a campaign column
keywords_df['Campaign'] = 'SEM_Sofas'

# Add a criterion type column
keywords_df['Criterion Type'] = 'Exact'

# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()

# Change criterion type match to phrase
keywords_phrase['Criterion Type'] = 'Phrase'

# Append the DataFrames
keywords_df_final = keywords_df.append(keywords_phrase)
