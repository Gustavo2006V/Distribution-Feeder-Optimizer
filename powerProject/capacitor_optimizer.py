from Economic_Analyzer import CalculatingCost
from Power import loadCurrents_calculate, lineCurrents_calculate, busVoltages_calculate, checkConvergence_pu
import math

def finalOutput(realPower, powerFactors):
	totalIterations = 100
	iterations = 0
	substationVoltage = 12470
	RperMileLine = .3
	XperMileLine = .4
	voltages = [12470, 12470, 12470]
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
def iterator(realPower, PowerFactors, CapacitorValues, Current, List, Limit, R, lengthOfLines):

	if Current in List or Limit == len(List):
		temporaryList = []
		newList = []
		newList.append(temporaryList)
		newList.append(float('inf'))
		return newList

	listCopy = List.copy()
	listCopy.append(Current)

	powerOfCurrent = realPower[Current]
	powerFactorCurrent = PowerFactors[Current]

	copiedPowerFactors = PowerFactors.copy()

	copiedPowerFactors[Current] = improved_PF(powerOfCurrent, CapacitorValues, copiedPowerFactors[Current])
	lineCurrents = finalOutput(realPower, copiedPowerFactors)
	
	cost = CalculatingCost(lineCurrents, R, len(listCopy), lengthOfLines, CapacitorValues)

	capacitorPlacementCost = []
	capacitorPlacementCost.append(listCopy)
	capacitorPlacementCost.append(cost)
	for i in range(len(realPower)):
		hold = iterator(realPower,copiedPowerFactors, CapacitorValues,i, listCopy, Limit, R , lengthOfLines)
		if hold[1] < capacitorPlacementCost[1]:
			capacitorPlacementCost = hold
	return capacitorPlacementCost
def improved_PF(realPower, capacitorVAR, previousPF):
	apparentPower = realPower/previousPF
	previousImaginaryPower = apparentPower * math.sin(math.acos(previousPF))
	newImaginaryPower = previousImaginaryPower - capacitorVAR
	radiansNewPF = math.atan(newImaginaryPower/realPower)
	return math.cos(radiansNewPF)

