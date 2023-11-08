import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'proyectos_finalizados_20231030.csv'

# Since we had an issue with the delimiter, we use automatic delimiter detection
data = pd.read_csv(file_path, delimiter=None, engine='python')

# Convert dates from integer format to datetime
data['FECHA_INICIO'] = pd.to_datetime(data['FECHA_INICIO'], format='%Y%m%d', errors='coerce')
data['FECHA_FIN'] = pd.to_datetime(data['FECHA_FIN'], format='%Y%m%d', errors='coerce')

# Summarize the financial amount by department
monto_por_departamento = data.groupby('DEPARTAMENTO')['MONTO_FINANCIERO'].sum().reset_index()

# Sort the data by project start date
data_sorted_by_date = data.sort_values(by='FECHA_INICIO')

# Plot the total financial amount by department
plt.figure(figsize=(10, 6))
plt.bar(monto_por_departamento['DEPARTAMENTO'], monto_por_departamento['MONTO_FINANCIERO'], color='skyblue')
plt.title('Monto Total Financiado por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Monto Financiado')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot the histogram of project start dates
plt.figure(figsize=(10, 6))
plt.hist(data_sorted_by_date['FECHA_INICIO'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title('Histograma de Fechas de Inicio de los Proyectos')
plt.xlabel('Fecha')
plt.ylabel('Cantidad de Proyectos')
plt.tight_layout()
plt.show()

# Group the data by start date and sum the financial amounts
monto_por_fecha = data.groupby(data['FECHA_INICIO'].dt.to_period('M'))['MONTO_FINANCIERO'].sum().reset_index()
# Convert period to timestamp for plotting
monto_por_fecha['FECHA_INICIO'] = monto_por_fecha['FECHA_INICIO'].dt.to_timestamp()

# Plot the line graph of financial amounts over time
plt.figure(figsize=(12, 6))
plt.plot(monto_por_fecha['FECHA_INICIO'], monto_por_fecha['MONTO_FINANCIERO'], marker='o', linestyle='-', color='skyblue')
plt.title('Monto Financiado de Proyectos a lo Largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Monto Financiado')
plt.grid(True)
plt.tight_layout()
plt.show()
