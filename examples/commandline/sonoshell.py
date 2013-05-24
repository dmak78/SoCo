#!/usr/bin/env python

import sys
import requests
import urllib
import atexit

from time import sleep
from threading import Timer

from soco import SoCo
from soco import SonosDiscovery

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        print "Usage: sonoshell.py [speaker's IP|all] [cmd]"
        print ""
        print "Valid commands (with IP): info, play, pause, stop, next, previous, current, and partymode"
        print "Valid commands (with 'all'): list_ips"
        sys.exit()

    speaker_spec = sys.argv[1]
    cmd = sys.argv[2].lower()

    if speaker_spec == "all":
        sonos = SonosDiscovery()
        if (cmd == 'list_ips'):
            print '\n'.join(sonos.get_speaker_ips())
        else:
            print "Valid commands (with 'all'): list_ips"
    else:
        sonos = SoCo(speaker_spec)
        if (cmd == 'partymode'):
            print sonos.partymode()
        elif (cmd == 'info'):
            all_info = sonos.get_speaker_info()
            for item in all_info:
                print "%s: %s" % (item, all_info[item])
        elif (cmd == 'play'):
            print sonos.play()
        elif (cmd == 'pause'):
            print sonos.pause()
        elif (cmd == 'stop'):
            print sonos.stop()
        elif (cmd == 'next'):
            print sonos.next()
        elif (cmd == 'previous'):
            print sonos.previous()
        elif (cmd == 'get_current_track_info'):
            print sonos.get_current_track_info()
        elif (cmd == 'add_to_queue'):
            print sonos.add_to_queue(sys.argv[3].lower())
        elif (cmd == 'mute'):
            print sonos.mute()
        elif (cmd == 'get_queue'):
            print sonos.get_queue()
        elif (cmd == 'testing'):
            print sonos.testing()
        elif (cmd == 'volume'):
            if(len(sys.argv) > 3):
                print sonos.volume(sys.argv[3])
            else:
                print sonos.volume()
        elif (cmd == 'say'):
            text = urllib.quote_plus(sys.argv[3])
            r = requests.get('http://tts-api.com/tts.mp3?q='+text+'&return_url=1')
            uri = r.text
            #print sonos.play_uri(uri, sys.argv[3])
            print uri
        elif (cmd == 'current'):
            track = sonos.get_current_track_info()
            print 'Current track: ' + track['artist'] + ' - ' + track['title'] + '. From album ' + track['album'] + '. This is track number ' + track['playlist_position'] + ' in the playlist. It is ' + track['duration'] + ' minutes long.'
        else:
            print "Valid commands (with IP): info, play, pause, stop, next, previous, current, and partymode"

