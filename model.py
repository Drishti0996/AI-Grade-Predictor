import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# Synthetic Data Generation (1500 students)
np.random.seed(42)
n = 1500
att = np.random.randint(75, 100, n)
study = np.random.uniform(1, 10, n)
prev = np.random.uniform(7, 10, n)
internals = np.random.randint(25, 50, n)

# Logic: High weight on study (4-5 hours is the "Sweet Spot")
gpa = (study * 0.75) + (internals * 0.1) + (prev * 0.1) + (att * 0.05)
gpa = np.clip(gpa - 1.8, 0, 10)

df = pd.DataFrame({'Att': att, 'Study': study, 'Prev': prev, 'Int': internals, 'GPA': gpa})

# Training the "Smart" Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(df[['Att', 'Study', 'Prev', 'Int']], df['GPA'])

# Save the brain
joblib.dump(model, 'grade_model.pkl')
# Save the data for transparency
df.head(50).to_csv('student_data.csv', index=False)
print("✅ model.py: AI Brain and Data sample created!")