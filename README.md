#### Date Created
30th June 2020

# Generate_UserId
Generate the User Id with the help of first and last name of the user.

### Introduction
In this project we will be generating the userid for the game.
It is being generated with the help of First name ,Last name, A pin number(random number)
and a Number N.

### Constraint to be Followed

1. If first name is longer than last name  set first name as longer name and last name as smaller name
2. If first name is smaller than last name  set first name as smaller name and last name as longer name
3. If both are equal in length then which comes first in alphabatical order would be termed as smaller name.
4. Extract two digits out of pin number with the help of N.
	First digit would be extracted such way that it comes at Nth position from left in the Pin Number.
	Second digit would be Nth Position from right of Pin Number.

### The UserId Generation
userid= "fist letter of longer name"+ "smaller name"+ fisrt digit + second digit

And , atlast toggle the obtained userid (Swap the cases).


#### Example:

1. fist name =Krishan
    last name = Pandey
    pin number =12345678
    N=4
    ##### Explaination:
	since First name is longer in length than last name.
	And extract 4th digit from left and 4th digit from right of the pin number.
	from left = 4
	from right = 5

	userid= KPandey45
	Atlast swap the cases and final userid becomes =kpANDEY45

2. fist name =Kunal
    last name = Pandey
    pin number =98765432
    N=5
    ##### Explaination:
	since First name is smaller in length than last name.
	And extract 5th digit from left and 5th digit from right of the pin number.
	from left = 5
	from right = 6

	userid= PKunal56
	Atlast swap the cases and final userid becomes =pkUNAL56

3.fist name =Kunal
    last name = Kumar
    pin number =98763450
    N=7
    ##### Explaination:
	since First name and last name both are equal in length.
	Then alphabetical order would come in the picture. And hence Last name is smaller and first name is longer 
	as in Kumar m comes first than n in Kunal.

	And extract 7th digit from left and 7th digit from right of the pin number.
	from left = 5
	from right = 8

	userid= KKumar58
	Atlast swap the cases and final userid becomes =kkUMAR58


