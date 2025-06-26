# start_selfbot.ps1 ─ instala dependências e executa o bot
Write-Host "🔧 Instalando dependências..."
pip install -r requirements.txt

Write-Host "`n🚀 Iniciando o selfbot..."
python selfbot.py
