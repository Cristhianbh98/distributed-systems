import pymongo

try:
  conn = pymongo.MongoClient('mongodb://facci:123456@192.168.100.247:27017/?authMechanism=DEFAULT&authSource=dbprueba')
  db = conn['dbprueba']
  col = db['clientes']
  col.insert_one({
    'nombres': 'Cristhian Bacusoy 2',
    'direccion':'Manta',
    'email': 'ctisthian@bacusoy.com',
    'saldo': '1000000000'
  })
  print("User created successfully! :D")
except pymongo.errors.OperationFailure as e:
  print("Could not connect to server: %s" % e)
