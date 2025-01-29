import datetime

class log:
    start_time: datetime       # Value to calculate the runtime

    # Contructor to initilice and set the start_time
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.print("Set up log and start time") 

    # Formatted Console Print
    def print(self, logText: str):
        runTime = round((datetime.datetime.now() - self.start_time).microseconds / 1000)
        x = f"[{datetime.datetime.now()}] - {runTime} ms: {logText}"
        print(x)

