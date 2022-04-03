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


<div class="footer">
    &copy; 2022 Fernando Sousa
    <br/>
    {{update}}
</div>