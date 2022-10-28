import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(fontsize=20)
    op = (elm.Opamp().right().label('741', loc='center', ofst=0)
                 .label('1', 'n1', fontsize=9, ofst=(-.1, -.25), halign='right', valign='top')
                 .label('5', 'n1a', fontsize=9, ofst=(-.1, -.25), halign='right', valign='top')
                 .label('4', 'vs', fontsize=9, ofst=(-.1, -.2), halign='right', valign='top')
                 .label('7', 'vd', fontsize=9, ofst=(-.1, .2), halign='right', valign='bottom')
                 .label('2', 'in1', fontsize=9, ofst=(-.1, .1), halign='right', valign='bottom')
                 .label('3', 'in2', fontsize=9, ofst=(-.1, .1), halign='right', valign='bottom')
                 .label('6', 'out', fontsize=9, ofst=(-.1, .1), halign='left', valign='bottom'))
    d += op
    d += (l0 := elm.Line().at(op.in1).left().length(0.5))
    d += (Ci := elm.Capacitor().at(l0.end).left().label('$C_i$'))
    d += (L1 := elm.Line().at(op.in2).left().length(0.2))
    d += (L2 := elm.Line().at(L1.end).down())
    d += (G1 := elm.Ground().at(L2.end))
    d += (l1 := elm.Line().at(l0.end).up().length(1.35))
    d += (l2 := elm.Line().at(op.out).right().length(0.2))
    d += (L3 := elm.Line().at(l2.end).up().length(2))
    d += (L4 := elm.Line().at(L3.start).right())

    d += (Rf := elm.Resistor().endpoints(l1.end, L3.end).label('$R_f$'))
    d += (Dot1 := elm.Dot(open=True).at(Ci.end).label('$V_i$'))
    d += (Dot2 := elm.Dot(open=True).at(L4.end).label('$V_o$'))
    d += (Dot3 := elm.Dot().at(l2.end))
    d += (Dot4 := elm.Dot().at(l0.end))
    