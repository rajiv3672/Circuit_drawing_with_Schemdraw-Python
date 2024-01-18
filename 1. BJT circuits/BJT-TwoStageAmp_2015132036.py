'''
Rajiv Das
2015132036(2nd major)
'''

import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += elm.Ground()
    d += elm.SourceSin().up().label('$v_g$')
    d += elm.Resistor().label('$R_G$').right()
    d += elm.Capacitor2().label('$C_i$').dot()
    d += (R1 := elm.Resistor().up().label('$R_{11}$'))
    d += (l1 := elm.Line().right())
    d += (Rc := elm.Resistor().down().label('$R_{C1}$'))
    d += (Q1 := elm.BjtNpn(circle=True).anchor('collector').right().label('$Q1$'))
    d += (Re := elm.Resistor().down().at(Q1.emitter).label('$R_{E1}$'))
    d += elm.Ground()
    d += (l2 := elm.Line().endpoints(Q1.base, R1.start))
    d += (R2 := elm.Resistor().down().at(R1.start).label('$R_{12}$'))
    d += elm.Ground().at(R2.end)
    d += (l3 := elm.Line().at(Re.start).right())
    d += (C2 := elm.Capacitor2().down().at(l3.end).label('$C_{E1}$'))
    d += elm.Ground().at(C2.end)
    d += (l4 := elm.Line().at(Rc.start).right())
    d += (C3 := elm.Capacitor2().at(Rc.end).right().label('$C_{1o}$'))
    d += (l5 := elm.Line().at(C3.end).right())
    d += (l6 := elm.Line().at(l4.end).right())
    d += (dot1 := elm.Dot().at(Rc.start))
    d += (dot2 := elm.Dot().at(Rc.end))
    d += (dot3 := elm.Dot().at(Re.start))

    '''Start of the second stage'''

    d += (R21 := elm.Resistor().endpoints(l5.end, l6.end).label('$R_{21}$'))
    d += (l7 := elm.Line().at(R21.end).right())
    d += (R2c := elm.Resistor().at(l7.end).down().label('$R_{C2}$'))
    d += (Q2 := elm.BjtNpn(circle=True).anchor('collector').right().label('$Q2$'))
    d += (R2e := elm.Resistor().down().at(Q2.emitter).label('$R_{E2}$'))
    d += elm.Ground().at(R2e.end)
    d += (l8 := elm.Line().endpoints(Q2.base, R21.start))
    d += (R22 := elm.Resistor().down().at(R21.start).label('$R_{22}$'))
    d += elm.Ground().at(R22.end)
    d += (C9 := elm.Capacitor2().at(R2c.end).right().label('$C_O$'))
    d += (l9 := elm.Line().at(R2e.start).right())
    d += (C8 := elm.Capacitor2().down().at(l9.end).label('$C_{E2}$'))
    d += elm.Ground()
    d += elm.Line().at(R2c.start).right().dot(open=True).label('$+V_{cc}$', 'right')
    d += (ll := elm.Line().at(C9.end).right())
    d += (Rl := elm.Resistor().at(ll.end).down().label('$R_L$'))
    d += elm.Ground()
    d += (dot4 := elm.Dot().at(R2c.start))
    d += (dot5 := elm.Dot().at(R2c.end))
    d += (dot6 := elm.Dot().at(R21.start))
    d += (dot7 := elm.Dot().at(R21.end))
    d += (dot8 := elm.Dot().at(R2e.start))
    