# -*- coding: utf-8 -*-
# By Martin Gyurkó (2020.05.31.) nospam@gyurma.de
# use at your own risk under GNU GENERAL PUBLIC LICENSE!


Netz = 31
Layer1 = "F.Cu"
Layer2 = "In1.Cu"
Layer3 = "In2.Cu"
Layer4 = "B.Cu"

Höhe = 50.0
# Breite = 20
Breite = 16.0 * 4.0 / 3.0

Trackbreite = 0.5
AbstandZumRand = 0.3
Abstand = 0.8


AnzahlKreise = min( (Höhe-AbstandZumRand*2)/Abstand, (Breite-AbstandZumRand*2)/Abstand)

print (AnzahlKreise)

punkte = []

def Kreis(p,xa,ya,xe,ye,a):
	p.append((xa,ya))
	p.append((xa,ye))
	p.append((xe,ye))
	p.append((xe,ya+a))
	if ((xa + 2*a) < (xe - 2*a ) ) and ((ya + 2*a) < (ye - 2*a)) :
		Kreis(p, xa+a,ya+a, xe-a,ye-a,a)
	return p

punkte = Kreis ( punkte, AbstandZumRand, AbstandZumRand, Breite-AbstandZumRand, Höhe-AbstandZumRand, Abstand)

for i in punkte:
	print(i)

for i in range(0,len(punkte)-1):
	xa,ya = punkte[i]
	xe,ye = punkte[i+1]
	print( "  (segment (start %0.3f %0.3f) (end %0.3f %0.3f)" %(xa,ya,xe,ye)," (width ",Trackbreite,") (layer", Layer1,") (net ",Netz,"))" )
for i in range(0,len(punkte)-1):
	xa,ya = punkte[i]
	xe,ye = punkte[i+1]
	print( "  (segment (start %0.3f %0.3f) (end %0.3f %0.3f)" %(Breite-xa,ya,Breite-xe,ye)," (width ",Trackbreite,") (layer", Layer2,") (net ",Netz,"))" )
for i in range(0,len(punkte)-1):
	xa,ya = punkte[i]
	xe,ye = punkte[i+1]
	print( "  (segment (start %0.3f %0.3f) (end %0.3f %0.3f)" %(xa,ya,xe,ye)," (width ",Trackbreite,") (layer", Layer3,") (net ",Netz,"))" )
for i in range(0,len(punkte)-1):
	xa,ya = punkte[i]
	xe,ye = punkte[i+1]
	print( "  (segment (start %0.3f %0.3f) (end %0.3f %0.3f)" %(Breite-xa,ya,Breite-xe,ye)," (width ",Trackbreite,") (layer", Layer4,") (net ",Netz,"))" )

  
  
  # (segment (start 140 20) (end 140 69) (width 0.25) (layer F.Cu) (net 0))