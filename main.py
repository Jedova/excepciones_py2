from foto import Foto
from error import DimensionError

def crear_foto_desde_usuario(): ###interaccion con el usuario###
    print("Bienvenido al sistema de creación de fotos\n")

    try:
        ancho = int(input("Ingresa el ANCHO de la foto: "))
        alto = int(input("Ingresa el ALTO de la foto: "))
        ruta = input("Ingresa la RUTA donde se guardará la foto: ")

        foto = Foto(ancho, alto, ruta)
        print(f"\n OK Foto creada con éxito: {foto.ancho}x{foto.alto} y guardada en {foto.ruta}")
        return foto

    except DimensionError as e:
        print(f"\n X Error al crear la foto: {e}")
        return None
    except ValueError:
        print("\n X Debes ingresar valores numéricos para ancho y alto.")
        return None

def modificar_foto(foto: Foto):
    print("\n Vamos a modificar las dimensiones de tu foto")
    try:
        nuevo_ancho = int(input("Nuevo ANCHO: "))
        foto.ancho = nuevo_ancho
        print(f"OK Ancho actualizado a {foto.ancho}")
    except DimensionError as e:
        print(f"X Error al modificar el ancho: {e}")

    try:
        nuevo_alto = int(input("Nuevo ALTO: "))
        foto.alto = nuevo_alto
        print(f"OK Alto actualizado a {foto.alto}")
    except DimensionError as e:
        print(f"X Error al modificar el alto: {e}")

if __name__ == "__main__":
    foto = crear_foto_desde_usuario()
    if foto:
        modificar_foto(foto)
