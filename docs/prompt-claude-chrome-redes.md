# Prompts para o Claude da extensão do Chrome (coleta completa de Instagram e Facebook)

Cole **um prompt de cada vez** no painel do Claude, dentro do Chrome. Copie cada resposta e cole na conversa do projeto, que faz a análise e gera os PDFs.

Se a resposta parar no meio, escreva **"continue de onde parou"**.

---

## Prompt 1: Instagram completo

```
MISSÃO: você vai fazer uma VARREDURA COMPLETA do Instagram da minha empresa, a Lírio do Vale Artigos Religiosos (@lv.artigosreligiosos), uma distribuidora 100% atacado para lojas e paróquias. Eu já estou logado no Chrome.

QUERO QUE VOCÊ LEIA E VISUALIZE ABSOLUTAMENTE TUDO O QUE CONSEGUIR. Não resuma por preguiça, não pule nada, não pare no primeiro post. Abra cada coisa, clique em cada "mais", "ver mais", "ver mais comentários", "ver respostas", "ver tradução", olhe cada imagem, cada slide de carrossel, cada capa de reels, cada story dos destaques. Quanto mais completo, melhor.

REGRAS (obrigatórias):
- Somente leitura. NÃO curta, NÃO comente, NÃO siga, NÃO salve, NÃO compartilhe, NÃO publique, NÃO altere nenhuma configuração.
- NÃO abra mensagens diretas (Direct) — privacidade dos clientes.
- NÃO invente nenhum número. O que não estiver visível, escreva "não visível".
- Não copie nomes ou @ de clientes; use "cliente 1", "cliente 2".
- Vá com calma, como uma pessoa navegando. Se o Instagram mostrar aviso de atividade incomum, PARE e me avise.
- Trabalhe em lotes de 10 posts. Ao fim de cada lote, me entregue o resultado e continue para o próximo lote até acabar ou eu mandar parar.

O QUE LER E VISUALIZAR:

1. PERFIL
- Foto de perfil (descreva), nome de exibição, @, categoria, bio COMPLETA, link(s) da bio (abra e diga para onde levam), botões (WhatsApp, e-mail, ligar, loja), número de publicações, seguidores, seguindo.
- Se houver: loja do Instagram, guias, reels fixados, posts fixados.

2. DESTAQUES (abra TODOS, um por um, e veja TODOS os stories de cada um)
- Nome do destaque, capa, quantos stories, o que cada story mostra/diz, se tem link/sticker, se a informação está atualizada.

3. POSTS (o máximo que conseguir, do mais recente para o mais antigo — no mínimo os últimos 60)
Para CADA post abra o post e anote:
- Data | formato (reels / carrossel com X slides / foto)
- Tema | fala com quem (lojista, paróquia, consumidor final, devoto em geral)
- Curtidas | comentários | visualizações (reels) | outros números visíveis
- Legenda COMPLETA (clique em "mais")
- Hashtags | menções | localização
- Chamada para ação? (WhatsApp, site, cadastro, link na bio, comentar) — qual
- VISUAL: descreva a imagem/cada slide/a capa e o começo do reels: cores, fontes, texto escrito na arte, foto de produto ou ambiente, qualidade (nítida/escura/amadora/profissional), se tem logo, se segue o marrom e dourado da marca
- COMENTÁRIOS: leia TODOS (clique em ver mais comentários e ver respostas). Quantos são de clientes, o que perguntam ou elogiam, se a Lírio respondeu, quanto tempo depois e como respondeu.

4. ABA REELS e ABA MARCADOS
- Na aba Reels: liste as visualizações de todos os reels visíveis (data + views).
- Na aba Marcados: quem marca a Lírio (lojas? clientes? — sem nomes pessoais), o que mostram.

5. VISÃO GERAL DA GRADE
- Padrão visual (cores, fontes, capas), consistência, frequência de postagem (posts por semana em cada mês), períodos sem postar.

FORMATO DA RESPOSTA: Markdown, com títulos, e uma tabela por lote de posts. No final, escreva 10 observações sinceras e rígidas (o que funciona, o que não funciona, o que está fraco), baseadas no que você viu.
```

---

## Prompt 2: Instagram Insights (painel profissional)

```
Agora abra o PAINEL PROFISSIONAL / INSIGHTS do Instagram @lv.artigosreligiosos e LEIA TUDO O QUE CONSEGUIR, em todas as abas e todos os períodos disponíveis (7, 30 e 90 dias e o maior período que existir).

Somente leitura, não mude nada, não abra mensagens diretas, não invente números.

Anote tudo: contas alcançadas (seguidores x não seguidores), impressões, contas com engajamento, interações (curtidas, comentários, salvamentos, compartilhamentos), visitas ao perfil, cliques no link, cliques nos botões (WhatsApp/e-mail/ligar), total de seguidores, seguidores ganhos e perdidos por dia/semana, principais cidades, países, faixa etária, gênero, dias e horários de maior atividade.

Na lista de conteúdos: ordene por alcance e anote os 20 primeiros (data, formato, alcance, curtidas, comentários, salvamentos, compartilhamentos, visualizações, tempo médio assistido se houver). Depois os 10 piores.

Se houver dados de anúncios/impulsionamentos aqui, anote também.

Responda em Markdown com tabelas.
```

---

## Prompt 3: Facebook completo

```
MISSÃO: VARREDURA COMPLETA da página do Facebook da Lírio do Vale Artigos Religiosos (facebook.com/lvartigosreligiosos). Eu já estou logado.

LEIA E VISUALIZE ABSOLUTAMENTE TUDO O QUE CONSEGUIR: entre em TODAS as abas da página (Publicações, Sobre, Avaliações/Recomendações, Fotos, Vídeos, Reels, Eventos, Loja, Mais), clique em todos os "Ver mais", abra os comentários e as respostas, olhe cada imagem.

REGRAS: somente leitura — não curta, não comente, não compartilhe, não publique, não altere nada. NÃO abra o Messenger/mensagens. Não invente números. Não copie nomes de clientes (use "cliente 1"...). Trabalhe em lotes de 10 posts e continue até acabar.

1. CABEÇALHO E SOBRE: foto de capa e perfil (descreva), nome, categoria, curtidas, seguidores, botões, telefone, WhatsApp, e-mail, endereço, horário de funcionamento, site, todas as informações da aba Sobre (inclusive transparência da página).
2. AVALIAÇÕES/RECOMENDAÇÕES: nota, quantidade, e TODAS as avaliações que conseguir ler (texto, positiva/negativa, data, se a Lírio respondeu).
3. FOTOS, VÍDEOS e REELS: abra cada aba, quantidade aproximada, data da mais recente, descrição do estilo, visualizações dos vídeos/reels visíveis.
4. PUBLICAÇÕES (no mínimo as últimas 40): para cada uma — data | formato | tema | fala com quem | reações | comentários | compartilhamentos | visualizações (vídeo) | texto COMPLETO | descrição do visual | é igual ao Instagram? | chamada para ação.
   COMENTÁRIOS: leia todos de cada post — perguntas de clientes, elogios, reclamações, se foram respondidos e em quanto tempo.
5. Se você tiver acesso ao painel da página / Meta Business Suite (Insights), leia também: alcance, engajamento, seguidores, público (cidades, idade) e os melhores posts dos últimos 90 dias.

FORMATO: Markdown com títulos e tabelas por lote. No final, 10 observações sinceras e rígidas sobre a página.
```
