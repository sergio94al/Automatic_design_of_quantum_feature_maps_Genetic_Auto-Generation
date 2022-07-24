# Automatic design of quantum feature maps: Genetically designed Quantum Kernels

This is the official code of the paper published on August 19, 2021: S. Altares-López, A. Ribeiro, J.J. García-Ripoll, Automatic design
of quantum feature maps, Quantum Science and Technology, vol. 6, no.4, 2021. 

DOI: https://doi.org/10.1088/2058-9565/ac1ab1

In this paper we propose a novel technique that allows the automatic generation of quantum circuits that function as quantum feature maps in QSVM for classification, based on multi-objective genetic algorithms.

<img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Ansatz_build.png" width="400" height="250">


## Genetic Quantum Feature Maps: Technique

<img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/General_tech.png" width="600" height="500">

The goal of the technique is to achieve the quantum circuit that provides the best test data accuracy, as well as the smallest ansatz size. As the objective of the fitness function is the test accuracy, we force the circuit to be robust and there is no overfitting. 

Taking into account the ansatz size, our goal is to minimize it as much as possible in order to have solutions that avoid expressibility problems. In addition, we penalize the occurrence of CNOT (entangling gates), in order to achieve solutions with lower computational cost and quantum-inspired solutions.

## Genetic Algorithms

These are algorithms allow the exploration of large solution spaces in order to find the most optimal or closest solutions, since the methodology is meta-heuristic.

<img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/GA.png" width="450" height="300">

### Step 1. 
A starting population is created -Initial population. En nuestro sistema son cadenas binarias.
### Step 2. 
This population is evaluated in a fitness function. The output of this function will determine whether the individual is accurate for the given problem or not. In the proposed technique, the binary strings are converted into quantum circuits qhich will act as feature maps.
### Step 3. 
We select the best individuals. We apply genetic operators of crossover and mutation, generating new individuals. The mutation operator allows us to reach other points in the search space since it allows us to avoid local minima, making the search for the best solution more efficient.
### Step 4. 
The process is repeated until convergence or when stop conditions are achieved.

## References

S. Altares-López, A. Ribeiro, J.J. García-Ripoll, Automatic design of quantum feature maps, Quantum Science and Technology, vol. 6, no.4, 2021. https://doi.org/10.1088/2058-9565/ac1ab1
