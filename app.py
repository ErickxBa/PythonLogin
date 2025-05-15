# Módulo de inicio de sesión con 3 intentos y contraseña oculta con asteriscos al mostrar mensajes

def inicio_sesion(usuario_correcto, contrasena_correcta):
    intentos = 3
    while intentos > 0:
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        
        # FALLO 1: Se usa '==' para usuario pero se compara con mayúsculas sin normalizar, 
        # lo que provoca que aunque se ingrese el usuario correcto en minúsculas, no funcione.
        if usuario == usuario_correcto.upper() and contrasena == contrasena_correcta:
            print("Inicio de sesión exitoso.")
            return True
        else:
            intentos -= 1
            # Mostrar asteriscos en lugar de la contraseña real en el mensaje
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
            print(f"Usuario ingresado: {usuario}")
            print(f"Contraseña ingresada: {'*' * len(contrasena)}")  # Aquí la contraseña oculta
            
    print("Acceso denegado. Se agotaron los intentos.")
    return False

# Ejemplo de uso:
usuario_esperado = "usuario1"
contrasena_esperada = "pass123"

inicio_sesion(usuario_esperado, contrasena_esperada)
