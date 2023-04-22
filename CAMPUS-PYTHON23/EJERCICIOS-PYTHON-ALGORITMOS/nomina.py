total_nomina=0
pension_empleados=0
seguridad_social_empleados=0
seguridad_social=0.04
pension=0.04
def validacion_novedad(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            if dato<1 or dato>2:
                print("El numero debe ser 1 o 2")
                continue
            break
        except ValueError:
            print("Debe ser un dato entero")
    return dato
def validacion_entero(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            break
        except ValueError:
            print("El dato a ingresar debe ser entero")
    return dato
def validacion_dias(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            if dato<1 or dato>30:
                print("El numero debe ser de 1 a 30")
                continue
            break
        except ValueError:
            print("Debe ser un dato entero")
    return dato
def validacion_subsidio(subsidio):
    if salario_basico<=1160000:
        subsidio=140000
    else:
        subsidio=0
    return subsidio
n=validacion_entero("Ingrese la cantidad de empleados: ")
for n in range (n):
    cedula=validacion_entero("Ingrese su numero de cedula: ")
    nombre=input("Ingrese su nombre: ")
    direccion=input("Ingrese su direccion: ")
    dias_trabajados=validacion_dias("Ingrese cantidad de dias trabajados: ")
    salario_basico=validacion_entero("Ingrese su salario basico: ")
    total_seguridad_social=salario_basico*seguridad_social
    total_pension=salario_basico*pension
    salario=salario_basico/30*dias_trabajados  
    devengados=salario+validacion_subsidio(salario_basico)
    deducidos=total_seguridad_social+total_pension 
    pension_empleados+=total_pension
    seguridad_social_empleados+=total_seguridad_social
    m=validacion_entero("Ingrese la cantidad novedades de nomina: ")
    for m in range (m):
        tipo_novedad=validacion_novedad("Ingrese el tipo de novedad(1.bonificacion-2.descuentos): ")
        if tipo_novedad==1:
            bonificaciones=validacion_entero("Ingrese el valor de bonificaciones: ")
        if tipo_novedad==2:
            descuentos_particulares=validacion_entero("Ingrese el valor de los descuentos particulares: ")
    t_devengados=devengados+bonificaciones
    t_deducidos=deducidos+descuentos_particulares
    neto_empleado=t_devengados-t_deducidos
    total_nomina+=neto_empleado
    print(f"Total a pagar de {nombre}: ","{:,}".format(neto_empleado))
print("Total de nomina a pagar: ","{:,}".format(total_nomina))
print("Total de pension: ","{:,}".format(pension_empleados))
print("Total de seguridad social: ","{:,}".format(seguridad_social_empleados))
        
    