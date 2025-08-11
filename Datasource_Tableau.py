import pandas as pd
import numpy as np
import random

# Número de linhas
n_linhas = 10000

# Listas fixas
SALES_YEAR = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
MARKET_SEGMENT = ["Automóveis", "Caminhões", "Motos", "Máquinas Agrícolas", "Ônibus", "Tratores", "Vans", "SUVs", "Veículos Elétricos", "Veículos Comerciais"]
PRODUCT_NAME = ["Pneu", "Motor", "Bateria", "Volante", "Caixa de Câmbio", "Filtro de Ar", "Suspensão", "Sistema de Freio", "Radiador", "Retrovisor"]
CUSTOMER_NAME = [f"Cliente {i}" for i in range(1, 11)]
FIRST_SALES_YEAR = SALES_YEAR
COUNTRY = ["Brasil", "Argentina", "Equador", "Uruguai", "Colombia", "Venezuela", "Republica Dominicana", "Guatemala", "Costa Rica", "Mexico", "Estados Unidos",
           "Canada", "Alemanha", "Holanda", "Belgica", "Espanha", "Japao", "China", "Vietna", "Coreia do Sul", "India", "França", "Itália", "Africa do Sul",
           "Costa do Marfim", "Angola", "Moçambique", "Cabo Verde", "Senegal", "Gana", "Nigeria", "Quenia", "Tanzania", "Uganda", "Zambia", "Zimbabwe",
           "Arabia Saudita", "Emirados Árabes Unidos", "Australia", "Nova Zelandia", "Reino Unido", "Irlanda", "Russia", "Polonia", "Republica Tcheca",
           "Suecia", "Noruega", "Dinamarca", "Finlandia"]
DESTINY_REGION = ["America do Sul", "America do Norte", "Europa", "Asia", "Africa", "Oceania", "Oriente Medio", "Europa Oriental", "Asia", "Caribe"]
HVA_CLASSIFICATION = ["HVA+", "HVA", "Médio", "Baixo", "Premium", "Standard", "Econômico", "Industrial", "Exportação", "Doméstico"]
ORIGINAL_DATABASE = ["Sistema A", "Sistema B", "Sistema C", "ERP1", "ERP2", "Planilha 2020", "Planilha 2021", "Importação CSV", "Integração API", "Base Histórica"]
SCENARIO = ["Actual", "Rolling Forecast", "Budget"]
FAMILY = ["Linha Pesada", "Linha Leve", "Linha Elétrica", "Linha Diesel", "Linha Híbrida", "Linha Compacta", "Linha SUV", "Linha Utilitária", "Linha Esportiva", "Linha Comercial"]
TYPE_OF_MARGIN = ["Additional", "Replacement"]

# Criação do DataFrame
df_sintetico = pd.DataFrame({
    "SALES YEAR": np.random.choice(SALES_YEAR, n_linhas),
    "MARKET SEGMENT": np.random.choice(MARKET_SEGMENT, n_linhas),
    "PRODUCT NAME": np.random.choice(PRODUCT_NAME, n_linhas),
    "CUSTOMER NAME": np.random.choice(CUSTOMER_NAME, n_linhas),
    "FIRST SALES YEAR": np.random.choice(FIRST_SALES_YEAR, n_linhas),
    "COUNTRY": np.random.choice(COUNTRY, n_linhas),
    "DESTINY REGION": np.random.choice(DESTINY_REGION, n_linhas),
    "VOLUME(tons)": np.random.randint(1, 1000, n_linhas),
    "REVENUE(USD)": np.round(np.random.uniform(1000, 1000000, n_linhas), 2),
    "COMA(USD)": np.round(np.random.uniform(1000, 100000, n_linhas), 2),
    "HVA CLASSIFICATION": np.random.choice(HVA_CLASSIFICATION, n_linhas),
    "HVA": np.random.choice(["Sim", "Não"], n_linhas),
    "ORIGINAL DATABASE": np.random.choice(ORIGINAL_DATABASE, n_linhas),
    "SCENARIO": np.random.choice(SCENARIO, n_linhas),
    "FAMILY": np.random.choice(FAMILY, n_linhas),
    "TYPE OF MARGIN": np.random.choice(TYPE_OF_MARGIN, n_linhas)
})


# Salvar no Excel
df_sintetico.to_excel("dados_sinteticos_personalizados.xlsx", index=False)

print("Base sintética criada e salva em 'dados_sinteticos_personalizados.xlsx'")