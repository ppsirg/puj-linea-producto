# product lines modeling and analysis

this repository contains a restriction model for GNU-Prolog that represents a line of products for real state services, also contain a python script to analyse information obtained.

to make it work, run:

```
gprolog --consult-file inmueble.pl >> oth.txt
```

replace oth.txt for any other file, then replace oth.txt in python file and run it, you will get something like:

```
true product model
possible products:  1238976
RF5 designed as variable is variable
RF7 designed as variable is not variable
RF8 designed as variable is variable
RF12 designed as variable is variable
RF22 designed as variable is variable
RF24 designed as variable is variable
RF31 designed as variable is variable
RF32 designed as variable is variable
RF33 designed as variable is variable
RF34 designed as variable is variable
RF35 designed as variable is variable
RF36 designed as variable is variable
RF37 designed as variable is variable
RF41 designed as variable is variable
RF43 designed as variable is variable
RF51 designed as variable is variable
RF52 designed as variable is variable
RF53 designed as variable is variable
RF63 designed as variable is variable
RF72 designed as variable is variable
RF73 designed as variable is variable
RF81 designed as variable is variable
RF92 designed as variable is variable
constant features:  ['F0', 'RF1', 'RF2', 'RF3', 'RF4', 'RF6', 'RF9', 'RF11', 'RF21', 'RF23', 'RF42', 'RF61', 'RF62', 'RF64', 'RF71', 'RF91']
```