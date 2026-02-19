from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account


def obtener_interaction_gifs():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    KEY = 'key.json'
    # Escribe aquí el ID de tu documento:
    SPREADSHEET_ID = '10Ow8H_1tvu85H2SNn9274FAm23iG0MY70YEEM07YqZ8'

    creds = None
    creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # Llamada a la api
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='InteractionGifs!A1:11').execute()
    # Extraemos values del resultado
    values = result.get('values',[])
    return values