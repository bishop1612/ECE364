#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2015-01-19 23:42:47 -0500 (Mon, 19 Jan 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h10/Prelab01/check_file.bash $
#$Revision: 72908 $
if (($#!=1))
then
    echo "Usage: check_file.bash <filename>"
    exit 0
fi
if [[  -e $1 ]]
then
    echo "$1 exists"
else
    echo "$1 does not exist"
fi

if [[ -d $1 ]]
then
    echo "$1 is a directory"
else
    echo "$1 is not a directory"
fi

if [[ -f $1 ]]
then
    echo "$1 is ordinary"
else
    echo "$1 is not ordinary"
fi

if [[ -r $1 ]]
then 
    echo "$1 is readable"
else
    echo "$1 is not readable"
fi

if [[ -w $1 ]]
then
    echo "$1 is writable"
else
    echo "$1 is not writable"
fi

if [[ -x $1 ]]
then
    echo "$1 is executable"
else
    echo "$1 is not executable"
fi
exit 0
