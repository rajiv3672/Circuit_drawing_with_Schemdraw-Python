'''
Rajiv Das
2015132036(2nd major)
'''
#from operator import truediv
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += elm.Ground()
    d += elm.SourceV().up().label('v_g').dot()
    d += elm.Resistor().label('R_G').right()
    d += elm.Capacitor2().label('C')
    d += (R1 := elm.Resistor().up().label('R_1'))
    d += (l1 := elm.Line().right())
    d += (Rc := elm.Resistor().down().label('R_C'))
    d += (Q1 := elm.BjtNpn(circle=True).anchor('collector').right().label('Q1'))
    d += (Re := elm.Resistor().down().at(Q1.emitter).label('R_E'))
    d += elm.Ground()
    d += (l2 := elm.Line().endpoints(Q1.base, R1.start))
    d += (R2 := elm.Resistor().down().at(R1.start).label('R_2'))
    d += elm.Ground().at(R2.end)
    d += (l3 := elm.Line().at(Re.start).right())
    d += (C2 := elm.Capacitor2().down().at(l3.end).label('C'))
    d += elm.Ground().at(C2.end)
    d += (l4 := elm.Line().at(Rc.start).right())
    d += (C3 := elm.Capacitor2().at(Rc.end).right().label('C'))
    d += (l5 := elm.Line().at(C3.end).right())
    d += (l6 := elm.Line().at(l4.end).right())

    '''Start of the second stage'''

    d += (R21 := elm.Resistor().endpoints(l5.end, l6.end).label('R1'))
    d += (l7 := elm.Line().at(R21.end).right())
    d += (R2c := elm.Resistor().at(l7.end).down().label('R_C'))
    d += (Q2 := elm.BjtNpn(circle=True).anchor('collector').right().label('Q2'))
    d += (R2e := elm.Resistor().down().at(Q2.emitter).label('R_E'))
    d += elm.Ground().at(R2e.end)
    d += (l8 := elm.Line().endpoints(Q2.base, R21.start))
    d += (R22 := elm.Resistor().down().at(R21.start).label('R_2'))
    d += elm.Ground().at(R22.end)
    d += (C9 := elm.Capacitor2().at(R2c.end).right().label('C'))
    d += (l9 := elm.Line().at(R2e.start).right())
    d += (C8 := elm.Capacitor2().down().at(l9.end).label('C'))
    d += elm.Ground()
    d += elm.Line().at(R2c.start).right().dot(open=True).label('+Vcc', 'right')
    d += (ll := elm.Line().at(C9.end).right())
    d += (Rl := elm.Resistor().at(ll.end).down().label('R_L'))
    d += elm.Ground()