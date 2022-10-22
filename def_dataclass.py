# -*- coding: utf-8 -*-


from dataclasses import dataclass


# parametres
@dataclass
class info_values:
    info: str
    nb: int


# ma fonction
def info(message, indice):
    info = 'voici mon info  ' + message + ' indice: ' + str(indice)
    nb = len(message)
    t = info_values(info, nb)
    return t


# utilisation de ma fonction
myinfo = info('information', 1)

# les valeurs
print('longueur de mon message :', myinfo.nb)
print(myinfo.info)
