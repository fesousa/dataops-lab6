# DataOps - Laboratório 6

Processmento e Análise de Dados em AWS GLue

As instruções do laboratório estão em português. Para alterar o idioma, procure a opção na barra inferior do console AWS.


## Objetivos

* Utilizar AWS Glue Crawler para encontrar dados no S3
* Armazenar dados encontrados pelo Crawler no AWS Glue Data Catalog
* Executar um processo de ETL no AWS Glue para extrair do Data Catalog, fazer transformações, e incluir no Redshift




## Arquitetura da solução

<img src="images/Imagem1.png" width='100%'/>


## Configurar um VPC Endpoint para conectar com S3

Para o Crawler do AWS Glue poder ler os dados do S3 é preciso criar um VPC Endpoint, que estabelece uma conexão privada entre a VPC e os serviços da AWS, em passar pela inter-net. Assim, o Glue consegue acessar os dados do S3 de forma privada e segura.

1. Procure na barra superior pelo serviço `VPC` e clique no serviço para abrir

2.	No menu ao lado esquerdo procure e clique em <img src="images/Imagem2.png" height='25'/>

3.	Depois clique em <img src="images/Imagem3.png" height='25'/>

4. No campo `Etiqueta de nome` coloque `s3-glue-endpoint`

5. Na barra de pesquisa da seção `Serviços`  escreva `s3` e aperte `Enter`

6. No resultado selecione a opção que tem seguintes características:
    
    Nome do serviço: `com.amazonaws.us-east-1.s3`    

    Tipo: `Gateway`


    <img src="images/Imagem7.png" width='100%'/>

7. Na seção `VPC` selecione a única opção disponível (`padrão`)


<img src="images/Imagem98.png" width='100%'/>


8.	Em  `Tabelas de rotas`  selecione o checkbox da única linha disponível

<img src="images/Imagem9.png" width='100%'/>

9.	Clique em <img src="images/Imagem10.png" height='25'/>

10.	Confirme o endpoint criado

<img src="images/Imagem12.png" width='100%'/>


## Criar Crawler no AWS Glue

1.	Procure na barra superior pelo serviço `Glue` e clique no serviço para abrir

2.	No menu lateral esquerdo, procure e clique em  <img src="images/Imagem13.png" height='25'/>

