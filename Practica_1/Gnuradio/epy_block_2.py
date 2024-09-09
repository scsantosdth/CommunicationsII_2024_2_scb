"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    
    def __init__(self):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name="e_Acum",  # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.accumulated_value = 0.0  # Inicializamos la acumulación en 0

    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada.
        y0 = output_items[0]  # Señal acumulada
        
        # Acumular la señal y mantener el estado entre llamadas
        y0[:] = np.cumsum(x) + self.accumulated_value
        self.accumulated_value = y0[-1]  # Actualizar la acumulación para la próxima llamada
        
        return len(x)
