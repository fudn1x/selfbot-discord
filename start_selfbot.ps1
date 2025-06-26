# start_selfbot.ps1
Write-Host ""
Write-Host "Instalando dependências..."
pip install -r requirements.txt

Write-Host ""
Write-Host "Iniciando o selfbot..."
python selfbot.py
