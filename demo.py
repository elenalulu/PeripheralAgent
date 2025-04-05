import subprocess
import os


folder_path = './scripts'
for root, dirs, files in os.walk(folder_path):
	for file in files:
		print (file)

		command = "python ./keymousego/KeymouseGo.py ./scripts/" + file + " --runtimes 1"
		subprocess.run(command, capture_output=True, text=True, shell=True)