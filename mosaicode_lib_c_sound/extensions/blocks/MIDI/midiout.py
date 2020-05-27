#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the MIDIOut class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class MIDIOut(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "MIDI Output"
        self.label = "MIDI_OUT"
        self.color = "205:178:95:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.midi",
                       "name":"input",
                       "conn_type":"Input",
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
void $port[input]$(snd_seq_event_t *ev){
    $label$_$id$->send_event(&$label$_$id$, ev);
}
"""

        self.codes["setup"] = \
"""
$label$_$id$ = mscsound_create_midi(\"$prop[device]$\",
                                    SND_SEQ_OPEN_OUTPUT,
                                    NULL);
"""
