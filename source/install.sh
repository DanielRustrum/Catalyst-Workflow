$DEP_SOURCE = "https://raw.githubusercontent.com/DanielRustrum/Catalyst-Workflow/main/source/dependencies/"
$CATALYST_CONFIG_DIR = "~/.config/catalyst"
$CATALYST_WORKING_DIR = "/bin/catalyst"

if [[ ! -d $CATALYST_WORKING_DIR ]]; then
	wget "$DEP_SOURCE/temp.txt" -P "$CATALYST_WORKING_DIR/dependencies"
fi
