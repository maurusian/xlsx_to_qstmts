import pandas as pd

# Replace 'your_excel_file.xlsx' with the path to your actual Excel file
excel_path = 'countries - Copy.xlsx'
output_file = 'quickstatements.txt'
lang="ary"

# Load the Excel file
df = pd.read_excel(excel_path)

# Open the output file to write the quickstatements
with open(output_file, 'w',encoding="utf-8") as file:
    for _, row in df.iterrows():
        # Prepare the quickstatement string for the current row
        # Using iloc to reference by index position
        # Write the quickstatement for masculine singular
        file.write(f"{row.iloc[0]}|P1549|{lang}:\"{row.iloc[2]}\"|P518|Q47088290||")
        # Write the quickstatement for feminine singular
        file.write(f"{row.iloc[0]}|P1549|{lang}:\"{row.iloc[3]}\"|P518|Q47088293||")
        # Write the quickstatement for masculine plural
        file.write(f"{row.iloc[0]}|P1549|{lang}:\"{row.iloc[4]}\"|P518|Q47088292||")
        # Write the quickstatement for feminine plural
        file.write(f"{row.iloc[0]}|P1549|{lang}:\"{row.iloc[5]}\"|P518|Q47088295||")
