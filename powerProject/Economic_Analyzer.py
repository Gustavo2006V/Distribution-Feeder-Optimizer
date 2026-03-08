
def CalculatingCost(lineCurrents, R, numberOfCapacitors, lengthOfLines, CapacitorVar):
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
