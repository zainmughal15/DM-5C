
import pandas as pd
import numpy as np

# Step 1: Define dataset with new Urdu-style names
passenger_info = {
    'PassengerId': [201, 202, 203, 204, 205, 206, 207, 208],
    'Survived': [0, 1, 1, 0, 0, 1, 1, 0],
    'Pclass': [2, 1, 3, 2, 1, 3, 2, 3],
    'Name': [
        "Ansari, Mr. Haris",
        "Begum, Mrs. Zainab",
        "Qureshi, Miss. Anaya",
        "Chaudhry, Mr. Danish",
        "Hashmi, Mr. Faizan",
        "Naz, Miss. Mahnoor",
        "Mirza, Mr. Imran",
        "Rehman, Miss. Emaan"
    ],
    'Sex': ['male', 'female', 'female', 'male', 'male', 'female', 'male', 'female'],
    'Age': [40, 33, np.nan, 27, np.nan, 19, 61, 5],
    'SibSp': [1, 0, 1, 0, 0, 2, 0, 1],
    'Parch': [0, 1, 0, 0, 2, 1, 0, 1],
    'Ticket': ['X100', 'Y200', 'Z300', 'W400', 'V500', 'U600', 'T700', 'S800'],
    'Fare': [60.0, 100.5, 7.85, 45.3, 80.0, 15.75, 70.25, 10.5],
    'Cabin': [np.nan, 'B45', 'Not Assigned', np.nan, 'C22', 'D10', np.nan, 'F33'],
    'Embarked': ['C', 'S', np.nan, 'S', 'Q', 'C', np.nan, 'Q']
}

# Step 2: Load into DataFrame
df = pd.DataFrame(passenger_info)

# Step 3: Display initial missing values
print("Missing Data Before Cleaning:\n", df.isnull().sum(), "\n")

# Step 4: Handle missing values
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Cabin'] = df['Cabin'].fillna("Not Assigned")

# Step 5: Define age categories
def age_to_category(age):
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 35:
        return "Adult"
    elif age <= 60:
        return "Middle-Aged"
    else:
        return "Senior"

df['AgeGroup'] = df['Age'].apply(age_to_category)

# Step 6: Extract surname from Name
df['Surname'] = df['Name'].apply(lambda x: x.split(',')[0].strip())

# Step 7: Final report
print("Missing Data After Cleaning:\n", df.isnull().sum(), "\n")
print("Cleaned Data Snapshot:\n", df[['PassengerId', 'Survived', 'Age', 'AgeGroup', 'Embarked', 'Cabin', 'Surname']])
