#!/bin/sh

usage ()
{
  echo 'Usage : triplet-encoding-controller.sh <input-genetree-file> <output-triplet_list>'
  exit
}

if [ "$#" -ne 2 ]
then
  usage
fi

sh triplet_count.sh $1 | perl summarize_triplets_stdin.pl > $2
