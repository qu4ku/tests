import os

stream = os.popen('ls -l')
output = stream.readlines()

[print(line) for line in output]