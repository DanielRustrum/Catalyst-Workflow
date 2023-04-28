#* Run if Admin Access Aquired
function RunIfAdmin() {
	#* Initial Catalyst Setup
	#* Inquire User About Configuration
	#* Check if Docker is Installed
		#* Fetch Latest Docker Installer for Windows and Install
		#* Setup Docker For Catalyst Use
	#* Check if Git is Installed
		#* Fetch Git Installer For Windows and Install
		#* Setup Git For Catalyst Use
	#* Check if Hyper-V/ is Installed
		#* Setup Hyper-V For Catalyst Use
		#* Prepare For Virtualization Use
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
