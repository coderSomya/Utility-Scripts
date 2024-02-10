import pandas as pd

file_path = "final.csv"

df = pd.read_csv(file_path)

selected_df = df[["Candidate's Name", "Candidate's Email"]]

new_file_name = "data.xlsx"

selected_df.to_excel(new_file_name, index=False)

print(f"Data saved to: {new_file_name}")
