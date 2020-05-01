#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Speaker class.
"""
from mosaicode.model.blockmodel import BlockModel

class Speaker(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Speaker"
        self.label = "Speaker"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                "name":"sound_value",
                "conn_type":"Input",
                "label":"Sound Value"}
            ]
        self.group = "Output"

        self.codes["declaration"] = \
"""
mscsound_speaker_t *$label$_$id$;
void $port[sound_value]$(float **value);
"""
        self.codes["function"] = \
"""
void $port[sound_value]$(float ** value){
    $label$_$id$->input0 = value;
}
"""
        self.codes["execution"] = """$label$_$id$->process(&$label$_$id$, &out);\n"""

        self.codes["setup"] = """$label$_$id$ = mscsound_create_speaker(FRAMES_PER_BUFFER);\n"""
