import streamlit as st
from database import add_hermano, get_hermanos

def main():
    st.title("Ministra con Amor")

    menu = ["Inicio", "Registrar Hermano", "Ver Hermanos"]
    choice = st.sidebar.selectbox("Selecciona una opción", menu)

    if choice == "Inicio":
        st.subheader("Bienvenido a Ministra con Amor")
        st.write("Esta aplicación te ayudará a registrar y hacer seguimiento del crecimiento espiritual de los hermanos.")

    elif choice == "Registrar Hermano":
        st.subheader("Registrar un Nuevo Hermano")
        nombre = st.text_input("Nombre")
        direccion = st.text_input("Dirección")
        telefono = st.text_input("Teléfono")
        correo = st.text_input("Correo Electrónico")
        necesidades = st.text_area("Necesidades Espirituales")

        if st.button("Registrar"):
            add_hermano(nombre, direccion, telefono, correo, necesidades)
            st.success("Hermano registrado exitosamente!")

    elif choice == "Ver Hermanos":
        st.subheader("Lista de Hermanos Registrados")
        hermanos = get_hermanos()
        for hermano in hermanos:
            st.write(f"Nombre: {hermano[1]}, Dirección: {hermano[2]}, Teléfono: {hermano[3]}, Correo: {hermano[4]}, Necesidades: {hermano[5]}")

if __name__ == "__main__":
    main()