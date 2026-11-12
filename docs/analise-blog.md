# Análise do Blog — Lírio do Vale (12/11/2026)

**Blog:** https://www.blog.lvartigosreligiosos.com.br/
**Como foi feita:** baixei os **135 posts** e as 5 páginas do blog e testei automaticamente **todos os links e imagens** (956 endereços). Também li os textos para avaliar conteúdo, estrutura e chamadas para ação.
**Lista de correções, item por item:** [`blog-correcoes.md`](blog-correcoes.md).

---

## Resumo em 30 segundos

O blog tem **bom conteúdo e o público certo** (lojistas e paróquias), e os posts de 2026 estão bem escritos. Mas ele tem **"vazamentos"** que fazem perder leitores e contatos:

1. 🔴 **A página "Seja um Revendedor" e todos os e-books gratuitos estão com o cadeado de segurança vencido.** O visitante vê o alerta "site não seguro", e a principal forma de captar novos lojistas pelo blog está travada.
2. 🔴 **111 imagens sumiram** em 32 posts, e **53 links levam a páginas que não existem mais** (29 posts).
3. 🟠 **O blog parou duas vezes:** de nov/2024 a fev/2026 saiu só 1 post, e desde 29/09/2026 não saiu nenhum, em plena temporada de Natal e Black Friday.
4. 🟠 **Quase nenhum post chama para o WhatsApp** (só 5 de 135), sendo que é por lá que o atacado fecha venda.

---

## ✅ O que está sendo feito certo

- **Público certo.** A maioria dos posts fala com quem compra no atacado: lojista ("para sua loja", estoque, precificação, Black Friday) e paróquia (secretaria, festa do padroeiro, dízimo). É exatamente o cliente da Lírio.
- **Conteúdo útil, não só propaganda.** Ensinar o lojista a vender mais cria confiança, e o lojista que vende mais compra mais. Em marketing, isso se chama **marketing de conteúdo**.
- **Os posts levam para a loja.** 117 dos 135 posts têm links para produtos ou buscas do site. Os posts recentes usam **links de busca** (ex.: `procura?procura=aparecida`), que nunca quebram, e esse é o jeito certo.
- **Calendário religioso bem usado.** Há posts para Quaresma de São Miguel, Santo Antônio, São Bento e Carmo, Dia das Mães, Natal e Black Friday, sempre com antecedência para o lojista se preparar.
- **SEO básico ok.** SEO é o que faz aparecer no Google. Os posts têm título, descrição para o Google (só 2 sem), um título principal (H1) por página e plugin de SEO (Yoast). Os posts de 2026 usam subtítulos (H2), o que ajuda o Google e o leitor.
- **Busca interna funciona.** A página de **Materiais** (e-books, planner, kit de cartões, wallpapers) é uma ótima ideia para captar contatos, mas está quebrada (ver abaixo).

---

## 🔴 Urgente: está quebrado agora

### 1. Certificado de segurança vencido em `oferta.lvartigosreligiosos.com.br`
Esse endereço hospeda as páginas de cadastro, provavelmente feitas no RD Station:
- **"Seja um Revendedor"**, no **menu principal** de todas as páginas do blog.
- **Todos os 14 materiais gratuitos** (planner, e-book de Natal, guia de artigos religiosos, roteiro de consagração, kit de cartões, wallpapers…), linkados na página Materiais e em vários posts.

O certificado SSL, o "cadeado" do navegador, está **expirado**. O navegador mostra "Sua conexão não é particular" e a maioria das pessoas desiste ali.
➡️ **Por que é o mais urgente:** são as páginas que **transformam leitor em contato**. Em marketing, esse contato é chamado de **lead**. Sem elas, o blog atrai gente e não captura ninguém.
➡️ **O que fazer (TI):** renovar o certificado do subdomínio. Se as páginas são do RD Station, a configuração de domínio é feita no painel do RD, em Landing Pages → Domínios. Teste abrindo https://oferta.lvartigosreligiosos.com.br/revendedores no navegador.

### 2. 111 imagens que não aparecem (32 posts)
Essas imagens foram coladas a partir de um Google Docs e ficaram hospedadas no Google (`googleusercontent.com`). O Google apagou os arquivos, e hoje há **espaços vazios** no meio dos posts. Alguns exemplos: "O que vender na loja da paróquia" (12 de 12 imagens quebradas), "Calendário 2022" (8 de 8) e "Irmã Dulce" (6 de 6).
➡️ Subir as imagens no próprio WordPress. Lista completa em `blog-correcoes.md`.

### 3. 53 links quebrados (29 posts) e 6 links mal formatados
- Quase todos são **produtos que saíram do site ou mudaram de endereço**. Exemplo: o post da Irmã Dulce tem 11 links de produtos que não existem mais.
- 1 link interno do blog quebrado: o post "7 curiosidades de Nossa Senhora Aparecida" não existe mais, mas 2 posts ainda apontam para ele.
- 6 links digitados errado, por exemplo `http:// https://…` com espaço, ou o texto do link colado no lugar do endereço.
➡️ **Regra para o futuro:** linkar para **buscas ou categorias** em vez de produtos específicos. Produto sai de linha, busca não.

