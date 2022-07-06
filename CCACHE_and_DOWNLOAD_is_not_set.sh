#!/bin/bash
#start point this shows you how long it took him to create the images
I_MATIK_PATH=$(cd `dirname $0` && pwd)
begin=$(date +"%s")
sed -i '$a# FREETZ_TOOLCHAIN_CCACHE is not set' $I_MATIK_PATH/support/freetz/openssl_10/config_fritz*
sed -i '$a# FREETZ_HOSTTOOLS_DOWNLOAD is not set' $I_MATIK_PATH/support/freetz/openssl_10/config_fritz*
sed -i '$a# FREETZ_TOOLCHAIN_CCACHE is not set' $I_MATIK_PATH/support/freetz/openssl_11/config_fritz*
sed -i '$a# FREETZ_HOSTTOOLS_DOWNLOAD is not set' $I_MATIK_PATH/support/freetz/openssl_11/config_fritz*
sed -i '$a# FREETZ_TOOLCHAIN_CCACHE is not set' $I_MATIK_PATH/support/freetz/openssl_30/config_fritz*
sed -i '$a# FREETZ_HOSTTOOLS_DOWNLOAD is not set' $I_MATIK_PATH/support/freetz/openssl_30/config_fritz*
sed -i '$a# FREETZ_TOOLCHAIN_CCACHE is not set' $I_MATIK_PATH/support/freetz/openssl_multi/config_fritz*
sed -i '$a# FREETZ_HOSTTOOLS_DOWNLOAD is not set' $I_MATIK_PATH/support/freetz/openssl_multi/config_fritz*

#end point this shows you how long it took him to create the images
termin=$(date +"%s")
difftimelps=$(($termin-$begin))
echo "$(($difftimelps / 60)) minutes and $(($difftimelps % 60)) seconds elapsed for Script Execution."


### read https://www.digital-eliteboard.com/threads/laberthread-fuer-i-matik.507656/post-4042163
