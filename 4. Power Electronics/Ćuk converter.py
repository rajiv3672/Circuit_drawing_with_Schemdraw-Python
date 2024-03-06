import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(fontsize=20)

    d += (S1 := elm.SourceV().up().label(['-', '$V_S$', '+'], loc='top'))
    d += (L1 := elm.Line().right().at(S1.end).length(0.5))
    d += (sw1 := elm.Button().right().flip().at(L1.end).label('Switch'))
    d += (Ind1 := elm.Inductor().down().at(sw1.end).label('L'))
    d += (D1 := elm.Diode(fill=True).right().reverse().at(sw1.end).label('D'))
    d += (C1 := elm.Capacitor().down().at(D1.end).label('C'))
    d += (L2 := elm.Line().endpoints(Ind1.end, C1.end))
    d += (L3 := elm.Line().right().at(C1.start))
    d += (Rl := elm.Resistor().down().at(L3.end).label('$R_L$', loc='top').label(['-', '$V_o$', '+'], loc='bot'))
    d += (L4 := elm.Line().endpoints(Rl.end, C1.end))
    d += (L5 := elm.Line().endpoints(Ind1.end, S1.start))
    d += (i1 :=  elm.CurrentLabel(top=False).reverse().at(Ind1).label('$i_L$').color('royalblue'))
    d += (i2 :=  elm.CurrentLabel(top=False).reverse().at(D1).label('$i_D$').color('royalblue'))
    d += (i3 :=  elm.CurrentLabel(top=False).at(C1).label('$i_C$').color('royalblue'))
    d += (Dt1 := elm.Dot().at(Ind1.start))
    d += (Dt2 := elm.Dot().at(Ind1.end))
    d += (Dt3 := elm.Dot().at(C1.start))
    d += (Dt4 := elm.Dot().at(C1.end))