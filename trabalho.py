import streamlit as st

import random

st.set_page_config(page_title="Recomendador de Looks", page_icon="👗")

# Título

st.title("👗 Recomendador de Looks Inteligente")

st.markdown("Monte seu look ideal respondendo a algumas perguntas rápidas!")

# --- Perguntas adicionais ---

opcao = st.selectbox("1️⃣ Qual a ocasião?", [

    "Faculdade", "Escola", "Shopping", "Date", "Praia",

    "Festa / Balada", "Piquenique", "Museu", "Brunch",

    "Churrasco", "Cinema", "Teatro"

])

tempo = st.selectbox("2️⃣ Como está o clima hoje?", [

    "Calor", "Frio", "Ameno", "Chuvoso"

])

horario = st.selectbox("3️⃣ Qual o horário do evento?", [

    "Manhã", "Tarde", "Noite"

])

# --- Look base ---

looks = {

    "Faculdade": [

        "Calça jeans + camiseta básica + tênis",

        "Vestido confortável + jaqueta jeans"

    ],

    "Escola": [

        "Calça de moletom + blusa larga + tênis",

        "Short + camiseta + mochila"

    ],

    "Shopping": [

        "Saia jeans + blusa estilosa + sandália",

        "Calça cargo + cropped + tênis estiloso"

    ],

    "Date": [

        "Vestido midi + salto baixo",

        "Calça de alfaiataria + top + jaqueta de couro"

    ],

    "Praia": [

        "Saída de praia + biquíni + chinelo",

        "Short leve + regata + chapéu"

    ],

    "Festa / Balada": [

        "Vestido colado + salto alto",

        "Top de brilho + saia + bota"

    ],

    "Piquenique": [

        "Vestido floral + tênis",

        "Jardineira + blusa leve"

    ],

    "Museu": [

        "Calça pantalona + regata + sandália",

        "Saia midi + camisa"

    ],

    "Brunch": [

        "Blusa romântica + saia rodada + sapatilha",

        "Macacão + sandália confortável"

    ],

    "Churrasco": [

        "Short jeans + cropped + rasteirinha",

        "Vestido soltinho + tênis"

    ],

    "Cinema": [

        "Calça jeans + blusa quentinha + tênis",

        "Moletom + legging + tênis"

    ],

    "Teatro": [

        "Blazer + vestido + sapato fechado",

        "Macacão + salto"

    ]

}

# --- Paleta de cores de sugestão ---

paletas = {

    "Calor": "https://i.pinimg.com/564x/67/ff/4a/67ff4a35439c31ea2ab53d5eb7e5a0ae.jpg",  # cores quentes

    "Frio": "https://i.pinimg.com/564x/94/49/ba/9449ba7bcb305108de7bde1e43ff635e.jpg",   # cores sóbrias

    "Ameno": "https://i.pinimg.com/564x/cf/99/41/cf99411b1e4f1b8a456cbbed3dbdc7c7.jpg", # tons neutros

    "Chuvoso": "https://i.pinimg.com/564x/79/23/95/792395b59bc25295a2798029e14f2cb1.jpg" # cinzas e escuros

}

# --- Botão ---

if st.button("🎯 Me dá uma sugestão!"):

    look = random.choice(looks[opcao])

    st.markdown(f"### ✅ Sugestão de look para **{opcao}**")

    st.write(f"🕓 Horário: {horario}")

    st.write(f"🌤️ Clima: {tempo}")

    st.success(f"👗 Look sugerido: {look}")

    # Mostrar paleta de cores

    st.markdown("### 🎨 Cores que combinam com o clima de hoje:")

    st.image(paletas[tempo], use_column_width=True)

    st.caption("Use essas cores como base na sua roupa ou nos acessórios!") 
    # Upload de imagem do look do usuário
# Imagens de inspiração para cada ocasião

imagens_look = {

    "Faculdade": "https://i.pinimg.com/564x/86/5b/8c/865b8c60a5e3cf316ac33a22c3012f9d.jpg",

    "Escola": "https://i.pinimg.com/564x/42/8f/5c/428f5c6f3ce88e5820d86ac3dce4c30e.jpg",

    "Shopping": "https://i.pinimg.com/564x/f1/33/61/f133611d54c5f661e4c6d0f4e2d57b3c.jpg",

    "Date": "https://i.pinimg.com/564x/0b/47/74/0b47749634f2ab59cfd2067005b8f13e.jpg",

    "Praia": "https://i.pinimg.com/564x/2b/44/e2/2b44e21d1948f6871eae2b148c561a62.jpg",

    "Festa / Balada": "https://i.pinimg.com/564x/bc/2e/82/bc2e82c8d63741be7ebc9aab39d2a04b.jpg",

    "Piquenique": "https://i.pinimg.com/564x/31/dc/43/31dc438f355bace25b2d4f4f95ed9a95.jpg",

    "Museu": "https://i.pinimg.com/564x/18/7d/3f/187d3fdcc3f338ce3b30cc11e173ea23.jpg",

    "Brunch": "https://i.pinimg.com/564x/52/15/e2/5215e2eb24a6f9ed235d1d7deccc84cb.jpg",

    "Churrasco": "https://i.pinimg.com/564x/9e/23/c6/9e23c60753a3a4a6cde84937cfbd716c.jpg",

    "Cinema": "https://i.pinimg.com/564x/24/93/45/249345b3cc2c3ff0f6e79b986fd12ac9.jpg",

    "Teatro": "https://i.pinimg.com/564x/32/d0/7a/32d07ad38910a978d6c81a9c9aa04123.jpg"

} 

