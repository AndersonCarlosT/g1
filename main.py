import streamlit as st
import pandas as pd

st.set_page_config(page_title="⚡ Extractor de Datos G1", layout="wide")
st.title("📊 Extractor de Datos de Centrales - G1")

# Subida del archivo
archivo = st.file_uploader("📥 Agrega el Excel G1", type=["xlsx"])

if archivo:
    # Leer la hoja "G-01 CENTRALES"
    df_excel = pd.read_excel(archivo, sheet_name="G-01 CENTRALES", header=None)

    # Primer bloque de datos (C15:C26, E15:F26, J15:L26, O15:O26)
    nombre_central = df_excel.loc[14:25, 2]
    tipo_generador = df_excel.loc[14:25, 4]
    numero_generador = df_excel.loc[14:25, 5]
    hp_mwh = df_excel.loc[14:25, 9]
    hfp_mwh = df_excel.loc[14:25, 10]
    total_mwh = df_excel.loc[14:25, 11]
    maxima_demanda = df_excel.loc[14:25, 14]

    df_original = pd.DataFrame({
        "Nombre de la Central": nombre_central,
        "Tipo de Generador": tipo_generador,
        "Numero de Generador": numero_generador,
        "HP (MWh)": hp_mwh,
        "HFP (MWh)": hfp_mwh,
        "Total (MWh)": total_mwh,
        "Máxima Demanda (MW)": maxima_demanda
    })

    # Segundo bloque de datos (datos adicionales)
    nuevas_centrales = ["MODASA MP-515", "CUMMINS ZQ-4288", "COMMINS C900", "COMMINS 925kw"]
    nuevos_generadores = ["G0016", "G01044", "G0653", "G0047", "G0064"]

    # Datos de J49:L49, J54:L54, J59:L59, J64:L64
    filas_extra = [48, 53, 58, 63]  # Rango en pandas (indexado desde 0)

    hp_mwh_extra = df_excel.loc[filas_extra, 9]
    hfp_mwh_extra = df_excel.loc[filas_extra, 10]
    total_mwh_extra = df_excel.loc[filas_extra, 11]
    maxima_demanda_extra = df_excel.loc[filas_extra, 14]

    # Crear dataframe adicional
    df_extra = pd.DataFrame({
        "Nombre de la Central": nuevas_centrales,
        "Tipo de Generador": [None]*4,  # Se deja en blanco
        "Numero de Generador": nuevos_generadores[:4],
        "HP (MWh)": hp_mwh_extra.values,
        "HFP (MWh)": hfp_mwh_extra.values,
        "Total (MWh)": total_mwh_extra.values,
        "Máxima Demanda (MW)": maxima_demanda_extra.values
    })

    # Agregar G0064 adicional si quieres una fila extra (opcional)
    if len(nuevos_generadores) > 4:
        fila_adicional = pd.DataFrame({
            "Nombre de la Central": [None],
            "Tipo de Generador": [None],
            "Numero de Generador": [nuevos_generadores[4]],
            "HP (MWh)": [None],
            "HFP (MWh)": [None],
            "Total (MWh)": [None],
            "Máxima Demanda (MW)": [None]
        })
        df_extra = pd.concat([df_extra, fila_adicional], ignore_index=True)

    # Concatenar los dataframes (verticalmente)
    df_final = pd.concat([df_original, df_extra], ignore_index=True)

    # Mostrar el dataframe
    st.dataframe(df_final, use_container_width=True)
