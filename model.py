from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import cv2
import os



def preprocess_image(image_path):

    image_pil = Image.open(image_path)  # Cargar con PIL
    image = np.array(image_pil)  # Convertir a un array de NumPy

    # Convertir a BGR (OpenCV usa BGR por defecto)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # Convertir a escala de grises
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Redimensionar a 256x256 (tamaño esperado por el modelo)
    resized_image = cv2.resize(gray_image, (256, 256))
    # Normalizar los valores de píxeles
    normalized_image = resized_image / 255.0
    # Expandir dimensiones para que coincida con la entrada del modelo (256, 256, 1)
    input_image = np.expand_dims(normalized_image, axis=-1)
    # Añadir dimensión del batch
    input_image = np.expand_dims(input_image, axis=0)

    os.remove(image_path)

    return input_image


def predict_plant(image_path):

    model = load_model("modelo_escala_de_grises.keras")
    class_names = ['Tomate Sano', 'Tomate Enfermo', 'Pimenton Sano',
                   'Pimenton Enfermo', 'Maiz Sano', 'Maiz Enfermo']
    # ?capture_width, capture_height = 256, 256
    # Preprocesar la imagen
    input_image = preprocess_image(image_path)
    # Realizar la predicción
    predictions = model.predict(input_image)
    # Obtener todas las clases y sus confianzas
    class_indices = np.argsort(predictions[0])[::-1]  # Orden descendente
    results = {}
    for idx in class_indices:
        results[class_names[idx]] = float(predictions[0][idx])
    return results


if __name__ == '__main__':
    pass
