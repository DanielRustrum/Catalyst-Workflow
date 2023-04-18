function Run() {
    if (Get-Module -ListAvailable -Name ps2exe) {
        Write-Host "PS2EXE is Installed"
    } 
    else {
        Install-Module ps2exe 
    }
}

if(!([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) {
    Start-Process -FilePath PowerShell.exe -Verb Runas -ArgumentList "-File `"$($MyInvocation.MyCommand.Path)`"  `"$($MyInvocation.MyCommand.UnboundArguments)`""
    Run
    Exit
}
