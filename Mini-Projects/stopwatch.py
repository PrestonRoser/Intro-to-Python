import time

# Basic stopwatch that only accepts 'start' and 'stop' inputs
# Notable elements:
#   - import time handles the time factor
#   - time.time() grabs the current system time in seconds (since the epoch)
#   - time.sleep() creates a program delay

def watch():
    start_time = 0
    end_time = 0

    initiate = input("Type 'start' to start the stopwatch. ").lower().strip()

    if initiate == "start":
        start_time = time.time()
    else:
        raise ValueError("Only 'start' is an accepted input value at this time")

    time.sleep(1)
    stop = input("Type 'stop' to stop.").lower().strip()
    if stop == "stop":
        end_time = time.time()
    else:
        raise ValueError("Only 'stop' is an accepted input value at this time. ")
        
    return end_time - start_time

def main():
    print(watch())
    
if __name__ == "__main__":
    main()