import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(fontsize=15)
    op = (elm.Opamp().label('741', loc='center', ofst=0).flip())

    d += op
    d += (S1 := elm.Line().at(op.vd).down().length(0.5).label('$+V_{CC}$', loc='left').dot(open=True))
    d += (S2 := elm.Line().at(op.vs).up().length(0.5).label('$-V_{EE}$', loc='right').dot(open=True))
    d += (L1 := elm.Line().at(op.in2).left().length(1).label('$V_{in}$', loc='left').dot(open=True))
    d += (L2 := elm.Line().at(op.in1).left().length(0.5))
    d += (L3 := elm.Line().at(L2.end).down().length(2).dot())
    d += (R1 := elm.Resistor().at(L3.end).down().label('$R_1$', loc='top'))
    d += (G1 := elm.Ground().at(R1.end))
    d += (R2 := elm.Resistor().at(L3.end).right().label('$R_2$', loc='bot'))
    d += (L4 := elm.Line().at(op.out).right().length(1.5))
    d += (Q1 := elm.BjtNpn(circle=True).at(L4.end).anchor('base'))
