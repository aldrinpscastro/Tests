#!/bin/bash

nonce=1

if [ -z $1 ]; then
	difficulty=1
else
	if [ $1 != 0 ]; then
		difficulty=$1
	else
		exit 1
	fi
fi

basezeros=$(echo 10^$difficulty | bc)

qzeros=${basezeros:1}

tinit=$(date +%s)

hash=$(echo -n $nonce | sha256sum | awk '{print $1}')

while [ ${hash:0:$difficulty} != $qzeros ]; do

	let "nonce=nonce+1"

	hash=$(echo -n $nonce | sha256sum | awk '{print $1}')

done

tend=$(date +%s)

let "delta=tend-tinit"

echo $hash $nonce $delta >> test.txt
