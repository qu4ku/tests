import subprocess

process = subprocess.Popen(['ping', '-c 4', 'python.org'],
	stdout=subprocess.PIPE,
	universal_newlines=True)

while True:
	output = process.stdout.readline()
	print(output.strip())

	# Use .poll() to check return code of the process
	# If None - still running
	return_code = process.poll()
	if return_code is not None:
		print('RETURNED CODE', return_code)
		# Process has finished, read rest of the output
		for output in process.stdout.readlines():
			print(output.strip())
		break