# Tutoriales de ESP32

# En este capitulo preparamos el entorno virtual


## Configurar la ESP32 para trabajar con Micropython

python -m esptool --port COMx erase_flash

python -m esptool --port COMx write_flash -z 0x100 <name_file>

## Programando la ESP32

ampy --port COMx run app.py