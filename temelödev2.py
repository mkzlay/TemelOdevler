yA = float(input("A noktasının bilinen Y koordinatını giriniz: "))
xA = float(input("A noktasının bilinen X koordinatını giriniz: "))
yB = float(input("B noktasının bilinen Y koordinatını giriniz: "))
xB = float(input("B noktasının bilinen Y koordinatını giriniz: "))
decimal = int(input("Çıktı hesapların arzu ettiğiniz ondalık hassasiyetini  giriniz: "))

def temel_odev2(yA, xA, yB, xB, decimal): # decimal argümanı, sonuçların virgülden sonra kaç hane olmasını istediğimizi belirler.
  deltaY = yB-yA
  deltaX = xB-xA
  tanAB = (yB-yA)/(xB-xA)
  semt = math.atan(tanAB)*(200/math.pi)
  semt = round(semt,decimal)
  print("                                   ")
  print("2. TEMEL ÖDEV HESABI SONUÇLARI")
  print("-----------------------------------")
  if deltaX < 0 or deltaY > 0 and deltaX < 0:
      print("A ve B noktaları arasındaki semt açısı: "+str(semt+200) + " grad")
  elif deltaY < 0 and deltaX > 0:
      print("A ve B noktaları arasındaki semt açısı: "+str(semt + 400)+ " grad")
  else:
      print("A ve B noktaları arasındaki semt açısı: "+str(semt)+ " grad")

  mesafe = math.sqrt((deltaY**2)+(deltaX**2))
  mesafe = round(mesafe,decimal)

  print("A ve B noktaları arasındaki yatay mesafe: " +str(mesafe)+ " metre")

temel_odev2(yA, xA, yB, xB, decimal)
