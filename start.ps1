$value=Test-Path ("$pwd"+"\chromedriver.exe")
pip3 install selenium
if($value -notmatch 'True')
{

Write-Output "Downloading chrome driver"
$ver=(Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe').'(Default)').VersionInfo.ProductVersion
$client = new-object System.Net.WebClient
$URI="https://chromedriver.storage.googleapis.com/LATEST_RELEASE_"+$ver[0]+$ver[1]
$HTML=Invoke-WebRequest -Uri $URI
$driver=$HTML.Content
$client.DownloadFile("https://chromedriver.storage.googleapis.com/"+$driver+"/chromedriver_win32.zip","$PWD"+'\chromedriver_win32.zip')
Expand-Archive -LiteralPath ("$PWD"+"\chromedriver_win32.zip") -DestinationPath "$pwd"
Remove-Item -Path ("$PWD"+"\chromedriver_win32.zip")
}

$search = Read-Host 'What is your search query?'
$number = Read-Host 'What is the number of professors you want to search?' 

python3 prof.py $search $number