import time
def timer(t):
    if t==0:
        print("Finished")
        return 0
    print("Remaining time",t)
    time.sleep(1)
    return timer(t-1)
timer(5)
