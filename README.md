# Aplicativo de busca de filmes

Este é um aplicativo Python que permite aos usuários pesquisar por filmes usando a API do IMDB. Com ele, os usuários poderão buscar filmes por título, ator ou diretor e obter informações detalhadas sobre o filme, como sinopse, elenco e avaliação do usuário.

## Como utilizar

Para utilizar o aplicativo, você precisará ter o Python instalado na sua máquina. Além disso, será necessário criar uma conta na API do IMDB para obter uma chave de acesso.

1. Faça o download do código fonte do aplicativo.
2. Execute o arquivo `requirements.txt` para instalar as dependências necessárias.
3. Adicione a chave de acesso da API do IMDB no arquivo `config.py`.
4. Execute o arquivo `main.py`.
5. Insira os termos de busca na linha de comando e pressione Enter.
6. O aplicativo exibirá uma lista de filmes correspondentes à busca. Selecione o filme desejado para obter informações detalhadas sobre ele.

## Estrutura do projeto

O projeto está estruturado da seguinte forma:
```
├── config.py
├── main.py
├── movie.py
├── requirements.txt
└── README.md
```

* O arquivo `config.py` contém a chave de acesso à API do IMDB.
* O arquivo `main.py` é o arquivo principal do aplicativo, que inicia a busca e exibe os resultados.
* O arquivo `movie.py` contém a classe `Movie`, que representa um filme e suas informações.
* O arquivo `requirements.txt` contém as dependências necessárias para executar o aplicativo.
* O arquivo `README.md` é este arquivo de documentação do projeto.

## Dependências

O aplicativo depende das seguintes bibliotecas Python:

* requests
* tabulate

Você pode instalá-las executando o seguinte comando:
```
pip install -r requirements.txt
```
## Licença

Este projeto está licenciado sob a licença MIT. Para mais informações, consulte o arquivo LICENSE.
