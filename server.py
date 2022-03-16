from deta import Deta
from numpy import true_divide
from estado_trafico import estado_trafico
i=1
while True:
    
    y = str(i)
    resultado_trafico = estado_trafico()
    valor = resultado_trafico['resultado']

    deta = Deta("b0rw9zgd_pktn6z7Yy9n2gZqY7ssHDzcS8UYXsAVF")

    registro_trafico = deta.Base("registro_trafico")

    i=i+1
    registro_trafico.put({'resultado':valor}, y)
    

