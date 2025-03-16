# Welcome to i-matik for freetz-ng

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
  				33 - OpenSSL 3.3.x (only intern)
  				multi - OpenSSL multiple Versions (only intern)
  -c,--config			show not freetz-ng configuration dialog
  -s,--skip-image2memory	do not create inmemory image
  -int,--international		International Version
  -yo,--yes-oscam		The image is with oscam add-on and an oscam is created
  -yoe,--yes-oscam		The image is with oscam_emu add-on and an oscam is created
  -ysmod,--yes-oscam-smod	The image is with oscam_smod add-on and an oscam is created
  -to,--tool-oscam              oscam ToolChain
  -do,--del-oscam		delete the old oscam and build a new one
  -deloscam			delete all oscams
  -nc,--no-clientbox		No client box image is created
  -nm,--no-masterbox		No master box image is created
  -kp,--kernel-precompiled      Make kernel-precompiled
  -kc,--kernel-clean            Make kernel-clean
  -km,--kernel-menuconfig       Make kernel-menuconfig
  -ta,--toolchain-activate      Activate toolchain
  -td,--toolchain-disable       Disable toolchain
  -tm,--toolchain-make		Toolchain make
  -cm,--callmonitor		Callmonitor
  -rr,--rrdstats		RRDstats for RRDtool 1.2.30
  -rr18,--rrdstats18		RRDstats for RRDtool 1.8.0
  -us,--user-skins		User Skin
  -us,--user-skins1		User Skin1
  -ua,--user-application	User Application
  -vs,--vnstat			VNSTAT
  -wg,--wireguard		WIREGUARD
  -ov,--openvpn			OpenVPN
  -tel,--telnet			telnet
  -key,--key-pack		Key Pack
  -idm,--inadyn-mt		Inadyn-mt
  -l4l,--lcd4linux		LCD 4 LINUX
  -vfp,--vsftpd			secure FTP server
  -push				push image to Fritz!Box or Fritz!Repeater or Fritz!Powerline
  -backup			make a backup of your freetz-signature and freetz-dl
  -us,--user-skins		user skins
  -us1,--user-skins1		user skins1
  -ua,--user-application	user application
  -sa,--samba			samba
```
List of currently OpenSSL 1.0.x supported devices (BOX_TYPE): 1240E 300E 3272 3370 3390 4020 450E 540E 546E 6430 6490 6590 6810 6840 7240 7270v2 7270v3 7272 7312 7320 7320-Alien7330 7330 7330SL 7340 7360v1 7360v2 7362 7369 7390 7412 7581 7582 DVB-C
```
To build an OpenSSL 1.0.x image for Fritz!Box 3272 use this command:
./i-matik 3272.10
```
List of currently OpenSSL 1.1.x supported devices (BOX_TYPE): 1200 1200AX 1240AX 1240E 1260E 1260v2 1750E 2400 3000 3000AX 300E 3272 3370 3370-Alien3490 3390 3390-Alien3490 3490 4020 4040 4060 450E 540E 546E 5490 5491 5530 5590 6000 6430 6490 6590 6591 6660 6690 6820v1 6820v2 6820v3 6840 68504g 68505g 6890 7272 7312 7320-Alien7330 7330 7330SL 7360v2 7362 7390 7412 7412-Alien7430 7430 7490 7510 7520 7520-Alien7530 7520B 7530 7530AX 7560 7580 7581 7582 7583 7583vdsl 7590 7590AX DVB-C DVB-c-Alien1750E Gateway
```
To build an OpenSSL 3.0.x image for Fritz!Box 7490 use this command:
./i-matik 7490.11
```
List of currently OpenSSL 3.0.x supported devices (BOX_TYPE): 1200 1200AX 1240AX 1240E 1260E 1260v2 2400 3000 3000AX 300E 3272 3370 3370-Alien3490 3390 3390-Alien3490 3490 4040 4050 4060 450E 540E 546E 5490 5491 5530 5590 5690Pro 6000 6430 6490 6590 6591 6660 6670 6690 6820v1 6820v2 6820v3 6840 68504g 68505g 6890 7272 7312 7320-Alien7330 7330 7330SL 7360v2 7362 7390 7412 7412-Alien7430 7430 7490 7510 7520 7520-Alien7530 7520B 7530 7530AX 7560 7580 7581 7582 7583 7583vdsl 7590 7590AX 7690 DVB-C 
```
To build an OpenSSL 3.0.x image for Fritz!Box 7490 use this command:
./i-matik 7490.30
```
List of currently OpenSSL 3.3.x supported devices (BOX_TYPE): 1200 1200AX 1240AX 1240E 1260E 1260v2 2400 3000 3000AX 300E 3272 3370 3370-Alien3490 3390 3390-Alien3490 3490 4020 4040 4060 450E 540E 546E 5490 5491 5530 5590 6000 6430 6490 6590 6591 6660 6690 6820v1 6820v2 6820v3 6840 68504g 68505g 6890 7272 7312 7320-Alien7330 7330 7330SL 7360v2 7362 7390 7412 7412-Alien7430 7430 7490 7510 7520 7520-Alien7530 7520B 7530 7530AX 7560 7580 7581 7582 7583 7583vdsl 7590 7590AX DVB-C
```
To build an OpenSSL 3.3.x image for Fritz!Box 7490 use this command:
./i-matik 7490.33
```
List of currently OpenSSL MULTI supported devices (BOX_TYPE): 33272 3370 3390 3490 4020 4040 4060 5490 5491 5590 6430 6490 6590 6591 6660 6690 6840 68504g 68505g 6890 7272 7320 7320-Alien7330 7330 7330SL 7360v2 7362 7390 7430 7490 7510 7520 7520-Alien7530 7520B 7530 7530AX 7560 7580 7583 7583vdsl 7590 7590AX
```
To build an OpenSSL MULTI image for Fritz!Box 7490 use this command:
./i-matik 7490.multi
```
List of currently push supported devices (BOX_TYPE): 1200 1200AX 1240AX 1240E 1260E 1260v2 1750E 2400 3000 3000AX 300E 3272 3370 3370-Alien3490 3390 3390-Alien3490 3490 4020 4040 4050 4060 450E 540E 546E 5490 5491 5530 5590 5690Pro 6000 6430 6490 6590 6591 6660 6670 6690 6810 6820v1 6820v2 6820v3 6840 68504g 68505g 6890 7240 7270v2 7270v3 7272 7312 7320 7320-Alien7330 7330 7330SL 7340 7360v1 7360v2 7362 7369 7390 7412 7412-Alien7430 7430 7490 7510 7520 7520-Alien7530 7520B 7530 7530AX 7560 7580 7581 7582 7583 7583vdsl 7590 7590AX 7690 DVB-C DVB-c-Alien1750E Gateway
```
Push the create image to the Fritz!Box 7490, use this command
./i-matik 7490 -push
```
./i-matik toolchain.11 
```
Create your own toolchains
```
./i-matik create
