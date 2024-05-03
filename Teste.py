import pandas as pd
from sqlalchemy import create_engine

# Crie o engine de conexão com o banco de dados
engine = create_engine('mysql+pymysql://root:@localhost:3306/mycaomer')

# Carregue os arquivos do Excel em DataFrames
df1 = pd.read_excel('animais.xlsx')
df2 = pd.read_excel('Cadastro.xlsx')
df3 = pd.read_excel('Saída.xlsx')

# Selecione as colunas desejadas
df1 = df1[['Nome2', 'Sexo', 'Espécie', 'Idade estimada']]
df2 = df2[['nome', 'CPF']]
df3 = df3[['ID', 'ID do animal', 'ID do tutor', 'Evento de saída', 'Datadasaída']]

# Renomeie as colunas para corresponder aos nomes desejados na tabela final
df1.columns = ['nome_animal', 'sexo', 'especie', 'idade estimada']
df2.columns = ['nome_tutor', 'CPF']
df3.columns = ['ID', 'ID_animal', 'ID_tutor', 'Evento de saída', 'Datadasaída']

# Concatene os dataframes
df_total = pd.concat([df3, df1, df2], axis=1)

# Reordene as colunas para a ordem desejada
df_total = df_total[['ID', 'ID_animal', 'nome_animal', 'sexo', 'especie', 'idade estimada', 'ID_tutor', 'nome_tutor', 'CPF', 'Evento de saída', 'Datadasaída']]

# Carregue o DataFrame na tabela SQL
df_total.to_sql('tabela_fato', con=engine, if_exists='replace', index=False)
