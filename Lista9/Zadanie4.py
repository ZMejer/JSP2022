import matplotlib.pyplot as plt
dane = {'Python':16.36,'C':16.26, 'C++':12.91, 'Java':12.21,'C#':5.73,'Visual Basic':4.64,'Javascript':2.87,'SQL':2.50,'Assembly':1.60,'PHP':1.39}
jezyki = list(dane.keys())
wartosci = list(dane.values())

plt.title("Popularność języków programowania")
plt.xlabel("Języki")
plt.ylabel("Popularność [%]")
plt.bar(jezyki,wartosci)

plt.show()