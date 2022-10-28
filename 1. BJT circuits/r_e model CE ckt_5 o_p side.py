import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(fontsize=30)
    d += (L1 := elm.Line().right().dot(open=True).length(1))
    d += (S1 := elm.SourceControlledI().down().at(L1.start).label('$\\beta I_b$'))
    d += (L2 := elm.Line().right().at(S1.end).dot(open=True).length(1))