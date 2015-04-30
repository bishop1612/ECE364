#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2015-01-21 22:40:12 -0500 (Wed, 21 Jan 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h10/Prelab01/sensor_sum.sh $
#$Revision: 73426 $
if (($#!=1))
then
    echo "Usage: sensor_sum.sh <filename>"
elif [[ ! -r $1 ]]
then
    echo "$1 is not readable"
else
    while read name
    do
        sum=0
        v=($name)
        ((sum = v[1] + v[2] + v[3]))
        echo -n "$name " | head -c2
        echo -n " "
        echo "$sum"
    done < $1
fi

exit 0


