import streamlit as st
import random
import time

def main():
    st.set_page_config(page_title="Валентинка", page_icon="❤️")

    # Анімація сердечок
    st.markdown(
        """
        <style>
        body {
            background-color: #ffc0cb;
            overflow: hidden;
        }
        .heart {
            color: red;
            font-size: 24px;
            animation: float 4s infinite ease-in-out;
            position: absolute;
        }
        @keyframes float {
            0% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0); }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Валентинка")

    if "scene" not in st.session_state:
        st.session_state.scene = "first"

    if st.session_state.scene == "first":
        st.subheader("Віриш в кохання з першого погляду чи мені пройти ще раз?")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Вірю"):
                st.session_state.scene = "second"
                st.experimental_rerun()
        with col2:
            if st.button("Не вірю"):
                st.session_state.scene = "second"
                st.experimental_rerun()

    elif st.session_state.scene == "second":
        st.subheader("Ти станеш моєю валентинкою? (Дашка шо за крінж)")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Так"):
                st.session_state.scene = "yes_choice"
                st.experimental_rerun()
        with col2:
            if st.button("Ні"):
                st.session_state.scene = "no_choice"
                st.experimental_rerun()

    elif st.session_state.scene == "yes_choice":
        st.success(
            "Лох згадав що треба жінку любить. Лох молодець. І я тебе також любить (При зустрічі руки поцілую, бо знаю, що ти це не обереш)))"
        )

    elif st.session_state.scene == "no_choice":
        st.markdown(
            """
            <style>
            body {
                background-color: black;
                color: white;
            }
            </style>
            <h1 style="color:white; text-align: center;">Venom</h1>
            <h2 style="color:red; text-align: center;">Ю луз</h2>
            <p style="color:white; text-align: center;">Вітаю, у вас закохався веном і вирішив вас з'їсти, щоб цю красу більше ніхто не бачив) Він ревнує ж! Цьом</p>
            """,
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    main()
