import pandas as pd
import numpy as np
data = {'A': [1, 2, np.nan, 4, 5],
        'B': [10, np.nan, 30, 40, 50],
        'C': [100, 200, 300, np.nan, 500]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df_removed = df.dropna()
print("\nDataFrame after removing missing values:")
print(df_removed)
df_imputed_mean = df.fillna(df.mean())
print("\nDataFrame after imputing missing values with mean:")
print(df_imputed_mean)
df_imputed_constant = df.fillna(-1)
print("\nDataFrame after imputing missing values with a constant value:")
print(df_imputed_constant)
