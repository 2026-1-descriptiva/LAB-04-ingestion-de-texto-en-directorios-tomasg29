# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import pandas as pd


def pregunta_01():
    """
    Descomprime el archivo input.zip y genera:
    - files/output/train_dataset.csv
    - files/output/test_dataset.csv
    """

    # Descomprimir el archivo ZIP
    with zipfile.ZipFile("files/input.zip", "r") as zip_ref:
        zip_ref.extractall(".")

    # Función auxiliar
    def procesar_carpeta(ruta_base):

        datos = []

        for sentimiento in ["negative", "neutral", "positive"]:

            carpeta = os.path.join(ruta_base, sentimiento)

            if os.path.exists(carpeta):

                for archivo in os.listdir(carpeta):

                    if archivo.endswith(".txt"):

                        ruta_archivo = os.path.join(
                            carpeta,
                            archivo,
                        )

                        with open(
                            ruta_archivo,
                            "r",
                            encoding="utf-8",
                        ) as file:

                            frase = file.read().strip()

                        datos.append(
                            {
                                "phrase": frase,
                                "target": sentimiento,
                            }
                        )

        return pd.DataFrame(datos)

    # Crear datasets
    train_dataset = procesar_carpeta("input/train")
    test_dataset = procesar_carpeta("input/test")

    # Crear carpeta output
    os.makedirs("files/output", exist_ok=True)

    # Guardar CSVs
    train_dataset.to_csv(
        "files/output/train_dataset.csv",
        index=False,
    )

    test_dataset.to_csv(
        "files/output/test_dataset.csv",
        index=False,
    )