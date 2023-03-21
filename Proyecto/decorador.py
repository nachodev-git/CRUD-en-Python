from datetime import datetime
from os.path import dirname
from os.path import join
from os.path import abspath
    

def get_logger(fn):
    
    def interno(*args, **kwargs):
        ruta = dirname(abspath(__file__))
        execute = fn(*args, **kwargs)
        log = join(ruta, "log_movimientos.txt")
        archivo = open(log, "a")
        fecha_y_hora = datetime.now()
        operacion = fn.__name__.upper()

        if operacion == 'alta':
            valores = 'cuilcuit: "{0}" - razonsocial: "{1}" - direccion: "{2}" - telefono: "{3}" - mail: "{4}"'.format(
                args[1],
                args[2],
                args[3],
                args[4],
                args[5]
            )
        elif operacion == 'baja':
            valores = 'Id: "{0}"' .format(
                args[1]
            )      
        elif operacion == 'modificar':
            valores = 'cuilcuit: "{0}" - razonsocial: "{1}" - direccion: "{2}" - telefono: "{3}" - mail: "{4}"'.format(
                args[1],
                args[2],
                args[3],
                args[4],
                args[5]                    
            )   
        else:
            valores = args[1]

        msg = "{0}-{1}-{2} {3} | {4} | {5}".format(
            fecha_y_hora.strftime('%Y'),
            fecha_y_hora.strftime('%m'),
            fecha_y_hora.strftime('%d'),
            fecha_y_hora.strftime('%X'),
            operacion,
            valores
        )
        print('-' * 79 + '\n' + msg, file = archivo)    
    
        print('Registro Ejecutado ({0}): {1}'.format(fn.__name__, fecha_y_hora))
        
        return execute
         
    return interno

