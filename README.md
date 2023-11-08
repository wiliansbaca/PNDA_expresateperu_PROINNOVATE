# Análisis de Proyectos Finalizados

Este repositorio contiene un script de Python que analiza un conjunto de datos de proyectos finalizados. El script realiza las siguientes acciones:

## Características

- **Carga de Datos**: Lee un archivo CSV que contiene datos sobre proyectos finalizados, incluyendo detalles financieros y temporales.
- **Limpieza de Datos**: Convierte las fechas en formato numérico a objetos `datetime` para facilitar su manipulación y análisis.
- **Análisis Descriptivo**: Calcula el monto total financiado de proyectos por departamento y ordena los proyectos por fecha de inicio.
- **Visualización de Datos**: Crea visualizaciones que incluyen:
  - Un gráfico de barras del monto total financiado por departamento.
  - Un histograma de las fechas de inicio de los proyectos para entender la distribución a lo largo del tiempo.
  - Un gráfico de líneas que muestra la tendencia del financiamiento de proyectos a lo largo del tiempo.

## Uso

Para ejecutar este script, necesitarás Python y las bibliotecas `pandas` y `matplotlib`. Asegúrate de que el archivo CSV esté en el mismo directorio que el script o actualiza la variable `file_path` para que apunte a la ubicación correcta de tu archivo.

Instala las dependencias con:

```sh
pip install pandas matplotlib
```

Ejecuta el script con:

```sh
python analysis_script.py
```

Reemplaza `analysis_script.py` con el nombre que le hayas dado a tu archivo de script.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias para mejorar el análisis o las visualizaciones, por favor abre un issue o realiza un pull request.