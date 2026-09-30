
# I calculate the cost a 20 year old distribution feeder simulation based on the 
# number of used capacitors the VAR associated with the capacitors; and the heat loss
# based on the line current, length of lines and the Resistance per mile(R).

def cost(lineCurrents, R, numberOfCapacitors, lengthOfLines, CapacitorVar):
	costPerVar = 10 * 1e-3
	capacitorInstallationCost = 2000 + CapacitorVar * costPerVar
	totalInstallationCost = numberOfCapacitors * capacitorInstallationCost
	projectedLifeTime = 20
	totalCost = totalInstallationCost
	wattHrMoney = .0001
	hoursPerYear = 8760

	for i in range(len(lineCurrents)):
		linePower = (pow(abs(lineCurrents[i]),2) * R * lengthOfLines[i] * 3)
		lineCostPerHour = linePower * wattHrMoney 
		totalCost = totalCost + lineCostPerHour * hoursPerYear * projectedLifeTime 
	return totalCost
