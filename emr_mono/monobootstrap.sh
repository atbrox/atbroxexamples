#!/bin/bash

#wget http://downloads.sourceforge.net/project/mono-parallel/mono-2.8.2-parallel-environment-amd64.deb?r=http%3A%2F%2Fblog.fusonic.net%2F2010%2F10%2Fmono-2-8-parallel-environment-debianubuntu-package%2F&ts=1296899984&use_mirror=surfnet
# http://www.devcomments.com/New-Elastic-MapReduce-Feature-Bootstrap-Actions-i24341.htm
hadoop fs -copyToLocal s3://emrmono/mono-2.8.2-parallel-environment-amd64.deb .
ls -l
type dpkg
sudo dpkg -i mono-2.8.2-parallel-environment-amd64.deb 

# fsharp stuf
# use wget or hadoop copyToLocal
wget http://www.microsoft.com/downloads/info.aspx?na=46&SrcFamilyId=EFFC5BC4-C3DF-4172-AD1C-BC62935861C5&SrcDisplayLang=en&u=http%3a%2f%2fdownload.microsoft.com%2fdownload%2f4%2f5%2fB%2f45BD9FBC-22BA-4B45-84B7-17D1AD0122A1%2ffsharp.zip
unzip fsharp.zip
cd fsharp
wget --no-check-certificate -O mono.snk https://github.com/mono/mono/raw/master/mcs/class/mono.snk
chmod +x install-mono.sh
sudo ./install-mono.sh

# compiling fsharp
mono bin/fsc.exe --standalone script.fsx
mkbundle -o script script.exe --deps --static




