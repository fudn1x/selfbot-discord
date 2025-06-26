# 🤖 Discord Selfbot — Modo Seguro 🛡️

Selfbot em Python para **apagar mensagens da própria conta** (DMs ou grupos) com delays automáticos, evitando rate limits.  
> ⚠️ **Aviso**: Selfbots violam os Termos do Discord. Use apenas com **contas secundárias**, por sua conta e risco.

---

## Comandos

| Comando | Descrição |
|---------|-----------|
| `!apagar <n>` | Apaga até **n** mensagens suas |
| `!apagarpalavra <texto>` | Apaga mensagens contendo **texto** |
| `!apagarlinks` | Apaga mensagens com links |
| `!nuke` | Apaga até 1000 mensagens no canal atual |

---

## 🚀 Como usar

### 🐧 Linux (Terminal)

```bash
# 1. Clone
git clone https://github.com/fudn1x/selfbot-discord
cd selfbot-discord

# 2. Instale dependências
pip install -r requirements.txt
sudo apt install python3-tk  # se não tiver Tk instalado

# 3. Rode
python3 selfbot.py
# Cole o token quando solicitado
```


### Windows (PowerShell)

```bash
# 1. Clone ou baixe o ZIP do projeto
git clone https://github.com/fudn1x/selfbot-discord
cd selfbot-discord

# 2. Execute o script (instala e roda de uma vez)
.\start_selfbot.ps1
# Cole o token quando solicitado
```
