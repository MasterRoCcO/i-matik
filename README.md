# i-matik
i-matik is a collection of helper scripts capable of efficient building
freetz-ng images for Fritz!Box or Fritz!Repeater or Fritz!Powerline.
```
Usage: i-matik [OPTION]... [BOX_TYPE.SSL_NUMBER]...
  or   i-matik [BOX_TYPE.SSL_NUMBER]... [OPTION]... 

Options
  BOX_TYPE			any currently supported devices
  SSL_NUMBER			10 - OpenSSL 1.0.x
  				11 - OpenSSL 1.1.x
  				30 - OpenSSL 3.0.x
  				multi - OpenSSL multiple Versions
  -c, --config			show not freetz-ng configuration dialog
  -s,--skip-image2memory	do not create inmemory image
  -yo,--yes-oscam		The image is with oscam add-on and an oscam is created 
  -push 			push image to Fritz!Box or Fritz!Repeater or Fritz!Powerline
```
List of currently OpenSSL 1.0.x supported devices (BOX_TYPE): 1240E 300E 3272 3370 3390 3490 4020 4040 4060 450E 540E 546E 5490 5491 6430 6490 6590 6591 6660 6810 6840 68504g 68505g 6890 7240 7270v2 7270v3 7272 7312 7320 7320-Alien7330 7330 7330SL 7340 7360v1 7360v2 7362 7369 7390 7412 7412-Alien7430 7430 7490 7510 7520 7520-Alien7530 7530 7530AX 7560 7580 7581 7582 7583 7583vdsl 7590 7590AX DVB-C 
To build an OpenSSL 1.0.x image for Fritz!Box 3272 use this command:
./i-matik 3272.10
```
List of currently OpenSSL 1.1.x supported devices (BOX_TYPE): 1200 1240E 1260E 1260v2 1750E 2400 3000 300E 3272 3370 3370-Alien3490 3390 3390-Alien3490 3490 4020 4040 4060 450E 540E 546E 5490 5491 5530 6000 6430 6490 6590 6591 6660 6820v1 6820v2 6820v3 6840 68504g 68505g 6890 7272 7312 7320-Alien7330 7330 7330SL 7360v2 7362 7390 7412 7412-Alien7430 7430 7490 7520 7520-Alien7530 7530 7530AX 7560 7580 7581 7582 7583 7583vdsl 7590 7590AX DVB-C DVB-c-Alien1750E 
To build an OpenSSL 3.0.x image for Fritz!Box 7490 use this command:
./i-matik 7490.11
```
List of currently OpenSSL 3.0.x supported devices (BOX_TYPE): 1200 1240E 1260E 1260v2 1750E 2400 3000 300E 3272 3370 3370-Alien3490 3390 3390-Alien3490 3490 4020 4040 4060 450E 540E 546E 5490 5491 5530 6000 6430 6490 6590 6591 6660 6820v1 6820v2 6820v3 6840 68504g 68505g 6890 7272 7312 7320-Alien7330 7330 7330SL 7360v2 7362 7390 7412 7412-Alien7430 7430 7490 7510 7520 7520-Alien7530 7530 7530AX 7560 7580 7581 7582 7583 7583vdsl 7590 7590AX DVB-C DVB-c-Alien1750E 
To build an OpenSSL 3.0.x image for Fritz!Box 7490 use this command:
./i-matik 7490.30
```
List of currently OpenSSL MULTI supported devices (BOX_TYPE): 3272 3370 3390 3490 4020 4040 4060 5490 5491 6430 6490 6590 6591 6660 6840 68504g 68505g 6890 7272 7320-Alien7330 7330 7330SL 7360v2 7362 7390 7430 7490 7510 7520 7520-Alien7530 7530 7530AX 7560 7580 7581 7582 7583 7583vdsl 7590 7590AX 
To build an OpenSSL MULTI image for Fritz!Box 7490 use this command:
./i-matik 7490.multi
```
List of currently push supported devices (BOX_TYPE): 1200 1240E 1260E 1260v2 1750E 2400 3000 300E 3272 3370 3370-Alien3490 3390 3390-Alien3490 3490 4020 4040 4060 450E 540E 546E 5490 5491 5530 6000 6430 6490 6590 6591 6660 6810 6820v1 6820v2 6820v3 6840 68504g 68505g 6890 7240 7270v2 7270v3 7272 7312 7320 7320-Alien7330 7330 7330SL 7340 7360v1 7360v2 7362 7369 7390 7412 7412-Alien7430 7430 7490 7510 7520 7520-Alien7530 7530 7530AX 7560 7580 7581 7582 7583 7583vdsl 7590 7590AX DVB-C DVB-c-Alien1750E 
To create an image for the Fritz!Box 7490 to push, use this command :
./i-matik 7490 -push


