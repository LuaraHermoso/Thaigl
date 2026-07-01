import streamlit as st
import pandas as pd

# 1. Configuração da página (Cores da bandeira da Tailândia)
st.set_page_config(
    page_title="Thai GL Travel Guide",
    page_icon="🗺️",
    layout="wide"
)

# Estilização CSS Premium e sem anúncios
st.markdown("""
    <style>
    .main { background-color: #0A1128; }
    h1 { color: #E01A22 !important; text-align: center; font-family: sans-serif; font-weight: 800; }
    h3 { color: #FFFFFF !important; border-bottom: 2px solid #00247D; padding-bottom: 8px; }
    .loc-card {
        background-color: #131F42;
        padding: 20px;
        border-radius: 10px;
        border-top: 4px solid #E01A22;
        border-bottom: 4px solid #00247D;
        margin-bottom: 25px;
        color: #FFFFFF;
        box-shadow: 0 4px 8px rgba(0,0,0,0.4);
    }
    .badge-serie {
        background-color: #E01A22;
        color: white;
        padding: 3px 8px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🗺️ THAI GL TRAVEL GUIDE")
st.markdown("<p style='text-align: center; color: #FFFFFF;'>⚡ <b>Hub de Turismo Premium:</b> O maior mapa interativo de locações reais de GLs, 100% livre de anúncios.</p>", unsafe_allow_html=True)
st.markdown("---")

# 2. BANCO DE DADOS EXPANSÍVEL (Contém as séries prontas para você atualizar)
dados_mapa = [
    {"Série": "GAP: The Series", "Local": "Escritório da Sam (Diversion)", "Descrição": "A famosa sede da empresa onde a Mon começa a trabalhar.", "lat": 13.7563, "lon": 100.5018, "Link": "https://maps.google.com/?q=Bangkok"},
    {"Série": "23.5 Degrees", "Local": "Campus Escolar Secundário", "Descrição": "A escola tailandesa que serve de cenário para o romance de Ongsa e Sun.", "lat": 13.7367, "lon": 100.5231, "Link": "https://maps.google.com"},
    {"Série": "The Secret of Us", "Local": "Hospital de Treinamento da Fahlada", "Descrição": "O cenário principal do hospital onde a Doutora Fahlada trabalha.", "lat": 13.7649, "lon": 100.5383, "Link": "https://maps.google.com"},
    {"Série": "Affair", "Local": "Píer Beira-Rio", "Descrição": "O icônico deck de madeira onde acontecem os diálogos mais intensos.", "lat": 13.7234, "lon": 100.5092, "Link": "https://maps.google.com"},
    {"Série": "Blank", "Local": "Galeria de Arte e Design", "Descrição": "O espaço conceitual de artes que serve de plano de fundo.", "lat": 13.7468, "lon": 100.5342, "Link": "https://maps.google.com"},
    {"Série": "Pluto", "Local": "Praça Central de Bangkok", "Descrição": "Locação externa usada para as cenas de transição na capital.", "lat": 13.7542, "lon": 100.4931, "Link": "https://maps.google.com"},
    {"Série": "Harmony Secret", "Local": "A definir (Bangkok)", "Descrição": "Locação oficial da série em breve.", "lat": 13.7563, "lon": 100.5018, "Link": "https://maps.google.com"}
]

df_loc = pd.DataFrame(dados_mapa)

# 3. FILTRO GLOBAL
st.subheader("🔍 Filtrar Destinos por Produtora/Série")
lista_series_completa = ["Mostrar Todas as Séries"] + sorted(list(df_loc["Série"].unique()))
selecao = st.selectbox("Selecione a série para ver os pontos no mapa da Tailândia:", lista_series_completa)

if selecao != "Mostrar Todas as Séries":
    df_filtrado = df_loc[df_loc["Série"] == selecao]
else:
    df_filtrado = df_loc

# 4. RENDERIZAÇÃO DO MAPA
st.write(f"🗺️ Exibindo {len(df_filtrado)} ponto(s) turístico(s) ativo(s):")
st.map(df_filtrado[['lat', 'lon']])

st.markdown("---")

# 5. VITRINE DE CARDS
st.subheader("✈️ Ficha Técnica das Locações")
col1, col2 = st.columns(2)

for idx, row in df_filtrado.reset_index().iterrows():
    with (col1 if idx % 2 == 0 else col2):
        st.markdown(f"""
        <div class="loc-card">
            <span class="badge-serie">{row['Série']}</span>
            <h3 style='margin-top:10px; margin-bottom:5px; color:#FFFFFF;'>📍 {row['Local']}</h3>
            <p style='color: #CFD8DC;'>{row['Descrição']}</p>
            <hr style='border: 0; border-top: 1px solid #00247D; margin: 10px 0;'>
            <a href="{row['Link']}" target="_blank" style="color: #4CAF50; text-decoration: none; font-weight: bold;">🧭 Abrir Rota no Google Maps →</a>
        </div>
        """, unsafe_allow_html=True)