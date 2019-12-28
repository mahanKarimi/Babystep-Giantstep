# Babystep-Giantstep

In group theory, a branch of mathematics, the baby-step giant-step is a meet-in-the-middle algorithm for computing the discrete logarithm. The discrete log problem is of fundamental importance to the area of public key cryptography. >https://en.wikipedia.org/wiki/Baby-step_giant-step

## Example
The discrete logarithm of ``` 5 to base 2 in (Z*11,*) is 4, because 5 is congruent modulo to 2^4 mod 11. ``` 

The discrete logarithm of ``` 3 to base 5 in (Z*2017,*) is 1030, because 3 is congruent modulo to 5^1030 mod 2017. ```

This is because we write the exponent as x = i*m + j. With the algorithm Babystep-Giantstep we find out i and j.


## Unit Test 
To run the unittest run the command in your terminal ``` python -m unittest test.py ``` 

