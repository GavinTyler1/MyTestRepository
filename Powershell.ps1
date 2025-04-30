
function decryptAPIKey ($file) {
    foreach ($line in $file){
      $line.APIKey = Decrypt-String "$($line.encryptedAPIKey)" -Passphrase $Passphrase -salt $salt -init $init
      }
  }

function set-headers($fart) {
  $headers = @{
    'accept' = 'application/json'
    'authorization' = 'Api-Key '+ $fart
    'cache-control' = 'no-cache'
    'content-type' =  'application/json'
  }
}

$Passphrase = '"GreatPass"'
$salt = '"GreatSalt"'
$init = '"GreatInit"'


#_MkK2O0Zi8ujD1mC3i8jky2gBJ442cE3B1EKrvnpyjNvehVmAvs
#Hard coded key example
$configFile = Get-Content "C:\Users\gtyler01\Scripts\TokenSecurity\Config.json" | ConvertFrom-json
decryptAPIKey $configFile 
$apitoken = $configFile.APIKey
$baseURL = $configFile.BaseURL
$headers = set-headers($apitoken)



write-host("test")
write-host($apitoken)
write-host($baseURL)
write-host($headers.authorization)

$response = Invoke-Webrequest $baseURL -Method 'POST' -Headers $headers
write-host($response)


