import requests
import os


def uploads_folder(nombre_carpeta):
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
        print(f"Carpeta '{nombre_carpeta}' creada exitosamente.")
    else:
        print(
            f"La carpeta '{nombre_carpeta}' ya existe. No se creó nuevamente.")


def download_model():
    '''
    el modelo pesa mas de 100mb, para desplegarlo se tenia que descargar de otro lado que no fuese github
    '''

    # URL del modelo
    url = "https://huggingface.co/S14vcH/crops-disease-classifier/resolve/main/new_model_hackaton_version.keras?download=true"

    output_file = "new_model_hackaton_version.keras"
    if os.path.exists(output_file):
        print(f"El modelo ya esta descargado")
    else:
        print("Descargando el modelo...")
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            with open(output_file, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Modelo descargado y guardado como {output_file}")
        else:
            print(
                f"Error al descargar el modelo. Código de estado: {response.status_code}")


if __name__ == "__main__":
    download_model()
