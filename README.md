# Integra-ao-com-API-GoogleSheets
Introdução
Este projeto fornece uma maneira fácil e eficiente de interagir com a API do Google Sheets usando Python. Com ele, você pode ler, escrever e atualizar dados em suas planilhas de forma simples e automatizada.

🔧 Funcionalidades
Autenticação com a API do Google Sheets
Leitura de dados de uma planilha
Escrita de dados em uma planilha
Atualização de células específicas
Criação de novas planilhas
📝 Como usar
Configuração inicial

Crie um projeto no Google Cloud Console
Ative a API do Google Sheets
Gere credenciais de OAuth 2.0 ou uma chave de API
Faça o download do arquivo
credentials.json
e coloque na pasta do projeto
Instalação

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

Exemplo de uso
from sheets_integration import SheetsClient

# Autenticação
client = SheetsClient('credentials.json')

# Leitura de dados
dados = client.read_sheet(spreadsheet_id='SEU_ID_AQUI', range='A1:D10')
print(dados)

# Escrita de dados
client.write_sheet(spreadsheet_id='SEU_ID_AQUI', range='A1', values=[['Nome', 'Idade'], ['João', 30], ['Maria', 25]])
🛠️ Estrutura do projeto
sheets_integration.py
: principal arquivo com a classe
SheetsClient
que encapsula as operações
examples/
: exemplos de uso
README.md
: este arquivo
📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🤝 Contribuições
Contribuições são bem-vindas! Abra uma issue ou envie um pull request.
