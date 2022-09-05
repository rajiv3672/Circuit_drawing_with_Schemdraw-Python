import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += (G1 := elm.Ground())
    d += (S1 := elm.SourceSin().up().label('$V_s$\n800m$V_{p-p}$'))
    d += (C1 := elm.Capacitor().right().label('$C_1$\n0.1$\mu$F'))
    d += (R1 := elm.Resistor().at(C1.end).up().label('$R_1$\n56k$\Omega$'))
    d += (R2 := elm.Resistor().at(C1.end).down().label('$R_2$\n12k$\Omega$'))
    d += (L1 := elm.Line().at(C1.end).right())
    d += (Q := elm.BjtNpn(circle=True).right().anchor('base').at(L1.end).label('Q\n2N2222'))
    d += (R3 := elm.Resistor().at(Q.collector).up().label('$R_C$\n2k$\Omega$'))
    d += (L2 := elm.Line().endpoints(R3.end, R1.end))
    d += (R4 := elm.Resistor().at(Q.emitter).down().label('$R_E$\n400$\Omega$'))
    d += (G2 := elm.Ground().at(R4.end))
    d += (G3 := elm.Ground().at(R2.end))
    d += (C2 := elm.Capacitor().right().at(Q.collector).label('$C_1$\n0.1$\mu$F').dot(open=True).label('$V_o$', 'right'))
    d += (L3 := elm.Line().right().at(R3.end).dot(open=True).label('$+V_{cc}$\n10V', 'right'))