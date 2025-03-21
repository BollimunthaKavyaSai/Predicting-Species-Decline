import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
climate_df = pd.read_csv(r"C:\Users\bolli\Desktop\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\Climate_impacts_by_country.csv")
shift_df = pd.read_csv(r"C:\Users\bolli\Desktop\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\transboundary_range_shifts.csv")
richness_df = pd.read_csv(r"C:\Users\bolli\Desktop\5bf972a8-c9a3-4721-8089-552dfe3ff124\5bf972a8-c9a3-4721-8089-552dfe3ff124\data\transboundary_richness.csv")
# Histogram of percentage decline in species richness
plt.figure(figsize=(10, 6))
sns.histplot(high_risk_species['rcp85_both_pctChange'], bins=15, kde=True, color='blue')
plt.xlabel("% Decline in Species Richness (RCP 8.5)")
plt.ylabel("Frequency of Countries")
plt.title("Distribution of Species Decline Across Countries")
plt.grid()
plt.show()
