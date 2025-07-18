import streamlit as st
import pandas as pd

def cargar_dataframe(df_excel):
    # Seleccionar la hoja específica
    df = pd.read_excel(df_excel, sheet_name="G-01 CENTRALES", engine="openpyxl", header=None)
    
    # Extraer rangos
    nombres = df.iloc[14:26, 2]    # C15:C26  -> índice 14:26, columna 2 (C)
    tipo     = df.iloc[14:26, 4]    # E15:E26  -> col 4
    numero   = df.iloc[14:26, 5]    # F15:F26  -> col 5
    hp       = df.iloc[14:26, 9]    # J15:J26  -> col 9
    hfp      = df.iloc[14:26, 10]   # K15:K26 -> col 10
    total    = df.iloc[14:26, 11]   # L15:L26 -> col 11
    maxima   = df.iloc[14:26, 14]   # O15:O26 -> col 14

    # Construir DataFrame
    df2 = pd.DataFrame({
        "Nombre de la Central": nombres,
        "Tipo de Generador": tipo,
        "Numero de Generador": numero,
        "HP (MWh)": hp,
        "HFP (MWh)": hfp,
        "Total (MWh)": total,
        "Máxima Demanda (MW)": maxima
    })

    # Reemplazar valores vacíos o NaN por 0
    df2 = df2.fillna(0)

    # Asegurar tipos: intentamos convertir numéricos
    cols_num = ["HP (MWh)", "HFP (MWh)", "Total (MWh)", "Máxima Demanda (MW)"]
    for c in cols_num:
        df2[c] = pd.to_numeric(df2[c], errors="coerce").fillna(0)

    return df2

def main():
    st.title("📊 Extracción Excel G1")

    st.write("Por favor, **agrega el Excel G1** a continuación:")

    archivo = st.file_uploader("Selecciona tu archivo Excel G1", type=["xlsx", "xls"])

    if archivo is not None:
        try:
            df = cargar_dataframe(archivo)
            st.write("### DataFrame generado:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    main()
