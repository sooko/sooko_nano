from machine import Timer
timer =timer(0)  
def cb(timer):
  print("timer is running")
timer.init(period=1000, mode=machine.Timer.PERIODIC, callback=cb)
