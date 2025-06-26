# 🤖 Discord Selfbot Educacional — Modo Seguro 🛡️

Este é um projeto que permite o uso de um **selfbot em Python** para apagar mensagens da **própria conta de usuário** no Discord — com foco em **privacidade, segurança e respeito aos limites da API**.

> ⚠️ **Atenção**: Selfbots violam os Termos de Uso do Discord. Use apenas com **contas secundárias**, por sua conta e risco, e exclusivamente para fins de aprendizado.

---

## 🧠 O que ele faz?

Este selfbot permite que você:

- Apague mensagens em massa em **DMs ou grupos**
- Filtre mensagens por palavra-chave ou links
- Execute comandos de forma segura e com delays automáticos
- Use o modo **“nuke seguro”** para apagar até 1000 mensagens disfarçadamente

---

## ✅ Comandos disponíveis

| Comando               | O que faz                                                  |
|-----------------------|------------------------------------------------------------|
| `!apagar <n>`         | Apaga até `n` mensagens suas no canal atual               |
| `!apagarpalavra <txt>`| Apaga mensagens que contenham a palavra especificada      |
| `!apagarlinks`        | Apaga mensagens que contenham links (https://...)         |
| `!nuke`               | Apaga até 1000 mensagens suas no canal atual              |

Todos os comandos têm **delays aleatórios** entre ações para reduzir a chance de detecção pela API do Discord.

---