---

## 🟠 Importante: ajustes de estrutura e SEO

| # | Problema | Por que importa | Como resolver |
|---|---|---|---|
| 1 | **WordPress 6.4 (2023) e Yoast 15.9 (2021)** desatualizados | Risco de invasão e recursos de SEO antigos | Backup → atualizar WordPress, tema (Themify Ultra) e plugins |
| 2 | **500 de 515 imagens sem texto alternativo (alt)** | O Google "lê" imagens pelo alt; também é acessibilidade | Preencher o alt descrevendo a foto (ex.: "Terço de São Bento em madeira") |
| 3 | **Data dos posts escondida** em todos | O leitor não sabe se o post de "calendário 2022" é atual; o Google prefere conteúdo com data | Mostrar a data de **atualização** |
| 4 | **Títulos longos no Google** (117 de 135 passam de 65 caracteres) | O sufixo " - Blog Lírio do Vale Artigos Religiosos" faz o Google cortar o título | Encurtar o sufixo no Yoast para " - Lírio do Vale" |
| 5 | **Categorias bagunçadas:** "Destaques" em 85 posts, "Sem categoria" em 8 (inclusive de 2026), categorias com 1 post | Dificulta navegar e confunde o Google | Reorganizar em poucas categorias (ver sugestão abaixo) |
| 6 | **432 páginas de tag** no mapa do site, quase todas com 1 post | Páginas "vazias" diluem a força do blog no Google | Marcar tags como `noindex` no Yoast |
| 7 | **Páginas sobrando:** "Santo do Dia" (vazia), "Portfolios" (sobra do tema) | Página vazia passa imagem de abandono | Remover, ou fazer o Santo do Dia de verdade (ver ideias) |
| 8 | **Comentários abertos** sem nenhum comentário | Só atrai spam | Desativar comentários |
| 9 | **E-mail diferente** em Contato (`vendas@`) e no rodapé (`atendimento@`) | Confunde o cliente | Padronizar |
| 10 | **Caracteres invisíveis** em títulos e links (copiados do Word/Docs) | Pode quebrar links e títulos | Revisar ao colar texto (colar "sem formatação") |
| 11 | **Tag Manager do blog é outro** (`GTM-TRN5ZVF7`) diferente do da loja (`GTM-P378H55Q`); sem Pixel do Meta visível | A medição blog → loja pode estar desconectada | Conferir se o GA4 do blog é o mesmo da loja; incluir o Pixel do Meta |

---

## 🟡 Conteúdo: desatualizado, repetido e o que falta

### Posts desatualizados (revisar ou atualizar)
- **"Mensagem do Papa Francisco para a Quaresma de 2022"** e **"São José dormindo: a devoção do Papa Francisco"**. Desde maio/2025 o Papa é **Leão XIV**. Os posts podem continuar, mas precisam de uma nota de contexto, e vale um post novo sobre o Papa Leão XIV e as devoções dele.
- **"Como aproveitar o calendário 2022"**, **"Como preparar suas vendas para 2025"**, **"Dicas para viver bem a quarentena"** e **"Vender mais em tempos de quarentena"**: o título já denuncia que estão velhos. Atualizar para 2027 ou unir com posts atuais.
- **"Instagram Shopping"** (2021) e **"Reels"** (2022): as ferramentas mudaram bastante; revisar.

### Posts repetidos (o blog "concorre com ele mesmo" no Google)
Quando vários posts falam da mesma coisa, o Google não sabe qual mostrar e todos perdem força. Isso se chama **canibalização**.
- **Vender no Natal:** pelo menos 6 posts (2019, 2019, 2020, 2020, 2021, 2024).
- **Por que revender artigos religiosos / renda extra:** pelo menos 7 posts.
- **Abrir uma loja católica:** 3 posts (2021, 2024, 2026).
- **Quaresma de São Miguel:** 5 posts.
- **Comprar no atacado:** 3 posts.

➡️ Para cada tema, juntar tudo em **um guia completo e atualizado**, e redirecionar os antigos para ele com um redirecionamento 301, que manda o visitante e o Google para o endereço novo sem perder nada.

### O que está faltando
- **Paróquias e sacramentos:** só 1 post em "Sacramentos". Faltam guias de **Primeira Comunhão, Crisma, Batismo e Catequese** (lembrancinhas, terços, kits), que são compras grandes de paróquia, planejadas meses antes.
- **Devoções em alta sem post próprio:** **São Carlo Acutis**, canonizado em set/2025 e muito procurado por jovens. Ele já aparece num link de busca, mas não tem post. Também falta **Papa Leão XIV**.
- **Advento e Natal 2026:** nada publicado desde setembro.
- **Conteúdo sobre a própria Lírio:** como comprar no atacado da Lírio (pedido mínimo, frete, prazo, cadastro de CNPJ), lançamentos do mês, bastidores e a presença na ExpoCatólica (só 1 post).
- **Vídeo:** só 4 vídeos incorporados em 135 posts, sendo que o YouTube da Lírio tem Shorts.

