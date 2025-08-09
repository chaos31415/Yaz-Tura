def yaziTura():
    import random
    sayi = random.random()

    if sayi > 0.5:
        return "Tura"
    else:
        return "Yazı"
    
sonuc = yaziTura()
print(sonuc)
