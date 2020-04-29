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
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                "name":"output",
                "conn_type":"Output",
                "label":"Output"}
            ]
        self.group = "Sound Sources"

        self.codes["declaration"] = """mscsound_noise_t *$label$_$id$;\n"""
        self.codes["execution"] = """$label$_$id$->process(&$label$_$id$);\n"""

        self.codes["setup"] = """$label$_$id$ = mscsound_create_noise(FRAMES_PER_BUFFER);\n"""
