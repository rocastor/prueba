import requests
from bs4 import BeautifulSoup

def buscar_licitaciones_secop1(palabras_clave):
    url_base = "https://www.contratos.gov.co/consultas/resultadosConsulta.do"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    resultados = []

    for palabra in palabras_clave:
        print(f"🔍 Buscando en SECOP I: {palabra}")
        params = {
            "entidad": "",
            "tipoProceso": "",
            "modalidad": "",
            "estado": "2",  # Estado 2 = Proceso de selección
            "criterio": "Objeto",
            "palabraClave": palabra,
            "registros": "20"
        }

        try:
            response = requests.get(url_base, params=params, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            tabla = soup.find("table", class_="tablaResultados")
            if tabla:
                filas = tabla.find_all("tr")[1:]  # Omitir encabezado
                for fila in filas:
                    columnas = fila.find_all("td")
                    if len(columnas) >= 6:
                        resultado = {
                            "Entidad": columnas[0].text.strip(),
                            "Modalidad": columnas[1].text.strip(),
                            "Número del proceso": columnas[2].text.strip(),
                            "Objeto": columnas[3].text.strip(),
                            "Cuantía": columnas[4].text.strip(),
                            "Fecha de cierre": columnas[5].text.strip(),
                            "Fuente": "SECOP I",
                            "Palabra clave": palabra
                        }
                        resultados.append(resultado)
        except Exception as e:
            print(f"Error buscando '{palabra}' en SECOP I: {e}")
    
    return resultados
