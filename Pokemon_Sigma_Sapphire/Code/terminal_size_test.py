import os
import time


time.sleep(2)

print("Checking size of terminal")

time.sleep(2)

x = os.get_terminal_size().lines
y = os.get_terminal_size().columns

print("X dimension: ", x)
print("Y dimension: ", y)

time.sleep(2)

print("Changing size of terminal")

time.sleep(2)

cmd = 'mode 50,20'
os.system(cmd)

inp = input("Type q to quit: ")
if inp == "q":
    quit()


