#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2015-01-21 22:44:25 -0500 (Wed, 21 Jan 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h10/Prelab01/sum.bash $
#$Revision: 73429 $
sum=0
while (($#>0))
do
    sum=`expr $sum + $1`
    shift
done
echo "$sum"

exit 0
