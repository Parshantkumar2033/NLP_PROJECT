import json
import fnmatch
from pathlib import Path
import csv

# dir_path = Path('C:/Users/PRASHANT KAJAL/Desktop/college_pro')
# pattern = 'marketaux_data*.json'

# with open('Marico_data.json', encoding='utf-8') as json_file:
#     d = json.load(json_file)
#     data_needed = d['data']
# with open('Marico_random.json', 'w') as random_file:
#     json.dump(data_needed, random_file, indent=4)

# for file in dir_path.glob('*.json'):
#     if fnmatch.fnmatch(file.name, pattern):
#         file.unlink()

# with open('Infosys_1_random.json', encoding='utf-8') as file1:
#     data = json.load(file1)
#     print(len(data))
# with open('Infosys_2_random.json', encoding='utf-8') as file2:
#     f2 = json.load(file2)
#     print(len(f2))
# with open('Infosys_3_random.json', encoding= 'utf-8') as file3:
#     f3 = json.load(file3)
#     print(len(f3))

# data.append(f2)
# data.append(f3)

# with open('Infosys_random.json', 'w') as file4:
#     json.dump(data, file4, indent=4)

with open('Infosys_random.json') as file:
    data = json.load(file)
    print(len(data))