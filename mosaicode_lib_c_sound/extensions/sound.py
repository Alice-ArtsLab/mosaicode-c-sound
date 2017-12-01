#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mosaicode.model.codetemplate import CodeTemplate

class Sound(CodeTemplate):
    def __init__(self):
        self.code = '''#include <mosaic-sound.h>
#include <portaudio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_SECONDS 12
#define SAMPLE_RATE 44100
#define FRAMES_PER_BUFFER 256

$code[declaration]$

static int mosaicsound_callback(const void *inputBuffer, void *outputBuffer,
                                unsigned long framesPerBuffer,
                                const PaStreamCallbackTimeInfo *timeInfo,
                                PaStreamCallbackFlags statusFlags,
                                void *userData) {
	float *in = (float *)inputBuffer;
	float *out = (float *)outputBuffer;

	(void)timeInfo; /* Prevent unused variable warnings. */
	(void)statusFlags;
	(void)userData;
	(void)in;
	(void)out;

	$code[execution]$

  return paContinue;
}

/*
 * This routine is called by mosaic-sound when mosaicsound_callback is done.
 */
static void mosaicsound_finished(void *data) { printf("Stream Completed!\n"); }

int main(int argc, char *argv[]) {
  	$code[setup]$
	$code[connections]$

	void *stream = mosaicsound_inicialize(SAMPLE_RATE, FRAMES_PER_BUFFER);

	printf("Playing until the Enter key is pressed.\n");
	getchar();

	mosaicsound_terminate(stream);

  return 0;
}'''
        self.name = '''sound'''
        self.extension = '''.c'''
        self.source = '''python'''
        self.language = '''c'''
        self.command = '''export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/lib/;
export PKG_CONFIG_PATH=/lib/pkgconfig/;
gcc $filename$$extension$  -I/usr/include/mosaic/mosaic-sound -lmosaic-sound -o $filename$ -g -Wall -lportaudio -lm `pkg-config --libs sndfile`
LD_LIBRARY_PATH=/lib/ $dir_name$./$filename$'''
        self.type = '''mosaicode_lib_c_sound.extensions.cfile'''
        self.code_parts = ['declaration', ' execution', ' setup', ' connections']
        self.description = '''c / mosaic-sound template'''
