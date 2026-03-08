# Distribution-Feeder-Optimizer
# Capacitor Placement for Optimization

I built a program which simulates a three phase distribution system. My program also tries to optimize for the best capacitor locations

# Assumptions

-The distribution feeder is assumed to be balanced, so the system is represented using a single phase equivalent model.
-All loads are assumed to be constant power loads.
-The impedance of each line segment is assumed to be uniform per mile.
-Capacitors are modeled as ideal reactive power injections placed in parallel with the load.
-The substation voltage is assumed to remain constant at 12.47 kV.
-Line losses are calculated using abs(I)^2 * R

# Inputs
-Substation voltage is 12.47 kV (phase voltage)
-The kilo VAR value of the capacitor: 200
-Real power for the 3 different loads, the first one is closest to the substation and the last one is the farthest from the substation: 400 kW, 600 kW, 500 kW
-Power factors for the 3 different loads, the first one is closest to the substation and the last one is the farthest from the substation: 0.8, 0.85, 0.9. All of these power factors are lagging.
-Resistance per mile is 0.3 ohms
-Inductance per mile is 0.4j ohms
-Distance between nodes, the first distance is closest to the substation and the last value is farthest from the substation: 2, 1.5, 1.0 miles
-Capacitor installation cost: 2000 dollars
-Projected lifetime for a 200 kilo VAR capacitor is 20 years
-Money per kilowatt hour is 10 cents
-Cost per kilo VAR is 10 dollars

Hours per year: 8760

# Description of my computer algorithm

My program does two distinct things. It simulates a three phase distribution system and it calculates the best capacitor location to reduce costs.
I will first describe the means by which I analyze a three phase distribution system with predetermined values, and then I will describe the capacitor optimization algorithm.

# Analyzing the 3 phase distribution system

1 - I first assume that the node voltages are equivalent to the substation voltage.
2 - I then calculate the load current by transforming the power associated with the load to current by getting the complex conjugate of apparent power and dividing it by the node voltage.
3 - Using these load currents I calculate the line currents through an iterative process by starting with the node farthest from the substation voltage and then moving to the lines closest to the substation. I assume that the line current is the sum of the respective load current and the line current closest to the line and farthest from the substation voltage. The line current for the line farthest from the substation is simply the load current.
4 - The node voltages are recalculated. I start from the node closest to the substation voltage and iteratively move gradually to the node farthest from the substation. For the node closest to the substation voltage I subtract the substation voltage by the voltage drop, which is given by multiplying the line current with the total impedance between the substation and the node. I repeat this process, but instead of using the substation voltage I use the voltage associated with the previous node to get the respective node voltage.
5 - I repeat the process starting at step 2 with the newly updated node voltages. This process is repeated until the node voltages converge.

# Capacitor optimization algorithm

1 - I create a loop which covers all possible nodes in my distribution system and call a function with the node as one of the inputs.
2 - The function calculates the expected cost after 20 years of putting the capacitor in parallel with that specific node.
3 - I then call the same function within the function iteratively for all the different nodes and calculate the cost while taking into account capacitor placements and costs.
4 - All of the costs of the recursive calls are compared and the one with the lowest overall cost after 20 years is returned. The associated list of capacitors placed in parallel with certain loads is also returned.
5 - The amount of recursive calls depends on the specific input.

# Calculating cost for the capacitor optimization algorithm

I calculate the cost of running the three phase distribution system after 20 years. I calculate the power loss associated with each line using the equation:
P_loss = |I|²R
where I is the magnitude of the line current and R is the resistance of the line.
I then multiply the power loss by the cost of electricity per kilowatt hour, the number of hours per year, and the number of years (20 years). I do the aforementioned process for all the lines in the single phase representation and add all of the costs. I then multiply the total cost by three to take into account the fact that this is a three phase distribution system.
Finally, I add the cost of installing the capacitors as well as the cost associated with the reactive power rating of the capacitors.

# Results for analysis of my three phase distribution system

After utilizing the algorithm described in analyzing the three phase distribution system, my node voltages are:
12454 V, 12444 V, and 12440 V,
with the first voltage being the node voltage closest to the substation and the voltages that come after being farther away from the substation.
My line currents came out as:
121.66 + j71.46
89.27 + j47.73
40.55 + j18.69
with the first line current being the current closest to the substation and the line currents that come after being farther away from the substation.

# Results for my capacitor optimization algorithm
I ran my optimization algorithm with limitations on the number of recursive calls that it could make. I did this with limitations of 1, 2, and 3 recursive calls.

# Capacitor optimization limited by only one recursive call
My optimization decided to put the capacitor in parallel with the third load. The overall cost of running the distribution system after 20 years is:

804800 dollars.

# Capacitor optimization limited by two recursive calls

My optimization algorithm decided to put capacitors in parallel with the third and second loads. The overall cost of running the three phase distribution system after 20 years came out to be:

741777 dollars.
