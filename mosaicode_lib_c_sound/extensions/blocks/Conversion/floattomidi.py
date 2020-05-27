#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class FloatToMIDI(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Float to MIDI"
        self.label = "Float_to_MIDI"
        self.color = "140:114:114:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.midi",
                       "name":"output",
                       "conn_type":"Output",
                       "label":"MIDI message"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"type",
                       "conn_type":"Input",
                       "label":"Message type"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"channel",
                       "conn_type":"Input",
                       "label":"MIDI channel"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"note",
                       "conn_type":"Input",
                       "label":"MIDI note"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"velocity",
                       "conn_type":"Input",
                       "label":"MIDI velocity (Note)"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"param",
                       "conn_type":"Input",
                       "label":"Param (Control)"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"control_value",
                       "conn_type":"Input",
                       "label":"Value (Control)"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"trigger",
                       "conn_type":"Input",
                       "label":"Trigger"}]

        self.properties = [{"name": "type",
                            "label": "Type",
                            "type": MOSAICODE_COMBO,
                            "values": ["SND_SEQ_EVENT_NOTEON",
                                       "SND_SEQ_EVENT_NOTEOFF",
                                       "SND_SEQ_EVENT_CONTROLLER"],
                            "value": "SND_SEQ_EVENT_NOTEON"},
                           {"name": "channel",
                            "label": "Channel",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 15,
                            "step": 1,
                            "value": 0},
                           {"name": "note",
                            "label": "Note",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 127,
                            "step": 1,
                            "value": 0},
                           {"name": "velocity",
                            "label": "Velocity (Note)",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 127,
                            "step": 1,
                            "value": 0},
                           {"name": "param",
                            "label": "Param (Control)",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 127,
                            "step": 1,
                            "value": 0},
                           {"name": "control_value",
                            "label": "Control value",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 127,
                            "step": 1,
                            "value": 0}]

        self.group = "Conversion"
        self.codes["declaration"] = \
"""
snd_seq_event_t $label$_$id$_event;

midi_callback *$port[output]$;
int $port[output]$_size = 0;

void $port[trigger]$(float value){
    if (value) {
        for(int i=0 ; i < $port[output]$_size ; i++){
            // Call the stored functions
            (*($port[output]$[i]))((void*)&$label$_$id$_event);
        }
    }
}

void $port[type]$(float value){
    $label$_$id$_event.type = value;
}

void $port[channel]$(float value){
    $label$_$id$_event.data.note.channel = value;
    $label$_$id$_event.data.control.channel = value;
}

void $port[note]$(float value){
    $label$_$id$_event.data.note.note = value;
}

void $port[velocity]$(float value){
    $label$_$id$_event.data.note.velocity = value;
}

void $port[param]$(float value){
    $label$_$id$_event.data.control.param = value;
}


void $port[control_value]$(float value){
    $label$_$id$_event.data.control.value = value;
}
"""

        self.codes["setup"] = \
"""
snd_seq_ev_clear(&$label$_$id$_event);
snd_seq_ev_set_source(&$label$_$id$_event, 0);
snd_seq_ev_set_subs(&$label$_$id$_event);
snd_seq_ev_set_direct(&$label$_$id$_event);
snd_seq_ev_set_fixed(&$label$_$id$_event);

$label$_$id$_event.type = $prop[type]$;
$label$_$id$_event.data.note.channel = $prop[channel]$;
$label$_$id$_event.data.control.channel = $prop[channel]$;
$label$_$id$_event.data.note.note = $prop[note]$;
$label$_$id$_event.data.note.velocity = $prop[velocity]$;
$label$_$id$_event.data.control.param = $prop[param]$;
$label$_$id$_event.data.control.value = $prop[control_value]$;
"""
