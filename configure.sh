#!/bin/bash          
#=====[ Step 1: find the user's python	]=====
USER_PYTHON=`which python`
echo "- Using python located at: $USER_PYTHON"

#=====[ Step 2: remove all hashbangs from pyroJect.py	]=====
TOP_LINE=`head -n 1 pyroJect.py`
while [ ${TOP_LINE:0:2} = "#!" ]
do
	cat pyroJect.py | tail -n +2 > temp && mv temp pyroJect.py
	TOP_LINE=`head -n 1 pyroJect.py`
done

#=====[ Step 3: insert it at the top of pyroJect.py	]=====
echo '#!'$USER_PYTHON | cat - pyroJect.py > temp && mv temp pyroJect.py

#=====[ Step 4: make the script executable	]=====
chmod +x pyroJect.py

