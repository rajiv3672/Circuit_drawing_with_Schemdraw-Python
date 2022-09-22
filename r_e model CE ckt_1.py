import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(fontsize=20)
    d += (L1 := elm.Line().left().dot(open=True).label('+', 'left').length(1))
    d += (Q1 := elm.BjtNpn().at(L1.start).right())
    d += (L2 := elm.Line().down().at(Q1.emitter).length(0.5))
    d += (L3 := elm.Line().at(L2.end).left().length(1.75).dot(open=True).label('-', 'left'))
    d += (H1 := elm.Gap().endpoints(L1.end, L3.end).label('$V_{be}$'))
    d += (L4 := elm.Line().up().at(Q1.collector).length(0.7))
    d += (L5 := elm.Line().right().at(L4.end).label('+', 'right').dot(open=True).length(1))
    d += (L6 := elm.Line().right().at(L3.start).label('-', 'right').dot(open=True).length(1))
    d += (I1 := elm.CurrentLabelInline(direction='in', headwidth=0.1).at(Q1.base).label('$I_b$').scale(0.1))
    d += (I2 := elm.CurrentLabelInline(direction='out', headwidth=0.1).at(L2.center).up().label('$I_e$').scale(0.1))
    d += (I3 := elm.CurrentLabelInline(direction='out', headwidth=0.1).at(L4.center).up().label('$I_c$').scale(0.1))
    d += (H2 := elm.Gap().endpoints(L5.end, L6.end).label('$V_{ce}$'))
    d += (Zi := elm.ZLabel(hofst=-0.6).at(L3.center).label('$Z_{in}$').right().linestyle('--'))