import streamlit as st
import pandas as pd

def main():
    st.title("Extracción de datos Excel – G‑01 CENTRALES")
    st.write("Sube tu archivo Excel correspondiente a *G1*")

    # Input para cargar el archivo
    uploaded_file = st.file_uploader("Agrega el Excel G1", type=["xls", "xlsx"])
    if not uploaded_file:
        st.info("Por favor, sube un archivo Excel.")
        return

    # Lee la hoja
    try:
        df_excel = pd.read_excel(uploaded_file, sheet_name="G-01 CENTRALES", header=None)
    except Exception as e:
        st.error(f"No se pudo leer la hoja 'G-01 CENTRALES': {e}")
        return

    # Define rangos (base 0)
    datos = {
        "Nombre de la Central":   df_excel.iloc[14:26, 2].astype(str),  # C15:C26 es columna index 2
        "Tipo de Generador":       df_excel.iloc[14:26, 4].astype(str),  # E15:E26 index 4
        "Numero de Generador":     df_excel.iloc[14:26, 5].astype(str),  # F15:F26 index 5
        "HP (MWh)":                pd.to_numeric(df_excel.iloc[14:26, 9], errors='coerce'),  # J15:J26 idx9
        "HFP (MWh)":               pd.to_numeric(df_excel.iloc[14:26, 10], errors='coerce'), # K15:K26 idx10
        "Total (MWh)":             pd.to_numeric(df_excel.iloc[14:26, 11], errors='coerce'), # L15:L26 idx11
        "Máxima Demanda (MW)":    pd.to_numeric(df_excel.iloc[14:26, 14], errors='coerce'), # O15:O26 idx14
    }

    df = pd.DataFrame(datos)

    st.subheader("📊 DataFrame generado")
    st.dataframe(df)

    # Opción: exportar como Excel o CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Descargar CSV", data=csv, file_name="G1_extraido.csv", mime="text/csv")

if __name__ == "__main__":
    main()
