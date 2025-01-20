#!/bin/bash

# Nombre del entorno virtual
env_name="training_env"

# Verificar si Python 3 está instalado
if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 no está instalado. Por favor, instálalo antes de continuar."
    exit 1
fi

# Crear el entorno virtual
if [ -d "$env_name" ]; then
    echo "El entorno virtual '$env_name' ya existe."
else
    echo "Creando el entorno virtual en '$env_name'..."
    python3 -m venv "$env_name"
    echo "Entorno virtual creado exitosamente."
fi

# Activar el entorno virtual
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source "$env_name\\Scripts\\activate"
else
    source "$env_name/bin/activate"
fi

# Instalar dependencias si existe requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Instalando dependencias desde requirements.txt..."
    pip install -r requirements.txt
    echo "Dependencias instaladas correctamente."
else
    echo "No se encontró un archivo requirements.txt."
fi

# Mensaje final
echo "El entorno virtual está configurado y listo para usarse."
echo "Para activar el entorno virtual, utiliza el comando 'source $env_name/bin/activate'."
echo "Para salir, utiliza el comando 'deactivate'."
