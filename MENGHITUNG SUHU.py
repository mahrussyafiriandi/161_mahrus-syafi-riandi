# Minta pengguna untuk memasukkan suhu dalam Celsius
celsius = float(input("Masukkan suhu dalam Celsius: "))

# Konversi suhu dari Celsius ke Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Tampilkan hasil konversi
print(f"Suhu dalam Fahrenheit: {fahrenheit}°F")

# Minta pengguna untuk memasukkan suhu dalam Fahrenheit
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))

# Konversi suhu dari Fahrenheit ke Celsius
celsius = (fahrenheit - 32) * 5/9

# Tampilkan hasil konversi
print(f"Suhu dalam Celsius: {celsius}°C")

# Minta pengguna untuk memasukkan suhu dalam Kelvin
kelvin = float(input("Masukkan suhu dalam Kelvin: "))

# Konversi suhu dari Kelvin ke Celsius
celsius = kelvin - 273.15

# Tampilkan hasil konversi
print(f"Suhu dalam Celsius: {celsius}°C")