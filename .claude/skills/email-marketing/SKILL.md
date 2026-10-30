---
name: email-marketing
description: Cria e-mails marketing para a base de clientes da Lírio do Vale (lojistas e paróquias) — campanhas de datas religiosas, lançamentos, reposição, reativação de clientes parados. Entrega assunto, pré-cabeçalho, texto e HTML pronto para colar no RD Station ou outra ferramenta. Use quando pedirem "monta um e-mail", "e-mail marketing", "campanha de e-mail", "mandar para a base".
---

# E-mail marketing

## 1. Entender o pedido (pergunte só o que faltar)
- **Objetivo:** vender um tema/data, lançamento, reposição, reativar cliente parado, convidar para live/evento.
- **Público:** todos, só lojistas, só paróquias, clientes que não compram há X meses.
- **Oferta:** tem desconto, frete, condição especial ou prazo? Se não informarem, **não invente promoção**.

Se a pessoa disser só "monta um e-mail", use o `insight-mercado` (data mais próxima relevante) para propor o tema e siga.

## 2. Escolher os produtos
- Busque produtos reais no site: `https://www.lvartigosreligiosos.com.br/procura?procura=<termo>` (nome, link, foto). Use 3 a 6 produtos.
- **Nunca** coloque preço sem confirmar no site, porque o preço de atacado pode depender de login.

## 3. Escrever
Pensando no **lojista/paróquia** (comprador profissional):
- **Assunto** (até ~50 caracteres): benefício claro ou urgência da data. Gere **3 opções** para teste A/B (mandar versões diferentes para partes da base e ver qual abre mais).
- **Pré-cabeçalho:** a frase cinza que aparece ao lado do assunto. Ela complementa o assunto.
- **Corpo:** curto. Gancho da data ou tema, por que isso vende na loja dele, produtos, chamada para ação.
- **Chamada para ação (CTA):** um botão principal ("Ver produtos de Natal") e um secundário para o **WhatsApp** (5512982540028), porque muito cliente prefere fechar por lá.
- Tom acolhedor e profissional, linguagem católica respeitosa.

## 4. Entregar
1. Resumo: objetivo, público, assuntos sugeridos.
2. Texto do e-mail para revisão.
3. **HTML** responsivo e simples (tabelas, largura de 600px, estilos inline), salvo em `emails/<aaaa-mm-dd>-<tema>.html`.
4. Links com rastreamento: adicione `?utm_source=email&utm_medium=email&utm_campaign=<tema>` aos links do site. Assim o Google Analytics mostra que a visita veio desse e-mail.

## 5. Nunca
- Enviar o e-mail. O envio é feito pela equipe na ferramenta de e-mail, ou pelo agente apenas com aprovação explícita quando houver conexão.
- Usar dados de clientes no repositório.
