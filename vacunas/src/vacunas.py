# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "rodma"
__date__ = "$18-oct-2015 16:17:33$"

vacunas=1000
while vacunas>0:
    uso=int(input("Ingrese vacunas utilizadas:"))
    if uso>vacunas or uso<0:
        print"No existe esa cantidad de vacunas ingresadas.( Disponibles:",vacunas,
        print")"
    else:
        if uso==0:
            print"Vacunas disponibles:",vacunas
        else:
            vacunas=vacunas-uso
            if vacunas<200 and vacunas>0:
                print"Aviso!, vacunas disponibles:",vacunas
            else:
                if vacunas<=0:
                    print"Atencion!, no hay vacunas disponibles!"
                    while vacunas<=0:
                        vacunas=input("Ingrese nueva cantidad de vacunas:")
    

    
