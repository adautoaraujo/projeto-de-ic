# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()

# Import your models for use in your script
from db.models import *

# Start of application script (demo code below)
campo1=input("insira seu nome: ")
campo2=int(input("insira sua idade: "))

pessoa=Dado.objects.create(nome = campo1,idade = campo2)
pessoa.save()

lista = Dado.objects.all()
for pessoa in lista:
        print("%s tem %i anos"%(pessoa.nome,pessoa.idade))
