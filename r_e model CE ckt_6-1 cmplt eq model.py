import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(fontsize=20)
    d += (L1 := elm.Line().left().dot(open=True).length(2))
    d += (L3 := elm.Line().down().at(L1.start).length(1))
    d += (R1 := elm.Resistor().down().at(L3.start).label('$\\beta r_e$'))
    d += (L2 := elm.Line().left().at(R1.end).dot(open=True).length(2))
    d += (H1 := elm.Gap().endpoints(L1.end, L2.end).label(('+', '$V_{be}$', '-')))
    d += (I1 := elm.CurrentLabelInline(direction='in', headwidth=0.15).at(L1.center).right().label('$I_b$').scale(0.1))
    d += (L4 := elm.Line().length(2).at(R1.end).right())
    d += (S1 := elm.SourceControlledI().reverse().up().label('$\\beta I_b$', 'bot'))
    d += (L5 := elm.Line().right().length(3).at(S1.start).dot(open=True))
    d += (L6 := elm.Line().right().length(3).at(S1.end).dot(open=True))
    d += (H2 := elm.Gap().endpoints(L5.end, L6.end).label(('+', '$V_{ce}$', '-')))
    d += (R2 := elm.Resistor().endpoints(L5.center, L6.center).label('$r_o$', 'bot'))