import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d.config(fontsize=15)
    op = (elm.Opamp().label('741', loc='center', ofst=0)
                 .label('1', 'n1', fontsize=9, ofst=(-.1, -.25), halign='right', valign='top')
                 .label('5', 'n1a', fontsize=9, ofst=(-.1, -.25), halign='right', valign='top')
                 .label('4', 'vs', fontsize=9, ofst=(-.1, -.2), halign='right', valign='top')
                 .label('7', 'vd', fontsize=9, ofst=(-.1, .2), halign='right', valign='bottom')
                 .label('2', 'in1', fontsize=9, ofst=(-.1, .1), halign='right', valign='bottom')
                 .label('3', 'in2', fontsize=9, ofst=(-.1, .1), halign='right', valign='bottom')
                 .label('6', 'out', fontsize=9, ofst=(-.1, .1), halign='left', valign='bottom'))
    d += op
    d += (L1 := elm.Line().at(op.in1).left().length(0.3).dot(open=True).label('Inverting input', 'left'))
    d += (L2 := elm.Line().at(op.in2).left().length(0.3).dot(open=True).label('Non-inverting input', 'left'))
    d += (L3 := elm.Line().at(op.vs).down().length(0.5).dot(open=True).label('$-V_{EE}$', 'left'))
    d += (L4 := elm.Line().at(op.n1a).down().length(0.5).dot(open=True).label('Offset Null', 'left'))
    d += (L5 := elm.Line().at(op.n1).down().length(0.5).dot(open=True).label('Offset Null', 'left'))
    d += (L6 := elm.Line().at(op.out).right().length(0.3).dot(open=True).label('Output', 'right'))
    d += (L7 := elm.Line().at(op.vd).up().length(0.3).dot(open=True).label('$+V_{CC}$', 'right'))
