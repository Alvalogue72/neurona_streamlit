import streamlit as st

st.image("img/neurona.webp", caption="")
st.title("¡Hola, Neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    
    st.subheader("Una neurona con una entrada y un peso")

    w = st.slider("Peso", 0.0, 5.0)
    x = st.number_input("Introduzca el valor de la entrada")

    if st.button("Calcular la salida"):
        y = x * w
        st.write("La salida de la neurona es:", str(y))
    
with tab2:

    col1, col2 = st.columns(2)

    with col1:
        w0 = st.slider("Peso $w_0$", 0.0, 5.0)
        x0 = st.number_input("Entrada $x_0$")

    with col2:
        w1 = st.slider("Peso $w_1$", 0.0, 5.0)
        x1 = st.number_input("Entrada $x_1$")

    if st.button("Calcular la salida", key="btn2"):
        y = w0 * x0 + w1 * x1
        st.write("La salida de la neurona es:", str(y))

with tab3:
    
    col1, col2, col3 = st.columns(3)

    with col1:
        w0 = st.slider("Peso $w_0$", 0.0, 5.0, key="tab3_w0")
        x0 = st.number_input("Entrada $x_0$", key="tab3_x0")

    with col2:
        w1 = st.slider("Peso $w_1$", 0.0, 5.0, key="tab3_w1")
        x1 = st.number_input("Entrada $x_1$", key="tab3_x1")
    with col3:
        w2 = st.slider("Peso $w_2$", 0.0, 5.0, key="tab3_w2")
        x2 = st.number_input("Entrada $x_2$", key="tab3_x2")

    b = st.number_input("Introduzca el valor del sesgo", key="tab3_b")

    if st.button("Calcular la salida", key="btn3"):
        y = w0 * x0 + w1 * x1 + w2 * x2 + b
        st.write("La salida de la neurona es:", str(y))
