This repository includes scripts and related tools for use with Caustic Visualizer™.

Caustic Visualizer is a 3D rendering tool from Imagination Technologies that extends
Autodesk® Maya® ond Autodesk® 3Ds Max®. You can find out more about it at http://www.caustic.com

The tools and scripts here are public and NOT part of the standard Visualizer release.

You can install and use these tools with or without a GitHub account -- with an account is easier.

If you have an account and your Maya installation locations are pretty "plain vanilla":

    1. Clone the VisualizerTools repo to the standard place: that is,
	    ..\Documents\GitHub\VisualizerTools
    2. For Maya users, copy the file ..\VisualizerTools\Maya\Python\VisualizerToolsSetup.py
	    to your maya script directory -- that's normally
	    ..\Documents\maya\scripts
    3. If you don't have an existing userSetup.py in that directory, jusy copy the one from
    	    VisualizerTools. If you DO have one, add the two lines from the sample:
	        from VisualizerToolsSetup import *
		VisualizerToolsSetup()
    4. Restart Maya and you should see the appropriate paths. Try
	    getenv "MAYA_SCRIPT_PATH"
	    in the Mel script editor to make sure you're good.

If you don't have or want a (free) GitHub account:
    1. Download the repository as a ZIP file, and unpack it into your ..\Documents\
            folder. The final path can be ..\Documents\GitHub\VisualizerTools-master\
	    or ..\Documents\VisualizerTools-master\
    2. Jump to step #2 in the list above.

More tools and instructions for 3DS Max are forthcoming -- in the meantime, feel free to
    report issues, make requests, and especially, for those inclined, CONTRIBUTE on GitHub!

Thanks!
kb


12 June 2013
