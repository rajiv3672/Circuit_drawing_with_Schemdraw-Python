import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(fontsize=30)
    d += (L1 := elm.Line().left().dot(open=True).label('$v_s$', 'left'))
    d += (C1 := elm.Capacitor().right().at(L1.start).label('$C_1$').dot())
    d += (R1 := elm.Resistor().down().at(C1.end).label('$R_i=R_1||R_2||$$\\beta r_e$'))# Using \beta causes problem because \b is a library thing so I used \\beta.
    d += (G1 := elm.Ground().at(R1.end))