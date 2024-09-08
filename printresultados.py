from bateria_electronica import BateriaElectronica

# Crear una instancia de la batería
bateria = BateriaElectronica(max_volumen=100, volumen_inicial=50)

# Mostrar el estado inicial
print(bateria)  # Debería mostrar "Batería Electrónica - Estado: Apagada, Volumen: 50"

# Encender la batería
bateria.encender()
print(bateria)  # Debería mostrar "Batería Electrónica - Estado: Encendida, Volumen: 50"

# Ajustar el volumen a 70
bateria.ajustar_volumen(70)
print(bateria)  # Debería mostrar "Batería Electrónica - Estado: Encendida, Volumen: 70"

# Apagar la batería
bateria.apagar()
print(bateria)  # Debería mostrar "Batería Electrónica - Estado: Apagada, Volumen: 70"
