#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2015-01-25 16:16:18 -0500 (Sun, 25 Jan 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h10/Prelab02/yards.bash $
#$Revision: 73818 $
if (($#!=1))
then
    echo "Usage: yards.bash <filename>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable"
    exit 1
fi
max_avg=0
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
    for I in ${Data[*]}
    do
        if (( $I != ${Data[0]} ))
        then
            var=$(($var+($I - $avg)*($I-$avg)))
        fi
    done
    var=$(($var/$t_num)) 

    echo "${Data[0]} schools averaged $avg yards receiving with a variance of $var"
    if (( $avg > $max_avg ))
    then
        max_avg=$(($avg))
    fi
done < $1
echo "The largest average yardage was $max_avg"
exit 0

