import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        # Solo argumentos por defecto aquí
        gr.sync_block.__init__(
            self,
            name='Diferenciador',  # Nombre que aparecerá en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        
        # Atributo inicializado fuera de la llamada a __init__
        self.acum_anterior = 0

    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y0 = output_items[0]  # Señal acumulada diferencial

        N = len(x)

        # Cálculo de la diferencia acumulada
        diff = np.cumsum(x) - self.acum_anterior
        self.acum_anterior = np.cumsum(x)[-1]  # Guardar el último valor acumulado

        # Asignar el resultado a la salida
        y0[:] = diff

        return len(x)  # Retorna la longitud de la señal de entrada procesada
