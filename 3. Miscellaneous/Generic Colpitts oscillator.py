import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += (Amp := elm.Opamp().label('A', loc='center', fontsize=20))
    d += (L1 := elm.Line().left().at(Amp.in1).length(4))
    d += (L2 := elm.Line().left().at(Amp.in2).length(1))
    d += (L3 := elm.Line().down().at(L1.end).length(4))
    d += (C1 := elm.Capacitor().right().at(L3.end).label('$C_1$'))
    d += (C2 := elm.Capacitor().right().at(C1.end).label('$C_2$'))
    d += (L4 := elm.Line().endpoints(C1.end, L2.end))
    d += (L5 := elm.Line().right().at(Amp.out).length(0.8))
    d += (Lc := elm.Line().right().at(C2.end).length(1))
    d += (L6 := elm.Line().endpoints(L5.end, Lc.end))
    d += (L7 := elm.Line().down().at(C1.start).length(1))
    d += (L8 := elm.Line().down().at(Lc.end).length(1))
    d += (Ind := elm.Inductor().endpoints(L7.end, L8.end).label('L'))
    d += (Dot1 := elm.Dot().at(C1.start))
    d += (Dot2 := elm.Dot().at(C1.end))
    d += (Dot3 := elm.Dot().at(Lc.end))