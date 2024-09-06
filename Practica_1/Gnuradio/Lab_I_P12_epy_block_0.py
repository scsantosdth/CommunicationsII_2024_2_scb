import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    
    def __init__(self):
        # solo argumentos por defecto aquí
        gr.sync_block.__init__(
            self,
            name='Acomulador',  # nombre que aparecerá en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y0 = output_items[0]  # Señal acumulada
        y0[:] = np.cumsum(x)  # Acumula la señal de entrada
        
        return len(y0)  # Devolver la longitud de la señal de salida

