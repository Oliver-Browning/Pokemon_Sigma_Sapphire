import time

#Create a function with this that takes in a Hit input
#call the function a ton of times in a while loop in the game 
#Send the button pressed boolean as the argument for this function


#Check if time stopped at is close enough to time target

seconds = 0
count_by = .01

#Idea is to make this so it has to stop at a certain time
while True:
    print(f"{seconds:.2f}", end="\r")
    time.sleep(count_by)
    seconds += count_by

