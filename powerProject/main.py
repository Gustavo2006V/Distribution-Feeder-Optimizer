from Power import loadCurrents_calculate, lineCurrents_calculate, busVoltages_calculate, checkConvergence_pu
from capacitor_optimizer import iterator
import math

totalIterations = 100
iterations = 0
substationVoltage = 12700
RperMileLine = .3
XperMileLine = .4
voltages = [12700, 12700, 12700]
secondVoltages = [0,0,0]
realPower = [500000, 400000, 450000]
powerFactors = [.8,.9, 0.3]
milesBetweenLoads = [10,40,50]
loadCurrents = [0,0,0]
lineCurrents =[0,0,0]
capacitorVAR = float('inf')
for i in range(len(realPower)):
	current = (realPower[i] * math.sin(math.acos(powerFactors[i])))/2
	if capacitorVAR > current:
		capacitorVAR = current

while not checkConvergence_pu(secondVoltages, voltages,substationVoltage, .001 ) and totalIterations >= iterations:
	loadCurrents = loadCurrents_calculate(realPower, voltages,powerFactors)
	lineCurrents = lineCurrents_calculate(loadCurrents)
	secondVoltages = busVoltages_calculate(RperMileLine, XperMileLine, lineCurrents, substationVoltage, milesBetweenLoads) 
	print(secondVoltages)
	print(voltages)
	print(lineCurrents)
	temporaryVoltages =  voltages
	voltages = secondVoltages
	secondVoltages = temporaryVoltages
	iterations = iterations + 1
if(totalIterations == iterations):
	print("the values did not converge")
print("this is where I dcheck my values")

print(lineCurrents[0])
print(lineCurrents[1])
print(lineCurrents[2])
i = 0
lowest = float('inf')
result = [ ]

for i in range(len(voltages)):
	empty = [ ]
	temporary = iterator(realPower, powerFactors, capacitorVAR, i, empty, 1,RperMileLine, 4, 50000, milesBetweenLoads)
	if lowest > temporary[1]:
		result = temporary
		lowest = result[1]
print("This is where I check my second round of values")
print(result[0])
print(result[1])
i = 0
lowest = float('inf')
secondResult = []

for i in range(len(voltages)):
	empty = []
	temporary = iterator(realPower, powerFactors, capacitorVAR, i, empty, 2, RperMileLine, 4, 50000, milesBetweenLoads)
	if lowest > temporary[1]:
		secondResult = temporary
		lowest = secondResult[1]
print("This is where I check my third round of values")
print(secondResult[0])
print(secondResult[1])
	