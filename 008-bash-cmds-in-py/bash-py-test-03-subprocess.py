import subprocess

process = subprocess.Popen(['ls', '-l'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

print(stdout)

with open('subprocess-output.txt', 'w') as f:
    process = subprocess.Popen(['ls', '-l'], stdout=f)