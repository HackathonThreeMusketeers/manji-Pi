import subprocess

def ManjiCamera4p3():

    p = subprocess.Popen("python main.py", shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    #ここでpyton2に文字列を渡す
    stdout_data, stderr_data = p.communicate(timeout=20)
    return stdout_data.decode("utf-8")


#if __name__ == '__main__':
print(ManjiCamera4p3());
