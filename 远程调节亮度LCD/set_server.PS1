Enable-PSRemoting -Force
Set-WSManQuickConfig -Force
Set-Item wsman:\localhost\client\trustedhosts * -Force
Restart-Service winRM
Get-Item wsman:\localhost\client\trustedhosts
Clear-Item WSMan:\localhost\Client\TrustedHosts -Force
Get-Item wsman:\localhost\client\trustedhosts