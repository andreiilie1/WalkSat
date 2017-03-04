from random import randint

N = int(input("Insert number of variables"))
M = int(input("Insert number of clauses"))

# {0, ... , N - 1} represent the literals {p0, ... , p(N - 1)}
# {N, ... , 2 * N - 1} represent the literals {not p0, ... , not p(N - 1)}

# Check if clause i is satisfied by the curreny assignment
def isSatisfied(i) :
	clause = CNF[i]
	x = clause[0]
	y = clause[1]
	if(getValue(x) == 1 or getValue(y) == 1):
		return True
	else:
		return False

# Get the value of the x-th literal
def getValue(x) :
	if(x < N):
		return assignment[x]
	else:
		return 1 - assignment[x - N]

# Print the i-th literal in the form p(i-1)
def printLiteral(i):
	if(i < N):
		print("p", end='')
		print(i, end='')
	else:
		print("!p", end='')
		print(i - N, end = '')

# Display the CNF in a visually nice way
def displayCNF() :
	for i in range(M):
		print("(",end = '')
		printLiteral(CNF[i][0])
		print(" v ",end = '')
		printLiteral(CNF[i][1])
		print(")",end = '')
		if(i < M - 1):
			print(" ^ ",end = '')

CNF = []

# Generate randomly the 2-CNF
for i in range(M) :
	literal1 = randint(0, 2 * N - 1)
	literal2 = randint(0, 2 * N - 1)
	CNF.append((literal1, literal2))

# Start with a random assignment
assignment = []
for i in range(N) :
	assignment.append(randint(0,0))

displayCNF()
print()
print(assignment)

satisfied = False
steps = 0

# Probability to get wrong UNSAT is < 1 / (2 ^ ct)
ct = 10
MAX = 2 * N * N * ct

# While there is no satisfying assignment and there are no more than MAX steps, pick an unsastisfied clause
# and flip one of its literals randomly
while(satisfied == False and steps < MAX):
	index = 0 
	found = False
	while(index < M and found == False):
		if(isSatisfied(index) == False):
			found = True
		else:
			index = index + 1
	if(found == False): 
		satisfied = True
	else:
		steps = steps + 1
		pickVar = randint(0,1)
		assignment[CNF[index][pickVar] % N] = 1 - assignment[CNF[index][pickVar] % N]


if(steps == MAX):
	print("UNSAT")
else:
	print(assignment)
