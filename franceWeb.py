import requests
import shutil

url = "https://service.annuaire.sante.fr/annuaire-sante-webservices/V300/services/extraction/PS_LibreAcces"
caCert = "C:\\Users\\dmiro\\Downloads\\Chaine_de_certification-IGC-Sante.pem"

local_filename = "C:\\Users\\dmiro\\FranceData2.zip"
with requests.get(url, verify=caCert) as r:
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)