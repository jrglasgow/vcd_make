#!/usr/bin/env python

import os, sys, subprocess, json
from pprint import pprint
from termcolor import colored

ffprobe = '/usr/bin/ffprobe'
ffmpeg = '/usr/bin/ffmpeg'



def transcode(this_file):
  this_dir = os.path.dirname(this_file)
  new_file = '%s.mpg' % ('.'.join(this_file.replace(this_dir + '/', '').split('.')[0:-1]))
  pprint(new_file)
  ffmpeg_command = '%s -i "%s" -target ntsc-svcd -y "%s"' % (ffmpeg, this_file, new_file)
  pprint(ffmpeg_command)
  os.system(ffmpeg_command)
  pass

if __name__=='__main__':
    files = sys.argv[1:]
    for this_file in files:
        transcode(this_file)
    pass