3.	Clique em <img src="images/Imagem14.png" height='25'/> e comece a configuração do novo Crawler

    3.1. `Name`: `crawler-vacinas`

    3.2. Clique em <img src="images/Imagem15.png" height='25'/>

    3.3.  Na tela seguinte, clique em <img src="images/Imagem99.png" height='25'/>. No popup, configure a nova conexão:

    3.4. No popup, selecione o bucket e pasta `dataops-impacta-dados-nomesobrenome/input` (bucket criado no [Laboratório 1](https://github.com/fesousa/dataops-lab1)), clicando em <img src="images/Imagem100.png" height='25'/>. Ao escolher o bucket e a pasta, clique em <img src="images/Imagem102.png" height='25'/>


    <img src="images/Imagem101.png" width='100%'/>

    3.5. Ao voltar para a tela anterior, clique em  <img src="images/Imagem103.png" height='25'/>

    3.6. Clique em <img src="images/Imagem15.png" height='25'/> 

    3.7. Em `IAM Role` selecione `Lab Role`

    3.8. Clique em <img src="images/Imagem15.png" height='25'/> 


    3.9. Na tela `Set output and scheduling`, clique em <img src="images/Imagem31.png" height='25'/>. Uma nova aba será aberta.
    
    3.10 Na nova aba coloque no campo `Name` o nome `vacinas_database` e clique em  <img src="images/Imagem32.png" height='25'/> 

    3.11. Volte para a aba onde está criando o crawler e clique em <img src="images/Imagem104.png" height='25'/> para atualizar as opções de `Target database`

    3.12. Em `Target database` selecione o database que acabou de criar (`vacinas_database`)
    
    3.13. No campo `Table name prefix`  escreva `vacinas_`

    3.14. Clique em <img src="images/Imagem34.png" height='25'/> 

    3.15. Revise as configurações e clique em <img src="images/Imagem35.png" height='25'/> 

    3.16. Verifique o Crawler criado na nova tela

    <img src="images/Imagem36.png" width='100%'/>



    3.17. Ainda nessa tela, execute o crawler clicando em  <img src="images/Imagem38.png" height='25'/>. A execuceção começará e poderá ser acompanhada no final da página, na seção `Crawler runs`

    <img src="images/Imagem105.png" width='100%'/>
   
    3.18. Aguarde até que o Status fique `Completed` 

     <img src="images/Imagem105.png" width='100%'/>

    3.19 Verifique a nova tabela criada clicando em `Tables` (`Data Catalog --> Database --> Tables`)

    <img src="images/Imagem41.png" width='100%'/>


## Consultar dados do Data Catalog com Amazon Athena

1.	O Amazon Athena precisa de um bucket para armazenar os resultados de consulta. Procure pelo serviço S3 e crie um novo bucket chamado `dataops-impacta-athena-nomesobrenome`. Troque `nomesobrenome` pelo seu nome e sobrenome

2.	Volte ao AWS Glue e selecione `Tables` no menu lateral esquerdo 

3.	Na tela das tabelas, abra a tabela `vacinas_input`

<img src="images/Imagem43.png" width='100%'/>
 
4.	Clique em <img src="images/Imagem44.png" height='25'/> e depois em  <img src="images/Imagem45.png" height='25'/>

<img src="images/Imagem43.png" width='100%'/>

5.	No popup, clique em <img src="images/Imagem46.png" height='25'/> para ser redirecionado para o Amazon Athena

6.	Já no Amazon Athena, clique em `Settings`  nas abas superiores

7.	Na seção `Query result and encryption settings`  clique em <img src="images/Imagem49.png" height='25'/>

8.	Clique em <img src="images/Imagem50.png" height='25'/> para selecionar o bucket S3 dos resultado

9.	Selecione o bucket `dataops-impacta-athena-nomesobrenome` (bucket que acabou de criar) e clique em <img src="images/Imagem51.png" height='25'/>

<img src="images/Imagem108.png" width='100%'/>


10.	Clique em <img src="images/Imagem52.png" height='25'/>

11.	De volta do Athena clique em `Editor`

12. Na seção `Data` ao lado esquerdo, verifique se em `Database` o baco de dados `vacinas_database` está selecionado

<img src="images/Imagem54.png" width='100%'/>
 
13.	Ao lado direito, no editor de consultas, verifique se já existe a seguinte consulta, para re-tornar os 10 primeiros registros:

```sql
SELECT * FROM "vacinas-database"."vacinas_input" limit 10;
```

Se não houver, coloque essa consulta no editor e clique em <img src="images/Imagem55.png" height='25'/>. Você deverá ver um resultado parecido com o seguinte:

<img src="images/Imagem56.png" width='100%'/>

14.	Execute uma nova consulta para retornar a quantidade de registros e veja o resultado

```sql
SELECT count(1) FROM "vacinas-database"."vacinas_input";
```

## Inserir mais dados do Data Catalog

1.	Na AWS, procure e abra o serviço `Lambda`

2.	Selecione a função lambda `dataops-coleta-vacinas-ci-cd` criada no [Laboratório 4](https://github.com/fesousa/dataops-lab4)

3.	Teste a função com o seguinte json

 OBS: O Link abaixo é dinâmico. Pegue outro link de arquivo de vacinação aqui: https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao/resource/5093679f-12c3-4d6b-b7bd-07694de54173

```json
{
    "url":"https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SIPNI/COVID/uf/uf%3DAP/part-00000-0e081da1-2126-45b3-8bfd-78667a8589af.c000.csv", 
    "uf":"ap"
}
```


A execução vai coletar dados de vacinação do Amapá e salvar no S3. Se precisar, veja no [Laboratório 4](https://github.com/fesousa/dataops-lab4) como testar a função lambda

4.	Volte para o Amazon Athena e execute a consulta para contar a quantidade de registros novamente e verifique o resultado. Os dados do Amapá foram inseridos.

5.	Ainda no Athena, execute uma consulta para contar quantos registros existem de cada Estado (campo `estabelecimento_uf`)



## Executar ETL com Glue Job (Trabalho)

1.	Na AWS, procure e abra o serviço `Glue`

2.	No menu da lateral esquerda, selecione `ETL Jobs`

3.	Selecione a opção `Spark script editor` e clique em  <img src="images/Imagem58.png" height='25'/>

4. Na nova tela, coloque o script `pyspark abaixo`

```python
${etl_vacinas.sql}
```

    4.1. No código verifique se está de acordo com o que está no seu ambiente:

        * Linha 41: database = "vacinas_database", table_name = "vacinas_input". Deve estar de acordo com o que está em seu data catalog

5. Na parte superior onde está escrito `Unitled Job`, edite o nome do job para `etl_vacinas`

<img src="images/Imagem109.png" width='100%'/>

6. Clique na aba `Job details` e configure:

    6.1. `IAM Role`: selecione `LabRole`]

    6.2. Na seção `Connections` (deve expandir `Advanced properties`) clique no link `AWS Glue` para abrir uma nova aba e adicionar a conexão do Redshift

    <img src="images/Imagem110.png" width='100%'/>

    6.3. Na nova aba, na seção `Connections` clique em `Create connection`

    <img src="images/Imagem111.png" width='100%'/>

    6.4. Em `Name` coloque `redshift-connection` (preste atenção neste nome. É o que está configurado no script do Job [linha 65]. Se for diferente, a execução vai falhar)

    6.5. Em `Connection type` escolha `Amazon Redshift`

    6.6. Em `Connection access` configure o cluster redshift criado no labortório 5. Você só precisa escolher `Database instances` e `Password`, os outros campos ficam iguais. Se não lembra a senha, altere no redshift.

    6.7. Clique em `Create connection`

    6.8. Volte a aba onde está configurando o job e selecione a conexão criada. Se não aparecer, clique no botão de atualizar ao lado do campo de opções

    <img src="images/Imagem112.png" width='100%'/>


7.	Clique em <img src="images/Imagem71.png" height='25'/> na parte superior

8.	Clique em <img src="images/Imagem113.png" height='25'/> na parte superior

9.	Acompanhe a execução do script clicando na aba `Runs`:    
    
    9.1. Espere até que a execução fique com o status `Succeeded`. A execução demora cerca de 4 minutos. Clique em <img src="images/Imagem75.png" height='25'/> de tempos em tempos para ver a atualização


    <img src="images/Imagem76.png" width='100%'/>

    9.2. Lembre-se de iniciar o cluster redshift antes de excutar o processo


10. Abra o redshift e verifique a tabela `vacinas_dw` criada pelo editor de consultas

11.	Utilize o editor de consultas para consultar os registros da tabela utilizando SQL

    9.1. Quantidade de registros na tabela

```sql
select count(1) from vacinas_dw;
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9.2. Quantidade de vacinas por UF

```sql
select sum(quantidade), uf from vacinas_dw group by uf;
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9.3. Registros de vacinação com mais de 1000 vacinas

```sql
select * from vacinas_dw where quantidade > 1000
```


12. Lembre-se de pausar o cluster Redshift quando terminar o laboratório.

<div class="footer">
    &copy; 2022 Fernando Sousa
    <br/>
    {{update}}
</div>