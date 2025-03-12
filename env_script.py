import requests



def download_model():
    '''
    el modelo pesa mas de 100mb, para desplegarlo se tenia que descargar de otro lado que no fuese github
    '''
    
    # URL del modelo
    url = "https://huggingface.co/S14vcH/crops-disease-classifier/resolve/main/new_model_hackaton_version.keras?download=true"

    # Nombre del archivo de salida
    output_file = "new_model_hackaton_version.keras"

    # Realizar la solicitud HTTP para descargar el archivo
    print("Descargando el modelo...")
    response = requests.get(url, stream=True)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Guardar el archivo en el sistema
        with open(output_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Modelo descargado y guardado como {output_file}")
    else:
        print(f"Error al descargar el modelo. Código de estado: {response.status_code}")


if __name__ == "__main__":
    download_model()