#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2015-01-21 22:42:44 -0500 (Wed, 21 Jan 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h10/Prelab01/line_num.bash $
#$Revision: 73428 $
if (($#!=1))
then
    echo "Usage: line_num.bash <filename>"
elif [[ ! -r $1 ]]
then
    echo "Cannot read $1"
else
    i=1
    while read name
    do
        echo "$i:$name"
        i=`expr $i + 1`
    done < $1
fi

exit 0
