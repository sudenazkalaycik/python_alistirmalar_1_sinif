#Girilen vize ve final notlarına göre öğrencinin dersten geçip geçmediğini bulan program

vize=float(input("Vize notunuzu giriniz: "))
final=float(input("Final notunuzu giriniz: "))

def ort(vize,final):
    yuzde_kırk=vize*(4/10)
    yuzde_atmis=final*(6/10)
    sonuc= yuzde_atmis+yuzde_kırk
    
    if sonuc>70.0:
        return "Geçti"
    else:
        return "Kaplumbaaaaa deden dostumm"
print(ort(vize,final))