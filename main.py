import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1aKOy3VdQbEk7Dc7jTVahAHoPXt5NW9b1sk34Gn4jglQ"
SAMPLE_RANGE_NAME = "Folha1!A1:C14"


def main():
    creds = None

    if os.path.exists("token.json"):

        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  #Se não houver credenciais (válidas) disponíveis, permita que o usuário efetue login.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("Credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Salva as credenciais para a próxima execução
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        #Ler informaçoes no googlesheets

        sheet = service.spreadsheets()
        result = (sheet.values().get(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, 
            range=SAMPLE_RANGE_NAME).execute())

        valores = result['values']
        #print(valores)

        # #Adiciona/editar informaçoes no googlesheets
        # sheet = service.spreadsheets()
        # valores_adicionados = [
        #     ['Dezembro', 'R$ 127.300,15'],
        #     ['Janeiro', 'R$ 100.000,00']
        # ]
        # result = (sheet.values().update(
        #     spreadsheetId=SAMPLE_SPREADSHEET_ID, 
        #     range="A13", 
        #     valueInputOption = "USER_ENTERED",
        #     body= {'values': valores_adicionados}).execute())
        valores_adicionados = [
            ['Imposto'],

        ]

        for i, linha in enumerate(valores):
            if i > 0:
                vendas = linha[1]
                vendas = float(vendas.replace('R$', '').replace('.', '').replace(',', '.'))
                imposto = vendas * 0.10
                imposto = f"R$ {imposto:.2f}".replace('.',',')
                valores_adicionados.append([imposto])
        print(valores_adicionados)

        #Adiciona/editar informaçoes no googlesheets

        result = (sheet.values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, 
            range="C1", 
            valueInputOption = "USER_ENTERED",
            body= {'values': valores_adicionados}).execute())


    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()

