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

#=====[ Step 3: make pyroJect hashbanged/executable	]=====
echo '#!'$USER_PYTHON | cat - pyroJect.py > temp && mv temp pyroJect
chmod +x pyroJect
echo "- Created executable ./pyroJect"

#=====[ Step 4: add this path to .bash_profile, if it doesn't already exist	]=====
#Copied/modified from:
# http://stackoverflow.com/questions/4479579/bash-script-only-echo-line-to-bash-profile-once-if-the-line-doesnt-yet-exis
TITLE_LINE="#=====[ pyroJect ]====="
PATH_LINE="export PATH=\$PATH:`pwd`"
BASH_PROFILE=~/.bash_profile
check_if_line_exists()
{
    grep -qsFx "$TITLE_LINE" $BASH_PROFILE
}
add_line_to_bash_profile()
{
    BASH_PROFILE=~/.bash_profile
    printf "\n%s\n%s\n" "$TITLE_LINE" "$PATH_LINE" >> "$BASH_PROFILE"
}
check_if_line_exists || add_line_to_bash_profile
echo "- Ensured path to ./pyroJect is in \$PATH environmental variable"


#=====[ Step 5: add it to current path	]=====
export PATH=$PATH:`pwd`