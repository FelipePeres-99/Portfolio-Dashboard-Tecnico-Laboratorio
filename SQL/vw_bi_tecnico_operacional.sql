-- dbo.vw_bi_tecnico_operacional source

CREATE VIEW vw_bi_tecnico_operacional AS
SELECT
    ea.ai_ensaioamostra,
    ea.idamostra,
    ea.idensaio,
    ea.ai_amostra,
    e.descricao AS nome_ensaio,
    a.datacadastro AS data_cadastro_amostra,
    a.dataliberacao,
    a.idstatus AS status_amostra_macro,
    a.idfichacoleta AS idficha,
    a.datapromessaentrega AS datapromessa,
    a.valorconfirmado,
    a.dataenviocliente,
    c.nomereduzido,
    p.ai_proposta,
    ea.datainicioensaio AS data_inicio_ensaio,
    ea.datarecebida AS data_recebimento_ensaio,
    ea.dataconclusaoensaio AS data_conclusao_ensaio,
    ea.idstatus AS status_ensaio,
    cr.descricao AS celula_realizada_nome,
    
    -- Coluna de Origem da Execução (Interno / Externo)
    CASE
        WHEN e.descricao IN (
            'FERRO', 'ALUMÍNIO', 'ANTIMÔNIO', 'ARSÊNIO', 'BÁRIO', 'BERÍLIO', 'BORO', 'BROMO', 'CÁDMIO', 'CÁLCIO', 'CHUMBO', 'COBALTO', 'COBRE', 'CROMO', 'ESTRANHO', 'LÍTIO', 'MÁGNESIO', 'MANGANÊS', 'MERCÚRIO', 'MOLIBDÊNIO', 'NÍQUEL', 'OURO', 'POTÁSSIO', 'PRATA', 'SELÊNIO', 'SÍLICA', 'SÓDIO', 'TÁLIO', 'TUNGSTÊNIO', 'URÂNIO', 'VANÁDIO', 'ZINCO', 'TOXICIDADE VIBRIO E ALFA',
            'SULFETO', 'COLIFORMES', 'E-COLI', 'ENXOFRE', 'DEMANDA BIOQUÍMICA DE OXIGÊNIO', 'DIÓXIDO DE TITÂNIO', 'FÓSFORO', 'NITROGÊNIO AMONIACAL', 'CLORAMINA', 'CONDUTIVIDADE', 'CIANETO', 'CARBONO, ORGÂNICO E TOTAL', 'SALMONELLA', 'AMÔNIA',
            'Carbofurano', 'Glifosato + AMPA', 'Tiodicarbe', 'PAH -Benzo(a)pireno', '2,4,6-Triclorofenol', '2,4-D', '2,4-Diclorofenol', 'Alacloro', 'Aldicarbe + Aldicarbesulfona + Aldicarbesulfóxido', 'Aldrin + Dieldrin', 'Atrazina + S-Clorotriazinas (Deetil-Atrazina - Dea, Deisopropil-Atrazina - Dia e Diaminoclorotriazina - Dact)', 'bis(2-etilhexil)ftalato', 'Clorotalonil', 'Clorpirifós + clorpirifós-oxon', 'DDT (p,p’-DDT; p,p’-DDE; p,p’-DDD)', 'Di(2-etilhexil)ftalato', 'Dimetoato + Ometoato', 'Diuron', 'Fipronil', 'g-Clordano', 'Hidroxi-Atrazina', 'Lindano (gama-HCH)', 'Malation', 'Mancozebe + ETU', 'Metamidofós + Acefato', 'Metolacloro', 'Metribuzin', 'Molinato', 'N-nitrosodimetilamina', 'Paraquate', 'Pentaclorofenol', 'Picloran', 'Profenofós', 'Propargito', 'Protioconazol + ProticonazolDestio', 'Simazina', 'Tebuconazol', 'Terbufos', 'Tiram', 'Trifluralina', 'THM Total', '1,2-Diclorobenzeno', '1,2-Dicloroetano', 'Cloreto de vinila', 'Diclorometano', 'Monoclorobenzeno', 'Tetracloreto de carbono', 'Tetracloroeteno', 'Tricloroeteno', 'Clorito (IC)', 'Gosto', 'N-nitrito', 'Odor', 'Sulfeto de hidrogênio', 'Microcistinas', 'Radioatividade Alfa Global', 'Radioatividade Beta Global', 'Saxitoxinas', 'Ametrina', 'Carbendazim', 'Ciproconazol', 'Difenoconazol', 'Dioxano', 'Epoxiconazol', 'Flutriafol', 'Tiametoxam', 'Cilindrospermopsina', 'Epicloridrina', '1,4-Diclorobenzeno', 'Ácidos haloacéticos total',
            '1,2-Dicloroetileno, todos os isômeros', '1,4 Dioxano', '1-Metil-2-Pirrolidona', '1-Metóxi-2-Propanol', '2-Butóxietanol', '2-Etóxietanol', 'Acetato de 2-Butóxietanol', 'Acetato de 2-Butóxietila', 'Acetato de 2-Etoxietila', 'Acetato de Éter Metílico do Monopropileno Glicol', 'Acetato de etila', 'Acetato de Isobutila', 'Acetato de Isopentila', 'Acetato de Isopropila', 'Acetato de Metila', 'Acetato de n-Butila', 'Acetato de n-Propila', 'Acetato de Pentila', 'Acetato de Sec-Butila', 'Acetato de sec-Butila', 'Acetato de Vinila', 'Acetona', 'Acetonitrila', 'Ácido acético', 'Ácido Acético', 'Ácido Acrílico', 'Ácido Bórico', 'Ácido bromídrico', 'Ácido Cianídrico/Sais de cianeto', 'Ácido clorídrico', 'Ácido Crômico', 'Ácido fluorídrico', 'Ácido fórmico', 'Ácido fosfórico', 'Ácido nítrico', 'Ácido oxálico', 'Ácido Peracético', 'Ácido sulfúrico', 'Acrilato de Etila', 'Acrilato de Metila', 'Acrilato de n-butila', 'Acrilonitrila', 'Aguarrás C9 a C12', 'Aguarrás Mineral - C9 a C12', 'Álcool Etílico', 'Álcool Isoamílico', 'Álcool Isobutílico', 'Álcool Isopropílico', 'Álcool Metílico', 'Álcool n-Butílico', 'Álcool n-Propílico', 'Álcool sec-Butílico', 'Álcool Sec-butílico', 'Alfa-metilestireno', 'Alquilbenzenos (C9) - Determinação de Limite de Exposição', 'Benzeno', 'Bromofórmio', 'BTXE(caso queira coletar esses 4 agentes no mesmo amostrador)', 'Ciclohexano', 'Ciclohexanol', 'Ciclohexanona', 'Ciclopentano', 'Cloreto de Benzila', 'Cloreto de metila', 'Cloreto de Metileno', 'Cloro Cassete', 'Clorobenzeno', 'Clorodifluormetano', 'Compostos Orgânicos Voláteis (VOC)', 'Cumeno', 'Diacetona Álcool', 'Dicloreto de Etileno', 'Diesel C10 a C28', 'Diesel, combustível como hidrocarbonetos totais - Fração Inalável e Vapor', 'Diesel, combustível como hidrocarbonetos totais', 'Dietanolamina', 'Dietilamina', 'Dietileno Glicol', 'di-Isobutil Cetona', 'Dimetilacetamida', 'Dimetilamina', 'Dimetilanilina', 'Dimetilformamida', 'Dióxido de enxofre', 'Dióxido de Nitrogênio', 'Dissulfeto de Carbono', 'Dodecano', 'Espíritos Minerais - C9 a C12 - Determinação de Limite de Exposição', 'Estireno', 'Éter Butílico do Dietileno Glicol', 'Éter de Petróleo (C5 e C6)', 'Éter de Petróleo (C5 e C6) - Determinação de Limite de Exposição', 'Éter Metílico do propileno Glicol', 'Etilbenzeno', 'Formaldeído', 'Gasolina', 'Heptano, todos os isômeros', 'Hexano Isômeros', 'Hexileno Glicol', 'Isoparafina - C8 a C14 - Determinação de Limite de Exposição', 'Limoneno', 'Metil Etil Cetona', 'Metil Isobutil Carbinol', 'Metil isobutil cetona', 'Metilciclohexano', 'Metileno Difenil Isocianato (MDI)', 'Nafta - C7 a C11 - Determinação de Limite de Exposição', 'Nafta de Alcatrão - C8 a C10 - Determinação de Limite de Exposição', 'Nafta de Petróleo - C6 a C8', 'Nafta de Petróleo - C6 a C8 - Determinação de Limite de Exposição', 'Naftas C5-C8 (alcanos alifáticos) solvente de borracha', 'Naftas Leves', 'Naftas Pesadas', 'Naftas VM&P', 'n-Decano', 'Negro de fumo', 'Névoa de óleo mineral', 'n-Heptano', 'n-Hexano', 'Nitrobenzeno', 'n-Octano', 'Nonano', 'n-Pentano', 'n-Tridecano', 'n-Undecano', 'o-Toluidina', 'p-Diclorobenzeno', 'Percloroetileno', 'Peróxido de Hidrogenio', 'Peróxido de Metil Etil Cetona', 'Piridina', 'Poeira respirável', 'Poeira respirável com sílica', 'Poeira total', 'Querosene - C9 a C16', 'Querosene', 'Solvente de Borracha (C5 a C8) - Determinação de Limite de Exposição', 'Sulfeto de Hidrogênio', 'Terebentina e monoterpenos', 'Tetrahidrofurano', 'Tolueno', 'Tricloroetileno', 'Trietanolamina', 'Trimetil Benzeno (Mistura de Isômeros)', 'Varredura de HidrocarbonetosAromáticos (Ensaio realizado por Provedor Externo)', 'Varredura de Naftas C5 à C16 (PCR)', 'Varredura de Vapores – 24 agentes', 'Xileno (p, m e o)', 'α Metil Estireno', 'Benzeno OSHA- Atender PPEOB', 'Varredura de Solvente', 'Etanol', '2-Propanol', 'Álcool terc-butílico', 'Metil etil cetona', 'Álcool sec-butílico', 'Acetato de etila ppm', 'Álcool isobutílico', 'Acetato de propila, isômeros (Acetato de n-Propila e Acetato de iso-Propila)', 'Álcool n-butílico', 'Ciclohexeno', 'Acetato de butila, isômeros (Acetato de n-Butila e Acetato de terc-Butila)', 'Diacetona álcool ppm', 'Xileno, todos os isômeros', 'Estireno, monômero', '2-Butóxi etanol (EGBE)', 'Trimetil benzeno', 'Acetato de 2-butoxietila', 'Varredura de Naftas', 'Hexano, outros isômeros que não o n-Hexano', 'Pentano, todos os isômeros', 'Octano, todos os isômeros', 'n-Dodecano', 'n-Tetradecano', 'n-Pentadecano', 'Indeno', '1-Metil naftaleno e 2-Metil naftaleno #', 'Trimetil benzeno (mistura de isômeros)'
        ) THEN 'Externo'
        ELSE 'Interno'
    END AS origem_execucao,
    
    categoria_status = 
        CASE
            WHEN a.idstatus IN ('Aceite Tecnico', 'Em Execucao') THEN 'Pendente'
            WHEN a.idstatus IN ('Concluida', 'Conferida', 'Descartada', 'Enviada', 'Finalizada', 'Liberada') THEN 'Concluída'
            ELSE 'Em Coleta / Outros'
        END,

    status_entrega =
        CASE
            WHEN a.dataliberacao IS NOT NULL THEN 'Liberada'
            WHEN a.datapromessaentrega < CAST(GETDATE() AS DATE) THEN 'Em Atraso'
            ELSE 'No Prazo'
        END,

    dias_em_atraso = DATEDIFF(day, a.datapromessaentrega, COALESCE(a.dataliberacao, CAST(GETDATE() AS DATE))),
    
    indicador_atraso =
        CASE
            WHEN 
                a.datapromessaentrega < CAST(GETDATE() AS DATE)
                AND a.dataliberacao IS NULL
                AND a.idstatus IN ('Aceite Tecnico', 'Em Execucao')
            THEN 1
            ELSE 0
        END,

    status_gargalo_ficha =
        FIRST_VALUE(ea.idstatus) OVER (
            PARTITION BY a.idfichacoleta 
            ORDER BY 
                CASE ea.idstatus
                    WHEN 'Frasco Pendente' THEN 1
                    WHEN 'Carta Controle' THEN 2
                    WHEN 'Em Coleta' THEN 10
                    WHEN 'Recoleta' THEN 11
                    WHEN 'Coletado' THEN 20
                    WHEN 'Pre Recebimento' THEN 30
                    WHEN 'Recebido' THEN 40
                    WHEN 'Aceite Tecnico' THEN 50
                    WHEN 'Em Execucao' THEN 60
                    WHEN 'Revisado' THEN 70
                    WHEN 'Concluido' THEN 80
                    WHEN 'Conferido' THEN 90
                    WHEN 'Cancelado' THEN 99
                    ELSE 100
                END
        )
FROM
    amostra a
LEFT JOIN
    ensaioamostra ea ON a.ai_amostra = ea.ai_amostra
LEFT JOIN
    ensaio e ON ea.idensaio = e.idensaio
LEFT JOIN
    proposta p ON a.ai_proposta = p.ai_proposta
LEFT JOIN
    cliente c ON a.ai_cliente = c.ai_cliente
LEFT JOIN 
    celularealiz cr ON ea.ai_celularealiz = cr.ai_celularealiz
WHERE
    a.idstatus <> 'Cancelada';
