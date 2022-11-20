# -*- coding: utf-8 -*-


from dataclasses import dataclass, field


# parametres
@dataclass
class info_values:
    message: str
    indice: int
    nb = 0
    params : list = field(default_factory=lambda : [])

    def info_total(self):
        info = 'voici mon info  ' + self.message + ' indice: ' + str(self.indice) + ' longueur:  ' + str(len(self.message))
        self.nb = len(self.message)
        return info


# instanciation
myinfo = info_values('information', 1)
myinfo.params.append('value')
myinfo.params.append('scaling_factor')
myinfo.params.append('offset')

print(myinfo.params)
print(myinfo.params[0])


print(myinfo.params)
print(myinfo)

print(myinfo)

print(myinfo.params.pop())



# les valeurs
print('longueur de mon message :', myinfo.nb)
print(myinfo.info_total())
