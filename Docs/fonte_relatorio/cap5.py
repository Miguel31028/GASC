DICT = {
    'CATEGORIA': [
        ('id_categoria', 'String', 'S', 'Identificador.'),
        ('nome', 'String(60)', 'S', 'Ex.: Lacticínios, Massas, Carne de aves, Vestuário.'),
        ('tipo_bem', 'TipoBem', 'S', 'ALIMENTAR, HIGIENE, LIMPEZA, VESTUARIO ou OUTRO.'),
        ('condicao_armazenamento', 'CondicaoArmazenamento', 'S', 'AMBIENTE, REFRIGERADO ou CONGELADO; determina o tipo de local sugerido.'),
        ('congelavel', 'Boolean', 'S', 'Se os produtos podem ser congelados para prolongar a validade.'),
        ('dias_aviso', 'Int', 'S', 'Antecedência, em dias, do alerta de validade (por omissão 7).'),
    ],
    'REGRA_CONGELACAO': [
        ('id_categoria', 'String', 'S', 'Categoria a que a regra se aplica (uma regra por categoria).'),
        ('dias_extensao', 'Int', 'S', 'Dias a somar à data de congelação para propor a nova validade.'),
        ('observacoes', 'String', 'N', 'Indicações de preparação para congelar.'),
    ],
    'PRODUTO': [
        ('id_produto', 'String', 'S', 'Identificador.'),
        ('id_categoria', 'String', 'S', 'Categoria do produto.'),
        ('nome', 'String(80)', 'S', 'Designação (ex.: Arroz agulha).'),
        ('marca', 'String(60)', 'N', 'Marca; distingue produtos e lotes.'),
        ('formato', 'String(30)', 'N', 'Formato de venda (ex.: 1 kg, 35 cl).'),
        ('unidade_stock', 'UnidadeStock', 'S', 'UN, KG ou L.'),
        ('conteudo_por_unidade', 'Decimal', 'N', 'Conteúdo de uma unidade (ex.: 0,5 kg), para estatísticas.'),
        ('tem_validade', 'Boolean', 'S', 'Falso para vestuário e alguns bens não alimentares.'),
        ('tipo_data_validade', 'TipoDataValidade', 'N', 'CONSUMIR_ATE ou CONSUMIR_PREFERENCIA (a validar com a equipa HACCP).'),
        ('stock_minimo', 'Decimal', 'N', 'Limiar para o alerta de stock mínimo.'),
        ('tamanho, genero', 'String', 'N', 'Atributos de vestuário.'),
        ('codigo_barras', 'String', 'N', 'EAN (melhoria futura).'),
        ('ativo', 'Boolean', 'S', 'Produtos inativos não aparecem na receção.'),
    ],
    'APRESENTACAO': [
        ('id_produto', 'String', 'S', 'Produto.'),
        ('nome', 'String(30)', 'S', 'Ex.: Unidade, Caixa, Palete, Saco.'),
        ('fator', 'Decimal', 'S', 'Quantidade na unidade de stock (ex.: 30 para palete de 30 UN; 50 para saco de 50 kg).'),
    ],
    'LOCAL': [
        ('id_local', 'String', 'S', 'Identificador.'),
        ('tipo', 'TipoLocal', 'S', 'CELULA ou ZONA_FRIO.'),
        ('codigo', 'String', 'S', 'Único. Célula: xxx-xx-xx; zona: EQUIPAMENTO-LadoNível (ex.: ARCA1-D1). Codificado no QR.'),
        ('coluna, linha, andar', 'Int', 'N', 'Componentes do código da célula.'),
        ('id_equipamento, lado, nivel', 'String/Char/Int', 'N', 'Componentes da zona de frio (lado ∈ {D, C, E}).'),
        ('cheio', 'Boolean', 'S', 'Assinalado pelo operador; excluído das sugestões.'),
        ('ativo', 'Boolean', 'S', 'Locais desativados não aparecem.'),
    ],
    'EQUIPAMENTO_FRIO': [
        ('id_equipamento', 'String', 'S', 'Identificador.'),
        ('codigo', 'String', 'S', 'Código curto (ex.: ARCA1, ARCA3).'),
        ('nome', 'String', 'S', 'Descrição.'),
        ('tipo', 'TipoEquipamento', 'S', 'CONGELADOR ou FRIGORIFICO.'),
        ('categorias_preferenciais', 'Lista', 'N', 'Categorias de uso preferencial (tabela EQUIPAMENTO_CATEGORIA).'),
    ],
    'DOADOR': [
        ('id_doador', 'String', 'S', 'Identificador.'),
        ('tipo', 'TipoDoador', 'S', 'PARTICULAR, EMPRESA, ORGANIZACAO ou CAMPANHA.'),
        ('nome', 'String', 'S', 'Nome ou designação.'),
        ('nif', 'String(9)', 'N', 'Número de identificação fiscal.'),
        ('morada, contacto', 'String', 'N', 'Dados de contacto.'),
    ],
    'RECECAO': [
        ('id_rececao', 'String', 'S', 'Identificador.'),
        ('id_doador', 'String', 'N', 'Nulo quando anónima.'),
        ('id_utilizador', 'String', 'S', 'Responsável pela receção (rubrica no RGDHSA049).'),
        ('data_hora', 'Timestamp', 'S', 'Momento da receção.'),
        ('tipo_origem', 'TipoDoador', 'S', 'Origem dos bens.'),
        ('anonimo', 'Boolean', 'S', 'Doação de particular anónimo.'),
        ('n_guia', 'String', 'C', 'Obrigatório quando a origem é EMPRESA.'),
        ('url_guia', 'String', 'N', 'Caminho da imagem da guia no Cloud Storage.'),
        ('temperatura, observacoes', 'Decimal/String', 'N', 'Dados gerais da receção.'),
    ],
    'LINHA_RECECAO': [
        ('id_rececao, id_produto', 'String', 'S', 'Receção e produto.'),
        ('id_apresentacao', 'String', 'N', 'Apresentação usada (nula = unidade de stock).'),
        ('quantidade', 'Decimal', 'S', 'Quantidade na apresentação indicada.'),
        ('validade', 'Date', 'C', 'Obrigatória se o produto tem validade.'),
        ('lote_fornecedor', 'String', 'N', 'Lote ou n.º de guia indicado pelo fornecedor.'),
        ('higiene_c, rotulagem_c, organoleticas_c, embalagem_c', 'Boolean', 'S', 'Critérios Conforme/Não conforme do RGDHSA049.'),
        ('temperatura', 'Decimal', 'N', 'Temperatura medida (refrigerados e congelados).'),
        ('aceite', 'Boolean', 'S', 'Falso quando a linha é rejeitada.'),
        ('observacoes', 'String', 'N', 'Motivo da não conformidade.'),
    ],
    'LOTE': [
        ('id_lote', 'String', 'S', 'Identificador (também impresso em etiqueta, se necessário).'),
        ('id_produto, id_linha', 'String', 'S', 'Produto e linha de receção de origem.'),
        ('id_local', 'String', 'N', 'Local atual (nulo enquanto pendente).'),
        ('validade', 'Date', 'N', 'Validade atual (alterada na congelação).'),
        ('validade_original', 'Date', 'N', 'Validade de origem.'),
        ('qtd_inicial, qtd_atual', 'Decimal', 'S', 'Quantidades na unidade de stock; qtd_atual ≥ 0.'),
        ('volumes', 'Int', 'N', 'Número de volumes (produtos a granel).'),
        ('estado', 'EstadoLote', 'S', 'Ciclo de vida descrito na secção 4.4.'),
        ('congelado_origem, congelado_interno', 'Boolean', 'S', 'Origem da congelação (relevante para FEFO).'),
        ('data_entrada', 'Timestamp', 'S', 'Critério de desempate FEFO.'),
    ],
    'MOVIMENTO': [
        ('id_lote, id_utilizador', 'String', 'S', 'Lote e autor.'),
        ('tipo', 'TipoMovimento', 'S', 'Tipo de movimento.'),
        ('quantidade', 'Decimal', 'S', 'Quantidade movimentada (sinal implícito no tipo).'),
        ('data_hora', 'Timestamp', 'S', 'Momento.'),
        ('id_local_origem, id_local_destino', 'String', 'N', 'Para arrumações e transferências.'),
        ('referencia', 'String', 'N', 'Id da entrega, saída para a cozinha ou receção.'),
    ],
    'DESPERDICIO': [
        ('id_lote, id_utilizador', 'String', 'S', 'Lote e autor.'),
        ('quantidade', 'Decimal', 'S', 'Quantidade desperdiçada na unidade de stock.'),
        ('motivo', 'MotivoDesperdicio', 'S', 'EXPIRADO, DANIFICADO ou NAO_CONFORME.'),
        ('data', 'Date', 'S', 'Data do registo.'),
    ],
    'ALERTA': [
        ('tipo', 'TipoAlerta', 'S', 'EXPIRADO, VALIDADE_PROXIMA ou STOCK_MINIMO.'),
        ('id_lote / id_produto', 'String', 'N', 'Objeto do alerta.'),
        ('data_hora, resolvido', 'Timestamp/Boolean', 'S', 'Criação e estado.'),
    ],
    'UTILIZADOR': [
        ('id_utilizador', 'String', 'S', 'UID do Firebase Authentication.'),
        ('nome, email', 'String', 'S', 'Identificação.'),
        ('perfis', 'Lista<Perfil>', 'S', 'ADMIN, RESPONSAVEL, TECNICO, OPERADOR, COZINHA (replicados em *custom claims*).'),
        ('ativo', 'Boolean', 'S', 'Utilizadores inativos não se autenticam.'),
    ],
    'AGREGADO': [
        ('id_agregado, codigo', 'String', 'S', 'Identificador interno e código legível (ex.: A-0142).'),
        ('morada, codigo_postal, localidade, telefone', 'String', 'S/N', 'Contactos.'),
        ('situacao', 'String', 'N', 'Caracterização socioeconómica resumida.'),
        ('beneficia_cabaz, beneficia_refeicoes', 'Boolean', 'S', 'Respostas de que beneficia.'),
        ('periodicidade', 'Periodicidade', 'N', 'SEMANAL, QUINZENAL, MENSAL, PONTUAL ou n.º de dias.'),
        ('estado', 'EstadoAgregado', 'S', 'ATIVO, SUSPENSO ou INATIVO.'),
        ('data_inscricao, id_tecnico, observacoes', 'Vários', 'S/N', 'Acompanhamento.'),
    ],
    'PESSOA': [
        ('id_pessoa, id_agregado', 'String', 'S', 'Identificação e agregado.'),
        ('nome', 'String', 'S', 'Nome completo.'),
        ('data_nascimento', 'Date', 'N', 'Para cálculo da idade.'),
        ('nif, niss', 'String', 'N', 'Identificadores fiscais e da segurança social.'),
        ('parentesco, titular', 'String/Boolean', 'S', 'Relação com o titular.'),
        ('autorizada_levantar', 'Boolean', 'S', 'Pode levantar cabazes e refeições.'),
        ('restricoes_alimentares, alergias', 'String', 'N', 'Mostrados na preparação do cabaz.'),
    ],
    'CREDENCIAL_QR': [
        ('token', 'String(32)', 'S', 'Valor aleatório criptograficamente seguro codificado no QR.'),
        ('id_pessoa', 'String', 'S', 'Titular.'),
        ('suporte, emitida_em, ativa', 'Vários', 'S', 'PAPEL ou APP; data; estado.'),
    ],
    'EQUIPAMENTO_CATEGORIA': [
        ('id_equipamento, id_categoria', 'String', 'S', 'Chave composta; associa um equipamento de frio a uma categoria de uso preferencial (sugestão).'),
    ],
    'CONSENTIMENTO': [
        ('id_consentimento, id_agregado', 'String', 'S', 'Identificação e agregado.'),
        ('data_hora', 'Timestamp', 'S', 'Momento em que o consentimento foi prestado.'),
        ('finalidades', 'String', 'S', 'Finalidades consentidas (ex.: gestão do apoio alimentar, contacto por SMS).'),
        ('url_documento', 'String', 'N', 'Digitalização do documento assinado.'),
    ],
    'CONTA_UTENTE': [
        ('uid', 'String', 'S', 'UID do Firebase Authentication (autenticação por telefone).'),
        ('id_pessoa', 'String', 'S', 'Pessoa associada (única).'),
        ('telefone', 'String', 'S', 'Número de telemóvel validado por SMS.'),
    ],
    'AGENDAMENTO / ENTREGA / LINHA_SAIDA': [
        ('AGENDAMENTO.data_hora, tipo, estado', 'Vários', 'S', 'Data prevista, CABAZ ou OUTROS_BENS, estado.'),
        ('ENTREGA.id_pessoa_levantou, id_utilizador', 'String', 'S', 'Quem levantou e quem entregou.'),
        ('ENTREGA.identificacao_manual', 'Boolean', 'S', 'Verdadeiro se não foi usado o QR.'),
        ('LINHA_SAIDA.id_lote, quantidade', 'String/Decimal', 'S', 'Lote e quantidade abatida.'),
        ('LINHA_SAIDA.id_entrega / id_saida_cozinha', 'String', 'C', 'Exatamente um dos dois é preenchido (restrição de exclusividade).'),
    ],
    'SERVICO_REFEICAO / PEDIDO_REFEICAO / LEVANTAMENTO / SAIDA_COZINHA': [
        ('SERVICO_REFEICAO.data, tipo, aberto', 'Vários', 'S', 'Dia, ALMOCO ou JANTAR, se aceita pedidos.'),
        ('SERVICO_REFEICAO.total_previsto, total_confecionado', 'Int', 'N', 'Totais do dia.'),
        ('PEDIDO_REFEICAO.n_refeicoes, origem, estado', 'Vários', 'S', 'Quantidade, canal (BALCAO, APP_UTENTE, TECNICO) e estado.'),
        ('LEVANTAMENTO.n_entregues, justificacao_excecao', 'Int/String', 'S/N', 'Refeições entregues e justificação de exceção (obrigatória quando não há pedido).'),
        ('SAIDA_COZINHA.id_servico, id_utilizador, data_hora', 'Vários', 'S', 'Serviço a que se destinam os produtos, autor e momento.'),
    ],
}

