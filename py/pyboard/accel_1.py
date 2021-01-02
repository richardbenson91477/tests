import pyb

a = pyb.Accel()
l = pyb.LED(3)

while True:
     x = a.x()
     if abs(x) > 5:
         l.on()
     else:
         l.off()

     pyb.delay(100)

