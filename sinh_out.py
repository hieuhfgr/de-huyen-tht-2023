import os
import subprocess
from glob import glob

id = int(input("id bai: "))

folder = f"./bai{id}"
subprocess.run(["g++", f"cau{id}.cpp", "-o", f"cau{id}.exe"])
fileinps = glob(os.path.join(folder, "*.inp"))
for fileinp in fileinps:
    ansfilename = fileinp.replace(folder, '').replace("\\", "").replace(".inp", "")
    ansfilename = f"{ansfilename}.ans"
    print(ansfilename)
    with open(fileinp, 'r') as f:
        inp = f.read()
        result = subprocess.run(f"cau{id}.exe", input=inp, text=True, capture_output=True)
        with open(os.path.join(folder,ansfilename), 'w') as f:
            f.write(result.stdout)
        print(result.stdout)