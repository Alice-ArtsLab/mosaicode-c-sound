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
                "name":"input0",
                "conn_type":"Input",
                "label":"Sound Value"}
            ]
        self.group = "Output"
        self.codes["declaration"] = "mscsound_speaker_t *$label$_$id$;\n"
        self.codes["execution"] = \
"$label$_$id$->process(&$label$_$id$, &out);\n"
        self.codes["setup"] = \
"$label$_$id$ = mscsound_create_speaker(FRAMES_PER_BUFFER);\n"
