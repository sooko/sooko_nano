from machine import Pin,PWM
gpio2 = machine.Pin(2,Pin.OUT)
pwm=PWM(gpio2)
pwm.freq(500)   #give 50% of dutycycle
pwm.duty(512)

# duty 1024 is full on and 0 in full of 
# max freq is  2047
