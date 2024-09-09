"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, window_size=5):  # Tamaño de la ventana ajustable
        gr.sync_block.__init__(
            self,
            name="e_MovingAverage",  # Nombre del bloque
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.window_size = window_size
        self.buffer = np.zeros(self.window_size)  # Buffer circular
        self.index = 0
        self.sum = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]
        N = len(x)

        for i in range(N):
            # Actualizar la suma eliminando el valor más antiguo y añadiendo el nuevo
            self.sum -= self.buffer[self.index]
            self.sum += x[i]
            # Actualizar el buffer
            self.buffer[self.index] = x[i]
            # Calcular el promedio
            y[i] = self.sum / self.window_size
            # Mover el índice circularmente
            self.index = (self.index + 1) % self.window_size

        return N
