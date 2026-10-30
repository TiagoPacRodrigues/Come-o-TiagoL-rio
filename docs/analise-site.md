# Análise do site e do blog (30/10/2026)

Análise feita "de fora", acessando o site como um visitante. Sem acesso a painéis.

## Loja — https://www.lvartigosreligiosos.com.br/
- **Plataforma:** Climba / IDCommerce (plataforma brasileira de e-commerce B2B).
- **Posicionamento no Google (título e descrição):** "Distribuidora de Artigos Religiosos — Vendas no Atacado", voltado a "lojistas, revendedores, igrejas, comunidades". Está coerente com o foco em atacado.
- **Busca de produtos:** funcionando bem nos testes. Aceita palavra sem acento ("terco", "sao bento") e até erro de digitação ("cruxifixo" achou crucifixos). Quando não acha nada, mostra "Nenhum registro encontrado".
- **Sitemap** (lista de páginas para o Google): existe e está declarado no robots.txt.
- **Canais ligados ao site:** WhatsApp, Instagram (@lv.artigosreligiosos), Facebook, YouTube, LinkedIn e cadastro de newsletter.

### Ferramentas de rastreamento instaladas
| Ferramenta | Para que serve | Encontrado |
|---|---|---|
| Google Tag Manager | "Caixa" que gerencia os outros códigos de rastreamento | GTM-P378H55Q |
| Google Analytics 4 | Mede visitas e comportamento no site | 2 IDs (G-Q17NWCFEC2 e G-JF5RCD21V4) |
| Google Ads | Mede resultado dos anúncios do Google | AW-647507859 |
| RD Station | Automação de marketing e e-mail | Script instalado |
| Pixel do Meta | Mede resultado dos anúncios do Instagram e do Facebook | **Não visto direto no código.** Pode estar dentro do Tag Manager; precisa confirmar |

## Blog — https://www.blog.lvartigosreligiosos.com.br/
- **Plataforma:** WordPress 6.4, versão do fim de 2023 e **desatualizada**, com o plugin de SEO Yoast.
- **Volume:** 135 artigos. Publica de 2 a 4 por mês, e o último é de 29/09/2026.
- **Temas:** bons e certos para o atacado: como revender, datas da Igreja, estoque, Black Friday, loja de paróquia, devoções.
- **Busca interna do blog:** funcionando ("terco" retornou artigos sobre terço).
- **SEO básico do artigo:** título, descrição e H1 corretos, além de dados estruturados.

## Achados principais
1. **As buscas internas funcionam.** Então "consertar as ferramentas de busca" provavelmente é sobre **aparecer no Google (SEO)**, ou é algo que só aparece no painel. Precisa confirmar com o patrão.
2. **O blog não leva para a loja.** O artigo mais recente analisado tem **zero links para produtos**. O leitor aprende, mas não tem um caminho fácil para comprar. É uma correção simples e de alto impacto.
3. **Dois Google Analytics diferentes.** Pode estar duplicando dados ou separando a medição em dois lugares. Precisa ver qual é o oficial.
4. **RD Station já está instalado.** Provavelmente já é a ferramenta de e-mail marketing, ou foi um dia. Precisa confirmar se ainda usam.
5. **Pixel do Meta não confirmado.** Sem ele, o Meta não sabe quem visitou o site, e o remarketing e a otimização dos anúncios ficam cegos.
6. **WordPress desatualizado:** risco de segurança e de lentidão. É uma tarefa de TI.

## Próximos passos sugeridos
- [ ] Confirmar com o patrão o que é "consertar as ferramentas de busca"
- [ ] Acesso de leitura ao Google Analytics, ao Google Ads, ao Gerenciador de Anúncios do Meta e ao RD Station
- [ ] Ver no Tag Manager se o Pixel do Meta está lá
- [ ] Atualizar o WordPress e os plugins do blog (fazer backup antes)
- [ ] Padronizar: todo artigo do blog termina com links para os produtos citados
