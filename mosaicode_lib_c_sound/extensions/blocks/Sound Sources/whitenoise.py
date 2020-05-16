#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Speaker class.
"""
from mosaicode.model.blockmodel import BlockModel

class WhiteNoise(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "White Noise"
        self.label = "WhiteNoise"
        self.color = "228:242:73:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                "name":"output0",
                "conn_type":"Output",
                "label":"Sound Value"}
            ]
        self.group = "Sound Sources"
        self.codes["declaration"] = "mscsound_whitenoise_t *$label$_$id$;\n"
        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"
        self.codes["setup"] = "$label$_$id$ = mscsound_create_whitenoise(FRAMES_PER_BUFFER);\n"