ENUMS = [
    ('TipoBem', 'ALIMENTAR, HIGIENE, LIMPEZA, VESTUARIO, OUTRO'),
    ('CondicaoArmazenamento', 'AMBIENTE, REFRIGERADO, CONGELADO'),
    ('UnidadeStock', 'UN, KG, L'),
    ('TipoDataValidade', 'CONSUMIR_ATE, CONSUMIR_PREFERENCIA'),
    ('TipoDoador', 'PARTICULAR, EMPRESA, ORGANIZACAO, CAMPANHA'),
    ('TipoEquipamento', 'CONGELADOR, FRIGORIFICO'),
    ('TipoLocal', 'CELULA, ZONA_FRIO'),
    ('EstadoLote', 'PENDENTE_ARRUMACAO, DISPONIVEL, CONGELADO, EXPIRADO, ESGOTADO, DESCARTADO'),
    ('TipoMovimento', 'ENTRADA, ARRUMACAO, TRANSFERENCIA, CONGELACAO, SAIDA_CABAZ, SAIDA_BENS, SAIDA_COZINHA, DESPERDICIO, AJUSTE'),
    ('MotivoDesperdicio', 'EXPIRADO, DANIFICADO, NAO_CONFORME'),
    ('TipoAlerta', 'EXPIRADO, VALIDADE_PROXIMA, STOCK_MINIMO'),
    ('Perfil', 'ADMIN, RESPONSAVEL, TECNICO, OPERADOR, COZINHA'),
    ('EstadoAgregado', 'ATIVO, SUSPENSO, INATIVO'),
    ('Periodicidade', 'SEMANAL, QUINZENAL, MENSAL, PONTUAL, PERSONALIZADA (n.º de dias)'),
    ('EstadoAgendamento', 'AGENDADO, ENTREGUE, FALTOU, CANCELADO'),
    ('TipoRefeicao', 'ALMOCO, JANTAR'),
    ('EstadoPedido', 'PEDIDO, LEVANTADO, NAO_LEVANTADO, CANCELADO'),
]

