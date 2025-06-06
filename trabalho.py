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

st.markdown("### 📸 Quer mostrar seu look?")

foto = st.file_uploader("Envie uma foto da sua roupa ou inspiração (formato .jpg ou .png)", type=["jpg", "jpeg", "png"])

if foto is not None:

    st.image(foto, caption="Seu look enviado!", use_column_width=True)

    st.success("Arrasou! Agora é só combinar com as sugestões que te dei 😍") 
