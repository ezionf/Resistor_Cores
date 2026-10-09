# Calculadora de Resistência (4 Cores)
Um programa para determinação rápida de resistência elétrica para 4 faixas.
## Descrição
O seguinte programa, desenvolvido em python, recebe as cores de faixas do resistor, determina a sua resistência automaticamente e informa para o usuário. O programa foi pensado para resistores com 4 faixas de cores, então use-o para tal resistor.
## Público-Alvo
Esse programa pode servir para estudantes de Eletrotécnica ou Engenharia Elétrica, para amantes de robôtica e eletrônica e até para profissionais da área.
## Estrutura do projeto
```text
Resistor_Cores/
│
├── images/        # Demonstração visual do programa
├── main.py        # Código principal do programa
├── LICENSE        # Termos da licença MIT do projeto
└── README.md      # Documentação do projeto
```
## Exemplo
O programa recebe 4 cores e retorna a resistência e tolerância, por exemplo. Caso o usuário entre com as cores "marrom preto laranja dourado" o programa irá retornar uma resistência de 10k com tolerância de 5%. Segue uma imagem com alguns exemplos do programa em funcionamento:  

![Exemplo de Execução do Programa](images/exemplo.png)
## Execução
### Pré-Requisitos
- Python 3 instalado  
Para obter o Python 3, basta acessar o site oficial do Python (https://www.python.org/) e buscar instalar a versão mais recente do programa.
### Utilização
Para utilizar o programa, com o Python 3 já instalado e com o arquivo "main.py" também baixado, você deve executar o arquivo utilizando o Python. Para isso, você deve abrir um terminal na pasta que o arquivo "main.py" está instalado, no terminal você irá executar o seguinte comando  
```bash
python main.py
```  
Já durante o programa, contém um loop, em que você pode ficar calculando infinitos resistores, porém para isso, será utilizado duas teclas, a tecla "S" para calcular a próxima resistência e a tecla "N" para encerrar o programa.
## Licença
O projeto está sob a licença do MIT. Para mais informações, consulte o arquivo [LICENSE](LICENSE).