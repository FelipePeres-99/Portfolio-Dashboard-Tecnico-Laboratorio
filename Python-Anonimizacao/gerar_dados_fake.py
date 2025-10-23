import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

print("Iniciando a geração de dados falsos...")

# Inicializa o Faker para gerar dados aleatórios
fake = Faker('pt_BR')

# --- 1. CONFIGURAÇÕES ---
NUMERO_DE_LINHAS = 2000 # Você pode aumentar ou diminuir este número
DATA_INICIO = datetime(2024, 1, 1)
DATA_FIM = datetime.now()

# --- 2. LISTAS DE VALORES POSSÍVEIS ---

# Nomes de ensaios (peguei alguns da nossa lista de terceirizados para dar realismo)
LISTA_ENSAIOS = [
    'FERRO', 'ALUMÍNIO', 'CÁLCIO', 'CHUMBO', 'COBRE', 'CROMO', 'ZINCO', 'SULFETO', 'COLIFORMES', 'E-COLI',
    'pH', 'Turbidez', 'Condutividade', 'Benzeno', 'Tolueno', 'Etilbenzeno', 'Xilenos', 'PAH -Benzo(a)pireno',
    '2,4-D', 'Glifosato + AMPA', 'Sólidos Sedimentáveis', 'Óleos e Graxas'
]

