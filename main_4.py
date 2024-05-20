import os
import time


folder = "demo"

N = 3

os.chdir(os.path.join(os.getcwd(), folder))

list_of_files = os.listdir()

current_time = time.time()

day = 86400

for i in list_of_files:
	file_location = os.path.join(os.getcwd(), i)
	file_time = os.stat(file_location).st_mtime
	if(file_time < current_time - day*N):
		print(f" Delete : {i}")
		os.remove(file_location)
