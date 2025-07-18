import streamlit as st
import pandas as pd

st.set_page_config(page_title="⚡ Extractor de Datos G1", layout="wide")
st.title("📊 Extractor de Datos de Centrales - G1")

# Subida del archivo
archivo = st.file_uploader("📥 Agrega el Excel G1", type=["xlsx"])

if archivo:
    # Leer la hoja "G-01 CENTRALES"
    df_excel = pd.read_excel(archivo, sheet_name="G-01 CENTRALES", header=None)

    # Datos originales C15:C26, E15:F26, J15:L26, O15:O26
    nombre_central = df_excel.loc[14:25, 2]
    tipo_generador = df_excel.loc[14:25, 4]
    numero_generador = df_excel.loc[14:25, 5]
    hp_mwh = df_excel.loc[14:25, 9]
    hfp_mwh = df_excel.loc[14:25, 10]
    total_mwh = df_excel.loc[14:25, 11]
    maxima_demanda = df_excel.loc[14:25, 14]

    # Crear el dataframe inicial
    df_resultado = pd.DataFrame({
        "Nombre de la Central": nombre_central,
        "Tipo de Generador": tipo_generador,
        "Numero de Generador": numero_generador,
        "HP (MWh)": hp_mwh,
        "HFP (MWh)": hfp_mwh,
        "Total (MWh)": total_mwh,
        "Máxima Demanda (MW)": maxima_demanda
    })

    # Datos adicionales a agregar

    # Columna 1: "Central Termica"
    nuevas_centrales = ["Central Termica"] * 4

    # Columna 2: nombres de los generadores
    nuevos_generadores = ["MODASA MP-515", "CUMMINS ZQ-4288", "COMMINS C900", "COMMINS 925kw"]

    # Columna 3: números de generador
    nuevos_codigos = ["G0016", "G01044", "G0653", "G0047"]

    # Columnas 4-6: J49:L49, J54:L54, J59:L59, J64:L64
    nuevas_hp = [
        df_excel.loc[48, 9], df_excel.loc[53, 9], df_excel.loc[58, 9], df_excel.loc[63, 9]
    ]
    nuevas_hfp = [
        df_excel.loc[48, 10], df_excel.loc[53, 10], df_excel.loc[58, 10], df_excel.loc[63, 10]
    ]
    nuevas_total = [
        df_excel.loc[48, 11], df_excel.loc[53, 11], df_excel.loc[58, 11], df_excel.loc[63, 11]
    ]

    # Columna 7: O49, O54, O59, O64
    nuevas_maxima_demanda = [
        df_excel.loc[48, 14], df_excel.loc[53, 14], df_excel.loc[58, 14], df_excel.loc[63, 14]
    ]

    # Crear dataframe adicional
    df_adicional = pd.DataFrame({
        "Nombre de la Central": nuevas_centrales,
        "Tipo de Generador": nuevos_generadores,
        "Numero de Generador": nuevos_codigos,
        "HP (MWh)": nuevas_hp,
        "HFP (MWh)": nuevas_hfp,
        "Total (MWh)": nuevas_total,
        "Máxima Demanda (MW)": nuevas_maxima_demanda
    })

    # Concatenar ambos dataframes
    df_final = pd.concat([df_resultado, df_adicional], ignore_index=True)

    # Mostrar el dataframe
    st.dataframe(df_final, use_container_width=True)
