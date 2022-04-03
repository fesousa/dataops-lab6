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

4.	No campo <img src="images/Imagem4.png" height='25'/> escreva `s3` e aperte `Enter`

5.	No resultado selecione a opção que tem seguintes características:
    
    Service Name:  <img src="images/Imagem5.png" height='25'/>    

    Type:  <img src="images/Imagem6.png" height='25'/>


    <img src="images/Imagem7.png" width='100%'/>


6.	Em  <img src="images/Imagem8.png" height='25'/>  selecione o checkbox da `Route Table` disponível

<img src="images/Imagem9.png" width='100%'/>

7.	Clique em <img src="images/Imagem10.png" height='25'/>

8.	Na nova tela, clique em <img src="images/Imagem11.png" height='25'/>

9.	Confirme o endpoint criado

<img src="images/Imagem12.png" width='100%'/>


## Criar Crawler no AWS Glue

1.	Procure na barra superior pelo serviço `Glue` e clique no serviço para abrir

2.	No menu lateral esquerdo, procure e clique em  <img src="images/Imagem13.png" height='25'/>

3.	Clique em <img src="images/Imagem14.png" height='25'/> e comece a configuração do novo Crawler

    3.1. Nome do Crawler: `crawler-vacinas`

    3.2. Clique em <img src="images/Imagem15.png" height='25'/>

    3.3. Na tela seguinte, clique em <img src="images/Imagem16.png" height='25'/> novamente 

    3.4. Na tela seguinte, configure o datastore

    3.5. No campo <img src="images/Imagem17.png" height='25'/>  selecione <img src="images/Imagem18.png" height='25'/>

    3.6. Clique em <img src="images/Imagem19.png" height='25'/>. No popup, configure a nova conexão:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Nome: `s3-connection`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. VPC: selecione a única opção disponível

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Subrede: selecione a primeira

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d. Grupo de segurança: selecione `default`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e. Clique em <img src="images/Imagem20.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.7. Em conexão, selecione a conexão recém criada (`s3-connection`)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.8. h.	Em `Incluir caminho`, clique em <img src="images/Imagem21.png" height='25'/>  para selecionar o bucket

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.9. No popup, selecione o bucket e pasta `dataops-impacta-dados-nomesobrenome/input` (bucket criado no [Laboratório 1](https://github.com/fesousa/dataops-lab1))


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/Imagem22.png" width='100%'/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.7. Clique em <img src="images/Imagem23.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.8. Clique em <img src="images/Imagem24.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.9. Na tela seguinte, clique novamente em <img src="images/Imagem25.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.10. Na próxima tela, selecione <img src="images/Imagem26.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.11. Em `Função do IAM` selecione <img src="images/Imagem27.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.12. Clique em <img src="images/Imagem28.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.13. Na próxima tela, verifique se a Frequência está como <img src="images/Imagem29.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.14. Clique em <img src="images/Imagem30.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.15. Na tela de configuração de saída, clique em <img src="images/Imagem31.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. No popup coloque no campo `Nome do banco de dados` o nome `vacinas_database`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Clique em <img src="images/Imagem32.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.16. De volta a tela de configuração de saída, no campo <img src="images/Imagem33.png" height='25'/>  escreva `vacinas_`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.17. Clique em <img src="images/Imagem34.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.18. Revise as configurações e clique em <img src="images/Imagem35.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.19. Verifique o Crawler criado na nova tela

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/Imagem36.png" width='100%'/>

4. Execute o Crawler

    4.1. Selecione o checkbox ao no registro do Crawler criado

    <img src="images/Imagem37.png" width='100%'/>
 
    4.2. Clique em <img src="images/Imagem38.png" height='25'/> 

    4.3. Clique no botão de atualizar (<img src="images/Imagem39.png" height='25'/>) para atualizar o status (canto superior direito)

    4.4. Aguarde até que o Status fique `Ready` novamente. Clique no atualizar de tempos em tempos para atualizar o status e verificar

    4.5. Verifique a nova tabela criada clicando em <img src="images/Imagem40.png" height='25'/> no menu lateral esquerdo

    <img src="images/Imagem41.png" width='100%'/>


## Consultar dados do Data Catalog com Amazon Athena

1.	O Amazon Athena precisa de um bucket para armazenar os resultados de consulta. Procure pelo serviço S3 e crie um novo bucket chamado `dataops-impacta-athena-nomesobrenome`. Troque `nomesobrenome` pelo seu nome e sobrenome

2.	Volte ao AWS Glue e selecione <img src="images/Imagem42.png" height='25'/> no menu lateral esquerdo 

3.	Na tela das tabelas, selecione o checkbox da tabela criada

<img src="images/Imagem43.png" width='100%'/>
 
4.	Clique em <img src="images/Imagem44.png" height='25'/> e depois em  <img src="images/Imagem45.png" height='25'/>

5.	No popup, clique em <img src="images/Imagem46.png" height='25'/> para ser redirecionado para o Amazon Athena

6.	Já no Amazon Athena, clique em <img src="images/Imagem47.png" height='25'/>  no canto superior direito

7.	Em <img src="images/Imagem48.png" height='25'/>  clique em <img src="images/Imagem49.png" height='25'/>

8.	No novo popup, selecione o bucket criado clicando em <img src="images/Imagem50.png" height='25'/>

9.	Clique em <img src="images/Imagem51.png" height='25'/>

10.	Clique em <img src="images/Imagem52.png" height='25'/>

11.	De volta ao editor de query do Athena (Query Editor), confira se a seção <img src="images/Imagem53.png" height='25'/> ao lado esquerdo está com o `Database`  `vacinas-database` selecionado

<img src="images/Imagem54.png" width='100%'/>
 
12.	Ao lado direito, no editor de consultas, verifique se já existe a seguinte consulta, para re-tornar os 10 primeiros registros:

```sql
SELECT * FROM "vacinas-database"."vacinas_input" limit 10;
```

Se não houver, coloque essa consulta no editor e clique em <img src="images/Imagem55.png" height='25'/>. Você deverá ver um resultado parecido com o seguinte:

<img src="images/Imagem56.png" width='100%'/>

13.	Execute uma nova consulta para retornar a quantidade de registros e veja o resultado

```sql
SELECT count(1) FROM "vacinas-database"."vacinas_input";
```

## Inserir mais dados do Data Catalog

1.	Na AWS, procure e abra o serviço `Lambda`

2.	Selecione a função lambda `dataops-coleta-vacinas-ci-cd` criada no [Laboratório 4](https://github.com/fesousa/dataops-lab4)

3.	Teste a função com o seguinte json

```json
{
    "url":"https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SIPNI/COVID/uf/uf%3DAP/part-00000-e024f7cd-7ba2-4b64-a285-ad08d98b1135.c000.csv", 
    "uf":"ap"
}
```


A execução vai coletar dados de vacinação do Amapá e salvar no S3. Se precisar, veja no [Laboratório 4](https://github.com/fesousa/dataops-lab4) como testar a função lambda

4.	Volte para o Amazon Athena e execute a consulta para contar a quantidade de registros novamente e verifique o resultado. Os dados do Amapá foram inseridos.

5.	Ainda no Athena, execute uma consulta para contar quantos registros existem de cada Estado (campo `estabelecimento_uf`)



## Executar ETL com Glue Job (Trabalho)

1.	Na AWS, procure e abra o serviço `Glue`

2.	No menu da lateral esquerda, selecione <img src="images/Imagem57.png" height='25'/>

3.	Clique em  <img src="images/Imagem58.png" height='25'/>

4.	Na tela <img src="images/Imagem59.png" height='25'/> , configure:

    4.1. Nome: `etl-vacinas`
    
    4.2. Função do IAM: `LabRole`

    4.3. Este trabalho executa: selecione a opção `Um script proposto gerado pelo AWS Glue`

    4.4. Clique em  <img src="images/Imagem60.png" height='25'/>

    4.5. Na tela <img src="images/Imagem61.png" height='25'/> selecione a opção do Data Catalog criado anteriormente (`vacinas-database`)

    <img src="images/Imagem62.png" width='100%'/>
 
    4.6.	Clique em <img src="images/Imagem63.png" height='25'/>

    4.7. Na tela seguinte, clique novamente em <img src="images/Imagem64.png" height='25'/>

    4.8. Na tela <img src="images/Imagem65.png" height='25'/> selecione a opção <img src="images/Imagem66.png" height='25'/>

    4.9. Clique em  <img src="images/Imagem67.png" height='25'/>

    4.10. No popup de configuração da conexão coloque:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Nome: `redshift-connection´

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Tipo de conexão: `Amazon Redshift`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Cluster: selecione o cluster criado no [Laboratório 5](https://github.com/fesousa/dataops-lab5)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d. Nome do banco de dados: `dev`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e. Nome de usuário: `awsuser`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f. Senha: coloque a senha criada para o Redshift do [Laboratório 5](https://github.com/fesousa/dataops-lab5)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g. Clique em <img src="images/Imagem68.png" height='25'/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.11. Retornando a tela de destino dos dados, complete o campo `Nome do banco de dados` com `dev`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.12. Clique em <img src="images/Imagem69.png" height='25'/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.13. Na tela seguinte, clique em <img src="images/Imagem70.png" height='25'/>

5.	A tela para editar o script será aberta
6.	Coloque o script `pyspark abaixo`

https://github.com/fesousa/dataops-lab6/blob/2738353683fb94c7f69c79c46396e445f77937d2/etl_vacinas.py#L1-L56

7.	Depois de atualizado o script, clique em <img src="images/Imagem71.png" height='25'/> na parte superior

8.	Execute o processo de ELT clicando em  <img src="images/Imagem72.png" height='25'/>

9.	Acompanhe a execução do script:
    
    9.1. Feche o editor de script clicando em <img src="images/Imagem73.png" height='25'/> no canto superior direito

    9.2. Confira se está na tela dos trabalhos do Glue, clicando em <img src="images/Imagem74.png" height='25'/> no menu lateral esquerdo

    9.3. Selecione o trabalho `etl-vacinas` criado neste laboratório

    9.4. Veja as execuções na parte inferior

    9.5. Espere até que a execução fique com o status `Succeeded`. A execução demora cerca de 4 minutos. Clique em <img src="images/Imagem75.png" height='25'/> do painel inferior de tempos em tempos para ver a atualização


    <img src="images/Imagem76.png" width='100%'/>

    9.6. Se precisar executar novamente, com o trabalho selecionado clique em <img src="images/Imagem77.png" height='25'/> e depois em <img src="images/Imagem78.png" height='25'/>

    9.7. Se precisar editar o script, clique em <img src="images/Imagem79.png" height='25'/>  e depois em <img src="images/Imagem80.png" height='25'/>

 
## Verificar tabela no Redshift e Executar Consultas

1.	Na AWS, procure e abra o serviço `Redshift`

2.	No menu lateral esquerdo clique em <img src="images/Imagem81.png" height='25'/> e depois em <img src="images/Imagem82.png" height='25'/> para abrir os clusters do Redshift

3. Inicie o cluster caso ele estiver parado

    3.1. Selecione o cluster criado no [Laboratório 5](https://github.com/fesousa/dataops-lab5) clicando no checkbox

    <img src="images/Imagem83.png" width='100%'/>
 
    3.2. Clique em  <img src="images/Imagem84.png" height='25'/> e depois em <img src="images/Imagem85.png" height='25'/>

    3.3. Na próxima tela clique em <img src="images/Imagem86.png" height='25'/> 

    3.4. Espere até que a coluna `Status` do cluster mostre <img src="images/Imagem87.png" height='25'/>

4.	Depois que o cluster estiver executando, no menu lateral esquerdo clique em <img src="images/Imagem88.png" height='25'/> e depois em <img src="images/Imagem89.png" height='25'/>

5.	Clique em <img src="images/Imagem90.png" height='25'/>

6.	Configure a conexão como na imagem abaixo:

<img src="images/Imagem91.png" width='100%'/>
 
7.	Clique em <img src="images/Imagem92.png" height='25'/>

8.	Na seção <img src="images/Imagem93.png" height='25'/>  verifique a configuração de conexão:

    8.1. <img src="images/Imagem94.png" height='100'/>


    8.2. <img src="images/Imagem95.png" height='100'/>


    8.3. Você deve ver a tabela <img src="images/Imagem96.png" height='25'/>   no final de <img src="images/Imagem97.png" height='25'/>

9.	Utilize o editor de consultas para consultar os registros da tabela utilizando SQL

    9.1. Quantidade de registros na tabela

```sql
select count(1) from vacinas_dw;
```

    9.2. Quantidade de vacinas por UF

```sql
select sum(quantidade), uf from vacinas_dw group by uf;
```

    9.3. Registros de vacinação com mais de 1000 vacinas

```sql
select * from vacinas_dw where quantidade > 1000
```


10. Lembre-se de pausar o cluster Redshift quando terminar o laboratório.

<div class="footer">
    &copy; 2022 Fernando Sousa
    <br/>
    {{update}}
</div>