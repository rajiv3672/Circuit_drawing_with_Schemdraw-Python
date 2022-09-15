import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += (V1 := elm.SourceSin().up().label('$V_{signal}$\n1V\npeak to peak'))
    d += (C1 := elm.Capacitor().at(V1.end).right().label('100$\mu$F'))
    d += (D1 := elm.Diode().down().reverse().at(C1.end).label('1N4148'))
    d += (Vd := elm.SourceV().at(D1.end).reverse().down().label('0.6V'))
    d += (L1 := elm.Line().at(Vd.end).right().length(2))
    d += (R1 := elm.Resistor().up().at(L1.end).label('$R_L$\n100k$\Omega$', loc='bot'))
    d += (L2 := elm.Line().at(R1.end).up().length(3))
    d += (L3 := elm.Line().endpoints(D1.start, L2.end).dot())
    d += (L4 := elm.Line().at(L3.end).right().length(0.5).dot(open=True).label('$V_{out}$'))
    d += (L5 := elm.Line().at(L1.start).left().length(3).dot())
    d += (G1 := elm.Ground().at(L5.end))
    d += (L6 := elm.Line().endpoints(L5.end, V1.start))


