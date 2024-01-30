import RPi.GPIO as GPIO
import time
from multiprocessing import Process
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

kitchen1Y = 3
kitchen2Y = 27
kitchen3Y = 9

kitchen1G = 4
kitchen2G = 22
kitchen3G = 11

kitchen1B = 2
kitchen2B = 17
kitchen3B = 10

table1 = 25
table2 = 8
table3 = 7
table4 = 12
table5 = 16

cr1 = 18
cr2 = 23
cr3 = 24

entrance1 = 5
entrance2 = 6
entrance3 = 13
entrance4 = 19
entrance5 = 26

GPIO.setup(kitchen1Y,GPIO.OUT)
GPIO.setup(kitchen2Y,GPIO.OUT)
GPIO.setup(kitchen3Y,GPIO.OUT)

GPIO.setup(kitchen1G,GPIO.OUT)
GPIO.setup(kitchen2G,GPIO.OUT)
GPIO.setup(kitchen3G,GPIO.OUT)

GPIO.setup(kitchen1B, GPIO.OUT)
GPIO.setup(kitchen2B, GPIO.OUT)
GPIO.setup(kitchen3B, GPIO.OUT)

GPIO.setup(table1, GPIO.OUT)
GPIO.setup(table2, GPIO.OUT)
GPIO.setup(table3, GPIO.OUT)
GPIO.setup(table4, GPIO.OUT)
GPIO.setup(table5, GPIO.OUT)
GPIO.setup(cr1, GPIO.OUT)
GPIO.setup(cr2, GPIO.OUT)
GPIO.setup(cr3, GPIO.OUT)
GPIO.setup(entrance1, GPIO.OUT)
GPIO.setup(entrance2, GPIO.OUT)
GPIO.setup(entrance3, GPIO.OUT)
GPIO.setup(entrance4, GPIO.OUT)
GPIO.setup(entrance5, GPIO.OUT)

def indiv(indiv, state, n):
	GPIO.output(indiv, state)
	time.sleep(n)
	
def tmless(indiv, state):
	GPIO.output(indiv, state)

