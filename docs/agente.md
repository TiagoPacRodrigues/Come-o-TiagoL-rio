# O Agente de Marketing — como funciona

## As 4 peças

```
        VOCÊ (aqui no Claude ou no Telegram)
                     │  pede
                     ▼
┌───────────────────────────────────────────┐
│ 1. CÉREBRO        CLAUDE.md               │  quem ele é, como pensa, regras
│ 2. MEMÓRIA        docs/                   │  segundo cérebro: empresa, marca, aprendizados
│ 3. HABILIDADES    .claude/skills/         │  relatório, insight, e-mail…
└───────────────────────────────────────────┘
                     │  busca dados / executa
                     ▼
 4. CONEXÕES   Meta Ads · Google Ads · GA4 · RD Station · site · ERP
```

| Peça | Status |
|---|---|
| Cérebro (`CLAUDE.md`) | ✅ Pronto (versão 1) |
| Memória (`docs/`) | 🟡 Começando: perfil, análise do site, glossário |
| Habilidades | 🟡 3 prontas: `relatorio-campanhas`, `insight-mercado`, `email-marketing` |
| Conexões | 🔴 Nenhuma ainda. Por enquanto, os dados entram por planilha exportada em `dados/` |
| Telegram | 🔴 A configurar (ver abaixo) |

## O que já funciona hoje (nesta conversa ou numa sessão nova deste repositório)
- **"Me traga um insight do mercado e no que focar agora"** → funciona: usa pesquisa na web e o calendário religioso.
- **"Monta um e-mail marketing para minha base"** → funciona: gera texto e HTML, você cola no RD Station.
- **"Como estão as campanhas?"** → funciona **com planilhas exportadas** em `dados/`. Fica automático depois das conexões.

## Telegram — duas formas

**A) Avisos e relatórios automáticos (de mão única)**
Tarefas agendadas na nuvem (ex.: todo dia às 8h, ou de hora em hora) rodam a habilidade e mandam o resultado para o Telegram por um bot.
- Precisa: criar um bot no Telegram (@BotFather), liberar `api.telegram.org` na rede do ambiente e guardar o token do bot como **segredo de rede** do ambiente (nunca no repositório).
- Bom para: "relatório de campanhas todo dia", "alerta se o gasto disparar".

**B) Conversa de verdade pelo Telegram (ida e volta)**
O Claude Code tem um plugin oficial de Telegram: você manda mensagem para o bot e o agente responde, com acesso a este repositório e às habilidades.
- Precisa de um **computador ou servidor sempre ligado** rodando o Claude Code com o plugin. Pode ser um PC da empresa ou um servidor pequeno na nuvem.
- Bom para: "monta um e-mail…", "e aquela campanha de Natal?" a qualquer hora, pelo celular.

**Sugestão:** começar pela A (rápida, sem servidor) e partir para a B quando o agente estiver maduro.

## Conexões — o que pedir e para quê
| Conexão | Libera | Como |
|---|---|---|
| Meta Ads | Relatório automático de Instagram/Facebook | API de Marketing do Meta (token de sistema do Gerenciador de Negócios, só leitura no começo) |
| Google Ads | Relatório automático do Google | API do Google Ads (token de desenvolvedor) |
| Google Analytics 4 | Visitas, origem, conversões do site | API de Dados do GA4 (conta de serviço com acesso de leitor) |
| RD Station | Base de e-mails, envio, resultados | API do RD Station Marketing |
| ERP | Vendas reais, inclusive WhatsApp/telefone | Depende do sistema (a descobrir) |

Cada conexão começa **só com leitura**. Ações que gastam dinheiro ou enviam algo sempre pedem aprovação.

## Sobre "relatório de hora em hora"
Anúncios oscilam muito de uma hora para outra, e o algoritmo do Meta e do Google precisa de dias para aprender. Mexer na campanha a cada hora costuma **piorar** o resultado. Por isso:
- **De hora em hora:** só **alertas** (gasto anormal, anúncio reprovado, campanha parada).
- **Diário:** resumo do que rendeu.
- **Semanal:** análise com recomendações de ajuste.
