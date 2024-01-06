import subprocess


# result = subprocess.run("dir", shell=True, capture_output=True, text=True)
# print(type(result))  # completedProcess
# print(result.returncode)
# print(result.stderr)  # standard error
# print(result.stdout)  # standard output

# legacy
""" subprocess.call
subprocess.check_call
subprocess.check_output
subprocess.Popen
 """

result = subprocess.run(["python", "other.py"],
                        shell=True, capture_output=True, text=True)
print(type(result))  # completedProcess
print(result.returncode)  # 0 for no code
print(result.stderr)  # standard error
print(result.stdout)  # standard output
