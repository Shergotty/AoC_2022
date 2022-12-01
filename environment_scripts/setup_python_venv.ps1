# redirect stderr into stdout
$p = & { python -V } 2>&1
$python_version = [System.Version]"3.11.0"
$reference_version = [System.Version]"3.10.8"
$version_number = if (!($p -is [System.Management.Automation.ErrorRecord])) {
    [System.Version]($p -replace '\D+(\s+)', '$1')
}

function install_python {

    $filename = "python-$python_version-amd64.exe"
    $uri = "https://www.python.org/ftp/python/$python_version/$filename"
    $outpath = "C:\Users\$env:UserName\Downloads\"    
    $out = $outpath + $filename

    Write-Output "Python $python_version will be downloaded. The Installer runs in the background and the Install path will be added to system variables."
    Start-Sleep -seconds 0.5
    $response = read-host "Press [enter] to continue or [any other key] (and then [enter]) to abort"
    $aborted = ! [bool]$response
    if (!$aborted) { exit }
    Write-Output "Python installation filw will be downloaded to $outpath"
    Invoke-WebRequest -URI $uri -OutFile $out
    Write-Output "Python installation started ..."
    Start-Process $out -Wait -ArgumentList '/quiet', 'InstallAllUsers=0', 'PrependPath=1', 'InstallLauncherAllUsers=0'
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
    Write-Output "... Python installation complete and system variables extendet"
    REMOVE-Item $out
    Write-Output "Python installation file deleted from $outpath"
}

function setup_venv {
    if (!(Test-Path env:VIRTUAL_ENV)) {
        python -m venv .\venv
    }
    .\venv\Scripts\Activate
    Write-Output "venv active"
    Write-Output "venv installed in $env:VIRTUAL_ENV"
}

# check if an ErrorRecord was returned or [System.Version] is less than $reference_version
if (!($p -is [System.Management.Automation.ErrorRecord] -or $version_number -lt $reference_version)) {
    # return as is and run setup_venv
    Write-Output $p" installed"
    setup_venv
}
else {
    # otherwise grab the version string from the error message and run install_python  
    Write-Output "python has not been found or your version number is lower than Python $reference_version"
    install_python
    setup_venv
}