# Lista de ensaios que são externos (baseado no nosso trabalho anterior)
ENSAIOS_EXTERNOS = {
    'FERRO', 'ALUMÍNIO', 'ANTIMÔNIO', 'ARSÊNIO', 'BÁRIO', 'BERÍLIO', 'BORO', 'BROMO', 'CÁDMIO', 'CÁLCIO', 'CHUMBO', 'COBALTO', 'COBRE', 'CROMO', 'ESTRANHO', 'LÍTIO', 'MÁGNESIO', 'MANGANÊS', 'MERCÚRIO', 'MOLIBDÊNIO', 'NÍQUEL', 'OURO', 'POTÁSSIO', 'PRATA', 'SELÊNIO', 'SÍLICA', 'SÓDIO', 'TÁLIO', 'TUNGSTÊNIO', 'URÂNIO', 'VANÁDIO', 'ZINCO', 'TOXICIDADE VIBRIO E ALFA', 'SULFETO', 'COLIFORMES', 'E-COLI', 'ENXOFRE', 'DEMANDA BIOQUÍMICA DE OXIGÊNIO', 'DIÓXIDO DE TITÂNIO', 'FÓSFORO', 'NITROGÊNIO AMONIACAL', 'CLORAMINA', 'CONDUTIVIDADE', 'CIANETO', 'CARBONO, ORGÂNICO E TOTAL', 'SALMONELLA', 'AMÔNIA', 'Carbofurano', 'Glifosato + AMPA', 'Tiodicarbe', 'PAH -Benzo(a)pireno', '2,4,6-Triclorofenol', '2,4-D', '2,4-Diclorofenol', 'Alacloro', 'Aldicarbe + Aldicarbesulfona + Aldicarbesulfóxido', 'Aldrin + Dieldrin', 'Atrazina + S-Clorotriazinas (Deetil-Atrazina - Dea, Deisopropil-Atrazina - Dia e Diaminoclorotriazina - Dact)', 'bis(2-etilhexil)ftalato', 'Clorotalonil', 'Clorpirifós + clorpirifós-oxon', 'DDT (p,p’-DDT; p,p’-DDE; p,p’-DDD)', 'Di(2-etilhexil)ftalato', 'Dimetoato + Ometoato', 'Diuron', 'Fipronil', 'g-Clordano', 'Hidroxi-Atrazina', 'Lindano (gama-HCH)', 'Malation', 'Mancozebe + ETU', 'Metamidofós + Acefato', 'Metolacloro', 'Metribuzin', 'Molinato', 'N-nitrosodimetilamina', 'Paraquate', 'Pentaclorofenol', 'Picloran', 'Profenofós', 'Propargito', 'Protioconazol + ProticonazolDestio', 'Simazina', 'Tebuconazol', 'Terbufos', 'Tiram', 'Trifluralina', 'THM Total', '1,2-Diclorobenzeno', '1,2-Dicloroetano', 'Cloreto de vinila', 'Diclorometano', 'Monoclorobenzeno', 'Tetracloreto de carbono', 'Tetracloroeteno', 'Tricloroeteno', 'Clorito (IC)', 'Gosto', 'N-nitrito', 'Odor', 'Sulfeto de hidrogênio', 'Microcistinas', 'Radioatividade Alfa Global', 'Radioatividade Beta Global', 'Saxitoxinas', 'Ametrina', 'Carbendazim', 'Ciproconazol', 'Difenoconazol', 'Dioxano', 'Epoxiconazol', 'Flutriafol', 'Tiametoxam', 'Cilindrospermopsina', 'Epicloridrina', '1,Dioxano', '1-Metil-2-Pirrolidona', '1-Metóxi-2-Propanol', '2-Butóxietanol', '2-Etóxietanol', 'Acetato de 2-Butóxietanol', 'Acetato de 2-Butóxietila', 'Acetato de 2-Etoxietila', 'Acetato de Éter Metílico do Monopropileno Glicol', 'Acetato de etila', 'Acetato de Isobutila', 'Acetato de Isopentila', 'Acetato de Isopropila', 'Acetato de Metila', 'Acetato de n-Butila', 'Acetato de n-Propila', 'Acetato de Pentila', 'Acetato de Sec-Butila', 'Acetato de sec-Butila', 'Acetato de Vinila', 'Acetona', 'Acetonitrila', 'Ácido acético', 'Ácido Acético', 'Ácido Acrílico', 'Ácido Bórico', 'Ácido bromídrico', 'Ácido Cianídrico/Sais de cianeto', 'Ácido clorídrico', 'Ácido Crômico', 'Ácido fluorídrico', 'Ácido fórmico', 'Ácido fosfórico', 'Ácido nítrico', 'Ácido oxálico', 'Ácido Peracético', 'Ácido sulfúrico', 'Acrilato de Etila', 'Acrilato de Metila', 'Acrilato de n-butila', 'Acrilonitrila', 'Aguarrás C9 a C12', 'Aguarrás Mineral - C9 a C12', 'Álcool Etílico', 'Álcool Isoamílico', 'Álcool Isobutílico', 'Álcool Isopropílico', 'Álcool Metílico', 'Álcool n-Butílico', 'Álcool n-Propílico', 'Álcool sec-Butílico', 'Álcool Sec-butílico', 'Alfa-metilestireno', 'Alquilbenzenos (C9) - Determinação de Limite de Exposição', 'Benzeno', 'Bromofórmio', 'BTXE(caso queira coletar esses 4 agentes no mesmo amostrador)', 'Ciclohexano', 'Ciclohexanol', 'Ciclohexanona', 'Ciclopentano', 'Cloreto de Benzila', 'Cloreto de metila', 'Cloreto de Metileno', 'Cloro Cassete', 'Clorobenzeno', 'Clorodifluormetano', 'Compostos Orgânicos Voláteis (VOC)', 'Cumeno', 'Diacetona Álcool', 'Dicloreto de Etileno', 'Diesel C10 a C28', 'Diesel, combustível como hidrocarbonetos totais - Fração Inalável e Vapor', 'Diesel, combustível como hidrocarbonetos totais', 'Dietanolamina', 'Dietilamina', 'Dietileno Glicol', 'di-Isobutil Cetona', 'Dimetilacetamida', 'Dimetilamina', 'Dimetilanilina', 'Dimetilformamida', 'Dióxido de enxofre', 'Dióxido de Nitrogênio', 'Dissulfeto de Carbono', 'Dodecano', 'Espíritos Minerais - C9 a C12 - Determinação de Limite de Exposição', 'Estireno', 'Éter Butílico do Dietileno Glicol', 'Éter de Petróleo (C5 e C6)', 'Éter de Petróleo (C5 e C6) - Determinação de Limite de Exposição', 'Éter Metílico do propileno Glicol', 'Etilbenzeno', 'Formaldeído', 'Gasolina', 'Heptano, todos os isômeros', 'Hexano Isômeros', 'Hexileno Glicol', 'Isoparafina - C8 a C14 - Determinação de Limite de Exposição', 'Limoneno', 'Metil Etil Cetona', 'Metil Isobutil Carbinol', 'Metil isobutil cetona', 'Metilciclohexano', 'Metileno Difenil Isocianato (MDI)', 'Nafta - C7 a C11 - Determinação de Limite de Exposição', 'Nafta de Alcatrão - C8 a C10 - Determinação de Limite de Exposição', 'Nafta de Petróleo - C6 a C8', 'Nafta de Petróleo - C6 a C8 - Determinação de Limite de Exposição', 'Naftas C5-C8 (alcanos alifáticos) solvente de borracha', 'Naftas Leves', 'Naftas Pesadas', 'Naftas VM&P', 'n-Decano', 'Negro de fumo', 'Névoa de óleo mineral', 'n-Heptano', 'n-Hexano', 'Nitrobenzeno', 'n-Octano', 'Nonano', 'n-Pentano', 'n-Tridecano', 'n-Undecano', 'o-Toluidina', 'p-Diclorobenzeno', 'Percloroetileno', 'Peróxido de Hidrogenio', 'Peróxido de Metil Etil Cetona', 'Piridina', 'Poeira respirável', 'Poeira respirável com sílica', 'Poeira total', 'Querosene - C9 a C16', 'Querosene', 'Solvente de Borracha (C5 a C8) - Determinação de Limite de Exposição', 'Sulfeto de Hidrogênio', 'Terebentina e monoterpenos', 'Tetrahidrofurano', 'Tolueno', 'Tricloroetileno', 'Trietanolamina', 'Trimetil Benzeno (Mistura de Isômeros)', 'Varredura de HidrocarbonetosAromáticos (Ensaio realizado por Provedor Externo)', 'Varredura de Naftas C5 à C16 (PCR)', 'Varredura de Vapores – 24 agentes', 'Xileno (p, m e o)', 'α Metil Estireno', 'Benzeno OSHA- Atender PPEOB', 'Varredura de Solvente', 'Etanol', '2-Propanol', 'Álcool terc-butílico', 'Metil etil cetona', 'Álcool sec-butílico', 'Acetato de etila ppm', 'Álcool isobutílico', 'Acetato de propila, isômeros (Acetato de n-Propila e Acetato de iso-Propila)', 'Álcool n-butílico', 'Ciclohexeno', 'Acetato de butila, isômeros (Acetato de n-Butila e Acetato de terc-Butila)', 'Diacetona álcool ppm', 'Xileno, todos os isômeros', 'Estireno, monômero', '2-Butóxi etanol (EGBE)', 'Trimetil benzeno', 'Acetato de 2-butoxietila', 'Varredura de Naftas', 'Hexano, outros isômeros que não o n-Hexano', 'Pentano, todos os isômeros', 'Octano, todos os isômeros', 'n-Dodecano', 'n-Tetradecano', 'n-Pentadecano', 'Indeno', '1-Metil naftaleno e 2-Metil naftaleno #', 'Trimetil benzeno (mistura de isômeros)'
}

