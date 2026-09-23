import pandas as pd #pandas kütüphanesini ekledi 
import numpy as np #numpy kütüphanesi 
# numPy array işlemleri
sayilar = np.array([10, 20, 30, 40, 50])

print("\nNumPy array:")
print(sayilar)

print("Array'in toplamı:", sayilar.sum())
print("Array'in ortalaması:", sayilar.mean())
veri = pd.read_csv("veri.csv")  


print(veri)

print("\nEksik veriler:")
print(veri.isnull().sum())


veri["Not"] = veri["Not"].fillna(veri["Not"].mean())


veri["Yaş"] = veri["Yaş"].fillna(veri["Yaş"].mean())


print("\nTemizlenmiş veriler:")
print(veri) 
# DataFrame filtreleme
yuksek_notlular = veri[veri["Not"] >= 80]

print("\n80 ve üzeri not alan öğrenciler:")
print(yuksek_notlular)

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Bölümlere göre ortalama not
ortalama_not = veri.groupby("Bölüm")["Not"].mean()

plt.figure()
ortalama_not.plot(kind="bar")
plt.title("Bölümlere Göre Ortalama Not")
plt.xlabel("Bölüm")
plt.ylabel("Ortalama Not")
plt.tight_layout()
plt.savefig("grafikler/bolum_ortalama_not.png")
plt.close()

# 2.Öğrencilerin notları
plt.figure()
plt.plot(veri["İsim"], veri["Not"], marker="o")
plt.title("Öğrencilerin Notları")
plt.xlabel("Öğrenci")
plt.ylabel("Not")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafikler/ogrenci_notlari.png")
plt.close()

# 3.Yaş ve not ilişkisi
plt.figure()
sns.scatterplot(data=veri, x="Yaş", y="Not")
plt.title("Yaş ve Not İlişkisi")
plt.xlabel("Yaş")
plt.ylabel("Not")
plt.tight_layout()
plt.savefig("grafikler/yas_not_iliskisi.png")
plt.close()

print("\n3 grafik başarıyla oluşturuldu.")