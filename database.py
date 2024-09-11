import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

#carregar variáveis do arquivo .env
load_dotenv()

#configuração do banco de dados
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

#função para inserir no banco
def salvar_no_postgre(dados: Vendas):

    #conexão com banco
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )

        cursor = conn.cursor()

        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )

        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto
        ))

        conn.commit()
        cursor.close()
        conn.close()

        st.success("Dados salvos no banco com sucesso!")

    except Exception as e:
        st.error(f"Erro ao salvar no banco {e}")



