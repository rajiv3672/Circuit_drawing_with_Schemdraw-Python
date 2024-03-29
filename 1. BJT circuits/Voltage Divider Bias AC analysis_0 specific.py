import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += (G1 := elm.Ground())
    d += (Lg := elm.Line().at(G1.end).up().length(0.7))
    d += (S1 := elm.SourceSin().up().at(Lg.end).label('$V_s$\n800m$V_{p-p}$'))
    d += (Ru := elm.Resistor().right().at(S1.end).label('$R_s$\n1M$\Omega$'))
    d += (C1 := elm.Capacitor().right().at(Ru.end).label('$C_1$\n0.1$\mu$F'))
    d += (R1 := elm.Resistor().at(C1.end).up().label('$R_1$\n56k$\Omega$'))
    d += (R2 := elm.Resistor().at(C1.end).down().label('$R_2$\n12k$\Omega$'))
    d += (L1 := elm.Line().at(C1.end).right())
    d += (Q := elm.BjtNpn(circle=True).right().anchor('base').at(L1.end).label('Q\n2N2222'))
    d += (Lp := elm.Line().up().at(R1.end).length(0.7))
    d += (R3 := elm.Resistor().at(Q.collector).up().label('$R_C$\n2k$\Omega$'))
    d += (L2 := elm.Line().endpoints(R3.end, Lp.end))
    d += (R4 := elm.Resistor().at(Q.emitter).down().label('$R_E$\n400$\Omega$'))
    d += (G2 := elm.Ground().at(R4.end))
    d += (Ly := elm.Line().down().at(R2.end).length(0.7))
    d += (G3 := elm.Ground().at(Ly.end))
    d += (C2 := elm.Capacitor().right().at(Q.collector).label('$C_2$\n0.1$\mu$F').dot(open=True).label('$V_o$', 'right'))
    d += (L3 := elm.Line().right().at(R3.end).dot(open=True).label('$+V_{cc}$\n10V', 'right'))
    d += (L4 := elm.Line().right().at(Q.emitter).length(1.5))
    d += (Ce := elm.Capacitor().down().at(L4.end).label('$C_E$\n47$\mu$F'))
    d += (Gc := elm.Ground().at(Ce.end))
    d += (Dt1 := elm.Dot().at(C1.end))
    d += (Dt2 := elm.Dot().at(R3.end))
    d += (Dt3 := elm.Dot().at(R3.start))
    d += (Dt4 := elm.Dot().at(R4.start))