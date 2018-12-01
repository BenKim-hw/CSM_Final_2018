#!/bin/bash

echo "Bash version ${BASH_VERSION}..."

 for i in {3..5..1}
    do
./gtrieScanner -s $i -m esu -g data/D_mouse_retina_1.txt -d -o result/D_mouse_retina_"$i".txt -r 10 -f simple_weight
	done

