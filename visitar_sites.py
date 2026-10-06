"""
Abre cada site de verdade num navegador (sem tela), espera a página carregar
por completo e a conexão em tempo real (WebSocket) do Streamlit se formar.
Isso conta como uma visita real e reinicia o contador de inatividade.
"""

from playwright.sync_api import sync_playwright

SITES = [
    "https://pcarena.streamlit.app/",
    "https://checklistpcholyrics.streamlit.app/",
    "https://checklistiluminacao.streamlit.app/",
    # Troque pela URL real do painel de acompanhamento:
    "https://SEU-PAINEL-AQUI.streamlit.app/",
]

TEMPO_ESPERA_MS = 8000  # tempo extra pra garantir que o WebSocket conectou


def visitar(pagina, url):
    print(f"Abrindo {url} ...")
    try:
        pagina.goto(url, wait_until="networkidle", timeout=30000)
        pagina.wait_for_timeout(TEMPO_ESPERA_MS)
        print(f"  OK: {url}")
    except Exception as erro:
        print(f"  Falhou: {url} -> {erro}")


def main():
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        pagina = navegador.new_page()
        for url in SITES:
            visitar(pagina, url)
        navegador.close()


if __name__ == "__main__":
    main()
