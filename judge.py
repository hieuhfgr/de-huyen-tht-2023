import os
import subprocess
from glob import glob
def get_file_ans(fileinp):
    fileans = fileinp.replace(folder, '').replace("\\", "").replace(".inp", "")
    fileans = f"{fileans}.ans"
    return fileans

def get_output(filecode, language, input):
    output = ""
    if (language == 'py'):
        result = subprocess.run(["python", f"{filecode}.py"])
        return result.stdout
    else:
        result = subprocess.run(f"{filecode}.exe", input=input, text=True, capture_output=True)
        return result.stdout


problem = int(input("Nhập id bài (1,2,3,4): "))
while not (problem in [1,2,3,4]):
    problem = int(input("Không hợp lệ!\nNhập id bài (1,2,3,4): "))
filecode = input("Nhập tên file code (chỉ tên không ghi đuôi mở rộng!): ")
language = input("Nhập ngôn ngữ (pas, py, cpp): ")
while not (language in ['pas', 'py', 'cpp']):
    language = input("Không hợp lệ!\nNhập ngôn ngữ (pas, py, cpp): ")

if (language == 'pas'):
    subprocess.run(["fpc", f"{filecode}.pas"])
elif (language == 'cpp'):
    subprocess.run(["g++", f"{filecode}.cpp", "-o", f"{filecode}.exe"])
folder = f"./bai{problem}"
fileinps = glob(os.path.join(folder, "*.inp"))
cnt=0
total=0
for fileinp in fileinps:
    fileans = get_file_ans(fileinp)
    inp = ''
    ans = ''
    with open(fileinp, 'r') as f:
        inp = f.read()
    with open(os.path.join(folder, fileans), 'r') as f:
        ans = f.read()

    out = get_output(filecode, language, inp)
    if (out.strip() == ans.strip()):
        print(f"#{total+1}: chấp nhận.")
        cnt += 1
    else:
        print(f"#{total+1}: sai.")
    total += 1

print('----')
print(f'Điểm của bạn: {cnt}/{total}')
