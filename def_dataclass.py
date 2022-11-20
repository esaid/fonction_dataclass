# -*- coding: utf-8 -*-


from dataclasses import dataclass


# parametres
@dataclass
class info_values:
    message: str
    indice: int
    nb = 0

    def info_total(self):
        info = 'voici mon info  ' + self.message + ' indice: ' + str(self.indice) + ' longueur:  ' + str(len(self.message))
        self.nb = len(self.message)
        return info


# instanciation
myinfo = info_values('information', 1)

# les valeurs
print('longueur de mon message :', myinfo.nb)
print(myinfo.info_total())
