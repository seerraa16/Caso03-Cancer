import pandas as pd

# Función para convertir comas decimales a puntos
def convertir_comas_a_puntos(df):
    return df.applymap(lambda x: str(x).replace(',', '.') if isinstance(x, str) and ',' in x else x)

# Leer todos los CSVs
bioquimicos = convertir_comas_a_puntos(pd.read_csv("Bioquimicos.csv"))
clinicos = pd.read_csv("Clinicos.csv")
economicos = convertir_comas_a_puntos(pd.read_csv("Economicos.csv"))
generales = pd.read_csv("Generales.csv")
geneticos = pd.read_csv("Geneticos.csv")
sociodemo = pd.read_csv("SocioDemograficos.csv")

# Convertir columnas numéricas a tipo float después de reemplazar comas
for df in [bioquimicos, economicos]:
    for col in df.columns:
        if col != 'paciente_id':
            df[col] = pd.to_numeric(df[col], errors='coerce')

# Unir todos los dataframes por paciente_id
df_merged = bioquimicos \
    .merge(clinicos, on='paciente_id', how='outer') \
    .merge(economicos, on='paciente_id', how='outer') \
    .merge(generales, on='paciente_id', how='outer') \
    .merge(geneticos, on='paciente_id', how='outer') \
    .merge(sociodemo, on='paciente_id', how='outer')

# Guardar el archivo final
df_merged.to_csv("JunteDatos.csv", index=False)

print("✅ CSV combinado creado exitosamente como 'JunteDatos.csv'")
