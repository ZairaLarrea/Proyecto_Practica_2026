from datetime import datetime

fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

hoy = datetime.today()
edad = hoy.year - fecha_nacimiento.year

if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1

print("Tu edad es:", edad)