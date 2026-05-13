import pandas as pd
import os
from datetime import datetime

results = []


def add_result(tc_id, status, error=None, evidence=None):

    results.append({
        "TC_ID": str(tc_id),
        "Status": "PASS" if status else "FAIL",
        "Error": str(error) if error else "",
        "Evidence": str(evidence) if evidence else ""
    })


def generate_excel_report():

    os.makedirs("reports", exist_ok=True)

    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"reports/results_{fecha}.xlsx"

    #  crear DataFrame con estructura fija
    df = pd.DataFrame(results, columns=[
        "TC_ID",
        "Status",
        "Error",
        "Evidence"
    ])

    # asegurar tipos de texto (evita errores de pandas)
    df = df.fillna("")  # elimina NaN
    df["TC_ID"] = df["TC_ID"].astype(str)
    df["Status"] = df["Status"].astype(str)
    df["Error"] = df["Error"].astype(str)
    df["Evidence"] = df["Evidence"].astype(str)

    df.to_excel(file_path, index=False)

    print(f"\nExcel generado: {file_path}\n")

    # opcional: limpiar resultados para próxima corrida
    results.clear()