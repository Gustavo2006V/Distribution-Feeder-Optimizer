# Distribution-Feeder-Optimizer

# Capcitor Placement for optimization
I built a program which simulates a three phase distribution system. 
My program also tries to optimize for the best capacitor loactions.

# Inputs
- Substation voltage is 12.47kv
- The Kilo VAR value of the capcitor: 200
- Real power for the 3 different loads, the first one is closest to the substation and the last one is the farthest from the substation: 400KW, 500kW, 600KW
- Power Factors for the 3 different loads, the first one is closest to the substation and the last one is the farthest from the substation: .8, .85, .9. All of thse powerfactors are obviously lagging.
- Resistance per mile is .3 ohms
- Indutance per mile is .4j ohms 
- Distance between nodes the first distance is closest to the substation and the last value is farthest from the substation: 20, 15, 10.
- Capacitor Installtion cost 2000 dollars
- Projected life time for a 200 kilo VAR capcitor.
- Money per kilo Watt is 10 cents
- Cost per Kilo VAR is 10 dollars
- Hours per year 8760
# Description of my algorithm 
My program does two distinct things it simulates a 3 phase distribution system and it calculalates the best capacitor location to reduce costs.
I will first describe the means by which I demonstrate how I analyze a 3 phase distribution system with predetermined values.
# Analyzing a 3 phase distribution systsem
1 - I first assume that the node voltages are equivalent to the substation voltage
2 - I then calculate the load currnet by transfoming the power of the load to current by getting the complex conjugate of apparent power and diving it by the node voltage
3 - Using these load currents I calcuate the line currents through an iterative process by starting with the node farthest from the substation voltage, and then moving to the lines closest to the substation. I assume that the line current is the sum of the respecitve load current and the line current closest to the line and farthest to the substation voltage. The currents for the line farthest to the substation is the load current.
4 -   
