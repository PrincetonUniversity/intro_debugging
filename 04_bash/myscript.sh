#!/bin/bash

echo "Number of command line parameters: $#"
echo "All the command line parameters: $@"

UPPER=3
for i in `seq $UPPER`; do
    echo $i
done

if [ $1 -ge 3 ]; then
    echo "$1 > 3"
fi

hostname
