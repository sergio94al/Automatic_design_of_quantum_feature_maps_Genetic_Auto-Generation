# Automatic-design-of-quantum-feature-maps

This is the official code of the paper published on August 19, 2021: S. Altares-López, A. Ribeiro, J.J. García-Ripoll, Automatic design
of quantum feature maps, Quantum Science and Technology, vol. 6, no.4, 2021. 

DOI: https://doi.org/10.1088/2058-9565/ac1ab1

In this paper we propose a novel technique that allows the automatic generation of quantum circuits that function as quantum feature maps in QSVM for classification, based on multi-objective genetic algorithms.

## Genetic Quantum Feature Maps: Objetives

The goal of the technique is to achieve the quantum circuit that provides the best test data accuracy, as well as the smallest ansatz size. As the objective of the fitness function is the test accuracy, we force the circuit to be robust and there is no overfitting. 

Taking into account the ansatz size, our goal is to minimize it as much as possible in order to have solutions that avoid expressibility problems. In addition, we penalize the occurrence of CNOT (entangling gates), in order to achieve quantum-inspired solutions.
