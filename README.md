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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.9. No popup, selecione o bucket e pasta `dataops-impacta-dados-nomesobrenome/input` (bucket criado no [Laboratório 1](https://github.com/fesousa/dataops-lab1))


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/Imagem21.png" width='100%'/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.7. Clique em <img src="images/Imagem22.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.8. Clique em <img src="images/Imagem23.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.9. Na tela seguinte, clique novamente em <img src="images/Imagem24.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.10. Na próxima tela, selecione <img src="images/Imagem25.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.11. Em `Função do IAM` selecione <img src="images/Imagem26.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.12. Clique em <img src="images/Imagem27.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.13. Na próxima tela, verifique se a Frequência está como <img src="images/Imagem28.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.14. Clique em <img src="images/Imagem29.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.15. Na tela de configuração de saída, clique em <img src="images/Imagem30.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. No popup coloque no campo `Nome do banco de dados` o nome `vacinas_database`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Clique em <img src="images/Imagem31.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.16. De volta a tela de configuração de saída, no campo <img src="images/Imagem32.png" height='25'/>  escreva `vacinas_`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.17. Clique em <img src="images/Imagem33.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.18. Revise as configurações e clique em <img src="images/Imagem34.png" height='25'/> 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.19. Verifique o Crawler criado na nova tela

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/Imagem35.png" width='100%'/>



<div class="footer">
    &copy; 2022 Fernando Sousa
    <br/>
    
Last update: 2022-04-03 15:13:26
</div>