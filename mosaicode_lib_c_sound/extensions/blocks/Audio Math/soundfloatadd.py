#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class SoundFloatAdd(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Sound Float Addition"
        self.label = "SoundFloatAdd"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                       "name":"input0",
                       "conn_type":"Input",
                       "label":"Sound Value"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"input1",
                       "conn_type":"Input",
                       "label":"Sound Value"},
                      {"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                       "name":"output0",
                       "conn_type":"Output",
                       "label":"Sound Value"}]

        self.properties = [{"name": "input1",
                             "label": "Float Value",
                             "type": MOSAICODE_FLOAT,
                             "lower": -2147483648,
                             "upper": 2147483647,
                             "step": 1,
                             "value": 0}]

        self.group = "Audio Math"
        self.codes["function_declaration"] = ""
        self.codes["declaration"] = \
"""
mscsound_audiofloatmath_t *$label$_$id$;
void $port[input1]$(float value);
"""
        self.codes["function"] =  \
"""
void $port[input1]$(float value){
    $label$_$id$->input1 = value;
}
"""
        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"
        self.codes["setup"] = \
"""
$label$_$id$ = mscsound_create_audiofloatmath(
FRAMES_PER_BUFFER, mscsound_add_freq_float);
$label$_$id$->input1 = $prop[input1]$;
"""
