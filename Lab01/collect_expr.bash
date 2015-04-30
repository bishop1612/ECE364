#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2015-01-22 11:22:58 -0500 (Thu, 22 Jan 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h10/Lab01/collect_expr.bash $
#$Revision: 73510 $
if (($#<2))
then
    echo "collect_expr.bash <output file> <input file 1> <input file 2> ... [input file N]"
    exit 1
fi
if [[  -e $1 ]]
then
    echo "error: output file $1 already exists!"
   exit 2
fi
output=$1
    while (($# > 0))
    do
        shift
        file=$1
        #if (( $I != 1))
        #then
            while read a b c d e f
            do
                sum=0
                avg=0
                v=($name)
                (( sum = b + c + d + e + f ))
                (( avg = $sum/5))
                echo "$a $b $c $d $e $f $sum $avg" >> $output
        done <<< $file
        #fi
    done

exit 0


