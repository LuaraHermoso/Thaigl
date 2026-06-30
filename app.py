import streamlit as st
import pandas as pd

# 1. Configuração da página e layout inspirado na Tailândia (Cores: Vermelho, Branco, Azul)
st.set_page_config(
    page_title="Thai GL Station",
    page_icon="🇹🇭",
    layout="wide"
)

# Estilização CSS customizada (Layout moderno, sem anúncios, cores da bandeira da Tailândia)
st.markdown("""
    <style>
    /* Fundo Azul Escuro Real */
    .main { background-color: #0A1128; }
    
    /* Títulos e Cabeçalhos em Vermelho e Branco */
    h1 { color: #E01A22 !important; font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 800; text-align: center; }
    h2 { color: #FFFFFF !important; }
    h3 { color: #F4F4F9 !important; border-bottom: 2px solid #E01A22; padding-bottom: 5px; }
    
    /* Cards das Séries */
    .gl-card {
        background-color: #131F42;
        padding: 20px;
        border-radius: 10px;
        border-top: 4px solid #E01A22;
        border-bottom: 4px solid #00247D;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.5);
    }
    
    /* Badges e Tags */
    .badge-shipp {
        background-color: #E01A22;
        color: #FFFFFF;
        padding: 3px 8px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.85rem;
    }
    .badge-ano {
        background-color: #FFFFFF;
        color: #00247D;
        padding: 3px 8px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.85rem;
        border: 1px solid #00247D;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Banco de Dados Oficial com todas as séries solicitadas
dados_gl = [
    {"Título": "Harmony Secret", "Ano": 2026, "Casal/Shipp": "LookmheeSonya", "Elenco": "Lookmhee Punyapat & Sonya Saranphat", "Status": "Futuro Lançamento"},
    {"Título": "Hometown Romance", "Ano": 2026, "Casal/Shipp": "LookmheeSonya", "Elenco": "Lookmhee Punyapat & Sonya Saranphat", "Status": "Futuro Lançamento"},
    {"Título": "Affair", "Ano": 2024, "Casal/Shipp": "LookkaewSonya", "Elenco": "Lookkaew Kamollak & Sonya Saranphat", "Status": "Completo"},
    {"Título": "Enemies With Benefits", "Ano": 2026, "Casal/Shipp": "JanJingJing", "Elenco": "Jan Ployshompoo & JingJing Yu", "Status": "Futuro Lançamento"},
    {"Título": "Pluto", "Ano": 2024, "Casal/Shipp": "NamtanFilm", "Elenco": "Namtan Tipnaree & Film Rachanun", "Status": "Completo"},
    {"Título": "GAP: The Series", "Ano": 2022, "Casal/Shipp": "FreenBecky", "Elenco": "Freen Sarocha & Becky Armstrong", "Status": "Clássico"},
    {"Título": "Blank", "Ano": 2024, "Casal/Shipp": "FayeYoko", "Elenco": "Faye Peraya & Yoko Apasra", "Status": "Completo"},
    {"Título": "Us", "Ano": 2024, "Casal/Shipp": "EmiBonnie", "Elenco": "Emi Thasorn & Bonnie Passanun", "Status": "Completo"},
    {"Título": "Dream (My Marvellous Dream Is You)", "Ano": 2024, "Casal/Shipp": "FayMay", "Elenco": "Fay Kanyaphat & May Yada", "Status": "Completo"},
    {"Título": "23.5 Degrees", "Ano": 2024, "Casal/Shipp": "MilkLove", "Elenco": "Milk Pansa & Love Pattranite", "Status": "Completo"},
    {"Título": "The Secret of Us", "Ano": 2024, "Casal/Shipp": "LingOrm", "Elenco": "Lingling Kwong & Orm Kornnaphat", "Status": "Completo"},
    {"Título": "Girl Rules", "Ano": 2026, "Casal/Shipp": "NamtanFilm / MilkLove", "Elenco": "Namtan, Film, Milk, Love, View, Mim", "Status": "Futuro Lançamento"},
    {"Título": "Dangerous Queen", "Ano": 2026, "Casal/Shipp": "A definir", "Elenco": "Elenco Tailandês", "Status": "Em Produção"},
    {"Título": "My Safe Zone", "Ano": 2025, "Casal/Shipp": "A definir", "Elenco": "Elenco Tailandês", "Status": "Anunciado"},
    {"Título": "Reverse of You", "Ano": 2024, "Casal/Shipp": "MaeFahn", "Elenco": "Christine Marie & Mae Nisachon", "Status": "Completo"},
    {"Título": "Player", "Ano": 2025, "Casal/Shipp": "A definir", "Elenco": "Elenco Tailandês", "Status": "Anunciado"},
    {"Título": "The Loyal Pin", "Ano": 2024, "Casal/Shipp": "FreenBecky", "Elenco": "Freen Sarocha & Becky Armstrong", "Status": "Completo"},
    {"Título": "The Air", "Ano": 2026, "Casal/Shipp": "Elementos", "Elenco": "Elenco Tailandês", "Status": "Em Produção"},
    {"Título": "The Water", "Ano": 2026, "Casal/Shipp": "Elementos", "Elenco": "Elenco Tailandês", "Status": "Em Produção"},
    {"Título": "The Fire", "Ano": 2026, "Casal/Shipp": "Elementos", "Elenco": "Elenco Tailandês", "Status": "Em Produção"},
    {"Título": "The Earth", "Ano": 2026, "Casal/Shipp": "Elementos", "Elenco": "Elenco Tailandês", "Status": "Em Produção"},
    {"Título": "Whale Store xoxo", "Ano": 2025, "Casal/Shipp": "MilkLove", "Elenco": "Milk Pansa & Love Pattranite", "Status": "Em Lançamento"},
    {"Título": "Petrichor The Series", "Ano": 2025, "Casal/Shipp": "A definir", "Elenco": "Elenco Tailandês", "Status": "Anunciado"},
    {"Título": "Denied Love", "Ano": 2025, "Casal/Shipp": "A definir", "Elenco": "Elenco Tailandês", "Status": "Anunciado"},
    {"Título": "Somewhere Somehow", "Ano": 2026, "Casal/Shipp": "A definir", "Elenco": "Elenco Tailandês", "Status": "Em Produção"},
    {"Título": "Ditto", "Ano": 2025, "Casal/Shipp": "A definir", "Elenco": "Elenco Tailandês", "Status": "Anunciado"},
    {"Título": "Her", "Ano": 2026, "Casal/Shipp": "A definir", "Elenco": "Elenco Tailandês", "Status": "Em Produção"},
    {"Título": "Bake Love Feeling", "Ano": 2025, "Casal/Shipp": "A definir", "Elenco": "Elenco Tailandês", "Status": "Anunciado"},
    {"Título": "Love’s Echoes", "Ano": 2026, "Casal/Shipp": "A definir", "Elenco": "Elenco Tailandês", "Status": "Em Produção"},
    {"Título": "Moonshadow", "Ano": 2026, "Casal/Shipp": "A definir", "Elenco": "Elenco Tailandês", "Status": "Em Produção"}
]

df = pd.DataFrame(dados_gl)

# 3. Cabeçalho Principal do App
st.title("🇹🇭 THAI GL STATION")
st.markdown("<p style='text-align: center; color: #FFFFFF;'>⚡ <b>Diferencial:</b> Hub de Conteúdo Premium 100% Livre de Anúncios e Comercialização</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. SISTEMA DE PÁGINAS (Abas para organizar o conteúdo)
aba_inicio, aba_catalogo, aba_filtros = st.tabs(["🏠 Início / Novidades", "📚 Catálogo Completo", "🔍 Filtros Avançados"])

# --- PÁGINA 1: INÍCIO ---
with aba_inicio:
    st.subheader("🔥 Lançamentos e Destaques 2026")
    st.write("Fique por dentro dos títulos que estão movimentando as telas este ano:")
    
    df_2026 = df[df["Ano"] == 2026]
    col_novidades = st.columns(2)
    for idx, row in df_2026.head(4).iterrows():
        with col_novidades[idx % 2]:
            st.markdown(f"""
            <div class="gl-card">
                <h3>{row['Título']}</h3>
                <p><b>🎭 Elenco:</b> {row['Elenco']}</p>
                <p><span class="badge-ano">📅 {row['Ano']}</span> <span class="badge-shipp">⚓ {row['Casal/Shipp']}</span></p>
            </div>
            """, unsafe_allow_html=True)

# --- PÁGINA 2: CATÁLOGO COMPLETO ---
with aba_catalogo:
    st.subheader("📋 Todas as Séries Cadastradas")
    st.write(f"Atualmente organizando um acervo com {len(df)} produções originais.")
    
    for idx, row in df.iterrows():
        st.markdown(f"""
        <div class="gl-card">
            <h3 style="margin-top:0;">{row['Título']}</h3>
            <p style="margin-bottom:8px;"><b>🎭 Estrelando:</b> {row['Elenco']}</p>
            <div>
                <span class="badge-ano">📅 Ano: {row['Ano']}</span>
                <span class="badge-shipp">⚓ Casal: {row['Casal/Shipp']}</span>
                <span style="background-color:#00247D; color:white; padding:3px 8px; border-radius:5px; font-size:0.85rem;">📌 {row['Status']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- PÁGINA 3: FILTROS AVANÇADOS (Por Ano ou Casal) ---
with aba_filtros:
    st.subheader("🔍 Encontre sua série ideal")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        lista_anos = sorted(df["Ano"].unique(), reverse=True)
        ano_selecionado = st.selectbox("📅 Selecione o Ano de Lançamento:", ["Todos"] + list(lista_anos))
        
    with col_f2:
        busca_casal = st.text_input("⚓ Digite o nome do Casal / Shipp (Ex: MilkLove, LingOrm):")

    # Aplicando os filtros
    df_filtrado = df.copy()
    if ano_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Ano"] == ano_selecionado]
    if busca_casal:
        df_filtrado = df_filtrado[df_filtrado["Casal/Shipp"].str.contains(busca_casal, case=False)]

    st.markdown("---")
    st.write(f"💡 Encontradas {len(df_filtrado)} séries com esses filtros:")
    
    if df_filtrado.empty:
        st.info("Nenhuma série encontrada com esses critérios. Tente outra busca, Noah!")
    else:
        for idx, row in df_filtrado.iterrows():
            st.markdown(f"""
            <div class="gl-card">
                <h3>{row['Título']}</h3>
                <p><b>🎭 Elenco:</b> {row['Elenco']}</p>
                <p><span class="badge-ano">📅 {row['Ano']}</span> <span class="badge-shipp">⚓ {row['Casal/Shipp']}</span></p>
            </div>
            """, unsafe_allow_html=True)