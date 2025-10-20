import random

print("🎮 Selamat datang di Game Tebak Angka!")
print("Saya sudah memilih angka dari 1 sampai 100.")
print("Coba tebak angka itu dalam 10 kali kesempatan!\n")

angka_rahasia = random.randint(1, 100)
kesempatan = 10

for percobaan in range(1, kesempatan + 1):
    try:
        tebakan = int(input(f"Tebakan ke-{percobaan}: "))
    except ValueError:
        print("⚠ Masukkan angka yang valid!")
        continue

    if tebakan == angka_rahasia:
        print(f"🎉 Selamat! Kamu menebak dengan benar di percobaan ke-{percobaan}!")
        break
    elif tebakan < angka_rahasia:
        print("📉 Terlalu kecil!")
    else:
        print("📈 Terlalu besar!")

    sisa = kesempatan - percobaan
    if sisa > 0:
        print(f"Sisa kesempatan: {sisa}\n")
    else:
        print("\n💥 Kesempatan habis! Kamu gagal.")
        print(f"Angka yang benar adalah: {angka_rahasia}")