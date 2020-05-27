#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class MIDIToFloat(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "MIDI to float"
        self.label = "MIDI_to_float"
        self.color = "140:114:114:150"
        self.ports = [{"type":"mosaicode_lib_c_sound.extensions.ports.midi",
                       "name":"input",
                       "conn_type":"Input",
                       "label":"MIDI message"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"type",
                       "conn_type":"Output",
                       "label":"Message type"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"channel",
                       "conn_type":"Output",
                       "label":"MIDI channel"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"note",
                       "conn_type":"Output",
                       "label":"MIDI note"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"velocity",
                       "conn_type":"Output",
                       "label":"MIDI velocity (Note)"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"param",
                       "conn_type":"Output",
                       "label":"Param (Control)"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"control_value",
                       "conn_type":"Output",
                       "label":"Value (Control)"}]

        self.group = "Conversion"
        self.codes["declaration"] = \
"""
float_callback *$port[type]$;
int $port[type]$_size = 0;
float_callback *$port[channel]$;
int $port[channel]$_size = 0;
float_callback *$port[note]$;
int $port[note]$_size = 0;
float_callback *$port[velocity]$;
int $port[velocity]$_size = 0;
float_callback *$port[param]$;
int $port[param]$_size = 0;
float_callback *$port[control_value]$;
int $port[control_value]$_size = 0;

void $port[input]$(snd_seq_event_t *ev){
  for(int i=0 ; i < $port[type]$_size ; i++){
    // Call the stored functions
    (*($port[type]$[i]))(ev->type);
  }

  for(int i=0 ; i < $port[channel]$_size ; i++){
    // Call the stored functions
    (*($port[channel]$[i]))(ev->data.note.channel);
  }

  for(int i=0 ; i < $port[note]$_size ; i++){
    // Call the stored functions
    (*($port[note]$[i]))(ev->data.note.note);
  }

  for(int i=0 ; i < $port[velocity]$_size ; i++){
    // Call the stored functions
    (*($port[velocity]$[i]))(ev->data.note.velocity);
  }

  for(int i=0 ; i < $port[param]$_size ; i++){
    // Call the stored functions
    (*($port[param]$[i]))(ev->data.control.param);
  }

   for(int i=0 ; i < $port[control_value]$_size ; i++){
     // Call the stored functions
     (*($port[control_value]$[i]))(ev->data.control.value);
   }
}
"""
