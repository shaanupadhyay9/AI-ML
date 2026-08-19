import joblib
from sklearn.tree import DecisionTreeClassifier

# Training data
X = [
    [25000],
    [30000],
    [35000],
    [40000],
    [45000],
    [50000],
    [60000],
    [75000]
]

y = [
    "Junior Employee",
    "Junior Employee",
    "Junior Employee",
    "Junior Employee",
    "Senior Employee",
    "Senior Employee",
    "Senior Employee",
    "Senior Employee"
]

# Create model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")