yA = float(input("A noktasının bilinen Y koordinatını giriniz: "))
xA = float(input("A noktasının bilinen X koordinatını giriniz: "))
mAB = float(input("A noktasından B noktasına ölçülen semt açısını giriniz: "))
sAB = float(input("A noktasından B noktasına ölçülen yatay mesafeyi giriniz: "))
comma = int(input("Çıktı hesapların arzu ettiğiniz ondalık hassasiyetini  giriniz: "))

def temel_odev1(yA, xA, mAB, sAB, comma): 
  yB=yA+(sAB*math.sin((mAB)/(200/math.pi)))
  xB=xA+(sAB*math.cos((mAB)/(200/math.pi)))
  yB = round(yB,comma)
  xB = round(xB,comma)
  
  print("                              ")
  print("1. TEMEL ÖDEV HESABI SONUÇLARI")
  print("------------------------------")
  print("B noktasının hesaplanan Y koordinatı: " + str(yB) + " metre")
  print("B noktasının hesaplanan X koordinatı: " + str(xB)+ " metre")

  temel_odev1(yA, xA, mAB, sAB, comma) 


