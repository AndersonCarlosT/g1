import streamlit as st
import pandas as pd

st.set_page_config(page_title="⚡ Extractor de Datos G1", layout="wide")
st.title("📊 Extractor de Datos de Centrales - G1")

# Subida del archivo
archivo = st.file_uploader("📥 Agrega el Excel G1", type=["xlsx"])

if archivo:
    # Leer la hoja "G-01 CENTRALES"
    df_excel = pd.read_excel(archivo, sheet_name="G-01 CENTRALES", header=None)

    # Definir los rangos a extraer (pandas indexa desde 0)
    nombre_central = df_excel.loc[14:25, 2]   # C15:C26
    tipo_generador = df_excel.loc[14:25, 4]   # E15:E26
    numero_generador = df_excel.loc[14:25, 5] # F15:F26
    hp_mwh = df_excel.loc[14:25, 9]           # J15:J26
    hfp_mwh = df_excel.loc[14:25, 10]         # K15:K26
    total_mwh = df_excel.loc[14:25, 11]       # L15:L26
    maxima_demanda = df_excel.loc[14:25, 14]  # O15:O26

    # Crear el dataframe
    df_resultado = pd.DataFrame({
        "Nombre de la Central": nombre_central.values,
        "Tipo de Generador": tipo_generador.values,
        "Numero de Generador": numero_generador.values,
        "HP (MWh)": hp_mwh.values,
        "HFP (MWh)": hfp_mwh.values,
        "Total (MWh)": total_mwh.values,
        "Máxima Demanda (MW)": maxima_demanda.values
    })

    # Rellenar ceros desde la fila 4 (índice 3), celda por celda
    for fila in range(3, len(df_resultado)):
        for columna in df_resultado.columns:
            if pd.isna(df_resultado.at[fila, columna]):
                df_resultado.at[fila, columna] = 0

    # Mostrar el dataframe
    st.dataframe(df_resultado, use_container_width=True)
