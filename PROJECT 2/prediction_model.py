import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# STEP 1: Load dataset
df = pd.read_csv("cleaned_ecommerce_data.csv")

# STEP 2: Select features and target
features = [
    'Product_Category',
    'User_Gender',
    'User_Age',
    'User_Location',
    'Payment_Method',
    'Shipping_Method',
    'Discount_Applied'
]
X = df[features]
y = df['Is_Returned']

# STEP 3: Preprocessing
categorical_features = ['Product_Category', 'User_Gender', 'User_Location', 'Payment_Method', 'Shipping_Method']
numeric_features = ['User_Age', 'Discount_Applied']

preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
    ('num', StandardScaler(), numeric_features)
])

# STEP 4: Model Pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])

# STEP 5: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# STEP 6: Train model
model.fit(X_train, y_train)

# STEP 7: Evaluate model
y_pred = model.predict(X_test)
print("\n🔍 Classification Report:\n")
print(classification_report(y_test, y_pred))

# STEP 8: Predict return probabilities
df['Return Probability'] = model.predict_proba(X)[:, 1]

# STEP 9: Filter high-risk products
high_risk = df[df['Return Probability'] > 0.7]
high_risk.to_csv("high_risk_products.csv", index=False)

print("\n✅ Saved high-risk products to: high_risk_products.csv")

