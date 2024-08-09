import random
MajorityDemand = [
	"Citizen demand for: Electricity",
	"Citizen demand for: Petrol",
	"Citizen demand for: Good Governance",	
	"Citizen demand for: Justice",
	"Citizen demand for: Constitutional reform",
	"Citizen demand for: Increment of minimum wages",
	"Citizen demand for: Education investment",
	"Citizen demand for: Security reform",
	"Citizen demand to: Prob past and present leader who had looted and deposit in a special account"]

ProtestAgainstMajorityDemand = [
	"Destruction of properties",
	"Loss of lives", 
	"Violent"]

Protest = 9
AntiProtest = 3
CitizenDemand = ""
CoveteousDemand = ""

print("<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>")
print("WELCOME TO NIGERIAN UPDATE ON THE ONGOING PROTEST.")
		
for index in range(Protest):
	randomProtester = random.choice(MajorityDemand)
	
	print("This is the majority protester demand: ")
	print(randomProtester)

for count in range (AntiProtest):
	randomAntiProtester = random.choice(ProtestAgainstMajorityDemand)

	print("This is anti protester point(COVETEOUSE CITIZEN): ")
	print(randomAntiProtester)
#

