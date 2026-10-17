# Plano de Automação de Marketing

## 1. O que saiu da reunião (anotação original)

```
MKT:
Anúncios Meta, google
Conteúdos
Blog

Criação dos anúncios
Geração de conteúdo
Inteligência de análise, acompanhamento e otimização

Segundo cérebro de marketing
Blog - consertar as ferramentas busca
Geração de calendário
Email marketing
```

## Visão (o que o patrão quer no final)

Com poucos comandos, ou só montando o calendário, todo o resto se organiza e anda sozinho:

```
Dados (vendas, anúncios, site)
        │
        ▼
  ANÁLISE: o que está dando certo e errado
        │
        ▼
  CALENDÁRIO: o que fazer, quando, em qual canal
        │
        ▼
  GERAÇÃO automática: posts, anúncios, blog, e-mails
        │
        ▼
  Revisão humana rápida → publicação → volta para os dados
```

**Prioridade dele:** primeiro a **análise** (o que está funcionando ou não), depois a **geração**.

## 2. Como os pontos se encaixam

Os itens da reunião se dividem em três camadas. A camada de baixo sustenta as de cima.

```
┌─────────────────────────────────────────────────────────────┐
│ 3. INTELIGÊNCIA — análise, acompanhamento e otimização       │
│    (mede o que funcionou e diz o que ajustar)                │
├─────────────────────────────────────────────────────────────┤
│ 2. PRODUÇÃO — o que é criado e publicado                     │
│    • Anúncios (Meta e Google)   • Conteúdo para redes        │
│    • Blog                       • E-mail marketing           │
│    • Calendário (organiza tudo isso no tempo)                │
├─────────────────────────────────────────────────────────────┤
│ 1. BASE — Segundo cérebro de marketing                       │
│    (tudo que a empresa sabe sobre si, seus produtos e        │
│     seus clientes, num lugar só)                             │
└─────────────────────────────────────────────────────────────┘
```

## 3. Cada frente, explicada

### 3.1 Segundo cérebro de marketing — BASE
**O que é:** uma central de conhecimento da marca: quem é a Lírio do Vale, como ela fala (tom de voz), produtos, público, datas importantes, o que já deu certo e o que não deu.

**Por que vem primeiro:** toda automação que gera texto (anúncio, post, blog, e-mail) precisa desse contexto. Sem ele, o conteúdo sai genérico, parece de qualquer loja. Com ele, sai com a cara da Lírio do Vale.

**Ideia de entrega:** documentos organizados aqui no repositório (ou no Google Drive), que todas as outras automações consultam.

### 3.2 Geração de calendário
**O que é:** o planejamento do que vai ser publicado, quando e onde.

**Por que importa no segmento religioso:** o calendário litúrgico e as datas de devoção movem as vendas (Páscoa, Quaresma, Natal, dias de santos, Nossa Senhora Aparecida, Primeira Comunhão, Crisma, batizados). Um calendário bem feito antecipa essas datas, já que a campanha precisa começar semanas antes.

### 3.3 Geração de conteúdo
**O que é:** posts, legendas, roteiros de vídeos e stories para as redes sociais.

**Automação possível:** a partir do calendário e do segundo cérebro, gerar rascunhos prontos para revisão.

### 3.4 Blog + consertar a busca
**O que é:** artigos no site que atraem pessoas pesquisando no Google (ex.: "o que dar de presente de Primeira Comunhão").

**"Consertar as ferramentas de busca"** — *precisa confirmar o que significa* (ver perguntas abaixo).

### 3.5 E-mail marketing
**O que é:** e-mails para quem já é cliente ou se cadastrou: novidades, promoções, datas especiais, carrinho abandonado.

**Por que vale a pena:** é o canal mais barato, porque a lista de contatos é da empresa, não depende de algoritmo nem de pagar por clique.

### 3.6 Anúncios (Meta e Google) — criação
**O que é:** anúncios pagos.
- **Meta** (Instagram e Facebook): aparece para quem *não estava procurando*, mas tem o perfil certo. Bom para mostrar produtos e criar desejo.
- **Google**: aparece para quem *já está procurando* (ex.: "terço de cristal"). Bom para capturar quem já quer comprar.

**Automação possível:** gerar variações de textos e títulos, sugerir públicos e briefings de imagens.

### 3.7 Inteligência de análise, acompanhamento e otimização — TOPO
**O que é:** acompanhar os números (quanto gastou, quanto vendeu, o que funcionou) e transformar isso em decisões.

**Por que fica por último:** precisa de dados acumulados e de acesso às contas (Meta, Google, site, loja). Mas vale começar a *registrar* os números desde já.

## 4. Ordem sugerida

Ajustada à prioridade do patrão (análise primeiro):

| # | Frente | Por quê nessa ordem |
|---|---|---|
| 1 | Análise inicial + segundo cérebro (em paralelo) | A análise diz o que funciona; o segundo cérebro guarda essas descobertas e o jeito da marca |
| 2 | Calendário | Vira o "painel de comando" que dispara o resto |
| 3 | Geração de conteúdo e anúncios | Alimentada pela análise e pelo calendário |
| 4 | Blog + busca | Depende de entender o problema da busca |
| 5 | E-mail marketing | Depende de saber qual ferramenta e lista existem |
| 6 | Análise contínua e automática | Fecha o ciclo: mede o que foi gerado e ajusta o próximo calendário |

**Como começar a análise sem integração nenhuma:** exportar relatórios (planilhas) do Meta Ads, Google Ads, da loja e do Instagram. Analisamos isso primeiro; as conexões automáticas vêm depois.

## 5. Perguntas em aberto

**Gerais**
- [ ] O que a Lírio do Vale vende e por onde (loja física, site, marketplace, WhatsApp)?
- [ ] Qual o site/loja virtual? Em que plataforma ele roda (Shopify, Nuvemshop, Tray, WordPress…)?
- [ ] Quem aprova o que for publicado?

**Segundo cérebro**
- [ ] Já existe algum material da marca (logo, cores, tom de voz, apresentação da empresa)?
- [ ] Onde preferem guardar: Google Drive, Notion, aqui no repositório?

**Blog / busca**
- [ ] "Consertar as ferramentas de busca" é: (a) a **busca interna** do site/blog que não acha os produtos, (b) o blog **não aparecer no Google** (SEO), ou (c) outra coisa?
- [ ] Em que plataforma está o blog? Tem quantos artigos?

**E-mail marketing**
- [ ] Já usam alguma ferramenta (Mailchimp, RD Station, Klaviyo, a da própria loja)?
- [ ] Têm uma lista de e-mails de clientes? Mais ou menos de que tamanho?

**Anúncios**
- [ ] Já anunciam hoje? Quanto investem por mês, mais ou menos?
- [ ] Quem cuida hoje (vocês, agência, freelancer)?

**Conteúdo / redes**
- [ ] Quais redes usam e com que frequência postam?
