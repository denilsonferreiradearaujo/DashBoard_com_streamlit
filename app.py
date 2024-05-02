import streamlit as st
from streamlit_option_menu import option_menu
from dashboards.dashboard import show_dashboard

st.markdown(
    """
    <style>
    .logo {
        position: absolute;
        top: 10px;
        left: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Carregue a imagem usando o caminho relativo ao diretório do seu script
# url = "https://www.imagensempng.com.br/wp-content/uploads/2020/12/logo-claro-png_optimized-1024x900.png"
# st.image(url, use_column_width=True, width=200, caption="Viva o novo!")

# Defina as opções de menu e ícones
menu_options = ["Home", "Settings", "DashBoards"]
menu_icons = ["house", "gear", "bar-chart"]

# Crie o menu na barra lateral
with st.sidebar:
     
    # Captura de imagem local
    image_path = "img/Logo_Uber.png"
    st.image(image_path, use_column_width=True, width=70, caption="")

    # Obtenha a opção selecionada pelo
    selected = option_menu("Menu", menu_options, icons=menu_icons, menu_icon="cast", default_index=0)

# Com base na opção selecionada, exiba o conteúdo correspondente
if selected == "Home":
    st.write("Este é o conteúdo da página Home.")
elif selected == "Settings":
    st.write("Este é o conteúdo da página de Configurações.")
elif selected == "DashBoards":
    show_dashboard()
