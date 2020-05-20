#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import sys

class ADSR(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "ADSR"
        self.label = "ADSR"
        self.color = "20:17:58:150"
        self.ports = [ {"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                        "name":"input0",
                        "conn_type":"Input",
                        "label":"Sound Value"},
                       {"type":"mosaicode_lib_c_base.extensions.ports.float",
                        "name":"attack",
                        "conn_type":"Input",
                        "label":"Attack"},
                       {"type":"mosaicode_lib_c_base.extensions.ports.float",
                        "name":"decay",
                        "conn_type":"Input",
                        "label":"Decay"},
                        {"type":"mosaicode_lib_c_base.extensions.ports.float",
                         "name":"sustain",
                         "conn_type":"Input",
                         "label":"Sustain"},
                        {"type":"mosaicode_lib_c_base.extensions.ports.float",
                         "name":"release",
                         "conn_type":"Input",
                         "label":"Release"},
                        {"type":"mosaicode_lib_c_base.extensions.ports.float",
                         "name":"gain",
                         "conn_type":"Input",
                        "label":"Gain"},
                        {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                         "name":"play",
                         "conn_type":"Input",
                        "label":"Play"},
                        {"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                         "name":"output0",
                         "conn_type":"Output",
                         "label":"Sound Value"}]

        self.properties = [{"name": "attack",
                             "label": "Attack",
                             "type": MOSAICODE_FLOAT,
                             "lower": 0,
                             "upper": sys.float_info.max,
                             "step": 1,
                             "value": 0},
                            {"name": "decay",
                             "label": "Decay",
                             "type": MOSAICODE_FLOAT,
                             "lower": 0,
                             "upper": sys.float_info.max,
                             "step": 1,
                             "value": 0},
                            {"name": "sustain",
                             "label": "Sustain",
                             "type": MOSAICODE_FLOAT,
                             "lower": 0,
                             "upper": sys.float_info.max,
                             "step": 1,
                             "value": 0},
                            {"name": "release",
                             "label": "Release",
                             "type": MOSAICODE_FLOAT,
                             "lower": 0,
                             "upper": sys.float_info.max,
                             "step": 1,
                             "value": 0},
                            {"name": "gain",
                             "label": "Gain",
                             "type": MOSAICODE_FLOAT,
                             "lower": 0,
                             "upper": 1,
                             "step": 0.1,
                             "value": 0.7}]

        self.group = "Envelopes"

        self.codes["declaration"] = \
"""
mscsound_adsr_t *$label$_$id$;

void $port[attack]$(float value){
    *($label$_$id$->attack) = value;
}

void $port[decay]$(float value){
    *($label$_$id$->decay) = value;
}

void $port[sustain]$(float value){
    *($label$_$id$->sustain) = value;
}

void $port[release]$(float value){
    *($label$_$id$->release) = value;
}

void $port[gain]$(float value){
    *($label$_$id$->gain) = value;
}

void $port[play]$(int value){
    *($label$_$id$->play) = (value && value);
}
"""


        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"
        self.codes["setup"] = \
"""
$label$_$id$ = mscsound_create_adsr(SAMPLE_RATE, FRAMES_PER_BUFFER);
$label$_$id$->attack = calloc(1, sizeof(float));
*($label$_$id$->attack) = $prop[attack]$;
$label$_$id$->decay = calloc(1, sizeof(float));
*($label$_$id$->decay) = $prop[decay]$;
$label$_$id$->sustain = calloc(1, sizeof(float));
*($label$_$id$->sustain) = $prop[sustain]$;
$label$_$id$->release = calloc(1, sizeof(float));
*($label$_$id$->release) = $prop[release]$;
$label$_$id$->gain = calloc(1, sizeof(float));
*($label$_$id$->gain) = $prop[gain]$;
$label$_$id$->play = calloc(1, sizeof(int));
"""
