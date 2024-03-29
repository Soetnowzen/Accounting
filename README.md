# Accounting
https://open.kattis.com/problems/bokforing

Erika the economist studies economic inequality. Her model starts in a situation where everybody has the same amount of money. After that, people’s wealth changes in various complicated ways.

Erika needs to run a simulation a large number of times to check if her model works. The simulation consists of *N* people, each of whom begins with *O* kroners. Then *Q* events happen, of three different types:

1. An event of type "`SET i x`" means that the *i*th person’s wealth is set to *x* 
2. An event of type "`RESTART x`" means that the simulation is restarted, and everybody’s wealth is set to *x*.
3. An event of type “`PRINT i`” reports the current wealth of the *i*th person.

Unfortunately, Erika’s current implementation is very slow; it takes far too much time to keep track of how much money everybody has. She decides to use her algorithmic insights to speed up the simulation.

## Input
The first line includes two integers *N* and *Q*, where $`1 \leq N \leq 10^6`$ and $`1 \leq Q \leq 2*15^5`$. The following *Q* lines each start with a string that is either “SET”, “RESTART”, or “PRINT”. There is guaranteed to be at least one event of type “PRINT”.

If the string is “SET” then it is followed by two integers *i* and *x* with $`1 \leq i \leq N`$ and $`0 \leq x \leq 10^4`$. If the string is “RESTART” then it is followed by an integer *x* with $`0 \leq x \leq 10^4`$. If the string is “PRINT” then it is followed by an integer *i* with $`1 \leq i \leq N`$.

## Output
For each event of type “PRINT”, write the 
th person’s capital.

### Sample 1
#### Input
```
3 5
SET 1 7
PRINT 1
PRINT 2
RESTART 33
PRINT 1
```

#### Output
```
7
0
33
```

### Sample 2
#### Input
```
5 7
RESTART 5
SET 3 7
PRINT 1
PRINT 2
PRINT 3
PRINT 4
PRINT 5
```

#### Output
```
5
5
7
5
5
```

## Version
Python 3.12.1

## Run command
python -m unittest .\tests\test_accounting.py