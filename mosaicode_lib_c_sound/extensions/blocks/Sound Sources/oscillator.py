#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Oscillator(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Oscillator"
        self.label = "Oscillator"
        self.color = "228:242:73:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                       "name":"input0",
                       "conn_type":"Input",
                       "label":"Sound Value"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"input1",
                       "conn_type":"Input",
                       "label":"Frequency Value"},
                       {"type":"mosaicode_lib_c_base.extensions.ports.string",
                        "name":"type",
                        "conn_type":"Input",
                        "label":"Oscillator Type"},
                      {"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                       "name":"output0",
                       "conn_type":"Output",
                       "label":"Sound Value"}]

        self.properties = [{"name": "input1",
                            "label": "Frequency Value",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                             "upper": 20000,
                            "step": 1,
                            "value": 440
                            },
                           {"name": "type",
                            "label": "Type",
                            "type": MOSAICODE_COMBO,
                            "values": ["square",
                                       "sine",
                                       "sawtooth",
                                       "triangle"],
                            "value": "sine"
                            }]
        self.group = "Sound Sources"
        self.codes["declaration"] = \
"""
mscsound_osc_t *$label$_$id$;
void $port[input1]$(float value){
    *($label$_$id$->input1) = value;
}

void $port[type]$(char *value){
    strcpy(*($label$_$id$->type), \"value\");
}
"""
        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"

        self.codes["setup"] = \
"""
$label$_$id$ = mscsound_create_osc(\"$prop[type]$\", FRAMES_PER_BUFFER, 2048);
$label$_$id$->input0 = NULL;
$label$_$id$->sampleRate = SAMPLE_RATE;
$label$_$id$->input1 = malloc(sizeof(float));
*($label$_$id$->input1) = $prop[input1]$;
"""
