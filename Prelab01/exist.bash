#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2015-01-21 22:41:30 -0500 (Wed, 21 Jan 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h10/Prelab01/exist.bash $
#$Revision: 73427 $
while (($#>0))
do 
    #echo $1
    if [[ -r $1 ]]
    then
        echo "File <$1> is readable!"
    elif [[ ! -e $1 ]]
    then
        touch $1
    fi
    shift
done

exit 0
