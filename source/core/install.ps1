function Run() {
    # ==== Get User Input ====

    # ==== Install and Setup ====
    #* Local Install Git

    # ==== Setup Interfacing Mechanisms ====
    #* Add Macros
    #* Group Policy
    #* Command and Module Manager
}

#* Require Admin
if(!([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) {
    Start-Process -FilePath PowerShell.exe -Verb Runas -ArgumentList "-File `"$($MyInvocation.MyCommand.Path)`"  `"$($MyInvocation.MyCommand.UnboundArguments)`""
    Run
    Exit
}
