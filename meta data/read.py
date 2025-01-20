    # import pandas as pd

    # # Load the existing CSV file
    # file_path = 'Animal.csv'
    # animal_data = pd.read_csv(file_path)

    # # Create a new row for the Orangutan
    # new_row = {
    #     "Animal_Name": "Orangutan",
    #     "Class": "Mammal",
    #     "Population": "112,200",
    #     "Weight": "87 kg (192 lbs) (Male), 37 kg (82 lbs) (Female)",
    #     "Length": "970 mm (38 in.) (Male), 780 mm (31 in.) (Female)",
    #     "Height": "1366 mm (54 in.) (Male), 1149 mm (45 in.) (Female)",
    #     "Habitats": "Tropical and subtropical rainforests",
    #     "Status": "Critically Endangered",
    #     "Country": "Indonesia, Malaysia",
    #     "Places": "Borneo, Sumatra"
    # }

    # # Append the new row to the DataFrame
    # animal_data = animal_data._append(new_row, ignore_index=True)

    # # Save the updated DataFrame back to the CSV
    # animal_data.to_csv(file_path, index=False)

    # print("New row added successfully!")

# import pandas as pd

# # Load the existing CSV file
# file_path = 'Effecting_Factor.csv'
# animal_factors = pd.read_csv(file_path)

# # Create a new row for Orangutan
# new_row = {
#     "Animal_Name": "Orangutan",
#     "Factor": "DEFORESTATION, HUNTING, LACK OF ENFORCEMENT",
#     "Country": "Indonesia, Malaysia"
# }

# # Append the new row to the DataFrame
# animal_factors = animal_factors._append(new_row, ignore_index=True)

# # Save the updated DataFrame back to the CSV
# animal_factors.to_csv(file_path, index=False)

# print("Orangutan details added successfully!")

# import pandas as pd

# # Load the existing CSV file
# file_path = "Endangered_Species.csv"
# data = pd.read_csv(file_path)

# # Orangutan details to add
# orangutan_details = {
#     "Animal_Name": "Orangutan",
#     "Population": "Bornean: 104,700; Sumatran: 7,500",
#     "Status": "Critically Endangered",
#     "Country": "Indonesia, Malaysia",
#     "Continent": "Asia",
#     "Year": "",
#     "Extinction_Rate": ""
# }

# # Append the details as a new row
# data = data._append(orangutan_details, ignore_index=True)

# # Save back to the CSV file
# data.to_csv(file_path, index=False)

# print("Orangutan details added successfully!")

# import pandas as pd

# # Load the existing CSV file
# file_path = "Remediation_measures.csv"
# data = pd.read_csv(file_path)

# # Orangutan details to add
# orangutan_details = {
#     "Animal_Name": "Orangutan",
#     "Measure_Taken": (
#         "CREATING AND MANAGING PROTECTED AREAS, "
#         "ENFORCING LAWS AGAINST CAPTURE AND TRADE, "
#         "REHABILITATION EFFORTS, "
#         "SELECTIVE LOGGING TO PROTECT HABITAT"
#     ),
#     "Country": "Indonesia, Malaysia",
#     "Effect_of_Measures": ""
# }

# # Append the details as a new row
# data = data._append(orangutan_details, ignore_index=True)

# # Save back to the CSV file
# data.to_csv(file_path, index=False)

# print("Orangutan details added successfully!")

import pandas as pd

# File paths
#endangered_species_file = "Endangered_Species.csv"
measures_taken_file = "Remediation_measures.csv"
#animal_file = "animal.csv"
factors_file = "Effecting_Factor.csv"

# Cheetah details for each file
cheetah_species_data = {
    "Animal_Name": "Cheetah",
    "Population": 7100,
    "Status": "Vulnerable",
    "Country": "Botswana, Namibia, Iran, Kenya, South Africa",
    "Continent": "Africa",
    "Year": "",
    "Extinction_Rate": ""
}

cheetah_measures_data = {
    "Animal_Name": "Cheetah",
    "Measure_Taken": "CREATING WILDLIFE CORRIDORS, ANTI-POACHING INITIATIVES, COMMUNITY-BASED CONSERVATION, CHEETAH REINTRODUCTION PROGRAMS",
    "Country": "Botswana, Namibia, Iran, Kenya, South Africa",
    "Effect_of_Measures": ""
}

cheetah_animal_data = {
    "Animal_Name": "Cheetah",
    "Class": "Mammal",
    "Population": 7100,
    "Weight": "77-143 pounds",
    "Length": "3.6-4.9 feet",
    "Height": "2-3 feet",
    "Habitats": "Grasslands, Savannahs, Open plains",
    "Status": "Vulnerable",
    "Country": "Botswana, Namibia, Iran, Kenya, South Africa",
    "Places": "Southern Africa, Eastern Africa"
}

# Cheetah details
cheetah_factors_data = {
    "Animal_Name": "Cheetah",
    "Factor": "HABITAT LOSS, HUMAN-WILDLIFE CONFLICT, POACHING, DECLINE IN PREY, CLIMATE CHANGE",
    "Country": "Botswana, Namibia, Iran, Kenya, South Africa"
}

# Function to append a row to a CSV file
def append_to_csv(file_path, row_data):
    try:
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([row_data])], ignore_index=True)
        df.to_csv(file_path, index=False)
        print(f"Data successfully added to {file_path}")
    except FileNotFoundError:
        # If file does not exist, create a new file with the given row
        df = pd.DataFrame([row_data])
        df.to_csv(file_path, index=False)
        print(f"File {file_path} created and data added.")

# Add cheetah details to each file
#append_to_csv(endangered_species_file, cheetah_species_data)
#append_to_csv(measures_taken_file,cheetah_measures_data)
#append_to_csv(animal_file, cheetah_animal_data)
append_to_csv(factors_file,cheetah_factors_data)
