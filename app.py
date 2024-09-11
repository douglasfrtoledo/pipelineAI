import streamlit as st
from datetime import datetime, time
from pydantic import ValidationError

from contrato import Vendas
from database import salvar_no_postgre

def main():
    st.title("Sistema de CRM")
    
    email = st.text_input("E-mail do vendedor:")
    data = st.date_input("Data da venda:", datetime.now())
    hora = st.time_input("Hora da venda:", value=time(9,0))
    valor = st.number_input("Valor da venda:", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produto:", min_value=0, step=1)
    produto = st.selectbox("Selecione o produto", options=["ZapFlox com Gemini", "ZapFlow com ChatGPT", "ZapFlow com Llama"])
    
    if st.button("Salvar"):

        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
        
            st.write(venda)
            salvar_no_postgre(venda)

        except ValidationError as e:
            st.error(f"Deu erro {e}")

if __name__ == "__main__":
    main()