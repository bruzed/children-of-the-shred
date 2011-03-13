#Children of the Shred v1.1

##Requirements
1. [PyGame](http://www.pygame.org/download.shtml)
2. [SimpleOSC](http://pypi.python.org/pypi/SimpleOSC/0.2.3)
3. [Max/MSP Runtime Environment](http://www.cycling74.com/downloads/max5)
4. A guitar and a MIDI keyboard.

##How to play
1. Plug in your guitar and MIDI keyboard
2. Run 'GuitarTranslator.maxpat' in Max/MSP (in presentation mode). There are 2 volume controls. The volume on the left is guitar output to your speakers and the one on the right is guitar output to python. Double clicking on the 'midiin' box will allow you to select your MIDI keyboard.
3. Run 'cotS.py'
4. If you don't have a guitar or keyboard you can still play! Run 'GuitarTranslator-MIDI-Debug.maxpat' in Max/MSP (in presentation mode). You'll see two keyboards for you and your opponent.
5. Playing notes generates zombies or slayers (depending on what you're playing as). Your opponent needs to play back the correct notes to destroy the zombies or slayers and gain points. You lose points if you play the wrong note and miss!