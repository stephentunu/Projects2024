#import time
import time
#defining the countDown function
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{02d}'.format(mins, secs)
        print(timer,end="\n")
        time.sleep(1)
        t -= 1
    print("fire in the annex")
#input the time in seconds
t = input("enter the time in seconds: ")   
#function call
countdown(int(t)) 
