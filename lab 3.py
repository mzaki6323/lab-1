import pandas as pd

# Exercise 1: Join two dataframes along rows and assign all data
data1 = {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
         'marks': [200, 210, 190, 222, 199]}
data2 = {'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
         'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
         'marks': [201, 200, 198, 219, 201]}
student_data1 = pd.DataFrame(data1)
student_data2 = pd.DataFrame(data2)
result1 = pd.concat([student_data1, student_data2])

# Exercise 2: Join two dataframes along columns and assign all data
result2 = pd.concat([student_data1, student_data2], axis=1)

# Exercise 3: Append rows to an existing DataFrame and display the combined data
new_row = pd.Series(['S6', 'Scarlette Fisher', 205], index=['student_id', 'name', 'marks'])
result3 = student_data1.append(new_row, ignore_index=True)

# Exercise 4: Append a list of dictionaries or series to an existing DataFrame and display the combined data
new_dict = {'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 205}
result4 = student_data1.append(new_dict, ignore_index=True)

# Exercise 5: Join the two dataframes along rows and merge with another dataframe along the common column id
exam_data = {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
             'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]}
exam_data_df = pd.DataFrame(exam_data)
result5 = pd.merge(pd.concat([student_data1, student_data2]), exam_data_df, on='student_id')

# Exercise 6: Join the two dataframes using the common column of both dataframes
result6 = pd.merge(student_data1, student_data2, on='student_id')

# Exercise 7: Join the two dataframes with matching records from both sides where available
result7 = pd.merge(student_data1, student_data2, on='student_id', how='inner')

# Exercise 8: Left join the two dataframes using keys from the left dataframe only
result8 = pd.merge(student_data1, student_data2, on='student_id', how='left')

# Exercise 9: Right join the two dataframes using keys from the right dataframe only
result9 = pd.merge(student_data1, student_data2, on='student_id', how='right')

# Exercise 10: Merge two datasets using multiple join keys
result10 = pd.merge(student_data1, student_data2, on=['key1', 'key2'])

# Exercise 11: Create a new DataFrame based on existing series and override existing column names
data_series = pd.Series(['A0', 'B0'], index=['A', 'B'])
new_df = pd.DataFrame(data_series, columns=['C']).T

# Exercise 12: Create a combination from two dataframes where a column id combination appears more than once
data1 = {'key1': ['K0', 'K0', 'K1', 'K2'],
         'key2': ['K0', 'K1', 'K0', 'K1'],
         'P': ['P0', 'P1', 'P2', 'P3'],
         'Q': ['Q0', 'Q1', 'Q2', 'Q3']}
data2 = {'key1': ['K0', 'K1', 'K1', 'K2'],
         'key2': ['K0', 'K0', 'K0', 'K0'],
         'R': ['R0', 'R1', 'R2', 'R3'],
         'S': ['S0', 'S1', 'S2', 'S3']}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
result12 = pd.merge(df1, df2, on=['key1', 'key2'])

# Exercise 13: Combine columns of two potentially differently-indexed DataFrames into a single result DataFrame
data1 = {'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}
data2 = {'C': ['C0', 'C2', 'C3'], 'D': ['D0', 'D2', 'D3']}
df1 = pd.DataFrame(data1, index=['K0', 'K1', 'K2'])
df2 = pd.DataFrame(data2, index=['K0', 'K2', 'K3'])
result13 = pd.concat([df1, df2], axis=1)

# Exercise 14: Merge two dataframes with different columns
data1 = {'key1': ['K0', 'K0', 'K1', 'K2'],
         'key2': ['K0', 'K1', 'K0', 'K1'],
         'P': ['P0', 'P1', 'P2', 'P3'],
         'Q': ['Q0', 'Q1', 'Q2', 'Q3']}
data2 = {'key1': ['K0', 'K1', 'K1', 'K2'],
         'key2': ['K0', 'K0', 'K0', 'K0'],
         'R': ['R0', 'R1', 'R2', 'R3'],
         'S': ['S0', 'S1', 'S2', 'S3']}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
result14 = pd.merge(df1, df2, on=['key1', 'key2'])

# Exercise 15: Combine two DataFrames by filling null values in one DataFrame with non-null values from the other
df1 = pd.DataFrame({'A': [None, 0, None], 'B': [3, 4, 5]})
df2 = pd.DataFrame({'A': [1, 1, 3], 'B': [3, None, 3]})
result15 = df1.combine_first(df2)

# Print results
print("Exercise 1:\n", result1)
print("\nExercise 2:\n", result2)
print("\nExercise 3:\n", result3)
print("\nExercise 4:\n", result4)
print("\nExercise 5:\n", result5)
print("\nExercise 6:\n", result6)
print("\nExercise 7:\n", result7)
print("\nExercise 8:\n", result8)
print("\nExercise 9:\n", result9)
print("\nExercise 10:\n", result10)
print("\nExercise 12:\n", result12)
print("\nExercise 13:\n", result13)
print("\nExercise 14:\n", result14)
print("\nExercise 15:\n", result15)
