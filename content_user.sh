#!/usr/bin/env bash

#!/bin/bash

if [[ -n "$1" ]];

then

    file=$1

else

    file=content_watch.csv

fi

count=$(echo "(cut -d',' -f1 $file| sort| uniq -c | sort |grep -v user_id| wc -l) / 100" | bc)
cut -d',' -f1 $file| sort| uniq -c | sort |grep -v user_id| head -$count > user.csv