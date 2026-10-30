---
name: relatorio-campanhas
description: Relatório de desempenho dos anúncios (Meta e Google) e do site da Lírio do Vale — o que está dando resultado, o que está desperdiçando verba e o que ajustar. Use quando pedirem "como estão as campanhas", "o que está dando mais resultado", "relatório de anúncios", "quanto gastamos", ou num relatório agendado (diário/por hora).
---

# Relatório de campanhas

## 1. Pegar os dados (na ordem de preferência)
1. **Conexão direta**: se houver ferramenta/conector de Meta Ads, Google Ads ou Google Analytics disponível na sessão, use-a.
2. **Planilhas exportadas**: procure em `dados/` arquivos CSV/XLSX exportados do Gerenciador de Anúncios do Meta, do Google Ads ou do GA4.
3. **Nada disponível**: diga exatamente o que falta e como exportar (ver "Como exportar" no fim). Não invente números.

## 2. Analisar
Para cada campanha/conjunto/anúncio, olhe:
- **Investimento**, **impressões**, **cliques**, **CTR** (cliques ÷ impressões), **CPC** (custo ÷ cliques).
- **Resultados**: compras no site, **contatos de WhatsApp**, formulários, cadastros. No atacado, contato gerado conta como resultado.
- **Custo por resultado** e, quando houver valor de venda, **ROAS** (receita ÷ investimento).

Classifique:
- 🟢 **Escalar**: custo por resultado abaixo da média e volume consistente.
- 🟡 **Observar**: poucos dados ainda (menos de ~3 dias ou poucos resultados). Não mexer cedo demais.
- 🔴 **Pausar/ajustar**: gastou bastante sem resultado, ou custo por resultado muito acima da média.

**Relatório por hora:** dados de uma hora oscilam muito. Nesse modo, só **alerte anomalias** (gasto disparou, anúncio reprovado, campanha parou de entregar, resultado zerado num horário que costuma ter). A análise de verdade é diária ou semanal. Explique isso se pedirem decisões com base em uma hora só.

## 3. Formato da resposta
Curto, para ler no celular (pode ir para o Telegram):

```
📊 Campanhas — <período>
Investido: R$ X | Resultados: N | Custo/resultado: R$ Y

🟢 Melhor: <campanha> — <por quê>
🔴 Atenção: <campanha> — <por quê>

✅ Recomendo agora:
1. ...
2. ...
```
Depois, se fizer sentido, detalhes em tabela. Explique em uma frase qualquer termo técnico usado.

## 4. Nunca
- Alterar orçamento, pausar ou criar campanha sem aprovação explícita.

## Como exportar (para a equipe)
- **Meta**: Gerenciador de Anúncios → selecionar período → Relatórios → Exportar dados da tabela (CSV). Salvar em `dados/meta/`.
- **Google Ads**: Campanhas → ícone de download → CSV. Salvar em `dados/google-ads/`.
- **GA4**: Relatórios → Aquisição → Aquisição de tráfego → Compartilhar → Fazer download (CSV). Salvar em `dados/ga4/`.
