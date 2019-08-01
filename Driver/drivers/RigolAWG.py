import numpy as np

from ..BaseDriver import visaDriver, QReal


class Driver(visaDriver):
    support_models = ['DG1062Z']

    quants = [
        # Set the waveform offset voltage of the specified channel.
        # Query the waveform offset voltage of the specified channel.
        # QReal('Voltage_Offset', unit='VDC',
        #   set_cmd=':SOUR1:VOLT:OFFS %(value).8e%(unit)s',
        #   get_cmd=':SOUR1:VOLT:OFFS?'),

        # Set the waveform of the specified channel to DC with the specified offset.
        QReal('Offset',
              value=0,
              unit='VDC',
              ch=1,
              set_cmd=':SOUR%(ch)d:APPL:DC 1,1, %(value).8e%(unit)s',
              get_cmd=''),

        # QOption('Output',
        #   set_cmd=':OUTP %(option)s', options=[('OFF', 'OFF'), ('ON', 'ON')]),
    ]
