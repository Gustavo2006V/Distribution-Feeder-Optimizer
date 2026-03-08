from Power import loadCurrents_calculate, lineCurrents_calculate, busVoltages_calculate, checkConvergence_pu
from capacitor_optimizer import iterator
import math

totalIterations = 100
iterations = 0
substationVoltage = 12470
RperMileLine = .3
XperMileLine = .4
voltages = [12470, 12470, 12470]
secondVoltages = [0,0,0]
realPower = [400000, 600000, 500000, ]
powerFactors = [.8,.85, 0.9]
milesBetweenLoads = [2,1.5,1.0]
loadCurrents = [0,0,0]
lineCurrents =[0,0 ,0]
capacitorVAR = 200000

while not checkConvergence_pu(secondVoltages, voltages,substationVoltage, 1e-5 ) and totalIterations >= iterations:
	loadCurrents = loadCurrents_calculate(realPower, voltages,powerFactors)
	lineCurrents = lineCurrents_calculate(loadCurrents)
	secondVoltages = busVoltages_calculate(RperMileLine, XperMileLine, lineCurrents, substationVoltage, milesBetweenLoads) 
	temporaryVoltages =  voltages
	voltages = secondVoltages
	secondVoltages = temporaryVoltages
	iterations = iterations + 1
if(totalIterations == iterations):
	print("the values did not converge")
print("this is where I dcheck my values (line currents)")

print(lineCurrents[0])
print(lineCurrents[1])
print(lineCurrents[2])
print("This is where I check my voltage values, (bus voltages)")
print(abs(secondVoltages[0]))
print(abs(secondVoltages[1]))
print(abs(secondVoltages[2]))
i = 0
lowest = float('inf')
result = []

for i in range(len(voltages)):
	empty = []
	temporary = iterator(realPower, powerFactors, capacitorVAR, i, empty, 1 ,RperMileLine, milesBetweenLoads)
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
	temporary = iterator(realPower, powerFactors, capacitorVAR, i, empty, 2, RperMileLine,  milesBetweenLoads)
	if lowest > temporary[1]:
		secondResult = temporary
		lowest = secondResult[1]
print("This is where I check my fourt round of values")
print(secondResult[0])
print(secondResult[1])
