import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

# SQL para agrupar e contar a quantidade de registros
sqlGroupData = '''
select count(1) as quantidade, sexo, municipio, uf, data_aplicacao, dose, vacina
from myDataSource
group by sexo, municipio, uf, data_aplicacao, dose, vacina

'''

#função para agrupar e contar a quantidade de registros
def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)

#função para transformar o campo dose
def transformaDose(rec):
    
    rec['dose'] = '1' if '1' in rec['vacina_descricao_dose'] else ('2' if '2' in rec['vacina_descricao_dose'] else 'Única')
    return rec

## @params: [TempDir, JOB_NAME]
args = getResolvedOptions(sys.argv, ['TempDir','JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Leitura dos dados do Data Catalog
# TROQUE TABLE_NAME PELO NOME DA SUA TABELA NO DATA CATALOG
datasource = glueContext.create_dynamic_frame.from_catalog(database = "vacinas_database", table_name = "vacinas_input", transformation_ctx = "datasource")

# Transformação da dose
transformacao1 = Map.apply(frame=datasource, f=transformaDose, transformation_ctx="transformacao1")

# Mapeamento das colunas para outros nomes, conversão de tipos e remover colunas desnecessárias
transformacao2 = ApplyMapping.apply(
    frame = transformacao1,
    mappings = [
        ("paciente_enumSexoBiologico", "string", "sexo", "string"), 
        ("estabelecimento_municipio_nome", "string", "municipio", "string"), 
        ("estabelecimento_uf", "string", "uf", "string"), 
        ("vacina_dataAplicacao", "string", "data_aplicacao", "date"), 
        ("dose", "string", "dose", "string"), 
        ("vacina_nome", "string", "vacina", "string")
    ], 
    transformation_ctx = "transformacao2"
)

# Agrupamento e contagem dos registros por sexo, municipio, up, dose, vacina e data de aplicação
transformacao3 = sparkSqlQuery(glueContext, query = sqlGroupData, mapping = {"myDataSource": transformacao2}, transformation_ctx = "transformacao3")


# Salvar dados no Redshift
destino = glueContext.write_dynamic_frame.from_jdbc_conf(frame = transformacao3, catalog_connection = "redshift-connection", connection_options = {"dbtable": "vacinas_dw", "database": "dev"}, redshift_tmp_dir = args["TempDir"], transformation_ctx = "destino")
job.commit()