import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi Sitio Web Estático", layout="wide")

# Encabezado
st.markdown("<h1 style='text-align:center; color:#0078D7;'>Bienvenido a mi sitio</h1>", unsafe_allow_html=True)

# Barra de navegación simulada
st.markdown("""
<div style='text-align:center;'>
    <a href='#inicio' style='margin:15px;'>Inicio</a>
    <a href='#sobre' style='margin:15px;'>Sobre mí</a>
    <a href='#contacto' style='margin:15px;'>Contacto</a>
</div>
""", unsafe_allow_html=True)

# Sección Inicio
st.markdown("## 🏠 Inicio")
st.write("Este es mi sitio web desplegado en la nube usando Streamlit Community Cloud.")

# Sección Sobre mí
st.markdown("## 👨‍💻 Sobre mí")
st.write("Soy Ángel Ricardo Pineda Díaz, estudiante de Computación en la Nube en la Universidad Tecnológica de Honduras (UTH).")

# Sección Contacto
st.markdown("## 📬 Contacto")
st.write("Correo: ejemplo@correo.com")

# Pie de página
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>© 2026 Ángel Ricardo Pineda Díaz</p>", unsafe_allow_html=True)
