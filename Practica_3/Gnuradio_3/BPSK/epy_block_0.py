import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is an RF Voltage-Controlled Oscillator (VCO) that generates a sinusoidal signal with a frequency controlled by the input signals. 

    Parameters:
    - fc (Carrier Frequency): This sets the base frequency (in Hz) of the oscillator. The default is set to 128 kHz.
    - samp_rate (Sampling Rate): Defines the number of samples per second used by the system, defaulted to 320 kHz.

    Inputs:
    - The first input (A): Controls the amplitude of the output signal. This input determines the strength of the signal.
    - The second input (Q): Acts as the phase offset, modulating the phase of the generated signal.

    Output:
    - The output is a sinusoidal signal with the amplitude controlled by the first input and phase modulated by the second input. The frequency of the signal is based on the carrier frequency 'fc' and the phase shift 'Q'.

    Recommended Usage:
    - This block is typically used in RF applications where a variable frequency or phase-controlled signal is needed, such as in modulation schemes.
    """

    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.samp_rate = samp_rate
        self.n_m=0

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        n=np.linspace(self.n_m,self.n_m+N-1,N)
        self.n_m += N
        y[:]=A*np.cos(2*math.pi*self.fc*n/self.samp_rate+Q)
        return len(output_items[0])


