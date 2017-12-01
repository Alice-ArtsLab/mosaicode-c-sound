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
        self.framework = "sound"
        self.help = "Speaker"
        self.label = "Speaker"
        self.color = "50:150:250:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.sound",
                "name":"input",
                "conn_type":"Input",
                "label":"Input"}
            ]
        self.group = "Output"

        self.codes["declaration"] = """speaker_t *block_$id$;"""
        self.codes["execution"] = """block_$id$->process(block_$id$, out);"""

        self.codes["setup"] = """speaker = create_speaker(FRAMES_PER_BUFFER);"""
