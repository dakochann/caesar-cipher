import sys

alfabet = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z"
]

print("""\033[0;31m  _____                                  _____  _         _                 
/  __ \                                /  __ \(_)       | |                
| /  \/  __ _   ___  ___   __ _  _ __  | /  \/ _  _ __  | |__    ___  _ __ 
| |     / _` | / _ \/ __| / _` || '__| | |    | || '_ \ | '_ \  / _ \| '__|
| \__/\| (_| ||  __/\__ \| (_| || |    | \__/\| || |_) || | | ||  __/| |   
 \____/ \__,_| \___||___/ \__,_||_|     \____/|_|| .__/ |_| |_| \___||_|   
                                                 | |                       
                                                 |_|                       """)
                                                
print("author : @dakochann\n\n")

pilihan = input("ketik 'd' jika mau decode,ketik 'e' jika mau encode : ")
pilihan2 = ''
if pilihan == 'd':
	pilihan2 += 'decode'
elif pilihan == 'e':
	pilihan2 += 'encode'
teks = input(f"Masukkan Teks yang mau di {pilihan2} : ")

try:
	shift = int(input(f"Masukkan Nomor Shift : "))
except ValueError:
	print("harap hanya masukkan angka")
	exit()

def encode(teks, s):
	teks_encoded = ""
	for i in teks:
		a = alfabet.index(i)
		posisi_baru = alfabet[a + s]
		teks_encoded += posisi_baru
	print(f'Teks Encoded Dari {teks} adalah : {teks_encoded}')
	

def decode(teks, s):
	teks_decoded = ""
	for i in teks:
		a = alfabet.index(i)
		posisi_baru = alfabet[a - s]
		teks_decoded += posisi_baru
	print(f'Teks Decoded Dari {teks} adalah : {teks_decoded}')
	
if pilihan == 'd':
	decode(teks, shift)
elif pilihan == 'e':
	encode(teks, shift)
else:
	print("upss harap hanya masukkan 'e' atau 'd' ")