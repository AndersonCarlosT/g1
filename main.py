import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="📊 Extractor de Datos G1", layout="wide")
st.title("📥 Extracción de Datos del Excel G1")

archivo_excel = st.file_uploader("Agrega el Excel G1", type=["xlsx"])

if archivo_excel:
    df_excel = pd.read_excel(archivo_excel, sheet_name=0, header=None)

    # Verificación de columnas mínimas
    columnas_necesarias = [2, 4, 5, 9, 10, 11, 14]  # C, E, F, J, K, L, O

    if max(columnas_necesarias) >= df_excel.shape[1]:
        st.error(f"❌ El archivo no tiene suficientes columnas. Se necesitan al menos {max(columnas_necesarias)+1} columnas (hasta la O).")
    elif df_excel.shape[0] < 26:
        st.error("❌ El archivo no tiene suficientes filas. Se necesitan al menos 26 filas.")
    else:
        # Extracción segura
        nombre_central = df_excel.iloc[14:26, 2].reset_index(drop=True)
        tipo_generador = df_excel.iloc[14:26, 4].reset_index(drop=True)
        numero_generador = df_excel.iloc[14:26, 5].reset_index(drop=True)
        hp_mwh = df_excel.iloc[14:26, 9].reset_index(drop=True)
        hfp_mwh = df_excel.iloc[14:26, 10].reset_index(drop=True)
        total_mwh = df_excel.iloc[14:26, 11].reset_index(drop=True)
        maxima_demanda = df_excel.iloc[14:26, 14].reset_index(drop=True)

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
