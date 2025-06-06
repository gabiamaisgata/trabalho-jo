import streamlit as st
import random
# Título do aplicativo
st.title("👗 Recomendador de Looks")
st.markdown("Escolha uma ocasião e receba uma sugestão de look estiloso!")
# Dicionário com sugestões de looks por ocasião
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
# Caixa de seleção para a ocasião
opcao = st.selectbox("Escolha a ocasião:", list(looks.keys()))
# Botão para gerar sugestão
if st.button("Me dá uma sugestão!"):
   sugestao = random.choice(looks[opcao])
   st.success(f"Para **{opcao}**, você pode usar:\n\n👗 {sugestao}")
