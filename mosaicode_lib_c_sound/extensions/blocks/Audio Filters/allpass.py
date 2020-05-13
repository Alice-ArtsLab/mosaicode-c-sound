#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Allpass(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Allpass"
        self.label = "Allpass"
        self.color = "50:150:250:150"
        self.ports = [ {"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                        "name":"input0",
                        "conn_type":"Input",
                        "label":"Sound Value"},
                       {"type":"mosaicode_lib_c_base.extensions.ports.float",
                        "name":"slope",
                        "conn_type":"Input",
                        "label":"Slope"},
                       {"type":"mosaicode_lib_c_base.extensions.ports.float",
                        "name":"cutOff",
                        "conn_type":"Input",
                        "label":"CuttOff"},
                       {"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                        "name":"output0",
                        "conn_type":"Output",
                        "label":"Sound Value"}]

        self.properties = [{"name": "order",
                             "label": "Order",
                             "type": MOSAICODE_COMBO,
                             "values": ["1","2"],
                             "value": "2"},
                            {"name": "slope",
                             "label": "Slope",
                             "type": MOSAICODE_FLOAT,
                             "lower": -2147483648,
                             "upper": 2147483647,
                             "step": 1,
                             "value": 0},
                            {"name": "cuttoff",
                             "label": "CuttOff",
                             "type": MOSAICODE_FLOAT,
                             "lower": -2147483648,
                             "upper": 2147483647,
                             "step": 1,
                             "value": 0}]

        self.group = "Audio Filters"

        self.codes["declaration"] = \
"""
mscsound_biquad_t *$label$_$id$;

void $port[slope]$(float value){
    *($label$_$id$->slope) = value;
}

void $port[cutOff]$(float value){
    *($label$_$id$->cutOff) = value;
}
"""


        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"
        self.codes["setup"] = \
"""
$label$_$id$ = mscsound_create_biquad(
                               \"allpass\", $prop[order]$, FRAMES_PER_BUFFER);
$label$_$id$->sampleRate = SAMPLE_RATE;
$label$_$id$->slope = calloc(1, sizeof(float));
*($label$_$id$->slope) = $prop[slope]$;
$label$_$id$->cutOff = calloc(1, sizeof(float));
*($label$_$id$->cutOff) = $prop[cuttoff]$;
"""
