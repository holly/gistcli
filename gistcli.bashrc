# Default values for shell variables we use
PYTHONPATH=${PYTHONPATH-""}
PATH=${PATH-""}
MANPATH=${MANPATH-""}

# When run using source as directed, $0 gets set to bash, so we must use $BASH_SOURCE
if [ -n "$BASH_SOURCE" ] ; then
    APP_DIR=$(dirname "$BASH_SOURCE")
elif [ $(basename -- "$0") = "cli.bashrc" ]; then
    APP_DIR=$(dirname "$0")
else
    APP_DIR="$PWD"
fi

APP_HOME=$(realpath $APP_DIR)

PREFIX_PYTHONPATH="$APP_HOME/lib"
PREFIX_PATH="$APP_HOME/bin"
PREFIX_MANPATH="$APP_HOME/docs/man"

echo "$PYTHONPATH" | grep -q "${PREFIX_PYTHONPATH}" || export PYTHONPATH="$PREFIX_PYTHONPATH:$PYTHONPATH"
echo "$PATH" | grep -q "${PREFIX_PATH}" || export PATH="$PREFIX_PATH:$PATH"
echo "$MANPATH" | grep -q "${PREFIX_MANPATH}" || export MANPATH="$PREFIX_MANPATH:$MANPATH"
