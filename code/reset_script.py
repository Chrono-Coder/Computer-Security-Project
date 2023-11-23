import subprocess
command = "lsof -i :6666"

try:
    result = subprocess.run(command, shell=True, check=True, text=False)
    print("Type: kill {PID}")
   
except subprocess.CalledProcessError as e:
    print(f"Python Error: {e}")
  



