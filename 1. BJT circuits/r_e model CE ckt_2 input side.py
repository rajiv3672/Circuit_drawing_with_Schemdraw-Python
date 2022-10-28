import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(fontsize=30)
    d += (L1 := elm.Line().left().dot(open=True).length(2))
    d += (L3 := elm.Line().down().at(L1.start).length(1))
    d += (D1 := elm.Diode().down().at(L3.start))
    d += (L2 := elm.Line().left().at(D1.end).dot(open=True).length(2))
    d += (H1 := elm.Gap().endpoints(L1.end, L2.end).label(('+', '$V_{be}$', '-')))
    d += (I1 := elm.CurrentLabelInline(direction='in', headwidth=0.15).at(L1.center).right().label('$I_b$').scale(0.1))
    d += (I2 := elm.CurrentLabelInline(direction='in', headwidth=0.15).at(L3.center).down().label('$I_e$', 'bot').scale(0.1))