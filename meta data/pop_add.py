# import csv

# # Data to be added to the CSV file for Bornean and Sumatran orangutans
# new_orangutan_data = [
#     # Bornean and Sumatran Orangutan population trend
#     ["Orangutans", "Bornean", 1970, 200000],
#     ["Orangutans", "Bornean", 1980, "Significant decline"],
#     ["Orangutans", "Bornean", 1996, 167000],
#     ["Orangutans", "Bornean", 1997, 167000],
#     ["Orangutans", "Bornean", 2000, 12500],
#     ["Orangutans", "Bornean", 2004, 54558],
#     ["Orangutans", "Bornean", 2016, 104700],
#     ["Orangutans", "Bornean", 2024, 104700],
#     ["Orangutans", "Sumatran", 2016, 13846],
#     ["Orangutans", "Sumatran", 2024, 13846],
# ]

# # Data to be added for Amur Leopards
# amur_leopard_data = [
#     ["Amur_Leopard", "World", 1960, 1500],
#     ["Amur_Leopard", "World", 1970, 30],
#     ["Amur_Leopard", "World", 1980, 35],
#     ["Amur_Leopard", "World", 1990, 30],
#     ["Amur_Leopard", "World", 2000, 30],
#     ["Amur_Leopard", "World", 2012, 32],
#     ["Amur_Leopard", "World", 2016, 80],
#     ["Amur_Leopard", "World", 2020, 100],
#     ["Amur_Leopard", "World", 2024, 143],
# ]

# # Data to be added for Cheetahs
# cheetah_data = [
#     ["Cheetahs", "World", 1960, 40000],
#     ["Cheetahs", "World", 1975, 15000],
#     ["Cheetahs", "World", 1980, 10000],
#     ["Cheetahs", "World", 1990, 50000],
#     ["Cheetahs", "World", 2000, 7100],
#     ["Cheetahs", "World", 2019, 7100],
#     ["Cheetahs", "World", 2020, 7100],
#     ["Cheetahs", "World", 2024, 7000],
# ]

# # Path to the existing CSV file
# file_path = "Population_by_year.csv"

# # Open the existing file in append mode and write the new orangutan data
# with open(file_path, mode='a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(new_orangutan_data)

#     # Writing Amur Leopard data
#     writer.writerows(amur_leopard_data)
    
#     # Writing Cheetah data
#     writer.writerows(cheetah_data)

# print("New population data successfully added to population_by_year.csv")

# import csv

# # Path to the existing CSV file
# file_path = "Population_by_year.csv"

# # Read the data from the CSV file
# with open(file_path, mode='r', newline='') as file:
#     reader = csv.reader(file)
#     data = list(reader)

# # Filter out rows containing Orangutans, Cheetahs, or Amur Leopards
# filtered_data = [row for row in data if row[0] not in ["Orangutans", "Cheetah", "Amur Leopard"]]

# # Write the filtered data back to the CSV file
# with open(file_path, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(filtered_data)

# print("Orangutans, Cheetah, and Amur Leopard data successfully removed from population_by_year.csv")

import csv

# Data to be added for Arctic Fox
arctic_fox_data = [
    ["Arctic Fox", "Canada", 1960, 22],
    ["Arctic Fox", "Canada", 1970, 23],
    ["Arctic Fox", "Canada", 1980, 1000],  # Historic low in Iceland
    ["Arctic Fox", "Canada", 1990, 120],  # Estimated around 120 adults
    ["Arctic Fox", "Canada", 2000, 100],  # Nordic countries at a low point
    ["Arctic Fox", "Canada", 2010, 120],  # Some recovery
    ["Arctic Fox", "Canada", 2020, 550],  # Estimated 550 adults
    ["Arctic Fox", "Canada", 2024, 550],  # Population steady at 550

    # Data for Iceland
    ["Arctic Fox", "Iceland", 1960, 1300],
    ["Arctic Fox", "Iceland", 1970, 900],  # Historic low
    ["Arctic Fox", "Iceland", 1980, 800],
    ["Arctic Fox", "Iceland", 1990, 1000],  # Recovery starts
    ["Arctic Fox", "Iceland", 2000, 1000],
    ["Arctic Fox", "Iceland", 2010, 1500],
    ["Arctic Fox", "Iceland", 2020, 1500],
    ["Arctic Fox", "Iceland", 2024, 1500],
]

# Path to the existing CSV file
file_path = "Population_by_year.csv"

# Open the existing file in append mode and write the new Arctic Fox data
with open(file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(arctic_fox_data)

print("New Arctic Fox population data successfully added to population_by_year.csv")