---

## 💡 Como atrair mais leitores e mais clientes

**1. Toda página do blog precisa ter um próximo passo claro.** Hoje o fim dos posts diz "acesse o site" (41 posts). Para quem ainda não é cliente, isso é pouco. Sugestão de rodapé padrão em todo post:
> **É lojista ou compra para sua paróquia?** Fale com a nossa equipe no WhatsApp e receba o catálogo atualizado → [botão WhatsApp]
> **Ainda não compra com a gente?** Cadastre-se como revendedor → [botão]

Também vale um **botão flutuante de WhatsApp** no blog, que hoje não tem.

**2. Use os materiais gratuitos para captar leads** (depois de consertar o certificado). Em cada post, ofereça o material que combina com o tema. Exemplo: post de estoque → "Baixe a planilha de planejamento de estoque". É assim que o blog gera **lista de contatos** para o e-mail marketing.

**3. Calendário editorial com antecedência do atacado.** Publicar o post da data **2 a 3 meses antes**, quando o lojista está comprando:
- **Agora (nov):** Quaresma e Páscoa 2027 (Quarta-feira de Cinzas em 10/02/2027), Primeira Comunhão e Crisma, volta da catequese.
- **Jan–fev:** Dia das Mães e Mês de Maria; São José (19/mar).
- **Mar–abr:** festas juninas (Santo Antônio, São João, São Pedro); Corpus Christi.
- **Jun–jul:** Quaresma de São Miguel, Aparecida (12/out), Finados.
- **Ago–set:** Natal e Black Friday.

**4. Frequência constante.** Melhor **1 post por semana, sempre** do que 4 num mês e depois 1 ano parado. O agente pode gerar os rascunhos a partir do calendário.

**5. Guias de "pilar" para o Google.** São poucos guias grandes e completos, cada um com vários posts menores linkando para ele:
- "Guia completo para abrir uma loja de artigos religiosos"
- "Guia de artigos religiosos para paróquias"
- "Calendário católico de vendas 2027" (atualizado todo ano)
- "Guia de devoções e santos para lojistas"

**6. Reaproveitar cada post em vários canais.** Cada post vira um carrossel no Instagram, um Short no YouTube, um trecho do e-mail marketing e uma mensagem na lista de transmissão do WhatsApp. Um texto rende uma semana de conteúdo.

**7. "Santo do Dia" de verdade** (opcional). A página existe e está vazia. Bem feita e automatizada, atrai visitas diárias do Google ("santo do dia hoje"). Mas esse público é consumidor final, então só vale se tiver uma chamada para lojistas.

### Categorias sugeridas (reorganização)
| Nova categoria | Junta |
|---|---|
| **Para sua Loja** (vendas, gestão, marketing) | Para sua Loja, Destaques |
| **Para sua Paróquia** | Igreja, Pastoral, Sacramentos |
| **Datas e Calendário** | posts de datas (Natal, Páscoa, Mães…) |
| **Santos e Devoções** | Santos, Devoção Mariana, Liturgia |
| **Produtos** | Produtos Religiosos, Acessórios |

---

## Plano de ação

| Quando | O quê | Quem |
|---|---|---|
| **Esta semana** | Renovar o certificado do `oferta.` (revendedores e e-books) | TI |
| **Esta semana** | Backup e atualização do WordPress, do tema e dos plugins | TI |
| **Esta semana** | Retomar as publicações: post de Advento/Natal e post de Quaresma/Páscoa 2027 | Marketing (rascunho pelo agente) |
| **Próximas 2 semanas** | Corrigir links quebrados e mal formatados (`blog-correcoes.md`) | Marketing/TI |
| **Próximas 2 semanas** | Rodapé padrão com WhatsApp e revendedor em todos os posts, e botão flutuante | TI |
| **Próximo mês** | Repor imagens quebradas com alt; encurtar o sufixo dos títulos; noindex nas tags; desativar comentários; remover páginas vazias | TI/Marketing |
| **Próximo mês** | Reorganizar categorias; atualizar posts datados (2022, 2025, quarentena, Papa) | Marketing |
| **Próximos 3 meses** | Unir posts repetidos em guias completos com redirecionamento 301; criar posts de Primeira Comunhão, Crisma, Carlo Acutis e Leão XIV | Marketing (agente ajuda) |
| **Contínuo** | 1 post por semana pelo calendário do atacado; cada post reaproveitado em Instagram, e-mail e WhatsApp | Agente + equipe |

## O que não deu para verificar
- **Posição no Google, visitas e cliques:** precisa de acesso ao **Google Search Console** e ao **GA4**.
- **Links para YouTube, Instagram, Facebook, TikTok e alguns sites externos:** esses sites bloqueiam verificação automática. Vale testar manualmente.
- Se o Pixel do Meta está dentro do Tag Manager: precisa de acesso ao GTM.
