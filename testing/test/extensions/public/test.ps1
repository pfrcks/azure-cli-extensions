$sslKeyPemFile = Join-Path (Join-Path (Split-Path $PSScriptRoot -Parent) "data") "test_key.pem"
$sslCertPemFile = Join-Path (Join-Path (Split-Path $PSScriptRoot -Parent) "data") "test_cert.pem"

Write-Output $sslKeyPemFile