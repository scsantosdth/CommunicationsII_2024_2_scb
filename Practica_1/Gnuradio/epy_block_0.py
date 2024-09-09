"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Diff',  # Nombre del bloque en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.prev_value = 0.0  # Almacena el valor anterior

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]
        N = len(x)

        # Concatenar el valor anterior con la señal actual
        concatenated = np.concatenate(([self.prev_value], x))
        # Calcular la diferencia
        diff = np.diff(concatenated)
        # Asignar al buffer de salida
        y[:] = diff
        # Actualizar el valor anterior
        self.prev_value = x[-1]

        return N