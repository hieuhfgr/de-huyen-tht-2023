import glob
import os

id = input('id: ')
files_to_delete = glob.glob(f"./bai{id}/*.out")

for file in files_to_delete:
    os.remove(file)
