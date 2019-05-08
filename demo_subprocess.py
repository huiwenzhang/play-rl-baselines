"""
Play with python subprocess module
"""

import subprocess

print("Start a subprocess to execute nslookup command")
r = subprocess.call(['nslookup', 'www.baidu.com'])
print("Exit code: ", r)


# start a sub-process with extra input arguments
print("================================================")
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
output, err = p.communicate(b"set q=mx \n www.baidu.com \n exit \n")
print(output.decode("utf-8"))
print("Exit code:", p.returncode)