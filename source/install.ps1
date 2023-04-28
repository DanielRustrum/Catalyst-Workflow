#* Run if Admin Access Aquired
function RunIfAdmin() {
	#* Initial Catalyst Setup
	#* Inquire User About Configuration
	
	#* Check if Docker is Installed
	try {
		docker --version
	} catch {
		echo "Docker Installation isn't Setup Yet"
		#* Fetch Latest Docker Installer for Windows and Install
		#* Setup Docker For Catalyst Use
	}

	#* Check if Git is Installed
	try {
		git --version
	} catch {
		echo "Git Installation isn't Setup Yet"
		#* Fetch Git Installer For Windows and Install
		#* Setup Git For Catalyst Use
	}
	
	#* Check if Hyper-V/ is Install
	$hyperv = Get-WindowsOptionalFeature -FeatureName Microsoft-Hyper-V-All -Online

	if($hyperv.State != "Enabled") {
		#* Setup Hyper-V For Catalyst Use
		#* Prepare For Catalyst Use
	}

	#* Check if NeoVim is Installed
		#* Fetch Latest NeoVim Installer and Install
		#* Setup NeoVim For Catalyst Use

	#* Check if Desired PowerToys are Installed
		#* Install and Setup PowerToys
	
	#* Final Catalyst Setup
}

#* Check if in Admin and Execute Run Function
if(
	!(
		[Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()
	).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')
) {
    Start-Process -FilePath PowerShell.exe -Verb Runas -ArgumentList \
    "-File `"$($MyInvocation.MyCommand.Path)`"  `"$($MyInvocation.MyCommand.UnboundArguments)`""
    
    RunIfAdmin
    Exit
}
