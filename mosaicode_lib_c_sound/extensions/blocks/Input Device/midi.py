#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the MIDI class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class MIDI(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "MIDI"
        self.label = "MIDI"
        self.color = "205:178:95:150"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"channel",
                       "conn_type":"Input",
                       "label":"Channel"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"velocity",
                       "conn_type":"Input",
                       "label":"Velocity"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"note",
                       "conn_type":"Input",
                       "label":"Note"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"send_noteon",
                       "conn_type":"Input",
                       "label":"Send note-on"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"send_noteoff",
                       "conn_type":"Input",
                       "label":"Send note-off"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.integer",
                       "name":"send_control",
                       "conn_type":"Input",
                       "label":"Send control"}]

        self.properties = [{"name": "device",
                            "label": "Device",
                            "type": MOSAICODE_STRING,
                            "value": ""
                           }]

        self.group = "Input Device"

        self.codes["declaration"] = \
"""
mscsound_midi_t *$label$_$id$;
int $label$_$id$_channel_value;
int $label$_$id$_velocity_value;
int $label$_$id$_note_value;

void $port[channel]$(int value){
    $label$_$id$_channel_value = value;
}

void $port[velocity]$(int value){
    $label$_$id$_velocity_value = value;
}

void $port[note]$(int value){
    $label$_$id$_note_value = value;
}

void $port[send_noteon]$(int value){
    if (value)
        $label$_$id$->send_note(&$label$_$id$, SND_SEQ_EVENT_NOTEON,
                                               $label$_$id$_channel_value,
                                               $label$_$id$_velocity_value,
                                               $label$_$id$_note_value);
}

void $port[send_noteoff]$(int value){
    if (value)
        $label$_$id$->send_note(&$label$_$id$, SND_SEQ_EVENT_NOTEOFF,
                                               $label$_$id$_channel_value,
                                               $label$_$id$_velocity_value,
                                               $label$_$id$_note_value);
}

void $port[send_control]$(int value){
    if (value)
        $label$_$id$->send_control(&$label$_$id$, $label$_$id$_channel_value,
                                                  $label$_$id$_velocity_value,
                                                  $label$_$id$_note_value);
}
"""

        self.codes["setup"] = \
"""
$label$_$id$ = mscsound_create_midi(\"$prop[device]$\",
                                    SND_SEQ_OPEN_DUPLEX,
                                    NULL);
"""
