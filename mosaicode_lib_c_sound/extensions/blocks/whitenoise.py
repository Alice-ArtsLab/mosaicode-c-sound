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
        self.framework = "sound"
        self.help = "White Noise"
        self.label = "White Noise"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                "name":"output",
                "conn_type":"Output",
                "label":"Output"}
            ]
        self.group = "Sound Sources"

        self.codes["declaration"] = """noise_t *block_$id$;"""
        self.codes["execution"] = """block_$id$->process(block_$id$);"""

        self.codes["setup"] = """noise = create_noise(FRAMES_PER_BUFFER);"""
