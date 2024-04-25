import os
import qrcode

def solicitar_datos():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero = input("Ingrese su número de teléfono (sin el código de país): ")
    return nombre, apellido, numero

def validar_numero(numero):
    # Verificar si el número contiene solo dígitos y tiene una longitud válida
    if numero.isdigit() and len(numero) >= 7 and len(numero) <= 10:
        return True
    else:
        return False

def generar_codigo_qr(nombre, apellido, numero):
    codigo_pais = "593"  # Código de país de Ecuador
    numero_whatsapp = codigo_pais + numero
    enlace_whatsapp = f'https://wa.me/{numero_whatsapp}'
    qr = qrcode.make(enlace_whatsapp)
    qr = qr.convert('RGB')
    return qr

def guardar_codigo_qr(imagen, nombre, apellido, ruta_carpeta):
    nombre_archivo = f'{nombre}_{apellido}_codigo_qr.png'
    ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
    imagen.save(ruta_archivo)
    print(f"Código QR generado y guardado como '{ruta_archivo}'.")

if __name__ == "__main__":
    # Definir la ruta de la carpeta donde se guardarán los códigos QR
    ruta_carpeta = input("Ingrese la ruta completa de la carpeta donde desea guardar los códigos QR: ")

    # Solicitar los datos al usuario
    nombre, apellido, numero = solicitar_datos()

    # Validar el número de teléfono
    while not validar_numero(numero):
        print("El número de teléfono ingresado no es válido. Por favor, inténtelo nuevamente.")
        numero = input("Ingrese su número de teléfono (sin el código de país): ")

    # Generar el código QR con el enlace directo a WhatsApp
    codigo_qr = generar_codigo_qr(nombre, apellido, numero)

    # Guardar el código QR generado
    guardar_codigo_qr(codigo_qr, nombre, apellido, ruta_carpeta)

    print("Por favor, escanea el código QR con tu dispositivo móvil para abrir WhatsApp.")
