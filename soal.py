def convert_to_uppercase(input_string, satuan_suhu):
    if satuan_suhu.upper() == "CELSIUS":
        #Mengonversi suhu celcius ke fahrenheit
        fahrenheit = (input_string * 9/5) + 32
        return f"{fahrenheit}°F"
    elif satuan_suhu.upper() == "FAHRENHEIT":
        #Mengonversi suhu fahrenheit ke celcius
        celsius = (input_string - 32) * 5/9
        return f"{celsius}°C"
    else:
        return input_string.upper()
nilai_suhu = float(input("Masukkan nilai suhu: "))
satuan_suhu = input("Masukkan satuan suhu (Celsius/Fahrenheit): ")    
print(convert_to_uppercase(nilai_suhu, satuan_suhu))