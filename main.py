# archivo: g1_extractor_app.py

import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="📊 Extractor de Datos G1", layout="wide")
st.title("📥 Extracción de Datos del Excel G1")

# Subir archivo
archivo_excel = st.file_uploader("Agrega el Excel G1", type=["xlsx"])

if archivo_excel:
    # Leer la primera hoja sin encabezados
    df_excel = pd.read_excel(archivo_excel, sheet_name=0, header=None)

    # Extraer los rangos usando iloc (por posición)
    nombre_central = df_excel.iloc[14:26, 2].reset_index(drop=True)  # C15:C26
    tipo_generador = df_excel.iloc[14:26, 4].reset_index(drop=True)  # E15:E26
    numero_generador = df_excel.iloc[14:26, 5].reset_index(drop=True)  # F15:F26
    hp_mwh = df_excel.iloc[14:26, 9].reset_index(drop=True)  # J15:J26
    hfp_mwh = df_excel.iloc[14:26, 10].reset_index(drop=True)  # K15:K26
    total_mwh = df_excel.iloc[14:26, 11].reset_index(drop=True)  # L15:L26
    maxima_demanda = df_excel.iloc[14:26, 14].reset_index(drop=True)  # O15:O26

    # Crear dataframe resultado
    df_resultado = pd.DataFrame({
        "Nombre de la Central": nombre_central,
        "Tipo de Generador": tipo_generador,
        "Numero de Generador": numero_generador,
        "HP (MWh)": hp_mwh,
        "HFP (MWh)": hfp_mwh,
        "Total (MWh)": total_mwh,
        "Máxima Demanda (MW)": maxima_demanda
    })

    st.success("✅ Datos extraídos correctamente")
    st.dataframe(df_resultado)

    # Descargar Excel
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_resultado.to_excel(writer, index=False, sheet_name='Datos G1')
    output.seek(0)

    st.download_button(
        label="📥 Descargar Excel de Resultados",
        data=output,
        file_name="Extraccion_G1.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
