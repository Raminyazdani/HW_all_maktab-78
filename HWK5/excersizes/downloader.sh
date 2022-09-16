#!bin/bash

validate_url() {
    if wget -q --spider $1
    then
        result=1
    else
        result=0
    fi
}
directory_exist(){
    if [[ ! -e log.txt ]]
    then
        echo "log.txt not found"
        echo "log.txt creating..."
        touch log.txt
    else
        echo "log.txt exists"
    fi
}

download() {
    echo "enter your URL addresee for download..."
    read URL
    validate_url $URL
    if (("$result"=="1"))
    then
        directory_exist
        mkdir download_"$URL"
        wget -q -O download_"$URL"/data $URL
        echo "download $URL successfully" >> log.txt
        echo "download complete"
    else
        directory_exist
        echo "download $URL Unsuccessfully" >> log.txt
        echo   "download failed"
    fi
}

download
