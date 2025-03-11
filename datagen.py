import numpy as np
import pandas as pd

np.random.seed(42)
n_samples = 1000
size = np.random.randint(500, 3000, n_samples)
bedrooms = np.random.randint(1, 6, n_samples)
price = 100 * size + 20000 * bedrooms + np.random.normal(0, 10000, n_samples)
data = pd.DataFrame({'Size': size, 'Bedrooms': bedrooms, 'Price': price})
data.to_csv('house_prices.csv', index=False)

print("Datos guardados en 'house_prices.csv'")
