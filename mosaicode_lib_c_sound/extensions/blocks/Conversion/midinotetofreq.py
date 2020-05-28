#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class MIDINoteToFreq(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "sound"
        self.help = "Convert MIDI Note to Frequency Value"
        self.label = "MIDI_Note_to_Freq"
        self.color = "140:114:114:150"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"midi_note",
                       "conn_type":"Input",
                       "label":"MIDI Note value"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"freq",
                       "conn_type":"Output",
                       "label":"Frequency value"}]

        self.group = "Conversion"
        self.codes["declaration"] = \
"""
float_callback *$port[freq]$;
int $port[freq]$_size = 0;

void $port[midi_note]$(float value){
  for(int i=0 ; i < $port[freq]$_size ; i++){
    // Call the stored functions
    (*($port[freq]$[i]))(mscsound_midi_midi_note_to_freq(value));
  }
}
"""
