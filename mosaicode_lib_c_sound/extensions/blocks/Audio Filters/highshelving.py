#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class HighShelving(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "High Shelving"
        self.label = "HighShelving"
        self.color = "50:150:250:150"
        self.ports = [ {"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                        "name":"input0",
                        "conn_type":"Input",
                        "label":"Sound Value"},
                       {"type":"mosaicode_lib_c_base.extensions.ports.float",
                        "name":"gain",
                        "conn_type":"Input",
                        "label":"Gain"},
                       {"type":"mosaicode_lib_c_base.extensions.ports.float",
                        "name":"cutOff",
                        "conn_type":"Input",
                        "label":"CuttOff"},
                       {"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                        "name":"output0",
                        "conn_type":"Output",
                        "label":"Sound Value"}]

        self.properties = [ {"name": "gain",
                             "label": "Gain",
                             "type": MOSAICODE_FLOAT,
                             "lower": -2147483648,
                             "upper": 2147483647,
                             "step": 1,
                             "value": 0},
                            {"name": "cuttOff",
                             "label": "CuttOff",
                             "type": MOSAICODE_FLOAT,
                             "lower": -2147483648,
                             "upper": 2147483647,
                             "step": 1,
                             "value": 0}]

        self.group = "Audio Filters"
        self.codes["function_declaration"] = ""
        self.codes["declaration"] = "mscsound_highshelving_t *$label$_$id$;\n"

        self.codes["function"] = ""
        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"
        self.codes["setup"] = \
"""
$label$_$id$ = mscsound_create_highshelving(FRAMES_PER_BUFFER);
$label$_$id$->sampleRate = SAMPLE_RATE;
$label$_$id$->gain = $prop[gain]$;
$label$_$id$->cutOff = $prop[cuttOff]$;
"""
