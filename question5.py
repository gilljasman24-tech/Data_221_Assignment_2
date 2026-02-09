import pandas as pd

# Load the student dataset
df = pd.read_csv("student.csv")

# Create the grade_band column
def assign_grade_band(grade):
    if grade <= 9:
        return "Low"
    elif grade <= 14:
        return "Medium"
    else:
        return "High"

df["grade_band"] = df["grade"].apply(assign_grade_band)

# Create the grouped summary table
summary = df.groupby("grade_band").agg(
    num_students=("grade", "count"),
    avg_absences=("absences", "mean"),
    internet_percentage=("internet", "mean")
)

# Convert internet proportion to percentage
summary["internet_percentage"] = summary["internet_percentage"] * 100

# Save the summary table to a CSV file
summary.to_csv("student_bands.csv")

# Print the summary table
print(summary)
