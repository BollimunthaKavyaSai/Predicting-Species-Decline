# Predicting-Species-Decline

## Overview  
This project analyzes climate-induced biodiversity loss using AI-driven techniques. It identifies species decline under the **RCP 8.5 scenario** and suggests conservation strategies based on predictive modeling.  

## Features  
- **Data Processing:** Cleans and merges climate and species datasets.  
- **Exploratory Data Analysis (EDA):** Generates correlation heatmaps, histograms, and outlier detection.  
- **Predictive Modeling:** Uses regression, clustering, and time-series forecasting to predict species decline.  
- **Visualization:** Plots species decline trends and high-risk transboundary biodiversity areas.  

## Dataset Sources  
- **Climate Impacts by Country**  
- **Transboundary Range Shifts**  
- **Transboundary Species Richness**  

## Technologies Used  
- **Python**  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  

## Setup Instructions  
1. Clone the repository:  
   ```bash
   git clone https://github.com/BollimunthaKavyaSai/Predicting-Species-Decline.git
   cd Predicting-Species-Decline

Install dependencies:
pip install pandas numpy matplotlib seaborn scikit-learn  


Run the main script:
python main.py

import os

# Define directory structure
dirs = [
    "Biodiversity-Analysis/data",
    "Biodiversity-Analysis/src",
    "Biodiversity-Analysis/results"
]

# Define files to create
files = [
    "Biodiversity-Analysis/src/data_preprocessing.py",
    "Biodiversity-Analysis/src/Species_decline_across_countries.py",
    "Biodiversity-Analysis/src/highest_species_decline.py",
    "Biodiversity-Analysis/src/heatmap.py",
    "Biodiversity-Analysis/README.md",
    "Biodiversity-Analysis/requirements.txt"
]

# Create directories
for dir in dirs:
    os.makedirs(dir, exist_ok=True)

# Create empty files
for file in files:
    with open(file, "w") as f:
        pass

print("Project directory structure created successfully!")





## Contributors  
- **Bollimuntha Kavya Sai**  
- **Sumithra**  
- **Chandrika**
- **Parvathy**
- **Renuka** 



##License
This project is licensed under the MIT License - see the LICENSE file for details.

This README provides a **clear project overview**, **setup steps**, and **structure details**. Let me know if you need any modifications!
