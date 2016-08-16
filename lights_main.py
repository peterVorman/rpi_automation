import sys
from qhue import Bridge
b = Bridge("100.66.30.18", "elbLovRPUcHaqss904iEJMH9LZrRwsvFeOKSfvOP")
lights = b.lights
print(b.config()['mac'])
print(b.lights())

command = sys.argv[-1]

if command == 'led_off':
	b.lights(1, 'state', bri=255, on=False)
	b.lights(2, 'state', bri=255, on=False)
	b.lights(3, 'state', bri=255, on=False)
elif command == 'led_on':
	b.lights(1, 'state', bri=255, on=True)
	b.lights(2, 'state', bri=255, on=True)
	b.lights(3, 'state', bri=255, on=True)
elif command == 'dota':
	b.lights(1, 'state', bri=255, on=True, xy=[0.6065, 0.3095])
	b.lights(2, 'state', bri=255, on=True, xy=[0.6883, 0.306])
	b.lights(3, 'state', bri=255, on=True, xy=[0.6883, 0.306])
elif command == 'blaze':
	b.lights(1, 'state', bri=255, on=True, xy=[0.3344, 0.5002])
	b.lights(2, 'state', bri=255, on=True, xy=[0.3254, 0.5028])
	b.lights(3, 'state', bri=255, on=True, xy=[0.3239, 0.4932])
elif command == 'chill':
	b.lights(1, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
	b.lights(2, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
	b.lights(3, 'state', bri=255, on=True, xy=[0.3069, 0.3152])
elif command == 'off':
	b.lights(1, 'state', bri=255, on=False)
	b.lights(2, 'state', bri=255, on=False)
	b.lights(3, 'state', bri=255, on=False)
	os.system("python /home/pi/rpi_automation/TransmitRF.py a_off")
elif command == 'on':
	os.system("python /home/pi/rpi_automation/TransmitRF.py a_on")