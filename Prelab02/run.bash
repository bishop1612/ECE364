#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2015-01-26 12:24:21 -0500 (Mon, 26 Jan 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h10/Prelab02/run.bash $
#$Revision: 73916 $
if (($#!=2))
then
    echo "Usage: run.bash <input file> <output file>"
    exit 0
elif [[ ! -e $1 ]]
then
    echo "Error: $1 does not exist"
    exit 0
fi
max_avg=0
OUTPUT=$2
if [[ -e $2 ]]
then
    read -p "$2 exists. Would you like to delete it?" CHOICE
    if [[ $CHOICE  == "n" ]]
    then
        read -p "Enter a filename: " OUTPUT
    else
        rm $2
    fi
fi

EXEC="quick_sim"

if [[ -e $EXEC ]]
then 
    rm $EXEC
fi

if $(gcc $1 -o $EXEC)
then
    echo  ""
else
    echo "error: $EXEC could not be compiled"
    exit 1
fi

for CACH in {1,2,4,8,16,32}
do
    for ISS in {1,2,4,8,16}
    do
        READ=$($EXEC $CACH $ISS a)
        while read -r line
        do
            VAL=$(echo "$line" | cut -d':' -f2,4,6,8,10 )
            #echo "$line"
            echo $VAL >> $OUTPUT
        done <<< "$READ"
        READ=$($EXEC $CACH $ISS i)
        while read -r line
        do
            VAL2=$(echo "$line" | cut -d':' -f2,4,6,8,10 )
            echo $VAL2 >> $OUTPUT
        done <<< "$READ"
    done
done
    
exit 0

