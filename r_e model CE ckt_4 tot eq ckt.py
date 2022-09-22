import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(fontsize=20)
    d += (L1 := elm.Line().left().dot(open=True).length(2))
    d += (L3 := elm.Line().down().at(L1.start).length(1))
    d += (R1 := elm.Resistor().down().at(L3.start).label('$r_e$'))
    d += (L2 := elm.Line().left().at(R1.end).dot(open=True).length(2))
    d += (H1 := elm.Gap().endpoints(L1.end, L2.end).label(('+', '$V_{be}$', '-')))
    d += (I1 := elm.CurrentLabelInline(direction='in', headwidth=0.15).at(L1.center).right().label('$I_b$').scale(0.1))
    d += (I2 := elm.CurrentLabelInline(direction='in', headwidth=0.15).at(L3.center).down().label('$I_e$', 'bot').scale(0.1))
    d += (S1 := elm.SourceControlledI().up().reverse().at(L3.start).label('$\\beta I_b$'))
    d += (L4 := elm.Line().right().at(S1.end).dot(open=True))
    d += (L5 := elm.Line().right().at(L2.start).dot(open=True))
    d += (H1 := elm.Gap().endpoints(L4.end, L5.end).label(('+', '$V_{ce}$', '-')))