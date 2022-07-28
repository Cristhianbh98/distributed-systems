import pymongo
import time

TOTAL_ENTRIES = 100
CONECTION_URI = 'mongodb://administrador:123456@server-quito,server-manta,serverguayaquil/?authMechanism=DEFAULT&readPreference=primary&replicaSet=rsfacci'

# Get collecion database
conn = pymongo.MongoClient(CONECTION_URI)
col = conn['dbpractica']['entradas']

for i in range(0, TOTAL_ENTRIES):
  try:
    title = 'Entrada #%s' %(i + 1)
    col.insert_one({
      'title': title
    })
    print (title + " creado correactamente")
  except pymongo.errors.OperationFailure as e:
    print("Could not connect to server: %s" % e)
  time.sleep(1)
