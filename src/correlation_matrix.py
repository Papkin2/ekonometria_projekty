import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns

data = pd.read_csv("data/dane_finalne.csv", sep =";", decimal=",")
print(data.head())

data = data.iloc[:,1:]
print(data.head())
macierz = data.corr(numeric_only=True)
# 5. Generowanie heatmapy (z większymi czcionkami)
plt.figure(figsize=(12, 10)) # Zwiększono rozmiar okna, by zmieścić większe napisy

# annot_kws={"size": 14} zwiększa czcionkę LICZB wewnątrz kwadratów
sns.heatmap(macierz, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, 
            annot_kws={"size": 13}) 

# Zwiększenie czcionki NAGŁÓWKA (fontsize) i dodanie odstępu (pad)
plt.title('Macierz korelacji', fontsize=22, pad=20) 

# Zwiększenie czcionki ZMIENNYCH na osiach (xticks i yticks)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14, rotation = 0)
plt.show()
















'''   
#scatter_matrix(data)
#plt.show()
# 3. Obliczenie macierzy korelacji
macierz = data.corr(numeric_only=True)

# 4. Wyświetlenie konkretnych wartości w konsoli
print("Macierz korelacji (wartości):")
print(macierz)

# 5. Generowanie heatmapy (ładny wykres kolorowy)
plt.figure(figsize=(10, 8))
sns.heatmap(macierz, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title('Macierz korelacji')
plt.show()









macierz = data.corr(numeric_only=True)
plt.matshow(macierz, cmap='coolwarm', vmin=-1, vmax=1,annot=True, fmt=".2f",)
plt.colorbar() # pasek skali

# Dodanie nazw zmiennych na osiach
plt.xticks(range(len(macierz.columns)), macierz.columns, rotation=45, ha='left')
plt.yticks(range(len(macierz.columns)), macierz.columns)

plt.show()
'''