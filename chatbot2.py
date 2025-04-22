#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 10:53:45 2025

@author: juan
"""

# chatbot_chin_chin_streamlit.py

import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Chin Chin: Tu Asistente de Vino", page_icon="🍷", layout="centered")

# Estado de sesión para la bodega y favoritos
if 'bodega' not in st.session_state:
    st.session_state.bodega = ["Viña Sol", "Marqués de Riscal"]
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

st.title("🍷 Chin Chin – Asistente Personal de Vinos")
st.subheader("¿En qué te podemos ayudar hoy como amante del vino?")

opcion = st.sidebar.radio("Menú principal", [
    "Inicio",
    "🔍 Recomendaciones según comida",
    "🛒 Buscar vinos por supermercado",
    "🍇 Ver vinos por tipo y precio",
    "📦 Mi bodega personal",
    "⭐ Mis vinos favoritos",
    "📬 Suscripción mensual",
    "🎉 Actividades y visitas"
])

# === FUNCIONES ===
def recomendaciones_comida():
    st.markdown("### ¿Qué vas a comer hoy?")
    tipo = st.selectbox("Selecciona el tipo de comida:", [
        "Carne roja", "Carne blanca", "Pescado", "Marisco",
        "Pasta", "Queso", "Postre", "Vegetariano"
    ])

    recomendaciones = {
        "Carne roja": "🍷 Un tinto con cuerpo como un Cabernet Sauvignon, Syrah o Ribera del Duero.",
        "Carne blanca": "🍷 Un tinto joven o un blanco con barrica puede combinar muy bien.",
        "Pescado": "🥂 Albariño, Verdejo o Chardonnay sin barrica.",
        "Marisco": "🥂 Vinos blancos frescos como Godello o Rías Baixas.",
        "Pasta": "🍝 Si es con salsa roja, un Chianti; con crema, un Chardonnay.",
        "Queso": "🧀 Tintos maduros o vinos dulces según el tipo de queso.",
        "Postre": "🍮 Un vino dulce como Moscatel, Pedro Ximénez o cava semiseco.",
        "Vegetariano": "🌱 Rosados, blancos aromáticos o espumosos ligeros."
    }

    st.success(recomendaciones[tipo])
    if st.button("Agregar a favoritos"):
        st.session_state.favoritos.append(f"Maridaje para {tipo}: {recomendaciones[tipo]}")
        st.toast("Añadido a favoritos")

def buscar_supermercado():
    supermercado = st.selectbox("Supermercado", ["Mercadona", "Carrefour", "Lidl", "Alcampo", "Otros"])
    precio = st.slider("Selecciona el rango de precio (€)", 2, 20, (5, 15))
    
    st.write(f"Mostrando vinos en **{supermercado}** entre **{precio[0]}€ y {precio[1]}€**:")
    st.info("🍷 *Ejemplos ficticios:*")
    st.markdown("- Viña Albali Reserva – 6,95€ (Carrefour)\n- Castillo de Liria – 3,20€ (Mercadona)\n- Cepa Lebrel Crianza – 4,80€ (Lidl)")

def buscar_por_tipo_precio():
    tipo = st.selectbox("Tipo de vino", ["Tinto", "Blanco", "Rosado", "Espumoso", "Dulce"])
    precio = st.slider("Rango de precio (€)", 3, 50, (6, 20))
    
    st.write(f"Resultados para **{tipo.lower()}s** entre {precio[0]}€ y {precio[1]}€:")
    st.success("🍾 Ejemplo: Marqués de Cáceres Crianza (9,50€), Protos Roble (11€), Enate Chardonnay (14€)")

def mi_bodega():
    st.markdown("### 📦 Tu Bodega")
    for vino in st.session_state.bodega:
        st.write(f"- {vino}")
    
    nuevo = st.text_input("Añade un nuevo vino a tu bodega")
    if st.button("Agregar vino"):
        if nuevo:
            st.session_state.bodega.append(nuevo)
            st.success(f"'{nuevo}' ha sido añadido.")
        else:
            st.warning("Introduce un nombre válido.")

def ver_favoritos():
    st.markdown("### ⭐ Vinos y maridajes favoritos")
    if st.session_state.favoritos:
        for fav in st.session_state.favoritos:
            st.write(f"👉 {fav}")
    else:
        st.info("Aún no has añadido favoritos.")

def suscripcion_mensual():
    st.markdown("""
    ### 📦 Suscripción mensual – Chin Chin Wine Club
    - Cada mes, 3 vinos especialmente seleccionados.
    - Sorpresa temática: tintos, blancos, regiones.
    - Guía de cata incluida.
    - Precio: **24,99€/mes** sin permanencia.

    ¿Te interesa? Contacta desde la app para activar tu suscripción. 🍷
    """)

def actividades_visitas():
    st.markdown("""
    ### 🍇 Actividades disponibles:
    - **Ruta del vino en La Rioja** con visita y cata – 39€
    - **Taller de maridaje** en Barcelona – 29€
    - **Fiesta de vino y tapas** en Madrid – 25€

    Reserva desde nuestra web. ¡Vive la experiencia!
    """)

# === FLUJO PRINCIPAL ===
if opcion == "Inicio":
    st.image("https://cdn.pixabay.com/photo/2017/05/31/14/43/wine-2362129_1280.jpg", use_column_width=True)
    st.markdown("""
    Bienvenido/a a **Chin Chin**, tu asistente digital para el mundo del vino 🍇

    Explora recomendaciones, gestiona tu bodega, descubre nuevos vinos y actividades únicas.
    """)

elif "Recomendaciones" in opcion:
    recomendaciones_comida()

elif "supermercado" in opcion:
    buscar_supermercado()

elif "tipo y precio" in opcion:
    buscar_por_tipo_precio()

elif "bodega personal" in opcion:
    mi_bodega()

elif "favoritos" in opcion:
    ver_favoritos()

elif "Suscripción" in opcion:
    suscripcion_mensual()

elif "Actividades" in opcion:
    actividades_visitas()
