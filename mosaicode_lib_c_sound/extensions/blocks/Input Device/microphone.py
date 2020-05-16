#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Speaker class.
"""
from mosaicode.model.blockmodel import BlockModel

class Microphone(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Microphone"
        self.label = "Microphone"
        self.color = "205:178:95:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                        "name":"output0",
                        "conn_type":"Output",
                        "label":"Sound Value"}
                    ]
        self.group = "Input Device"
        self.codes["declaration"] = "mscsound_mic_t *$label$_$id$;\n"
        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$, &in);\n"
        self.codes["setup"] = \
"$label$_$id$ = mscsound_create_mic(FRAMES_PER_BUFFER);\n"
