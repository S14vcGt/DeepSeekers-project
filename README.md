# **API de Diagnóstico de Enfermedades en Plantas de Cultivo 🌱🩺**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.x-green) ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)

Esta API web 🌐 utiliza un modelo de red neuronal convolucional (CNN) 🧠 entrenado para identificar enfermedades en plantas de cultivo como uva 🍇, tomate 🍅, maíz 🌽 y manzana 🍎. El modelo procesa imágenes de hojas de plantas 🍃 y devuelve predicciones sobre posibles enfermedades o condiciones de salud 🩹.

## **Características 🌟**
- Identificación automática de enfermedades en plantas de cultivo 🌱.
- Compatible con imágenes de hojas de uva 🍇, tomate 🍅, maíz 🌽 y manzana 🍎.
    - uva:
        - Sarampión negro
        - Tizón foliar(Mancha foliar por Isariopsis)
    - tomate:
        - Tizón tardío
        - Mancha foliar por Septoriosis
    - maíz:
        - Mancha foliar por Cercospora Mancha gris
        - Tizón foliar norteño
    - manzana:
        - Roña del manzano
        - Podredumbre negra

- API RESTful fácil de integrar en aplicaciones agrícolas o sistemas de monitoreo 🚜.
- Modelo basado en una red convolucional (CNN) optimizada para precisión y rendimiento 📊.

---

## **Tabla de Contenidos 📋**
1. [Requisitos 🛠️](#requisitos)
2. [Instalación ⚙️](#instalación)
3. [Uso 🖥️](#uso)
4. [Endpoints 🌐](#endpoints)
5. [Modelo 🧠](#modelo)

---

## **Requisitos 🛠️**

Para ejecutar este proyecto, necesitarás lo siguiente:

- Python 3.12 o superior 🐍
- Conexion a internet

---

## **Instalación ⚙️**

1. Clona este repositorio 📂

2. Instala las dependencias 📦:
   ```bash
   pip install -r requirements.txt
   ```

3. Descarga los pesos del modelo preentrenado 📥:
   - al ejecutar el servidor el modelo preentrenado se descarga desde [HugginFace](https://huggingface.co/S14vcH/crops-disease-classifier/tree/main)

4. Inicia el servidor 🚀:
   ```bash
   gunicorn app:app
   ```

El servidor se ejecutará localmente en `http://127.0.0.1:8000`.

---

## **Uso 🖥️**

### **Cargar una imagen para diagnóstico 📸**

Envía una solicitud POST al endpoint `/api/predict` con una imagen de una hoja de planta 🍃. La API devolverá un JSON con la predicción de la enfermedad 🩺.

#### Ejemplo usando `curl` 💻:
```bash
curl -X POST -F "file=@ruta/a/tu/imagen.jpg" http://127.0.0.1:5000/predict
```

#### Respuesta esperada ✅:
```json
 { 
 "Manzana___Podredumbre_negra": 0.022210918366909027, 
 "Manzana___Roña_del_manzano": 0.6731756329536438, 
 "Manzana___saludable": 0.2475418746471405, 
 "Maíz___Mancha_foliar_por_Cercospora": 0.02118958719074726, 
 "Maíz___Tizón_foliar_norteño": 0.0009554149582982063, 
 "Maíz___saludable": 0.013545230962336063, 
 "Tomate___Mancha_foliar_por_Septoriosis": 0.007391240913420916, 
 "Tomate___Tizón_tardío": 0.0006959199672564864, 
 "Tomate___saludable": 0.002276195678859949, 
 "Uva___Sarampión_negro": 0.0017166787292808294, 
 "Uva___Tizón_foliar_Isariopsis": 0.001491655595600605, 
 "Uva___saludable": 0.007809591479599476 
 }
```

---

## **Endpoints 🌐**

| Método 🔧 | Endpoint       | Descripción                                                                 |
|-----------|----------------|-----------------------------------------------------------------------------|
| POST 📥   | `/api/predict`     | Recibe una imagen de una hoja de planta y devuelve la predicción de la enfermedad. |

---

## **Modelo 🧠**

El modelo utilizado es una red convolucional (CNN) 🧠 entrenada con un conjunto de datos que incluye imágenes de hojas de plantas de uva 🍇, tomate 🍅, maíz 🌽 y manzana 🍎. El modelo fue entrenado utilizando TensorFlow 🐍 y alcanza una precisión del 98% en los conjuntos de prueba y validacion. 📈.
