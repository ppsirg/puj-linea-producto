% cargar archivo por defecto compilandolo con: 
% gprolog --consult-file inmueble.pl
% si se desea tener en un archivo de texto el resultado, correr:
% gprolog --consult-file inmueble.pl >> oth.txt
% de esta manera oth.txt puede usarse para los analisis encontrados en verifications.py
lpinmuebles(L):-
L = [F0, RF1, RF2, RF3, RF4, RF5, RF6, RF7, RF8, RF9, RF11, RF12, RF21, RF22, RF23, RF24, RF31, RF32, RF33, RF34, RF35, RF36, RF37, RF41, RF42, RF43, RF51, RF52, RF53, RF61, RF62, RF63, RF64, RF71, RF72, RF73, RF81, RF91, RF92],
fd_domain(L, 0, 1),
F0 #= 1,
%publicidad
RF1 #= F0,
RF11 #= RF1,
RF12 #=< RF1,
%contratacion
RF2 #= F0,
RF21 #= RF2,
RF22 #=< RF2,
RF23 #= RF2,
RF24 #=< RF2,
RF24 #==> RF23,
%recaudos
RF3 #= F0,
RF31 #=< RF3,
RF32 #=< RF3,
RF33 #=< RF3,
RF34 #=< RF3,
RF35 #=< RF3,
RF36 #=< RF3,
RF37 #=< RF3,
1 #=< RF31 + RF32 + RF33 + RF34 + RF35 + RF36 + RF37,
RF31 + RF32 + RF33 + RF34 + RF35 + RF36 + RF37 #=< 7,
%gestion legal
RF4 #= F0,
RF41 #=< RF4,
RF42 #= RF4,
RF43 #=< RF4,
%procesos administrativos
RF5 #=< F0,
RF51 #=< RF5,
RF52 #=< RF5,
RF53 #=< RF5,
%mensajeria
RF6 #= F0,
RF61 #= RF6,
RF62 #= RF6,
RF63 #=< RF6,
RF64 #= RF6,
%consultas
RF7 #=< F0,
RF71 #= RF7,
RF72 #=< RF7,
RF73 #=< RF7,
RF72 + RF73 #=< 1,
%facturacion
RF8 #=< F0,
RF81 #=< RF8,
%seguridad
RF9 #= F0,
RF91 #= RF9,
RF92 #=< RF9,
%restriccion dificil de graficar
RF92 #=< RF34 + RF35 + RF36,
RF34 + RF35 + RF36 #=< 3,
fd_labeling(L).