FS = [
    ('utilizadores/{uid}', 'Dados do colaborador e perfis.', 'Perfis replicados em *custom claims* pela função de administração.'),
    ('categorias/{id}', 'Categoria com a regra de congelação embebida (`regraCongelacao`).', 'Relação 1:0..1 embebida.'),
    ('produtos/{id}', 'Produto com a lista `apresentacoes` embebida e o campo derivado `stockAtual`.', '`stockAtual` mantido pelas Cloud Functions.'),
    ('locais/{id}', 'Células e zonas de frio (campo `tipo`), com `chaveOrdenacao` pré-calculada.', 'Permite ordenar diretamente por consulta.'),
    ('equipamentos/{id}', 'Equipamentos de frio e categorias preferenciais.', '–'),
    ('doadores/{id}', 'Doadores.', '–'),
    ('rececoes/{id}', 'Cabeçalho da receção e subcoleção `linhas/{id}`.', 'Nome do doador e do responsável desnormalizados para o RGDHSA049.'),
    ('lotes/{id}', 'Lote com `produtoId`, `categoriaId`, `localId`, `validade`, `estado`, `qtdAtual`.', 'Nome do produto e código do local desnormalizados para listagens.'),
    ('movimentos/{id}', 'Registo imutável de movimentos.', 'Só escrita pelas Cloud Functions.'),
    ('desperdicios/{id}', 'Registos de desperdício.', 'Inclui `categoriaId` para agregações.'),
    ('alertas/{id}', 'Alertas gerados pela tarefa diária.', 'Id determinístico (tipo+lote+data) para idempotência.'),
    ('agregados/{id}', 'Agregado, subcoleções `pessoas/{id}` e `consentimentos/{id}`.', 'Acesso restrito a TEC e RESP; utente só ao seu.'),
    ('credenciais/{token}', 'Mapeia o token QR para a pessoa e o agregado.', 'Leitura apenas por Cloud Function.'),
    ('agendamentos/{id}', 'Agendamentos de cabazes e outros bens.', 'Lido pelo painel web (campos não sensíveis).'),
    ('entregas/{id}', 'Entrega com as linhas embebidas (`linhas`).', 'Linhas embebidas: são sempre lidas em conjunto.'),
    ('servicosRefeicao/{data_tipo}', 'Serviço do dia (ex.: `2026-10-22_ALMOCO`).', 'Id determinístico facilita a consulta.'),
    ('pedidosRefeicao/{id}', 'Pedidos por agregado e serviço.', '–'),
    ('levantamentos/{id}', 'Levantamentos de refeições.', '–'),
    ('saidasCozinha/{id}', 'Saídas para a cozinha com linhas embebidas.', '–'),
    ('parametros/geral', 'Parâmetros globais (hora limite dos pedidos, dias de distribuição).', 'Documento único.'),
    ('auditoria/{id}', 'Registo de operações sensíveis (acesso a dados de utentes, alterações).', 'Só escrita pelo servidor.'),
]

