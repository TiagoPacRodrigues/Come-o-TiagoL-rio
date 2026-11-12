---
name: analise-redes-sociais
description: Analisa o Instagram (@lv.artigosreligiosos) e a página do Facebook (lvartigosreligiosos) da Lírio do Vale usando o navegador Chrome do usuário (extensão Claude in Chrome, já logado na conta dele) e gera um PDF por rede. Use quando pedirem "analise o Instagram", "analise o Facebook", "analise as redes sociais pelo meu navegador".
---

# Análise de Instagram e Facebook pelo navegador do usuário

## Regras
- Use **somente** as ferramentas do Claude in Chrome (`mcp__claude-in-chrome__*`), no Chrome do usuário, que já está logado. **Nunca** peça, digite ou guarde senha.
- **Só leitura.** Não curta, não comente, não siga, não publique, não envie mensagem e não altere configurações.
- Vá devagar: role a página com calma e não abra dezenas de abas. Se aparecer aviso de atividade incomum, pare e avise o usuário.
- Nunca invente número. O que não estiver visível, anote como "não visível".
- Feche as abas que você abriu ao terminar.

## 1. Instagram: https://www.instagram.com/lv.artigosreligiosos/
Colete e anote:
1. **Perfil:** nome de exibição, bio completa, link da bio, categoria, botões de contato, número de publicações, seguidores e seguindo, destaques (nomes e capas). Tire um print do topo do perfil.
2. **Grade:** print dos últimos 12 posts.
3. **Últimos 30 posts** (ou 90 dias, o que vier primeiro). Para cada um: data, formato (reels, carrossel ou foto), tema, para quem fala (lojista, paróquia ou consumidor final), curtidas, comentários, visualizações (nos reels), primeira linha da legenda, se tem chamada para ação (WhatsApp, site, cadastro) e hashtags.
4. **Insights**, se a conta do usuário for administradora (Painel profissional → Insights → últimos 30 e 90 dias): contas alcançadas, contas com engajamento, seguidores (ganhos e perdidos), principais cidades, faixa etária e o top 5 de conteúdos por alcance.
5. **Stories e destaques:** frequência aparente e se os destaques respondem às dúvidas do atacado.

## 2. Facebook: https://www.facebook.com/lvartigosreligiosos
1. **Página:** nome, categoria, curtidas e seguidores, "Sobre" (telefone, endereço, horário, site), avaliações e recomendações.
2. **Últimos 20 posts:** data, formato, tema, reações, comentários e compartilhamentos. Anote também se são apenas cópias do Instagram.
3. Comentários sem resposta ou mensagens visíveis sem resposta.

## 3. Análise (ser rígido e sincero)
Para cada rede, calcule e comente:
- Frequência por semana e regularidade (há buracos?).
- Mix de formatos e o desempenho médio por formato.
- % de conteúdo para lojista versus consumidor final (meta: ≥60% lojista).
- Engajamento médio = (curtidas + comentários) ÷ seguidores. Se houver Insights, use o alcance em vez de seguidores.
- Top 5 e piores 5 posts, e **por que** performaram assim.
- Identidade visual (marrom `#7A4A1E`, dourado `#FBC32D`, Montserrat): está consistente?
- Bio, destaques e chamadas para o WhatsApp e o cadastro.
- Nota de 0 a 10 por área e um plano de ação priorizado.
- Ideias de conteúdo baseadas no que já funcionou (ver o banco de ideias em `docs/relatorios/4-instagram-facebook.md`).

## 4. Entrega
- Salve os prints em `docs/relatorios/img/` (`ig-perfil.jpg`, `ig-grade.jpg`, `fb-pagina.jpg`…).
- Escreva `docs/relatorios/5-instagram.md` e `docs/relatorios/6-facebook.md` no mesmo formato dos relatórios 1 a 4: front matter com `titulo`, `subtitulo` e `plataforma`, seções numeradas, tabelas, ✅🟡🔴 e anotações 📌.
- Gere os PDFs com `python3 scripts/gerar_pdf.py docs/relatorios/5-instagram.md docs/relatorios/6-facebook.md`. No Windows ou Mac, passe o caminho do Chrome na variável `CHROME`.
- Salve os dados coletados em `dados/redes/` (CSV), sem dados pessoais de seguidores.
- Faça commit e avise o usuário com o resumo.
