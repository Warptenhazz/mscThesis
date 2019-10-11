import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import random 
import operator
import matplotlib.pylab as plt

overallfitnessGrupal = {}
#this procedure generate a dict with 40 items
def generateRules(): 
	rules = {} #all rules of an single agent
	for i in range(40): #create 40 rules per agent
		a = {} #create only one rule 
		rules[i] = a #fill all the rules, for a total of 40
		for j in range(30):
			a[j] = random.randint(0,1)
	return rules

def addRule(poolRules,rule,position):
	newRule = {}
	newRule = dict(rule)
	poolRules[position] = newRule
	return poolRules

#function for calculate the fitness of a rule according to a pool
def calculateFitness(generatedRules):
	fit = {} 
	for key, value in generatedRules.iteritems(): #nid to select only one rule from the pool of 40
		numberOne = 0 #count the number of ones in each rule
		for key1, value1 in value.iteritems(): #value nid to be a dict
			if value1 == 1: #evaluate if an item of a rules is 1 
				numberOne += 1 #add to the auxiliar variable
		fitness = numberOne/float(30) #calculate the fitness 
		fit[key] = fitness
		numberOne = 0 #reset the number of ones per rule
		fitness = 0 #reset the fitness of each rule
	#print "rules with their fitness " + str((fit,generatedRules))
	return (fit,generatedRules)

def bestRule(iteration,fitnessRule): #nid to return a collection of dicts with the fitness and the rules; not only one rule
	x = fitnessRule[0] #de first positions are extracted, the fitness
	sorted_x = sorted(x.items(), key=operator.itemgetter(1)) #then, the fitness are sorted by 
	sorted_x.reverse() #ordered by the major
	firstRule = sorted_x[0][0] #the first rule with the relative fitness
	ruleSelected = {}
	overallfitnessGrupal[iteration] = sorted_x[0][1]
	for key, value in fitnessRule[1].iteritems():
		if key == firstRule:
			ruleSelected = dict(value)
	return ruleSelected #return a dict with the selected rule


#-%-%-%--%-%-%--%-%-%--%-%-%--%-%-%--%-%-%--%-%-%- G E N E T I C -%-%-%--%-%-%--%-%-%--%-%-%--%-%-%--%-%-%--%-%-%--%-%-%-
#-%-%-%--%-%-%--%-%-%--%-%-%--%-%-%--%-%-%- O P E R A T I O N S -%-%-%--%-%-%--%-%-%--%-%-%--%-%-%--%-%-%--%-%-%--%-%-%-

#each time a rule enter to any genetic operation, de rule nid to bi copied for
#not be modified by de operation
#genxx = {} #dis one ned to be modified/created by the best rule by iterations
#for i in range(11):
#	genxx[i] = random.randint(0,1) #create the rule
#gen = dict(genxx) #copy de rule into another dict

#this part is working 
#nid one rule
def mutation(gen): 
	#prob of mutation
	probMutation = 0.5
	for key, value in gen.iteritems():
		coin = random.randint(1,21)*0.5
		if coin <= probMutation:
			if value == 1:
				gen[key] = 0
			if value == 0:
				gen[key] = 1
		else:
			gen[key] = value 
	genMutation = dict(gen)
	return genMutation

#dis is generated random each time
#its used in the crossover operation
gen1 = {}
for i in range(11):
	gen1[i] = random.randint(0,1) #random rule
#nid 2 rules

def crossover(gen1,gen2):
	k = random.randint(1,10)
	for key1, value1 in gen1.iteritems():
		for key2, value2 in gen2.iteritems():				
			if key1 <= k and  key2 <= k:
				if key1 == key2:
					gen1[key1] = value2
					gen2[key2] = value1
	crossoverRule = {}
	crossoverRule = dict(gen1)
	return crossoverRule


#the first stage of the operations, like the inizialitons of de shit
print("INITIALIZATION OF THE GROUPAL ALGORITHM")
generation = 0
proc1 = generateRules()
proc2 = calculateFitness(proc1)
while generation < 5000:
	#if generation%100 == 0:
		#when manipulating the genetic operations, the initial operations nid to be changued by the rules generated
		#GENETIC OPERATION: MUTATION
		proc3 = bestRule(generation,proc2)
		goMutation = mutation(proc3)
		#NEW GENERATION CREATED
		add1 = addRule(proc1,goMutation,40+generation)
		proc4 = calculateFitness(add1)
		proc5 = bestRule(generation,proc4)
		#GENETIC OPERATION: CROSSOVER
		goCrossover = crossover(proc5,gen1)
		#NEW GENERATION CREATED
		add2 = addRule(proc1,goCrossover,41+generation)
		proc6 = calculateFitness(add2)
		generation += 1 
	#print "Iteration Number --> " + str(generation)


fitListGrupal = sorted(overallfitnessGrupal.items()) # sorted by key, return a list of tuples
x1, y1 = zip(*fitListGrupal) # unpack a list of pairs into two tuples
print("Graph generated")
plt.plot(x1, y1, label = "Grupal")



















