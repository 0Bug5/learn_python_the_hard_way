#here is the fnx!
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheese!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print(f"Man that's enough for a party!")
	print(f"Get a blanket.\n")

#i can call my fnx directly.
print("We can just give the functions number directly: ")
cheese_and_crackers(20, 30)

#i can declear a variable to my fnx.
print("OR,  we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

#here i call my fnx with its variable.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#i can do math inside my fnx.
print("We can even do math inside too: ")
cheese_and_crackers(15 + 23, 30 + 49)

#i can combine math and variable in my fnx together.
print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

import sys

#The following is my fnx to run it 10 different ways!.
def emergency_and_theater(N_of_pupils_in_emergency, N_of_pupils_in_theater, week):
		print(f"Our school clinic reports on {week}")
		print(f"Emergency have {N_of_pupils_in_emergency} patiens.")
		print(f"Theater have {N_of_pupils_in_theater} patiens.")
	

emergency_and_theater(18, 4, 'Monday')

print()
#way number one(1st)
print('This is the first way to call fnx')
emergency_and_theater(5, 3, week = 'Tuesday')

print()
#second way(2nd)
print("This is the second way to call fnx")
argvs = sys.argv[1:]

for action in argvs:
	eval(action)()
print("This second method need a tiny work on terminal!!")

print()
#Third way(3rd)
print("This is third way to call fnx")
class Task:
	@staticmethod
	def pre_task():
		print("running pre_task")
		
	@staticmethod
	def task():
		print("running task")
	
	@staticmethod
	def post_task():
		print("running post_task")
		
argvs = sys.argv[1:]

task = Task()

for action in argvs:
	func = getattr(task, action)
	func()
print("This third fnx need tiny work on a terminal!!")

print()
#Fouth way(4th)
print("This is the fourth to call fnx")

def host(server, port_number = 443):
	print("[+] Start the ser ... {server} from RJ-45")
	print("[+] Conneting port {port_number}")
	print("__dict__attack!")