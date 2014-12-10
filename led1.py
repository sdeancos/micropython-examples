import pyb

led = pyb.LED(1) # red led
led.toggle()
led.on()
pyb.delay(2000)
led.off()
