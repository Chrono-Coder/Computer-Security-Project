import subprocess
compile_lib = "gcc -shared -fPIC -I/usr/lib/jvm/default-java/include -I/usr/lib/jvm/default-java/include/linux -o libs/libopencv_info.so code.c"

run_java_code =  "java -Djava.library.path=/home/kali/Desktop/code/server/code/libs Test"

try:
    result = subprocess.run(compile_lib, shell=True, check=True, text=False)
    result2 = subprocess.run(run_java_code, shell=True, check=True, text=False)
   
except subprocess.CalledProcessError as e:
    print(f"Python Error: {e}")
  



