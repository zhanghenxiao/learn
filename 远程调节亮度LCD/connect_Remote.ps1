$ip='10.10.10.11'    #ip 也是对方  
#$Username = 'Administrator' #需要连接对应 username ，用户需设密码
$brightness=Read-Host "Please enter the Server unit name:"
$Password = '123'
$pass = ConvertTo-SecureString -AsPlainText $Password -Force
$Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass
Set-Item WSMan:\localhost\Client\TrustedHosts -Value * -Force
Invoke-Command -ComputerName $ip -ScriptBlock { Get-ChildItem C:\ } -Credential $Cred
Enter-PSSession -ComputerName $ip -Credential $Cred