STATUS_MACRO = ['Aceite Tecnico', 'Em Execucao', 'Concluida', 'Conferida', 'Descartada', 'Enviada', 'Finalizada', 'Liberada', 'Em Coleta', 'Coletada', 'Pre Recebimento', 'Recebido', 'Recoleta']
STATUS_ENSAIO = ['Aceite Tecnico', 'Em Execucao', 'Concluido', 'Conferido', 'Em Coleta', 'Coletado', 'Recebido', 'Revisado', 'Frasco Pendente', 'Recoleta']
CELULAS = ['Célula A - Cromatografia', 'Célula B - Metais', 'Célula C - Microbiologia', 'Célula D - Voláteis', None] # Adicionando None para simular "em branco"
CLIENTES = [fake.company() for _ in range(50)] # Gera 50 nomes de empresas falsas
HOJE = datetime.now().date()

# --- 3. GERANDO OS DADOS BASE ---
print(f"Gerando {NUMERO_DE_LINHAS} linhas de dados base...")
data = {
    'ai_ensaioamostra': np.arange(1, NUMERO_DE_LINHAS + 1),
    'idamostra': np.random.randint(1000, 5000, size=NUMERO_DE_LINHAS),
    'idensaio': np.random.randint(1, 200, size=NUMERO_DE_LINHAS),
    'ai_amostra': np.random.choice(np.arange(10000, 20000), size=NUMERO_DE_LINHAS // 5).repeat(5)[:NUMERO_DE_LINHAS], # Simula 5 ensaios por amostra
    'nome_ensaio': np.random.choice(LISTA_ENSAIOS, size=NUMERO_DE_LINHAS),
    'datacadastro': [fake.date_between(start_date=DATA_INICIO, end_date=DATA_FIM) for _ in range(NUMERO_DE_LINHAS)],
    'status_amostra_macro': np.random.choice(STATUS_MACRO, size=NUMERO_DE_LINHAS, p=[0.1, 0.2, 0.1, 0.1, 0.05, 0.1, 0.1, 0.1, 0.05, 0.05, 0.02, 0.02, 0.01]),
    'idficha': np.random.randint(1, 1000, size=NUMERO_DE_LINHAS),
    'valorconfirmado': np.round(np.random.uniform(50, 2000, size=NUMERO_DE_LINHAS), 2),
    'nomereduzido': np.random.choice(CLIENTES, size=NUMERO_DE_LINHAS),
    'ai_proposta': np.random.choice(np.arange(30000, 40000), size=NUMERO_DE_LINHAS // 10).repeat(10)[:NUMERO_DE_LINHAS], # Simula 10 amostras por proposta
    'status_ensaio': np.random.choice(STATUS_ENSAIO, size=NUMERO_DE_LINHAS),
    'celula_realizada_nome': np.random.choice(CELULAS, size=NUMERO_DE_LINHAS, p=[0.2, 0.2, 0.2, 0.2, 0.2]),
}

# --- 4. CONSTRUINDO O DATAFRAME ---
df = pd.DataFrame(data)

# --- 5. GERANDO AS COLUNAS CALCULADAS (REPLICANDO A LÓGICA DA VIEW) ---
print("Replicando a lógica da VIEW (colunas calculadas)...")

# Gerando datas baseadas na data de cadastro
df['datapromessa'] = df['datacadastro'].apply(lambda x: x + timedelta(days=np.random.randint(7, 30)))
df['datarecebimento_ensaio'] = df['datacadastro'].apply(lambda x: x + timedelta(days=np.random.randint(0, 2)))
df['data_inicio_ensaio'] = df['datarecebimento_ensaio'].apply(lambda x: x + timedelta(days=np.random.randint(1, 5)))
df['data_conclusao_ensaio'] = df['data_inicio_ensaio'].apply(lambda x: x + timedelta(days=np.random.randint(1, 10)))

# Lógica de Liberação e Envio (algumas ainda estão em branco)
df['dataliberacao'] = df['data_conclusao_ensaio'].apply(lambda x: x + timedelta(days=np.random.randint(0, 2)) if np.random.rand() > 0.3 else pd.NaT)
df['dataenviocliente'] = df['dataliberacao'].apply(lambda x: x + timedelta(days=np.random.randint(0, 1)) if pd.notna(x) else pd.NaT)

# Lógica da coluna 'origem_execucao'
df['origem_execucao'] = df['nome_ensaio'].apply(lambda x: 'Externo' if x in ENSAIOS_EXTERNOS else 'Interno')

# Lógica da coluna 'categoria_status'
def get_categoria_status(status):
    if status in ('Aceite Tecnico', 'Em Execucao'):
        return 'Pendente'
    elif status in ('Concluida', 'Conferida', 'Descartada', 'Enviada', 'Finalizada', 'Liberada'):
        return 'Concluída'
    else:
        return 'Em Coleta / Outros'
df['categoria_status'] = df['status_amostra_macro'].apply(get_categoria_status)

# Lógica da coluna 'status_entrega'
def get_status_entrega(row):
    if pd.notna(row['dataliberacao']):
        return 'Liberada'
    elif row['datapromessa'] < HOJE:
        return 'Em Atraso'
    else:
        return 'No Prazo'
df['status_entrega'] = df.apply(get_status_entrega, axis=1)

# Lógica da coluna 'dias_em_atraso'
def get_dias_em_atraso(row):
    data_fim = row['dataliberacao'] if pd.notna(row['dataliberacao']) else HOJE
    return (data_fim - row['datapromessa']).days
df['dias_em_atraso'] = df.apply(get_dias_em_atraso, axis=1)

# Lógica da coluna 'indicador_atraso'
def get_indicador_atraso(row):
    if (row['datapromessa'] < HOJE and 
        pd.isna(row['dataliberacao']) and 
        row['status_amostra_macro'] in ('Aceite Tecnico', 'Em Execucao')):
        return 1
    else:
        return 0
df['indicador_atraso'] = df.apply(get_indicador_atraso, axis=1)

# Lógica da coluna 'status_gargalo_ficha' (Simplificada para performance)
# Em um script real, isso é complexo. Para dados FALSOS, podemos apenas atribuir um status de ensaio.
df['status_gargalo_ficha'] = df['status_ensaio'] 

# --- 6. SALVANDO O ARQUIVO EXCEL ---
NOME_ARQUIVO = 'vw_bi_tecnico_operacional_fake.xlsx'
df.to_excel(NOME_ARQUIVO, index=False, engine='openpyxl')

print(f"\n--- SUCESSO! ---")
print(f"Arquivo '{NOME_ARQUIVO}' criado com {NUMERO_DE_LINHAS} linhas de dados falsos.")
print("Agora você pode criar uma cópia do seu Power BI e usar este arquivo Excel como a nova fonte de dados.")
