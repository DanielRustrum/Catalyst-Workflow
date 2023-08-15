$DEP_SOURCE = "https://raw.githubusercontent.com/DanielRustrum/Catalyst-Workflow/main/source/dependencies/"
$CATALYST_CONFIG_DIR = "~/.config/catalyst"
$CATALYST_WORKING_DIR = "/bin/catalyst"

if [[ ! -d $CATALYST_WORKING_DIR ]]; then
	$CATALYST_DEP_DIR = $CATALYST_WORKING_DIR/dependencies
	mkdir $CATALYST_DEP_DIR
	wget $DEP_SOURCE/temp.txt -P $CATALYST_DEP_DIR
	wget $DEP_SOURCE/temp.txt -P $CATALYST_DEP_DIR
	wget $DEP_SOURCE/temp.txt -P $CATALYST_DEP_DIR
fi
