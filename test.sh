#!/bin/bash

images=( "lixo1_420.jpg" "lixo2_420.jpg" "flower_420.jpg" "trash_420.jpg" )

for i in "${images[@]}"
do
    printf "Image %s\n" "$i" >> resp
    { time python test_1_time.py "$i" ; } 2>> resp
    { time python test_2_time.py "$i" ; } 2>> resp
    python test_1_memory.py "$i" >> resp
    python test_2_memory.py "$i" >> resp

done
