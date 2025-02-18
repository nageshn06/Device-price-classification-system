import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

# Load dataset
train_df = pd.read_excel('data/train.xlsx')

# Fill missing values with the median (for simplicity)
imputer = SimpleImputer(strategy='median')
train_df_imputed = pd.DataFrame(imputer.fit_transform(train_df), columns=train_df.columns)

# Prepare features and target
X = train_df_imputed.drop('price_range', axis=1)
y = train_df_imputed['price_range']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'random_forest_model.pkl')
