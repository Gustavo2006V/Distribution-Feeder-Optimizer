# Distribution-Feeder-Optimizer

# Capcitor Placement for optimization
I built a program which simulates a three phase distribution system. 
My program also tries to optimize for the best capacitor loactions.

# Inputs
- Substation voltage is 12.47kv (phase voltage)
- The Kilo VAR value of the capcitor: 200
- Real power for the 3 different loads, the first one is closest to the substation and the last one is the farthest from the substation: 400KW, 500kW, 600KW
- Power Factors for the 3 different loads, the first one is closest to the substation and the last one is the farthest from the substation: .8, .85, .9. All of thse powerfactors are lagging.
- Resistance per mile is .3 ohms
- Indutance per mile is .4j ohms 
- Distance between nodes the first distance is closest to the substation and the last value is farthest from the substation: 2, 1.5, 1.0.
- Capacitor Installtion cost 2000 dollars
- Projected life time for a 200 kilo VAR capcitor is 20 years
- Money per kilo Watt is 10 cents
- Cost per Kilo VAR is 10 dollars
- Hours per year 8760
  
# Description of my computer algorithm 
My program does two distinct things it simulates a 3 phase distribution system and it calculalates the best capacitor location to reduce costs.
I will first describe the means by which I demonstrate how I analyze a 3 phase distribution system with predetermined values, and then the capacitor optimization algorithm.
# Analyzing the 3 phase distribution systsem

1 - I first assume that the node voltages are equivalent to the substation voltage
2 - I then calculate the load currnet by transfoming the power associated with the load to current by getting the complex conjugate of apparent power and diving it by the node voltage
3 - Using these load currents I calcuate the line currents through an iterative process by starting with the node farthest from the substation voltage, and then moving to the lines closest to the substation. I assume that the line current is the sum of the respecitve load current and the line current closest to the line and farthest to the substation voltage. The line current for the line farthest to the substation is the load current.
4 - The node voltages are recalculated, I start from the node closest to the substation voltage and iteratively move gradually to the node farthest from the substation. For the node closest to the node voltage I substract the substation voltage by the voltage drop which is given by multiplying the line current with the total resistance between the substation and the node. I repeat this process but instead of using the substation voltage I use voltage associated with the previous node to get the respetive node voltage.
5 - Repeat the process starting at step 2 and with the newly update node voltages. Repeat until the noad voltages converge.

# Capacitor optimization algorithm

1 - I create a loop which covers all posible nodes in my distribution system and call a function with the node as one of the inputs.
2 - The function calculates the expected cost after 20 years of putting the capacitor parallel to that specific node
3 - I then call the same function within the function iteratively for all the different nodes and calculate the cost taking into account capacitor placements and costs.
4 - All the of the costs of the recursive calls are compared and the one with the lowest overall cost after 20 years is returned, and the associated list of capacitors in parallel to certain loads is also returned.
5 - The amount of recursive calls depends on specific input

# Calculating cost for Capacitor optimization algorithm
I calculate the cost of running the three phase distribution system after 20 years I calculate the power associated with each line, (abs(current)^2 * resistance). I then multiply the power by the the cost of watts per hour (this is a predetermined value), the hours per year, and the number of years(predetermined 20 years). I do the aformentioned process for all the lines in the single phase representation and add all of the costs, and I multiply by three to take into account the fact that this is a 3 phase distribution system. I additionally, divide the overall cost by the square root of 2 to account for the fact that the input voltage and thus, the input current is sinusodial. Furthremore, to the overall cost 

# Results for analyzation of my three phase distribution system
After utilizing the algorithm described in analyzing the 3 phase distribution system my node voltages are 12454, 12444 and 12440, with the first voltage being the node voltage closest to the substation and the voltages that come after are farther away from the substation. My line currents came out as 121.66 + j71.46, 89.27 + j47.73, and finally 40.55 + j18.69, with the first line current being the current closest to the substation and the line currents that come after are farther away from the substation.

# Restults for my capacitor optimization algorithm 
I ran my optimization algorithm with the limitations on the number of recursive calls that it could make, I did this with the limitation of the recusive calls being 1, 2 and 3. 
# Capacitor Optimization optimization limited by only one recursive call
My optimization decided to put the capcitor parallel to third load the overall cost of running the distribution system after 20 years is 937225 dollars
# Capacitor Optimization algorithm limited by two recursive call
My optimization algorithm decided to put the capcitors in parallel to the third and second load, the overall cost of running the three phase distribution system after 20 years came out to be 914971 dollars 
# Capacitor Optimization algorithm limited by two recursive call
My optimization algorithm decided to put the capcitors in parallel to the third and second load the overall cost of running the distribution system after 20 years came out to be 914971 dollars 



