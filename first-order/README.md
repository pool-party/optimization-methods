# Homework 1: First order optimization methods

## 1 Task

1. Implement the method of one-dimensional searching: Dichotomy, Gold Ratio and the Fibonacci method.
   Compare them in terms of number of iterations and number of function evaluations
   in terms of varying degrees of precision.
   For each method, be sure to indicate how the section changes to the next iteration.
2. Implement the gradient descent. Select method and linear search procedure.
   Evaluate, how the speed of convergence changes when using different one-step procedures.
3. Analyse the gradient slope trajectory for a number of quadratic functions:
   design two or three different quadratic functions for which the method will differ,
   draw graphs with level lines functions and method trajectories.
   Try to answer the following question:
   How does the behaviour of the method differ depending on the number of features,
   choice of starting point, and strategy, how does the method behave?
   what is the step selection strategy?
4. Investigate how the number of iterations needed for a graded approach to the following two
   parameters must be taken into account in order to ensure consistency:

   1. the number of certainty k ≤ 1 of the approximated function
   2. the dimension of the space n of the approximated variables

   To do this, for the given parameters n and k, approximate in the following way
   a quadratic problem of dimension n with a number of consistency k and negate on it
   a gradual rate with a certain fixed accuracy required.
   Measure the number of iterations T(n, k) that it takes to make the method converge
   (a successful exit according to the stopping criterion).

## 2 Task

Based on the results of the laboratory work a report should be prepared.
The report should include a description of the algorithms you have implemented, a link to the
the implementation, and the required tests and tables.
