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
                "name":"sound_value",
                "conn_type":"Output",
                "label":"Sound Value"}
            ]
        self.group = "Sound Sources"


        self.codes["function_declaration"] = \
r"""
typedef void (*sound_callback)(float **value);
"""

        self.codes["declaration"] = \
r"""
mscsound_noise_t *$label$_$id$;

sound_callback * $port[sound_value]$ = (sound_callback *)malloc(sizeof(sound_callback));
int $port[sound_value]$_size = 0;
void $label$$id$_callback();
"""

        self.codes["function"] = \
r"""
void $label$_$id$_callback(){
   for(int i = 0 ; i < $port[sound_value]$_size ; i++){
        // Call the stored functions
        (*($port[sound_value]$[i]))($label$_$id$->output0);
   }
}
"""
        self.codes["execution"] = "$label$_$id$->process(&$label$_$id$);\n"

        self.codes["setup"] = "$label$_$id$ = mscsound_create_noise(FRAMES_PER_BUFFER);\n"
