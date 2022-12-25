import schemdraw
import schemdraw.elements as elm

#Guide: If there are Three wires in a junction and there is no dot then there is no junction
with schemdraw.Drawing() as d:
    
    d += (C1 := elm.Capacitor().right().label('$C_i$\n$1\mu F$'))
    d += (R1 := elm.Resistor().at(C1.end).up().label('$R_1$\n$100k\Omega$'))
    d += (R2 := elm.Resistor().at(C1.end).down().label('$R_2$\n$18k\Omega$'))
    d += (L1 := elm.Line().at(C1.end).right())
    d += (Q := elm.BjtNpn(circle=True).right().anchor('base').at(L1.end).label('Q\n2N2222'))
    d += (Lp := elm.Line().up().at(R1.end).length(0.7))
    d += (R3 := elm.Resistor().at(Q.collector).up().label('$R_C$\n$10k\Omega$'))
    d += (L2 := elm.Line().endpoints(R3.end, Lp.end))
    d += (R4 := elm.Resistor().at(Q.emitter).down().label('$R_E$\n$1k\Omega$'))
    d += (G2 := elm.Ground().at(R4.end))
    d += (Ly := elm.Line().down().at(R2.end).length(0.7))
    d += (G3 := elm.Ground().at(Ly.end))
    d += (C2 := elm.Capacitor().right().at(Q.collector).label('$C_o$\n$1\mu F$'))
    d += (L3 := elm.Line().right().at(R3.end).dot(open=True).label('$+V_{cc}$\n$10V$', 'right'))
    d += (L4 := elm.Line().right().at(C2.end))
    d += (I1 := elm.Inductor().down().at(L4.start).label('$L_1$\n $1mH$'))
    d += (C3 := elm.Capacitor().down().at(L4.end).label('$C_1$\n$0.01\mu F$'))
    d += (C4 := elm.Capacitor().down().endpoints(I1.end, C3.end).label('$C_2$\n$0.011\mu F$'))
    d += (G4 := elm.Ground().at(C3.end))
    d += (L5 := elm.Line().down().at(I1.end))
    d += (L6 := elm.Line().down().at(C1.start).length(5.3))
    d += (L7 := elm.Line().endpoints(L5.end, L6.end))
    d += (L8 := elm.Line().right().at(C3.start).dot(open=True).label('$V_{out}$'))
    d += (supernode := elm.EncircleBox([I1, C3, C4]).linestyle('--').linewidth(1).color('red'))
    #Wire juctions are denoted bby dots.
    d += (Dt1 := elm.Dot().at(I1.end))
    d += (Dt2 := elm.Dot().at(I1.start))
    d += (Dt3 := elm.Dot().at(C3.end))
    d += (Dt4 := elm.Dot().at(C1.end))
    d += (Dt5 := elm.Dot().at(R3.end))