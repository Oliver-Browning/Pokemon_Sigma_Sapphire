import time



seconds = 0
count_by = .01

#Idea is to make this so it has to stop at a certain time
while True:
    print(f"{seconds:.2f}", end="\r")
    time.sleep(count_by)
    seconds += count_by

