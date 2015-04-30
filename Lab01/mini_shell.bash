#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2015-01-22 10:12:21 -0500 (Thu, 22 Jan 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364h10/Lab01/mini_shell.bash $
#$Revision: 73469 $
exitcode=0
while (( $exitcode == 0 ))
do
    echo -n "Enter a command: "
    read command
    if [[ $command == "hello" ]]
    then
        echo "Hello $(whoami)"
    fi
    if [[ $command == "quit" ]]
    then
       echo "Exiting..."
        exitcode=1
    fi
    if [[ $command == "compile" ]]
    then
        echo -n "Enter filename: " 
        read name
        if [[ -r $name ]]
        then
            gcc -Wall -Werror $name
            if (( $? == 0 ))
            then
                echo "Compilation succeeded"
            else
                 echo "Compilation failed"
            fi
        else
            echo "File does not exist"
        fi
    fi
    if [[ $command != "quit" && $command != "hello" && $command != "compile" ]]
    then
        echo "Error: Unrecognized input"
    fi
done

exit 0

