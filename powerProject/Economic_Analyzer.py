
def CalculatingCost(lineCurrents, R, paybackYears, numberOfCapacitors, budgetInstallation, lengthOfLines):
	totalInstallationCost = numberOfCapacitors * 5000
	if (budgetInstallation < totalInstallationCost):
		return float('inf')
	totalCost = totalInstallationCost
	kilowattHrMoney = .10
	wattHrMoney = kilowattHrMoney/1000
	hoursPerYear = 8760

	for i in range(len(lineCurrents)):
		linePower = pow(abs(lineCurrents[i]),2) * R * lengthOfLines[i] * 3
		lineCostPerHour = linePower * wattHrMoney 
		totalCost = totalCost + lineCostPerHour * hoursPerYear * paybackYears
	return totalCost
