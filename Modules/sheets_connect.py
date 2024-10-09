import google.auth
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


# Ruta del archivo de las credenciales de JSON
SERVICE_ACCOUNT_FILE = r"../Controllers/key_sheets.json"

# Esta estructura nos permite validar los permisos de escritura y 
# lectura de Google Sheets
SCOPES_URL = ['https://www.googleapis.com/auth/spreadsheets']

credencial_user = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES_URL
    )
# El id de la hoja de calculo
SPREADSHEETS_ID = "1Y4y0HzIXyS2CYrO-hAW3vmAPeJBXJXzm0DHz7_U3IMM"

# Rango de celdas seleccionadas
RANGE_NAME = "Hoja 1!A1:A2"

# Conexión a el servicio de google sheets
service_account = build("sheets",'v4',credentials=credencial_user)
data_sheet = service_account.spreadsheets()





