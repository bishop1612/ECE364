#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2015-01-25 16:33:07 -0500 (Sun, 25 Jan 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h10/Prelab02/process_temps.bash $
#$Revision: 73823 $
if (($#!=1))
then
    echo "Usage: process_temps.bash <input file>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable"
    exit 2
fi
loop=0
while read -a Data
do
    sum=0
    var=0
    t_num=$(( ${#Data[*]} -1 ))
    for I in ${Data[*]}
    do
        if (( $I != ${Data[0]} ))
        then
             sum=$(($sum+$I))
        fi
    done
    avg=$(($sum/$t_num))
    if (( $loop != 0 ))
    then
        echo "Average temperature for time ${Data[0]} was $avg C"
    fi
    loop=$(($loop+1))
done < $1
exit 0

