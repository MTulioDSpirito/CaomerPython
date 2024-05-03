import pandas as pd
from sqlalchemy import create_engine

# Crie o engine de conexão com o banco de dados
engine = create_engine('sqlite:///meu_banco_de_dados.db')  # Substitua por sua string de conexão

# Carregue os arquivos do Excel em DataFrames
df1 = pd.read_excel('animais.xlsx')
df2 = pd.read_excel('Cadastro.xlsx')
df3 = pd.read_excel('Saída.xlsx')

#print(df2)

# Selecione as colunas desejadas
df1 = df1[['Nome2', 'Sexo','Espécie']]  # Substitua pelos nomes das colunas desejadas
df2 = df2[['nome','CPF']]  # Substitua pelos nomes das colunas desejadas
df3 = df3[['ID', 'Datadasaída', 'Evento de saída' , 'ID do tutor' , 'ID do animal', 'Descrição do óbito'   ]]  # Substitua pelos nomes das colunas desejadas

 #Concatene os dataframes
df_total = pd.concat([df1, df2, df3], axis=1)

print(df3)

# Crie o engine de conexão com o banco de dados MySQL
# Substitua 'your_database' pelo nome do seu banco de dados
engine = create_engine('mysql+pymysql://root:@localhost:3306/mycaomer')

# Carregue o DataFrame na tabela SQL
# Substitua 'sua_tabela' pelo nome da tabela que você deseja criar ou atualizar
df_total.to_sql('tabela_nova3', con=engine, if_exists='replace', index=False)

