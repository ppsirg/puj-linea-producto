# product lines modeling and analysis

this repository contains a restriction model for GNU-Prolog that represents a line of products for real state services, also contain a python script to analyse information obtained.

to make it work, run:

```
gprolog --consult-file inmueble.pl >> oth.txt
```

then create a list variable where all items are variables, validation_code_generators function in python script can make it for you, after that, run model with your variable defined and wait a couple of minutes, and then type a letter to calculate all possible response and wait solver to end.

```
➜  linpro gprolog --consult-file inmueble.pl >> oth.txt
| ?- L = [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _].
| ?- lpinmuebles(L).
a| ?- e%                                                                                      ➜  linpro git
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

this is only suitable for small product line models with a few features, this project only meant to help to make validations in a faster way.


## Usefull resources:

- https://en.wikipedia.org/wiki/Prolog_syntax_and_semantics
- http://www.cs.trincoll.edu/~ram/cpsc352/notes/prolog/factsrules.html
- http://pauillac.inria.fr/~haemmerl/gprolog-rh/doc/manual006.html
- http://www.gprolog.org/manual/html_node/gprolog007.html
- https://scholar.lib.vt.edu/ejournals/JFLP/jflp-mirror/articles/2001/S01-02/JFLP-A01-06.pdf