import json
import os
import shutil
import tempfile

def rewriteJsonFile(sourceObj, targetFilePath):
  temp = tempfile.NamedTemporaryFile()
  tempHandle = os.fdopen(temp, 'w')
  tempFilePath = temp.name
  json.dump(sourceObj, tempHandle)
  tempHandle.close()
  shutil.move(tempFilePath, targetFilePath)
  print(temp.name)

nome = {
            "nome": 'Henrique',
            "cpf": '465.123.348-17',
            "senha": '5564',
            "dinheiro": 30000,
            "num": '4030-8'
        }

rewriteJsonFile(nome, './')
print(nome)