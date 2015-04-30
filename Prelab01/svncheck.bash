#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2015-01-21 22:31:44 -0500 (Wed, 21 Jan 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h10/Prelab01/svncheck.bash $
#$Revision: 73425 $
if (($#!=1))
then
    echo "Usage: svncheck.bash <filename>"
elif [[ ! -r $1 ]]
then
    echo "Cannot read $1"
else
    while read name
    do
        echo "Reading $name"
        STAS=$(svn status $name)
        if [[ $STAS == ?* ]]
        then
           if  [[ -e $name ]]
           then
               if [[ ! -x $name ]]
               then
                   echo "Do you want to make the file \"line\" executable? (y/n" 
                   read ans
                   if (($ans=='y'))
                   then
                       chmod +x $name
                   fi
               fi
               svn add $name
           else
               echo "Error: File $name appear to not exist here or in svn"
           fi
       elif [[ $STAS != ?* ]]
       then
           if [[ ! -x $name ]]
           then
               svn propset svn:executable ON $name
           fi
       fi
    done < $1
fi

exit 0

