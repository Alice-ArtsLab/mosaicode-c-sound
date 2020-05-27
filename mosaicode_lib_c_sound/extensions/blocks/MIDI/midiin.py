#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the MIDIIn class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class MIDIIn(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "MIDI IN"
        self.label = "MIDI_IN"
        self.color = "205:178:95:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.midi",
                       "name":"output",
                       "conn_type":"Output",
                       "label":"MIDI message"}]

        self.properties = [{"name": "device",
                            "label": "Device",
                            "type": MOSAICODE_STRING,
                            "value": ""
                           }]

        self.group = "MIDI"

        self.codes["declaration"] = \
"""
mscsound_midi_t *$label$_$id$;
midi_callback *$port[output]$;
int $port[output]$_size = 0;

void $label$_$id$_callback(snd_seq_event_t *ev) {
    for(int i=0 ; i < $port[output]$_size ; i++){
        // Call the stored functions
        (*($port[output]$[i]))((void*)ev);
    }
}
"""

        self.codes["setup"] = \
"""
$label$_$id$ = mscsound_create_midi(\"$prop[device]$\",
                                    SND_SEQ_OPEN_INPUT,
                                    $label$_$id$_callback);
"""
