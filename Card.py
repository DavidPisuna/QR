import qrcode
import vobject
import os

def solicitar_datos():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = input("Ingrese el número de teléfono: ")
    return nombre, apellido, telefono

def generar_qr_vcard(nombre, apellido, telefono):
    # Crear objeto vCard
    vcard = vobject.vCard()
    vcard.add('fn').value = f'{nombre} {apellido}'
    vcard.add('n').value = vobject.vcard.Name(family=apellido, given=nombre)
    vcard.add('tel').value = telefono

    # Generar el código QR con la información de la vCard
    qr = qrcode.make(vcard.serialize())
    return qr

def guardar_qr(qr, nombre, apellido, ruta_guardado):
    # Crear la carpeta si no existe
    if not os.path.exists(ruta_guardado):
        os.makedirs(ruta_guardado)

    # Guardar el código QR como imagen
    qr_path = os.path.join(ruta_guardado, f"{nombre}_{apellido}_contacto.png")
    qr.save(qr_path)
    print(f"Código QR generado y guardado como '{qr_path}'.")

if __name__ == "__main__":
    # Solicitar datos del contactoD
    nombre, apellido, telefono = solicitar_datos()

    # Generar el código QR
    qr = generar_qr_vcard(nombre, apellido, telefono)

    # Especificar la ruta donde se guardará el código QR
    ruta_guardado = input("Ingrese la ruta donde desea guardar el código QR: ")

    # Guardar el código QR en el disco local
    guardar_qr(qr, nombre, apellido, ruta_guardado)
