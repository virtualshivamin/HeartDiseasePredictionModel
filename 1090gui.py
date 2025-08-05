
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, auc


df = pd.read_csv("heart.csv")

df.head()

df.columns = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'cholesterol',
              'fasting_blood_sugar', 'rest_ecg', 'max_heart_rate_achieved',
              'exercise_induced_angina', 'st_depression', 'st_slope', 'num_major_vessels',
              'thalassemia', 'target']


X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size = 0.30, random_state=42)

model = RandomForestClassifier(max_depth=5)
model.fit(X_train, y_train)

y_predict = model.predict(X_test)
"""#Conclusion:- Random Forest Classifier Performed the best among the above models

GUI
"""

import tkinter as tk
from tkinter import messagebox
import numpy as np

# Tkinter GUI
def predict():
    try:
        # Get input values
        inputs = [
            float(age_entry.get()),
            int(sex_entry.get()),
            int(chest_pain_type_entry.get()),
            float(resting_blood_pressure_entry.get()),
            float(cholesterol_entry.get()),
            int(fasting_blood_sugar_entry.get()),
            int(rest_ecg_entry.get()),
            float(max_heart_rate_entry.get()),
            int(exercise_induced_angina_entry.get()),
            float(st_depression_entry.get()),
            int(st_slope_entry.get()),
            int(num_major_vessels_entry.get()),
            int(thalassemia_entry.get())
        ]

        # Convert inputs to numpy array and reshape for prediction
        inputs = np.array(inputs).reshape(1, -1)
        prediction = model.predict(inputs)[0]

        # Display result
        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
        messagebox.showinfo("Prediction Result", result)
    except Exception as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

# Create the GUI window
root = tk.Tk()
root.title("Heart Disease Prediction")
root.geometry("400x600")

# Input fields
fields = [
    "Age", "Sex", "Chest Pain Type", "Resting Blood Pressure", "Cholesterol",
    "Fasting Blood Sugar", "Rest ECG", "Max Heart Rate Achieved",
    "Exercise Induced Angina", "ST Depression", "ST Slope", "Num Major Vessels",
    "Thalassemia"
]

entries = []
for i, field in enumerate(fields):
    label = tk.Label(root, text=field, font=("Arial", 12))
    label.grid(row=i, column=0, pady=5, padx=5, sticky="w")
    entry = tk.Entry(root, font=("Arial", 12))
    entry.grid(row=i, column=1, pady=5, padx=5)
    entries.append(entry)

# Assign entries to variables for easy access
(
    age_entry, sex_entry, chest_pain_type_entry, resting_blood_pressure_entry,
    cholesterol_entry, fasting_blood_sugar_entry, rest_ecg_entry,
    max_heart_rate_entry, exercise_induced_angina_entry, st_depression_entry,
    st_slope_entry, num_major_vessels_entry, thalassemia_entry
) = entries

# Predict button
predict_button = tk.Button(root, text="Predict", font=("Arial", 14), bg="blue", fg="white", command=predict)
predict_button.grid(row=len(fields), column=0, columnspan=2, pady=20)

# Run the Tkinter loop
root.mainloop()