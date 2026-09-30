from Economic_Analyzer import cost
from Power import loadCurrents_calculate, lineCurrents_calculate, busVoltages_calculate, checkConvergence_pu
import math
# I calculate the current along the wire which holds the nodes("lineCurrents"); the nodes are connected to the loads.
# I use the function checkConvergence_pu to check the validity of my results 
def finalOutput(realPower, powerFactors):
	totalIterations = 100
	iterations = 0
	substationVoltage = 7200
	RperMileLine = .3
	XperMileLine = .4
	voltages = [7200, 7200, 7200]
	secondVoltages = [0,0,0]
	milesBetweenLoads = [2,1.5,1]
	loadCurrents = [0,0,0]
	lineCurrents =[0,0,0]

	while not checkConvergence_pu(secondVoltages, voltages,substationVoltage) and totalIterations != iterations:
		iterations = iterations + 1
		loadCurrents = loadCurrents_calculate(realPower, voltages,powerFactors)
		lineCurrents = lineCurrents_calculate(loadCurrents)
		secondVoltages = busVoltages_calculate(RperMileLine, XperMileLine, lineCurrents, substationVoltage, milesBetweenLoads) 
		temporaryVoltages =  voltages
		voltages = secondVoltages
		secondVoltages = temporaryVoltages
	return lineCurrents 
# With this function I iterate over all possible capacitor combinatinos(parallel to the load and associated with 
# a node). I try to find the lowest cost associated with a capacitor combination by comparing the cost of all capacitor combinations. 
# There is a limited ammount of capcitors that be can use given by numberOfAvailCapacitors
# The function returns [capacitor combination, cost(after 20 year analysis)]
def iterator(realPower, PowerFactors, CapacitorVar, Node, List, numberOfAvailCapacitors, Resistanc_P_M, lengthOfLines):
	

	if Node in List or numberOfAvailCapacitors == len(List):
		temporaryList = []
		newList = []
		newList.append(temporaryList)
		newList.append(float('inf'))
		return newList

	listCopy = List.copy()
	listCopy.append(Node)
	powerOfNode = realPower[Node]

	copiedPowerFactors = PowerFactors.copy()

	copiedPowerFactors[Node] = improved_PF(powerOfNode, CapacitorVar, copiedPowerFactors[Node])
	lineCurrents = finalOutput(realPower, copiedPowerFactors)
	
	Cost = cost(lineCurrents, Resistanc_P_M, len(listCopy), lengthOfLines, CapacitorVar)

	lowcapNodesAndCost = []
	lowcapNodesAndCost.append(listCopy)
	lowcapNodesAndCost.append(Cost)

	for Node2 in range(len(realPower)):
		capNodesAndCost = iterator(realPower, copiedPowerFactors, CapacitorVar, Node2, listCopy, numberOfAvailCapacitors, Resistanc_P_M , lengthOfLines)
		if capNodesAndCost[1] < lowcapNodesAndCost[1]:
			lowcapNodesAndCost = capNodesAndCost
	return lowcapNodesAndCost
# Here I calculate the improved power factor based on the value of the imaginary power of the
#  load subtracted by the imaginary power of the capacitor, the real power of the load.
def improved_PF(realPower, capacitorVAR, previousPF):
	apparentPower = realPower/previousPF
	previousImaginaryPower = apparentPower * math.sin(math.acos(previousPF))
	newImaginaryPower = previousImaginaryPower - capacitorVAR
	radiansNewPF = math.atan(newImaginaryPower/realPower)
	return math.cos(radiansNewPF)

