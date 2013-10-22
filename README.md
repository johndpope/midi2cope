midi2cope
=========

Converts a midi file to cope events (as invented by David C. Cope, algorithmic composer and professor at UCSC)

Call it on the command line by:
>>python midi2cope.py midifile_1.mid midifile_2.mid ... midifile_n.mid 

A csv file for each midifile will be created. 
Format:

ontime, pitch, duration, channel, velocity
ontime, pitch, duration, channel, velocity
...
