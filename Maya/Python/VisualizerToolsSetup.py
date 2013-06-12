"""
VisualizerToolsSetup.py is to be imported (and run) from your local "userSetup.py" file.

It assumes that "VisualizerTools" are in the default location as defined by the Windows GitHub
   client, and if that location is valid it appendes the appropriate strings to both the Python
   and Mel paths.

put this in the same directory as userSetup.py and call it so:

from VisualizerToolsSetup import *
VisualizerToolsSetup()

"""
import os, sys, maya

def VisualizerToolsSetup():
  """
  This sets the paths. Note that under Windows Python uses backslash as a separator,
     while Mel always uses a forward slash -- so we can use os.path.join() for Python,
     but not for Mel.
  """
  homeDir = os.environ.get('HOME','.')
  visToolsDir = os.path.join(homeDir,'GitHub','VisualizerTools','Maya')
  if not os.path.exists(visToolsDir):
    return
  sys.path.append(os.path.join(visToolsDir,'Python'))
  # Mel uses a different path separator!
  melPath = maya.mel.eval('getenv("MAYA_SCRIPT_PATH");') 
  if melPath != "":
    melPath += ';'
  melPath += '%s/GitHub/VisualizerTools/Maya/MEL'%(homeDir)
  maya.mel.eval('putenv "MAYA_SCRIPT_PATH" "%s";'%(melPath))


########### eof ##
