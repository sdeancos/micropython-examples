import pyb

sw = pyb.Switch()
sw.callback(lambda:pyb.LED(1).toggle())