def kitchen(kitchen1, kitchen2, kitchen3):
	GPIO.output(kitchen1, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(kitchen1, GPIO.LOW)
	GPIO.output(kitchen2, GPIO.HIGH)
	time.sleep(5)
	GPIO.output(kitchen2, GPIO.LOW)
	for x in range(25):
		GPIO.output(kitchen3, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(kitchen3, GPIO.LOW)
		time.sleep(0.2)
	
def table(table, state):
	while state == "eating":
		GPIO.output(table,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(table,GPIO.LOW)
		time.sleep(0.5)
	else:
		GPIO.output(table,GPIO.LOW)
		
def waitstaff():
	time.sleep(0.5)
		
def off():
	GPIO.output(kitchen1Y,GPIO.LOW)
	GPIO.output(kitchen2Y,GPIO.LOW)
	GPIO.output(kitchen3Y,GPIO.LOW)
	GPIO.output(kitchen1G,GPIO.LOW)
	GPIO.output(kitchen2G,GPIO.LOW)
	GPIO.output(kitchen3G,GPIO.LOW)
	GPIO.output(kitchen1B, GPIO.LOW)
	GPIO.output(kitchen2B, GPIO.LOW)
	GPIO.output(kitchen3B, GPIO.LOW)
	GPIO.output(table1, GPIO.LOW)
	GPIO.output(table2, GPIO.LOW)
	GPIO.output(table3, GPIO.LOW)
	GPIO.output(table4, GPIO.LOW)
	GPIO.output(table5, GPIO.LOW)
	GPIO.output(cr1, GPIO.LOW)
	GPIO.output(cr2, GPIO.LOW)
	GPIO.output(cr3, GPIO.LOW)
	GPIO.output(entrance1, GPIO.LOW)
	GPIO.output(entrance2, GPIO.LOW)
	GPIO.output(entrance3, GPIO.LOW)
	GPIO.output(entrance4, GPIO.LOW)
	GPIO.output(entrance5, GPIO.LOW)
	
while True:
	off()
	indiv(entrance1, GPIO.HIGH, 0.5)
	indiv(entrance2, GPIO.HIGH, 0.5)
	indiv(entrance3, GPIO.HIGH, 0.5)
	indiv(entrance4, GPIO.HIGH, 0.5)
	indiv(entrance5, GPIO.HIGH, 0.5)
	indiv(table1, GPIO.HIGH, 0.5)
	indiv(table2, GPIO.HIGH, 0.5)
	indiv(table3, GPIO.HIGH, 0.5)
	indiv(table4, GPIO.HIGH, 0.5)
	indiv(table5, GPIO.HIGH, 0.5)

	k1 = Process(target = kitchen, args = (kitchen1B, kitchen1Y, kitchen1G))
	k2 = Process(target = kitchen, args = (kitchen2B, kitchen2Y, kitchen2G))
	k3 = Process(target = kitchen, args = (kitchen3B, kitchen3Y, kitchen3G))
	k4 = Process(target = kitchen, args = (kitchen2B, kitchen2Y, kitchen2G))
	e1 = Process(target = table, args = (table1, "eating"))
	e2 = Process(target = table, args = (table2, "eating"))
	e3 = Process(target = table, args = (table3, "eating"))
	e4 = Process(target = table, args = (table4, "eating"))
	e5 = Process(target = table, args = (table5, "eating"))
	c1 = Process(target = tmless, args = (cr1, GPIO.HIGH))
	c2 = Process(target = tmless, args = (cr1, GPIO.HIGH))
	c3 = Process(target = tmless, args = (cr1, GPIO.HIGH))
	x1 = Process(target = tmless, args = (entrance1, GPIO.LOW))
	x2 = Process(target = tmless, args = (entrance2, GPIO.LOW))
	x3 = Process(target = tmless, args = (entrance3, GPIO.LOW))
	x4 = Process(target = tmless, args = (entrance4, GPIO.LOW))
	x5 = Process(target = tmless, args = (entrance5, GPIO.LOW))
		
	kitchen(kitchen1B, kitchen1Y, kitchen1G)
	e1.start()
	time.sleep(2)
	
	k2.start()
	time.sleep(5)
	
	e1.terminate()
	tmless(table1, GPIO.LOW)
	tmless(cr1, GPIO.HIGH)
	k3.start()
	time.sleep(5)
	
	tmless(cr1, GPIO.LOW)
	tmless(entrance1, GPIO.LOW)
	k1.start()
	time.sleep(8)
	
	k4.start()
	k2.terminate()
	e2.start()
	time.sleep(5)
	
	e3.start()
	k3.terminate()
	e2.terminate()
	tmless(table2, GPIO.LOW)
	tmless(cr1, GPIO.HIGH)
	time.sleep(5)
	
	e4.start()
	k1.terminate()
	e3.terminate()
	tmless(table3, GPIO.LOW)
	tmless(cr2, GPIO.HIGH)
	time.sleep(4)
	
	e5.start()
	k4.terminate()
	e4.terminate()
	tmless(table4, GPIO.LOW)
	tmless(cr3, GPIO.HIGH)
	time.sleep(4)
	
	e5.terminate()
	tmless(table5, GPIO.HIGH)
	time.sleep(5)
	
	tmless(cr1, GPIO.LOW)
	tmless(entrance2, GPIO.LOW)
	time.sleep(2)
	
	tmless(table5, GPIO.LOW)
	tmless(cr1, GPIO.HIGH)
	tmless(cr2, GPIO.LOW)
	tmless(entrance3, GPIO.LOW)
	time.sleep(2)
	
	tmless(cr3, GPIO.LOW)
	tmless(entrance4, GPIO.LOW)
	time.sleep(2)
	
	tmless(cr1, GPIO.LOW)
	tmless(entrance5, GPIO.LOW)
	time.sleep(2)
	
	off()
	
	

