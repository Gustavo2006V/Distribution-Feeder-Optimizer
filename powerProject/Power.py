import math
import numpy as np
def loadCurrents_calculate(realPower, voltages, PowerFactors):
	i = 0
	current = []
	for i in range(len(voltages)):
		totalPower = realPower[i] - 1j * (realPower[i]/PowerFactors[i]) * math.sin(math.acos(PowerFactors[i]))
		current.append(np.conj(totalPower/voltages[i]))
		
	return current
def lineCurrents_calculate(loadCurrents):
	i = len(loadCurrents) - 1
	lineCurrents = [1,2,3]
	previousCurrent = 0
	while  i >= 0:
		lineCurrents[i] = loadCurrents[i] + previousCurrent
		previousCurrent = lineCurrents[i]
		i = i -1
	return lineCurrents

def busVoltages_calculate(R, X, lineCurrents, substationVoltage, lengthOfLines):
	busVoltages = []
	i = 0
	previousVoltage = 0
	previousVoltage = substationVoltage
	for i in range(len(lineCurrents)):
		Z = lengthOfLines[i] * (R + 1j * X)
		busVoltages.append(previousVoltage - Z * (lineCurrents[i]))
		previousVoltage = busVoltages[i]
	return busVoltages 

def checkConvergence_pu(voltages_old, voltages_new, V_base, tolerance= .01):
	maxDiff  = 0
	i = 0
	for i in range(len(voltages_old)):
		difference = abs(abs(voltages_old[i]) - abs(voltages_new[i])) / V_base
		if difference > maxDiff:
			maxDiff = difference
	return maxDiff < tolerance 
