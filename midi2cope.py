from sys import argv
import midi
from time import time

t = time()

midifilenames = argv[1:]

for midifilename in midifilenames:
    try:
        events = midi.read_midifile(midifilename)
    except:
        print "Midi file {} not found or unreadable.".format(midifilename)
        continue

    ons = [sorted([e for e in track if e.type is "NoteOnEvent" and e.velocity is not 0], key = lambda x: x.msdelay) for track in events]

    offs = [sorted([e for e in track if e.type is "NoteOffEvent" or (e.type is midi.NoteOnEvent and e.velocity is 0)], key = lambda x: x.msdelay) for track in events]
    
    CopeEvents = [] 	
    for tr, track in enumerate(ons):
        for on in track:
            ontime = on.msdelay
            pitch = on.pitch
            channel = on.channel
            velocity = on.velocity
            for off in offs[tr]:
                if off.msdelay < ontime:
	            continue
                if off.channel == channel and off.pitch == pitch:
                    duration = off.msdelay - ontime
                    break
            print '({}\t{}\t{}\t{}\t{}\t)'.format(ontime, pitch, duration, channel, velocity)
            CopeEvents.append((ontime, pitch, duration, channel, velocity))
    
    copeeventfilename = midifilename.split('.')[0]+'.csv'
    f = open(copeeventfilename, 'w')
    for ce in CopeEvents:
        f.write('{0}, {1}, {2}, {3}, {4}\n'.format(*ce))
    f.close()         
