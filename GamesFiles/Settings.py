# Display settings
XDisplay = 500
YDisplay = 500

# Simulation settings
AmountCreatures = 1000
MaxStep = 500
Xsafecenter = 0.5*XDisplay
Ysafecenter = 0.5*YDisplay
SafeZoneRadius = 100
possibilities = ['idle','up','down', 'left', 'right']
ScenarioStep= 1000
# Percentiles for specifications for the childs
Clones = 0.2
Mutated = 0.7
Random = 0.1
BestPerformingTotal = 25
#  Determines how much the mutation is and how likely it is to occur
MutationSize = (-0.2, 0.2)
MutationRate = 0.05