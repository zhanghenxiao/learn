Set-ExecutionPolicy Unrestricted -Force

$delay=5
$myMonitor = Get-WmiObject -Namespace root\wmi -Class WmiMonitorBrightnessMethods
$brightness=Read-Host "Please enter the brightness you need to adjust.(0~100)"
$brightness=$brightness -as [int]

if($brightness -is [int])
{
    
    if($brightness -ge 0 -and $brightness -le 90)
    {
                  
        $myMonitor.wmisetbrightness($delay, $brightness)
        
    }
    else
    {
        Echo "There only support nunber:0~100"
        Read-Host
    
    }


}
else
{
    echo "Types other than numbers are not supported,please try again"
    Read-Host

        
}


