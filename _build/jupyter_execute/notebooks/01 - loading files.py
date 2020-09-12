# Loading Files

## Loading CSV file

import pandas as pd
import numpy as np

table_df = pd.read_csv('../data/open_restaurant_applications_1.csv')

table_df.head()

table_df.info()

table_df.describe()

table_df.plot.scatter(x='longitude',y='latitude')

## Adding new columns

(
    table_df
    .assign(approved=lambda x : np.where(x.approved_for_roadway_seating == 'yes','g','r'))
    .plot.scatter(x='longitude',y='latitude',c='approved')
)

