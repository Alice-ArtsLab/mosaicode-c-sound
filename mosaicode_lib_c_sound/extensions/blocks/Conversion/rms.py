#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class RMS(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "RMS"
        self.label = "RMS"
        self.color = "140:114:114:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                       "name":"input0",
                       "conn_type":"Input",
                       "label":"Sound value"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"output0",
                       "conn_type":"Output",
                       "label":"Float value"}]

        self.group = "Conversion"
        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(float value);
$label$_$id$_callback_t* $port[output0]$;
int $port[output0]$_size = 0;
mscsound_rms_t  *$label$_$id$;
"""
        self.codes["execution"] = \
"""
$label$_$id$->process(&$label$_$id$);
for(int i=0 ; i < $port[output0]$_size ; i++){
    // Call the stored functions
    (*($port[output0]$[i]))(*($label$_$id$->output0));
}
"""
        self.codes["setup"] = "$label$_$id$ = mscsound_create_rms(FRAMES_PER_BUFFER);\n"
