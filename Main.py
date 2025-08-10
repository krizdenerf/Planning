
import json


from datetime import datetime

datedujour = datetime.now()
today = datedujour.strftime("%d/%m")

#var date recup la date et l’heure
#var today recup le format jour/mois
#Aniki est une table clé/valeur

Aniki = {
    "09/08":"too late",
    "10/08":"first try",
    "11/08":"second try",
    "12/08":"still working?",
    "13/08":"last day"
  }

message = Aniki.get(today,"0 et big bang")

output = {
    "date": today
    "message": message
}

print(json.dumps(output,ensure_ascii=false))
