import pandas as pd

# Load the student dataset
df = pd.read_csv("student.csv")

# Filter students based on the given conditions
filtered_df = df[
    (df["studytime"] >= 3) &
    (df["internet"] == 1) &
    (df["absences"] <= 5)
]

# Save the filtered data to a new CSV file
filtered_df.to_csv("high_engagement.csv", index=False)

# Compute the number of students and the average grade
num_students = len(filtered_df)
average_grade = filtered_df["grade"].mean()

# Print the results
print("Number of students saved:", num_students)
print("Average grade:", round(average_grade, 2))
