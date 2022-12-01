try { deactivate }
catch {Write-Output "venv already deactivated"}
Remove-Item .\venv -Force -Recurse