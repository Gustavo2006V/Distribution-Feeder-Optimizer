from Power import loadCurrents_calculate, lineCurrents_calculate, busVoltages_calculate, checkConvergence_pu
from capacitor_optimizer import iterator
from Economic_Analyzer import cost
import math

maxIterations = 100
iterations = 0
substationVoltage = 7200
#Resistance per Mile
Resistance_P_M = .3
#Reactance per Mile
Reactance_P_M = .4
voltages = [7200, 7200, 7200]
secondVoltages = [0,0,0]
realPower = [400000, 600000, 500000]
realPower_Per_phase = [p / 3 for p in realPower]
powerFactors = [.8,.85, 0.9]
milesBetweenLoads = [2,1.5,1.0]
loadCurrents = [0,0,0]
lineCurrents =[0,0 ,0]
capacitorVAR = 200000/3
# In this while funciton I try to find the current along the wire which touches the nodes("lineCurrents"); 
# the nodes are connected to the loads. I use the line currents to find the bus voltages. I use convergence to 
# find the correct values. After 100 iterations if it does not converge I conclude nonconvergence.
while not checkConvergence_pu(secondVoltages, voltages,substationVoltage, 1e-5 ) and maxIterations >= iterations:
	loadCurrents = loadCurrents_calculate(realPower_Per_phase, voltages,powerFactors)
	lineCurrents = lineCurrents_calculate(loadCurrents)
	secondVoltages = busVoltages_calculate(Resistance_P_M, Reactance_P_M, lineCurrents, substationVoltage, milesBetweenLoads) 
	temporaryVoltages =  voltages
	voltages = secondVoltages
	secondVoltages = temporaryVoltages
	iterations = iterations + 1
if(maxIterations < iterations):
	print("The values did not converge")
print("This is where I dcheck my values (line currents)")

print(lineCurrents[0])
print(lineCurrents[1])
print(lineCurrents[2])
print("This is where I check my voltage values, (bus voltages)")
print(abs(voltages[0]))
print(abs(voltages[1]))
print(abs(voltages[2]))

noCapacitorCosts = cost(lineCurrents, Resistance_P_M, 0, milesBetweenLoads, 0)
print("The cost for no capacitor placement after a 20 year period is")
print(noCapacitorCosts)
i = 0
lowestCost = float('inf')
lowCostandCapNodes = []
# Here I check all possible capacitor combinations and pick the combination with the lowest cost. 
# The number of maximum possible capacitors is one.
for i in range(len(voltages)):
	empty = []
	CostAndCapNodes = iterator(realPower_Per_phase, powerFactors, capacitorVAR, i, empty, 1 ,Resistance_P_M, milesBetweenLoads)
	if lowestCost > CostAndCapNodes[1]:
		lowCostandCapNodes = CostAndCapNodes
		lowestCost = lowCostandCapNodes[1]

print("The cost for one capacitor after a 20 year period with an optimized placement is (and the location of the capacitors)")
print(lowCostandCapNodes[0])
print(lowCostandCapNodes[1])

i = 0
lowestCost = float('inf')
lowCostAndCapNodes = []
# Here I check all possible capacitor combinations and pick the combination with the lowest cost. 
# The number of maximum possible capacitors is two.
for i in range(len(voltages)):
	empty = []
	CostAndCapNodes = iterator(realPower_Per_phase, powerFactors, capacitorVAR, i, empty, 2, Resistance_P_M,  milesBetweenLoads)
	if lowestCost > CostAndCapNodes[1]:
		lowCostAndCapNodes = CostAndCapNodes
		lowestCost = CostAndCapNodes[1]
print("The cost for two capacitors after a 20 year period with a optimized placements is (and the location of the capacitors)")
print(lowCostAndCapNodes[0])
print(lowCostAndCapNodes[1])
