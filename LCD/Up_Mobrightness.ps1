﻿$delay=30
$FileName = ".\CurrentBrightnessLog.txt"
$myMonitor = Get-WmiObject -Namespace root\wmi -Class WmiMonitorBrightnessMethods



if (Test-Path $FileName) 
{
    $brightness=Get-Content .\CurrentBrightnessLog.txt
    $brightness=$brightness -as [int]
    Echo change_brightness=$brightness


        if($brightness -eq 100)
            {

                Echo change_brightness=$brightness
                $myMonitor.wmisetbrightness($delay, $brightness)
            
            }
            else
            {
            
                while($brightness -ge 0 -and $brightness -le 90)
                    {
                         $brightness=$brightness+10
                         Echo change_brightness=$brightness
                         $myMonitor.wmisetbrightness($delay, $brightness)
                         $brightness=$brightness > CurrentBrightnessLog.txt
                    }
    
            }

}
else
{
    $brightness=0 > CurrentBrightnessLog.txt
    $myMonitor.wmisetbrightness($delay, 0)
    $brightness=Get-Content .\CurrentBrightnessLog.txt
    Echo change_brightness=$brightness
}
