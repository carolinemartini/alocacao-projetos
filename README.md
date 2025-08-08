### Alocação de Avaliadores para Projetos

Este projeto é uma aplicação em Python para a alocação automática de avaliadores a projetos em um contexto de avaliação por categorias e restrições de distrito.

Descrição
  - O sistema permite distribuir a avaliação de projetos para avaliadores, respeitando as seguintes regras:
  - Cada projeto deve ser avaliado por um número fixo de avaliadores (default: 5).
  - Avaliadores possuem categorias preferenciais que podem avaliar.
  - Avaliadores não podem avaliar projetos do próprio distrito de origem.
  - Avaliadores têm um limite máximo de projetos que podem avaliar.

Como Usar?
  1. Prepare os arquivos avaliadores.csv e projetos.csv com as informações necessárias.
  2. Faça upload dos arquivos via interface web.
  3. Clique em "Rodar alocação".
  4. Baixe os arquivos gerados com as alocações.


### Exemplo de avaliadores.csv

| Avaliador | Distrito | MaxProjetos | Cat1 | Cat2 | Cat3 | Cat4 | Cat5 | Cat6 | Cat7 | Cat8 |
|-----------|----------|-------------|------|------|------|------|------|------|------|------|
| Ana       | 1234     | 10          | SIM  | NÃO  | SIM  | SIM  | NÃO  | NÃO  | SIM  | NÃO  |
| Paula     | 5678     | 20          | SIM  | SIM  | NÃO  | NÃO  | SIM  | SIM  | NÃO  | SIM  |

### Exemplo de projetos.csv

| Projeto | Distrito | Categoria |
|---------|----------|-----------|
| A       | 9999     | Cat1      |
| B       | 8888     | Cat2      |
| C       | 7777     | Cat3      |
| D       | 1234     | Cat4      |
| E       | 5678     | Cat5      |





Para dúvidas, sugestões ou contribuições, entre em contato:

Caroline Martini - carolinefmartini@gmail.com

