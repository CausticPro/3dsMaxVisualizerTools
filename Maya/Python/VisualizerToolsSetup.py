"""
VisualizerToolsSetup.py is to be imported (and run) from your local "userSetup.py" file.

It assumes that "VisualizerTools" are in the default location as defined by the Windows GitHub
   client, and if that location is valid it appendes the appropriate strings to both the Python
   and Mel paths.

put this in the same directory as userSetup.py (usually ..\Documents\Maya\scripts) and call it so:

from VisualizerToolsSetup import *
VisualizerToolsSetup()

"""
import os, sys, maya

def VisualizerToolsSetup():
  """
  This sets the paths. Note that under Windows Python uses backslash as a separator,
     while Mel always uses a forward slash -- so we can use os.path.join() for Python,
     but not for Mel.
  Since the user may have downloaded a zip of the repo, rather than using the git client,
     we also accept the name "VisualizerTools-master" which would be the default top-folder
     name for such zipped collections.
  """
  homeDir = os.environ.get('HOME','.')
  gitD = 'GitHub'
  visD = 'VisualizerTools'
  visToolsDir = os.path.join(homeDir,gitD,visD,'Maya')
  if not os.path.exists(visToolsDir):   # try some other permutations
    visD += '-master'
    visToolsDir = os.path.join(homeDir,gitD,visD,'Maya')
    if not os.path.exists(visToolsDir):
      gitD = None
      visToolsDir = os.path.join(homeDir,visD,'Maya')
      if not os.path.exists(visToolsDir):
        print "VisualizerTools folders not found. See https://github.com/CausticPro/VisualizerTools"
        return
  sys.path.append(os.path.join(visToolsDir,'Python'))
  # Mel uses a different path separator!
  melPath = maya.mel.eval('getenv("MAYA_SCRIPT_PATH");') 
  if melPath != "":
    melPath += ';'
  if gitD:
    melPath += '%s/%s/%s/Maya/MEL'%(homeDir,gitD,visD)
  else:
    melPath += '%s/%s/Maya/MEL'%(homeDir,visD)
  maya.mel.eval('putenv "MAYA_SCRIPT_PATH" "%s";'%(melPath))


########### eof ##
