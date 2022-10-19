import math

dzielenie_bez_reszty = 32//3 # 32/3 = 10.6666666667
zaokraglenie1 = round(32/3) # zaokrągla biorac pod uwage liczbe po przecinku
zaokraglenie2 = math.floor(32/3) # zaokragla zawsze w dol nie jest wazne co jest po przecinku
print(dzielenie_bez_reszty,zaokraglenie1,zaokraglenie2)