IDX = [
    ('lotes', 'produtoId ASC, estado ASC, congeladoInterno ASC, validade ASC', 'Seleção FEFO de um produto.'),
    ('lotes', 'estado ASC, validade ASC', 'Tarefa diária de validades e lista de expirados.'),
    ('lotes', 'localId ASC, estado ASC', 'Conteúdo de um local.'),
    ('rececoes', 'dataHora ASC', 'Emissão do RGDHSA049 por intervalo.'),
    ('agendamentos', 'dataHora ASC, estado ASC', 'Entregas do dia e painel web.'),
    ('pedidosRefeicao', 'servicoId ASC, estado ASC', 'Pedidos de um serviço.'),
    ('pedidosRefeicao', 'agregadoId ASC, data DESC', 'Histórico do agregado e App Utente.'),
    ('desperdicios', 'categoriaId ASC, data ASC', 'Relatório de desperdício.'),
]


def cap5(r, D):
    r.chapter('Modelo de Dados')
    r.para('Este capítulo apresenta o modelo de dados em três níveis: o modelo conceptual entidade-relacionamento, o dicionário de dados e o modelo físico em Cloud Firestore, uma base de dados NoSQL orientada a documentos.')

    r.h2('Modelo entidade-relacionamento')
    r.para('O modelo ER usa a notação de *crow\'s foot*. Para facilitar a leitura foi dividido em seis diagramas, um por área. As entidades marcadas com "(ref.)" estão definidas noutro diagrama e aparecem apenas com a chave primária. As chaves estão assinaladas como PK (primária), FK (estrangeira) e UQ (única); os atributos marcados com • são obrigatórios.')
    for img, cap, txt in [
        ('er_catalogo_armazem', 'Catálogo e armazém', 'As categorias agrupam produtos e têm no máximo uma regra de congelação. A associação muitos-para-muitos entre equipamentos e categorias (uso preferencial) é resolvida pela entidade EQUIPAMENTO_CATEGORIA. A entidade LOCAL generaliza células e zonas de frio.'),
        ('er_rececao', 'Receção', 'Cada receção tem uma ou mais linhas e pode não ter doador (anónima). Cada linha refere um produto e, opcionalmente, a apresentação usada, e origina zero ou mais lotes.'),
        ('er_stock', 'Stock', 'O lote é a entidade central do stock: refere o produto, a linha de origem e o local atual e tem associados os movimentos, os desperdícios e os alertas.'),
        ('er_agregados', 'Agregados e pessoas', 'Um agregado tem uma ou mais pessoas e um ou mais consentimentos. Cada pessoa pode ter credenciais QR (só uma ativa) e uma conta na App Utente.'),
        ('er_entregas', 'Entregas', 'Uma entrega pertence a um agregado, pode concretizar um agendamento e regista a pessoa que levantou e o colaborador que entregou. As linhas de saída ligam a entrega aos lotes abatidos.'),
        ('er_refeicoes', 'Refeições', 'Os pedidos ligam o agregado ao serviço de refeição. Os levantamentos registam a pessoa e podem existir sem pedido (exceções). As saídas para a cozinha reutilizam as linhas de saída.'),
    ]:
        n = r.next_fig()
        r.para(f'Figura {n} – {cap}. {txt}')
        r.figure(f'{D}/{img}.png', f'Modelo entidade-relacionamento – {cap}.', max_h=17)

    r.h2('Dicionário de dados')
    r.para('As tabelas seguintes descrevem os atributos das entidades. Na coluna "Obr." indica-se se o atributo é obrigatório (S), opcional (N) ou condicionalmente obrigatório (C). Atributos com a mesma natureza aparecem agrupados.')
    for ent, rows in DICT.items():
        r.table(['Atributo', 'Tipo', 'Obr.', 'Descrição'], [list(x) for x in rows],
                f'Dicionário de dados – {ent}.', widths=[3.2, 2.2, 0.8, 4.4])

    r.h2('Tipos enumerados')
    n = r.next_tab()
    r.para(f'A Tabela {n} lista os tipos enumerados usados no modelo. Em Kotlin são implementados como `enum class` e no Firestore são guardados como texto.')
    r.table(['Tipo', 'Valores'], [list(x) for x in ENUMS], 'Tipos enumerados.', widths=[3, 7], first_bold=True)

    r.h2('Modelo físico em Cloud Firestore')
    r.paras(
        'O Cloud Firestore organiza os dados em coleções de documentos JSON, sem junções nem chaves estrangeiras impostas pela base de dados (Google, 2026b). A passagem do modelo ER para o Firestore seguiu três critérios: (i) **embeber** as relações de composição que são sempre lidas em conjunto e têm cardinalidade limitada (apresentações no produto, linhas na entrega); (ii) usar **subcoleções** quando os filhos podem crescer ou ter acessos diferentes (linhas da receção, pessoas do agregado); e (iii) **desnormalizar** os campos necessários às listagens (nome do produto e código do local no lote), mantendo-os coerentes através das Cloud Functions.',
    )
    n = r.next_tab()
    r.para(f'A Tabela {n} apresenta as coleções propostas.')
    r.table(['Coleção / documento', 'Conteúdo', 'Notas'], [list(x) for x in FS],
            'Coleções do Cloud Firestore.', widths=[3, 4.2, 3.2])
    r.para('Exemplo de um documento da coleção `lotes`:')
    r.code('''
lotes/Lx8k2P {
  "produtoId": "p_arroz_agulha_1kg",   "produtoNome": "Arroz agulha 1 kg (Marca X)",
  "categoriaId": "c_massas_arroz",     "linhaRececaoId": "r_2026_0153/l_04",
  "localId": "loc_003_02_01",          "localCodigo": "003-02-01",
  "validade": "2026-12-02",           "validadeOriginal": "2026-12-02",
  "qtdInicial": 12, "qtdAtual": 10, "unidade": "UN", "volumes": null,
  "estado": "DISPONIVEL", "congeladoOrigem": false, "congeladoInterno": false,
  "dataEntrada": "2026-10-20T10:42:00Z"
}
''')
    n = r.next_tab()
    r.para(f'As consultas compostas exigem índices declarados no ficheiro `firestore.indexes.json`. A Tabela {n} lista os principais.')
    r.table(['Coleção', 'Campos do índice', 'Consulta suportada'], [list(x) for x in IDX],
            'Índices compostos do Firestore.', widths=[2.2, 4.6, 3.6])
