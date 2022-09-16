#!/bin/bash

check_file (){
    local file_name_pass
    file_name_pass=$1
    local files
    files=$(pwd)
    files+="/"
    files+="$file_name_pass"

    if [ -f "${files}" ]; then
        echo "********************************"
        echo "File \"${files}\" exists"
        local data_file
        data_file=$(tail -10 "${files}")
        local lines
        lines=$(wc -l "${files}")
        if [[ lines -gt  10 ]]; then
           echo "it has minimum line of 10"
        else
           echo "it has only ${lines} lines"
        fi        
        echo "********************************"
        echo "$data_file"
        echo "********************************"

    else
        echo "********************************"
        echo "File \"${files}\"does not exists"
        echo "********************************"
    fi  

}


if [[ $# = 0 ]]; then
    echo "please enter file name"
    read -r file_name
elif [[ $# = 1 ]]; then
    file_name=$1
else
   echo 'too many arguments'   
fi

check_file "$file_name"