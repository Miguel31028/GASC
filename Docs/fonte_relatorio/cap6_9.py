def cap6(r, D):
    r.chapter('Arquitetura e Implementação Proposta')
    r.para('Este capítulo descreve as tecnologias escolhidas e as alternativas consideradas, a arquitetura do sistema e da aplicação, as medidas de segurança e de proteção de dados, o planeamento da implementação e os riscos do projeto.')

    r.h2('Tecnologias')
    n = r.next_tab()
    r.para(f'A instituição definiu como obrigatórios o Kotlin e o Firebase. A Tabela {n} detalha as tecnologias e a justificação de cada escolha.')
    r.table(['Tecnologia', 'Utilização', 'Justificação'], [
        ['Kotlin', 'Linguagem das aplicações Android.', 'Linguagem preferencial da Google para o desenvolvimento Android (Google, 2026e), concisa, com segurança de nulos e corrotinas para operações assíncronas (JetBrains, 2026).'],
        ['Jetpack Compose', 'Interface declarativa.', 'Biblioteca de interface recomendada para Android, com menos código e pré-visualização e testes da interface (Google, 2026f).'],
        ['Arquitetura MVVM + Hilt', 'Organização em camadas e injeção de dependências.', 'Separação de responsabilidades e testes da camada de domínio (Google, 2026d; Martin, 2017).'],
        ['Firebase Authentication', 'Autenticação de colaboradores (email) e utentes (telemóvel).', 'Integrado com as regras de segurança; suporta *custom claims* para perfis.'],
        ['Cloud Firestore', 'Base de dados principal.', 'Sincronização em tempo real, cache local, transações e regras de segurança declarativas (Google, 2026b).'],
        ['Cloud Functions (TypeScript)', 'Regras de negócio críticas, transações, geração de PDF, tarefas agendadas.', 'Executam no servidor, impedindo que um cliente adulterado contorne as regras de stock (ver secção 7.1.1).'],
        ['Cloud Storage', 'Imagens de guias e PDF gerados.', 'Armazenamento de ficheiros com regras de acesso.'],
        ['Cloud Messaging (FCM)', 'Notificações de alertas.', 'Notificações *push* por tópico (perfil).'],
        ['Firebase Hosting', 'Painel web da agenda.', 'Alojamento estático com HTTPS (*HyperText Transfer Protocol Secure*), no mesmo projeto.'],
        ['ML Kit Barcode Scanning', 'Leitura de QR de locais e credenciais.', 'Funciona no dispositivo, sem custos nem envio de imagens (Google, 2026c).'],
        ['Biblioteca PDF (ex.: pdfmake)', 'Geração do RGDHSA049.', 'Permite reproduzir a disposição do modelo em papel, em formato A4 horizontal.'],
        ['Firebase Emulator Suite, JUnit, Compose UI Test', 'Testes.', 'Testes locais das regras e funções sem afetar dados reais.'],
        ['GitHub e GitHub Actions', 'Controlo de versões, documentação (diagramas e *mockups*) e integração contínua (CI).', 'Histórico, revisão de código e execução automática dos testes.'],
    ], 'Tecnologias propostas.', widths=[2.6, 3.2, 4.4], first_bold=True)

    r.h3('Alternativas consideradas')
    n = r.next_tab()
    r.para(f'Dentro da restrição de usar Firebase, foram ponderadas as alternativas da Tabela {n}. O modelo de dados tem uma componente relacional e transacional (lotes, movimentos, entregas), pelo que a escolha da base de dados foi a decisão mais relevante.')
    r.table(['Decisão', 'Alternativas', 'Escolha e justificação'], [
        ['Base de dados', 'Realtime Database; Firebase Data Connect (PostgreSQL); Cloud Firestore', 'Cloud Firestore: transações multi-documento, consultas compostas com índices, cache e sincronização no Android e regras de segurança por documento. A Realtime Database tem consultas demasiado limitadas para o FEFO e os relatórios; o Data Connect daria integridade referencial nativa, mas acrescenta um serviço relacional pago e menos maduro no SDK Android. A integridade é garantida pelas Cloud Functions e pelas transações.'],
        ['Lógica de servidor', 'Lógica só no cliente com regras de segurança; Cloud Functions em TypeScript; Cloud Functions em Python', 'Cloud Functions em TypeScript: as regras de stock não podem depender do cliente (dispositivos pessoais); o Kotlin não é suportado nativamente pelas Cloud Functions e o TypeScript tem o SDK de administração mais completo. O requisito "Kotlin" aplica-se às aplicações móveis.'],
        ['Interface Android', 'Views XML; Jetpack Compose', 'Jetpack Compose: padrão atual, adequado aos componentes Material Design 3 usados nos *mockups*.'],
        ['Identificação de utentes', 'Cartão em papel com número; QR; biometria', 'QR em papel ou na App Utente no MVP: simples, sem dados pessoais no código e sem os requisitos legais da biometria (Capítulo 9).'],
    ], 'Alternativas tecnológicas consideradas.', widths=[2.2, 3.4, 4.6])

    r.h2('Arquitetura do sistema')
    n = r.next_fig()
    r.para(f'A Figura {n} apresenta a arquitetura lógica em três camadas: clientes, *backend* Firebase e serviços externos previstos para a evolução futura. Os clientes comunicam com o *backend* através dos SDK do Firebase, sobre HTTPS.')
    r.figure(f'{D}/arq_componentes.png', 'Arquitetura lógica do sistema.', max_h=10)
    r.para('As leituras são feitas diretamente no Firestore, com subscrições em tempo real filtradas pelas regras de segurança. As escritas que afetam o stock ou que envolvem várias entidades (receção, arrumação, marcação de local cheio, congelação, entrega, saída para a cozinha, desperdício, pedido e levantamento de refeições) são feitas através de Cloud Functions do tipo *callable*, que validam o perfil do utilizador, aplicam as regras de negócio e executam a operação numa transação. A resolução das credenciais QR é também feita por uma função (`identificarPessoa`), que devolve apenas os dados necessários à entrega e regista o acesso. As tarefas agendadas (validades e fecho do dia) e a projeção do painel web são executadas por funções acionadas pelo Cloud Scheduler ou por eventos do Firestore (*triggers*). As escritas simples de dados mestre (por exemplo, editar um agregado) podem ser feitas diretamente pelo cliente, protegidas pelas regras de segurança.')
    n = r.next_fig()
    r.para(f'A Figura {n} mostra a implantação física. Inclui o posto biométrico previsto como melhoria futura, num computador fixo.')
    r.figure(f'{D}/arq_implantacao.png', 'Diagrama de implantação.', max_h=8)

    r.h2('Arquitetura da aplicação Android')
    n = r.next_fig()
    r.para(f'As aplicações Android seguem a arquitetura recomendada pela Google (Google, 2026d), com as camadas de apresentação, domínio e dados (Figura {n}). Os ecrãs Compose observam o estado exposto pelos *ViewModels* (StateFlow). Os casos de uso encapsulam as regras de negócio que também correm no cliente, como a conversão de unidades ou a pré-visualização FEFO. Os repositórios abstraem o acesso ao Firebase.')
    r.figure(f'{D}/arq_camadas.png', 'Camadas da aplicação Android.', max_h=9)
    r.para('A organização proposta para os pacotes do projeto é a seguinte:')
    r.code(''+"""
pt.gasc.gestao
 ├─ ui/            rececao, arrumacao, stock, utentes, entregas, refeicoes, relatorios, admin
 ├─ domain/
 │   ├─ model/     Lote, Produto, Local, Agregado, Pessoa, PedidoRefeicao, ...
 │   ├─ usecase/   RegistarRececaoUseCase, SugerirLocalUseCase, SelecionarFefoUseCase, ...
 │   └─ rules/     ConversaoUnidades, Fefo, RegraCongelacao
 ├─ data/
 │   ├─ remote/    FirestoreDataSource, FunctionsDataSource, StorageDataSource
 │   ├─ dto/       documentos Firestore e mapeadores
 │   └─ repository/
 └─ di/            módulos Hilt
""")

    r.h2('Segurança e proteção de dados')
    r.para('O sistema trata dados pessoais de pessoas em situação de vulnerabilidade, incluindo dados relativos à saúde (alergias e restrições alimentares), que são uma categoria especial de dados pessoais. A segurança e a conformidade com o RGPD (Parlamento Europeu e Conselho, 2016) são, por isso, requisitos estruturais.')
    r.h3('Base legal e avaliação de impacto')
    r.paras(
        'A base de licitude de cada tratamento deve ser fixada pela instituição com o seu encarregado de proteção de dados. Para os dados de identificação e de contacto necessários à prestação do apoio social, a base mais adequada é, em princípio, o exercício de funções de interesse público ou o cumprimento de obrigações decorrentes dos acordos de cooperação (artigo 6.º, n.º 1, alíneas c) e e), do RGPD), e não o consentimento: dada a dependência das pessoas apoiadas face à instituição, um consentimento como condição do apoio dificilmente seria livre. Para os dados de saúde, propõe-se o consentimento explícito (artigo 9.º, n.º 2, alínea a)), recolhido separadamente e apenas para a finalidade de adequar os bens entregues; a recusa não impede o apoio.',
        'O NIF e o NISS são opcionais (RF-UTE-02) e só devem ser recolhidos quando exigidos pelos programas de apoio a que a instituição reporta, em cumprimento do princípio da minimização. Atendendo à vulnerabilidade dos titulares, ao tratamento de dados de saúde e à sistematicidade do registo, recomenda-se a realização de uma avaliação de impacto sobre a proteção de dados (AIPD), nos termos do artigo 35.º do RGPD, antes da entrada em produção do MVP, e não apenas no caso da biometria.',
    )
    r.h3('Medidas técnicas e organizativas')
    r.bullets([
        '**Autorização no servidor:** os perfis são atribuídos como *custom claims* no *token* do Firebase Authentication e verificados pelas *Security Rules* e pelas Cloud Functions. A interface limita-se a esconder o que o perfil não pode fazer.',
        f'**Princípio do menor privilégio:** cada perfil acede apenas às coleções de que necessita (matriz de permissões da Tabela {r.tab_no("Matriz de permissões")}); o Operador e a Cozinha recebem apenas os dados necessários à entrega; o utente acede apenas aos dados do seu agregado.',
        '**Credenciais QR sem dados pessoais:** o QR contém um *token* aleatório que só é resolvido por uma Cloud Function, que regista o acesso.',
        '**Minimização e finalidade:** só são recolhidos os dados necessários; a base legal, o consentimento e as finalidades ficam registados por agregado.',
        '**Direitos dos titulares:** funções de exportação (acesso e portabilidade) e de anonimização (apagamento) que preservam as estatísticas agregadas.',
        '**Localização dos dados:** projeto Firebase numa região da União Europeia.',
        '**Auditoria:** registo das operações sensíveis e dos acessos a fichas de utentes.',
        '**Painel público:** projeção própria (`painelAgenda`) apenas com códigos de agregado.',
        '**Dispositivos próprios:** sem armazenamento de dados sensíveis fora da cache do SDK; fim de sessão remoto ao desativar o utilizador; recomendação de bloqueio de ecrã.',
    ])
    r.para('Extrato ilustrativo das regras de segurança do Firestore:')
    r.code(''+"""
rules_version = '2';
service cloud.firestore {
  match /databases/{db}/documents {
    function perfil(p) { return request.auth != null && request.auth.token[p] == true; }
    function doAgregado() { return request.auth.token.agregadoId == resource.data.agregadoId; }

    match /lotes/{id} {
      allow read: if perfil('OPERADOR') || perfil('RESPONSAVEL') || perfil('COZINHA');
      allow write: if false;            // apenas Cloud Functions (Admin SDK)
    }
    match /agregados/{id} {
      allow read, write: if perfil('TECNICO') || perfil('RESPONSAVEL');
      allow read: if request.auth.token.agregadoId == id;   // utente: só o seu
      match /pessoas/{p} {
        allow read, write: if perfil('TECNICO') || perfil('RESPONSAVEL');
      }
    }
    match /pedidosRefeicao/{id} {
      allow read: if perfil('TECNICO') || perfil('RESPONSAVEL') || perfil('COZINHA') || doAgregado();
      allow write: if false;            // apenas registarPedido / registarLevantamento
    }
    match /agendamentos/{id} {
      allow read: if perfil('OPERADOR') || perfil('TECNICO') || perfil('RESPONSAVEL') || doAgregado();
    }
    match /credenciais/{token} { allow read, write: if false; }
  }
}
""")

    r.h2('Planeamento')
    n = r.next_tab()
    r.para(f'A implementação segue um processo iterativo, com iterações de duas a três semanas (20 semanas no total) e validação com a instituição no fim de cada uma. A Tabela {n} apresenta a sequência proposta; as durações são estimativas.')
    r.table(['Iteração', 'Âmbito', 'Duração', 'Entregável'], [
        ['0', 'Aceitação formal dos requisitos e dos protótipos; AIPD; configuração do projeto Firebase, repositório, CI, autenticação, perfis e parâmetros gerais.', '2 sem.', 'Aplicação com autenticação e perfis.'],
        ['1', 'Catálogo, categorias, tabela de congelação, células e equipamentos de frio, etiquetas QR.', '2 sem.', 'Configuração do armazém.'],
        ['2', 'Receção com controlo RGDHSA049, doadores, conversão de unidades e criação de lotes.', '2 sem.', 'Registo de receções.'],
        ['3', 'Arrumação com sugestão de local, consulta de stock, transferências e ajustes.', '2 sem.', 'Armazém operacional.'],
        ['4', 'FEFO, congelação, tarefas agendadas, desperdício e alertas.', '2 sem.', 'Controlo de validades.'],
        ['5', 'Agregados, pessoas, consentimentos, credenciais QR, agendamentos e entregas.', '3 sem.', 'Distribuição de cabazes.'],
        ['6', 'Refeições: serviços, pedidos, saídas para a cozinha, levantamentos, fecho do serviço.', '2 sem.', 'Gestão de refeições.'],
        ['7', 'RGDHSA049 em PDF, histórico, indicadores, exportações, painel web.', '2 sem.', 'Relatórios.'],
        ['8', 'App Utente; testes de aceitação e de usabilidade; correções; formação.', '3 sem.', 'Versão 1.0 (MVP).'],
    ], 'Plano de iterações.', widths=[1.1, 5.4, 1.2, 2.4])

    r.h2('Riscos')
    n = r.next_tab()
    r.para(f'A Tabela {n} identifica os principais riscos do projeto, avaliados qualitativamente quanto à probabilidade e ao impacto, e as medidas de mitigação previstas.')
    r.table(['ID', 'Risco', 'Prob.', 'Impacto', 'Mitigação'], [
        ['R01', 'Baixa adesão dos colaboradores e voluntários (literacia digital variável).', 'Média', 'Alto', 'Interface simples e orientada à tarefa, validação dos protótipos, formação curta e período em paralelo com o papel.'],
        ['R02', 'Má qualidade dos dados do catálogo (produtos duplicados), que começa vazio.', 'Alta', 'Médio', 'Sugestão de produtos semelhantes na criação (RF-CAT-07), revisão periódica pelo Responsável.'],
        ['R03', 'Incidente de segurança com dados pessoais de utentes.', 'Baixa', 'Alto', 'Autorização no servidor, menor privilégio, auditoria, dados na UE, avaliação de impacto antes da biometria.'],
        ['R04', 'Perda ou roubo de um dispositivo pessoal com sessão ativa.', 'Média', 'Médio', 'Desativação remota do utilizador, ausência de dados sensíveis fora da cache, bloqueio de ecrã recomendado.'],
        ['R05', 'Dependência do Firebase (custos e dependência do fornecedor).', 'Baixa', 'Médio', 'Alertas de orçamento, camada de repositórios que isola o acesso a dados, exportações regulares.'],
        ['R06', 'Alargamento do âmbito durante o desenvolvimento.', 'Alta', 'Médio', 'Priorização MoSCoW, iterações curtas com validação e registo das novas ideias como trabalho futuro.'],
        ['R07', 'Etiquetas QR danificadas ou ilegíveis nas arcas e prateleiras.', 'Média', 'Baixo', 'Etiquetas plastificadas, reimpressão a partir da aplicação e seleção manual do local como alternativa.'],
        ['R08', 'Divergência entre o stock registado e o físico.', 'Média', 'Médio', 'Confirmação por QR, transações atómicas, ajustes de inventário justificados e contagens periódicas.'],
    ], 'Riscos do projeto e medidas de mitigação.', widths=[0.8, 3.4, 1.0, 1.1, 4.0])


TESTES = [
    ('TA-01', 'Receção da empresa Pingo Doce sem n.º de guia.', 'O sistema não permite confirmar e pede o n.º da guia.', 'RF-REC-03; RN-11'),
    ('TA-02', 'Receção de particular anónimo com 2 linhas.', 'Receção gravada sem doador e marcada como anónima.', 'RF-REC-02'),
    ('TA-03', 'Receção de 1 palete de leite 35 cl (30 UN).', 'Lote criado com 30 UN.', 'RF-REC-06; RN-02'),
    ('TA-04', 'Na mesma receção, 10 pacotes de arroz da mesma marca e validade e 5 de outra validade.', 'Dois lotes: 10 UN e 5 UN.', 'RF-REC-07; RN-01'),
    ('TA-05', 'Saída de 10 kg de um saco de batatas de 50 kg.', 'Stock: 1 UN com 40 kg.', 'RF-STK-07; RN-02'),
    ('TA-06', 'Arrumação de arroz com uma célula com arroz disponível.', 'É sugerida a célula que já contém arroz.', 'RF-ARM-04; RN-06'),
    ('TA-07', 'Operador assinala a célula 003-02-01 como cheia.', 'É sugerida a célula seguinte mais próxima (003-02-02).', 'RF-ARM-05'),
    ('TA-08', 'Arrumação de frango inteiro congelado na origem.', 'É sugerida primeiro uma zona da arca 1 (uso preferencial para aves).', 'RF-ARM-04; RN-05; RN-06'),
    ('TA-09', 'Cabaz com dois lotes de iogurte (validades 24/10 e 30/10).', 'O lote de 24/10 é sugerido primeiro.', 'RF-ENT-06; RN-07'),
    ('TA-10', 'Congelar coxas de frango (Carne de aves, +90 dias).', 'Nova validade proposta = hoje + 90; validade original preservada.', 'RF-STK-03; RN-08'),
    ('TA-11', 'Tentar congelar um lote de iogurtes (categoria não congelável).', 'Operação indisponível.', 'RN-08'),
    ('TA-12', 'Tarefa diária com um lote de validade de ontem.', 'Lote EXPIRADO na lista de remoção, sem poder sair para cabaz.', 'RF-STK-04; RN-09'),
    ('TA-13', 'Pessoa apresenta uma credencial QR revogada (deixou de estar autorizada).', 'Levantamento recusado, sem possibilidade de exceção.', 'RF-ENT-04; RN-13; RN-17'),
    ('TA-14', 'Pedido de 2 refeições de seg. a qui. e 3 à sex. numa semana.', 'Cinco pedidos com as quantidades corretas.', 'RF-REF-03'),
    ('TA-15', 'Pedido de jantar num dia sem serviço de jantar.', 'Pedido recusado.', 'RN-15'),
    ('TA-16', 'Emissão do RGDHSA049 de 1 a 15 de outubro.', 'PDF com todas as receções do intervalo e colunas preenchidas.', 'RF-REL-01; RN-12'),
    ('TA-17', 'Operador tenta abrir a ficha de um agregado.', 'Acesso negado pelas regras de segurança.', 'RNF-06'),
    ('TA-18', 'Entrega com stock entretanto insuficiente num lote.', 'Transação recusada; stock inalterado; aviso ao operador.', 'RF-ENT-07; RN-18'),
    ('TA-19', 'Utilizador desativado tenta autenticar-se.', 'Autenticação recusada e sessões ativas terminadas.', 'RF-UTZ-01; RF-UTZ-02'),
    ('TA-20', 'Utente consulta a App Utente.', 'Vê apenas a credencial, entregas e pedidos do próprio agregado.', 'RF-APU-02; RF-APU-03; RNF-07'),
    ('TA-21', 'Utente altera um pedido depois da hora limite.', 'Alteração recusada pelo servidor.', 'RF-APU-04; RF-REF-04; RN-14'),
    ('TA-22', 'Correção de uma receção cujos lotes já tiveram saídas.', 'Correção bloqueada; correção permitida numa receção sem saídas, com registo de auditoria.', 'RF-REC-09; RF-UTZ-05'),
    ('TA-23', 'Pedido de apagamento dos dados de um agregado.', 'Dados pessoais anonimizados; totais de entregas e refeições preservados.', 'RNF-07'),
    ('TA-24', 'Fim do dia com um agendamento não concretizado e pedidos não levantados.', 'Agendamento FALTOU; pedidos NAO_LEVANTADO; serviço fechado.', 'RF-ENT-09; RF-REF-10'),
]


def cap7(r, D):
    r.chapter('Plano de Testes e Validação')
    r.para('A validação do sistema combina testes automáticos, executados em cada alteração, com testes de aceitação e de usabilidade realizados com os colaboradores da instituição.')

    r.h2('Estratégia de testes')
    n = r.next_tab()
    r.para(f'A Tabela {n} resume os níveis de teste, o objeto de cada nível, as ferramentas e o critério de sucesso.')
    r.table(['Nível', 'Objeto', 'Ferramentas', 'Critério'], [
        ['Unitário', 'Regras de domínio (FEFO, conversão de unidades, sugestão de local, congelação, periodicidade).', 'JUnit, MockK', 'Cobertura ≥ 60% no domínio; todas as regras de negócio com testes.'],
        ['Integração', 'Cloud Functions e *Security Rules*.', 'Firebase Emulator Suite, Jest', 'Cada perfil só consegue o que a matriz de permissões define.'],
        ['Interface', 'Fluxos principais em Compose.', 'Compose UI Test', 'UC01, UC02, UC06 e UC09 sem erros.'],
        ['Aceitação', 'Cenários reais com dados de teste.', 'Guião de testes de aceitação (TA)', 'Todos os casos TA aprovados pela instituição.'],
        ['Usabilidade', 'Operadores, técnicos e cozinha.', 'Observação e questionário *System Usability Scale* (SUS) (Brooke, 1996)', 'Pontuação SUS ≥ 70, limiar de aceitabilidade proposto por Bangor et al. (2008).'],
    ], 'Níveis de teste.', widths=[1.6, 3.4, 2.6, 2.8], first_bold=True)

    r.h2('Casos de teste de aceitação')
    n = r.next_tab()
    r.para(f'A Tabela {n} lista os casos de teste de aceitação (TA), construídos a partir das regras de negócio e dos exemplos fornecidos pela instituição. A matriz do Anexo C relaciona-os com os requisitos.')
    r.table(['ID', 'Cenário', 'Resultado esperado', 'Req.'], [list(t) for t in TESTES], 'Casos de teste de aceitação.', widths=[1.1, 3.9, 3.8, 1.6])

    r.h2('Critérios de aceitação do MVP')
    r.bullets([
        'Todos os requisitos *Must* e, pelo menos, 80% dos requisitos *Should* do MVP implementados.',
        'Todos os casos de teste de aceitação (TA-01 a TA-24) aprovados pela instituição.',
        'Uma semana de utilização em paralelo com o processo em papel, sem divergências de stock superiores a 2%.',
        'Pontuação média SUS igual ou superior a 70 e tempo de registo de uma receção de 5 linhas igual ou inferior a 5 minutos.',
        'RGDHSA049 gerado pelo sistema aceite pela equipa HACCP.',
        'Regras de segurança validadas no emulador para todos os perfis e AIPD concluída.',
    ])


FUTURO = [
    ('F01', 'RF-REC-11', 'Reconhecimento de produtos por imagem', 'Fotografar o produto e identificar automaticamente o produto do catálogo, para dar entrada e saída.', 'Exige um catálogo estabilizado e testes de fiabilidade; o erro de classificação tem impacto direto no stock.', 'LLM multimodal ou modelo próprio treinado com imagens do catálogo; confirmação sempre pelo operador.'),
    ('F02', 'RF-REC-12', 'Leitura da validade por imagem', 'Ler a data de validade impressa na embalagem.', 'Os formatos de data são muito variados; requer validação.', 'ML Kit Text Recognition no dispositivo, com heurísticas de datas e confirmação.'),
    ('F03', 'RF-REC-10', 'Extração automática das guias', 'Ler a guia digitalizada e propor as linhas da receção (descrição, quantidade, unidade).', 'As guias são digitalizações de qualidade variável; é necessário associar descrições do fornecedor a produtos.', 'OCR + LLM com saída estruturada; tabela de correspondência código do fornecedor → produto.'),
    ('F04', 'RF-UTE-10', 'Identificação biométrica facial', 'Identificar o utente pelo rosto num posto fixo.', 'Os dados biométricos são uma categoria especial (artigo 9.º do RGPD): exigem consentimento explícito, AIPD e alternativa não biométrica.', 'Aplicação para computador pessoal (PC) num local fixo, com reconhecimento facial local; o QR mantém-se como alternativa.'),
    ('F05', 'RF-ENT-11', 'Cabaz automático equilibrado', 'Propor cabazes com proteína, hidratos de carbono, etc., segundo regras do Responsável e a dimensão do agregado.', 'Requer informação nutricional por categoria e a definição das regras pela instituição.', 'Heurística de otimização (*knapsack* multiobjetivo) sobre os lotes FEFO, respeitando alergias.'),
    ('F06', 'RF-REF-11', 'Sugestão de pratos', 'Propor pratos a confecionar com base no stock e nas validades.', 'Depende de uma base de receitas e da validação da cozinha.', 'LLM com o stock FEFO como contexto e restrições de quantidade; ou base de receitas própria.'),
    ('F07', 'RF-ARM-09', 'Mapa do armazém', 'Representar graficamente o armazém e usar distâncias reais nas sugestões.', 'Ainda não existe mapa das prateleiras.', 'Editor de planta e coordenadas por coluna; algoritmo de proximidade por distância.'),
    ('F08', 'RF-REL-09', 'Painéis analíticos avançados', 'Indicadores históricos e comparativos na web.', 'O MVP inclui apenas indicadores básicos.', 'Exportação para BigQuery e Looker Studio, ou página web própria.'),
    ('F09', 'RF-CAT-08', 'Códigos de barras EAN', 'Associar o EAN ao produto e pesquisar por leitura.', 'Ganho elevado, mas não essencial para o MVP.', 'ML Kit Barcode (já usado para o QR).'),
    ('F10', 'RF-APU-05', 'Avisos na App Utente', 'Comunicações da instituição aos utentes.', 'Requer definição editorial e de consentimento.', 'FCM por tópico de agregado.'),
    ('F11', '–', 'Valorização em euros', 'Valorizar doações e desperdício em euros (relatórios, mecenato).', 'Para já só se contabilizam quantidades.', 'Preço de referência por produto ou o valor da guia.'),
    ('F12', '–', 'Sensores de temperatura', 'Monitorizar a temperatura das arcas (HACCP).', 'Exige equipamento físico.', 'Sensores da Internet das Coisas (IoT) com envio periódico e alertas.'),
    ('F13', '–', 'Integração com outras entidades', 'Exportar dados para programas de apoio alimentar e para a Câmara Municipal.', 'Formatos ainda por definir.', 'Exportações normalizadas (CSV ou API) no âmbito do Barcelos Solidário.'),
    ('F14', '–', 'Previsão de refeições', 'Prever a procura diária com base no histórico.', 'Requer histórico de vários meses.', 'Modelos simples de séries temporais.'),
    ('F15', '–', 'Gestão de voluntários', 'Escalas e turnos de voluntários no armazém.', 'Fora do âmbito inicial.', 'Novo módulo sobre os perfis existentes.'),
]


def cap8(r, D):
    r.chapter('Trabalho Futuro')
    r.para('De acordo com a decisão acordada com o Responsável da instituição durante o levantamento de requisitos (outubro de 2026), de concentrar a primeira versão no essencial, as funcionalidades seguintes ficam registadas como intenção futura de melhoria. Para cada uma indica-se o requisito correspondente, a razão de não integrar o MVP e a abordagem prevista. As melhorias F01 a F10 correspondem a requisitos *Could* e *Won\'t (agora)* do Capítulo 3; as melhorias F11 a F15 resultam da análise do autor e não constavam do pedido inicial. O modelo de dados e a arquitetura (camada de serviços externos, campos como `codigo_barras`, `url_guia` ou `tipo_data_validade`) já preparam a sua introdução sem alterações estruturais.')
    n = r.next_tab()
    r.para(f'A Tabela {n} resume as melhorias identificadas.')
    r.table(['ID', 'RF', 'Melhoria', 'Descrição', 'Razão para adiar', 'Abordagem prevista'],
            [list(x) for x in FUTURO], 'Melhorias futuras.', widths=[0.7, 1.3, 1.7, 2.3, 2.3, 2.3], size=7.5)

    r.h2('Inteligência artificial na receção')
    r.para('As melhorias F01 a F03 têm o mesmo objetivo: reduzir o tempo de registo na receção. A abordagem recomendada é incremental. Começa-se pela leitura de códigos de barras (F09), que é determinística. Segue-se a extração das guias (F03), já que as guias das grandes superfícies têm estrutura tabular regular (código, descrição, quantidade, unidade), como mostram os exemplos do Anexo B. Por fim, o reconhecimento por imagem (F01 e F02). Em todos os casos o sistema **propõe** e o operador **confirma**, para que um erro do modelo não chegue ao stock.')

    r.h2('Identificação biométrica')
    r.para('A identificação facial (F04) foi admitida pela instituição apenas se não for muito complexa e preferencialmente como sistema à parte, num PC em local fixo. Para além da complexidade técnica, os dados biométricos para identificação inequívoca são uma categoria especial de dados pessoais (artigo 9.º do RGPD). A sua utilização exige consentimento explícito, uma AIPD específica e a garantia de uma alternativa (o QR) para quem não consinta. Recomenda-se que esta funcionalidade seja reavaliada depois de o MVP estar em produção.')

    r.h2('Cabaz automático e sugestão de pratos')
    r.para('O cabaz automático (F05) pode ser formulado como um problema de otimização: escolher lotes que satisfaçam metas por grupo alimentar (proteína, hidratos de carbono, leguminosas, laticínios, fruta e legumes), definidas pelo Responsável em função da dimensão do agregado, minimizando a validade média dos lotes escolhidos e respeitando alergias e restrições. A sugestão de pratos (F06) pode usar um LLM a que se forneça o stock prioritário (FEFO) e o número de refeições, pedindo propostas de pratos com quantidades que a cozinha valida.')


def cap9(r, D):
    from cap3 import RF, RNF, RN
    N_RF = sum(len(v) for v in RF.values())
    r.chapter('Conclusão')
    r.paras(
        f'Este documento apresentou a análise e modelação de um sistema de informação para a gestão do Espaço Social do GASC, no âmbito do projeto Barcelos Solidário. Partindo da descrição do problema e de três rondas de clarificação com a instituição, foram documentados os atores e as permissões, {N_RF} requisitos funcionais organizados por módulo e priorizados, {len(RNF)} requisitos não funcionais e {len(RN)} regras de negócio. Estas regras traduzem a realidade do armazém: lotes definidos por produto, marca e validade; unidades múltiplas e produtos a granel; codificação de células e zonas de frio; FEFO com preferência por produtos não congelados; e controlo das pessoas autorizadas a levantar.',
        'A modelação UML, dividida por áreas para preservar a legibilidade, cobre os casos de uso, os processos (atividades), a estrutura (classes), o ciclo de vida das entidades principais (estados) e a colaboração entre componentes (sequências). O modelo entidade-relacionamento e o dicionário de dados foram traduzidos para um modelo físico em Cloud Firestore, com critérios explícitos de incorporação, subcoleções e desnormalização. Os 42 protótipos de alta fidelidade do Capítulo 6 completam a especificação, descrevendo ecrã a ecrã o comportamento esperado, e a matriz do Anexo C garante que todos os requisitos do MVP têm concretização na interface.',
        'A arquitetura proposta, em Kotlin com Firebase, concentra as operações críticas em Cloud Functions transacionais e aplica a segurança no servidor. Esta opção é especialmente importante porque os colaboradores usam os seus próprios dispositivos e porque estão em causa dados pessoais sensíveis, cujo tratamento deve ser precedido de uma AIPD.',
        'A separação entre MVP e trabalho futuro torna o projeto exequível sem perder a visão completa. As funcionalidades de maior complexidade, como o reconhecimento de produtos e validades por imagem, a leitura automática de guias, a biometria, o cabaz automático e a sugestão de pratos, ficaram documentadas com a justificação e a abordagem prevista, e o modelo de dados já as acomoda.',
        'O trabalho tem limitações que importa reconhecer. O levantamento assentou num único interlocutor, o Responsável da instituição, e em respostas escritas, sem observação direta das operações no armazém e na cozinha. Os protótipos ainda não foram validados com os utilizadores finais. As durações do plano são estimativas e os indicadores do projeto não têm ainda valores de referência medidos. Por fim, a proximidade entre locais é aproximada pela ordenação dos códigos, enquanto não existir o mapa do armazém.',
        'Como próximos passos, recomenda-se: validar os protótipos com os colaboradores e obter a aceitação formal dos requisitos; realizar a AIPD; confirmar com a equipa HACCP o tratamento dos tipos de data de validade e a disposição do RGDHSA049 gerado; recolher a tabela de congelação por categoria; e iniciar a implementação pela iteração 0 do plano proposto.',
    )


BIB = [
    'Bangor, A., Kortum, P. T., & Miller, J. T. (2008). An empirical evaluation of the System Usability Scale. *International Journal of Human–Computer Interaction, 24*(6), 574–594. https://doi.org/10.1080/10447310802205776',
    'Brooke, J. (1996). SUS: A "quick and dirty" usability scale. Em P. W. Jordan, B. Thomas, B. A. Weerdmeester & I. L. McClelland (Eds.), *Usability Evaluation in Industry* (pp. 189–194). Taylor & Francis.',
    'Cedar Mountain Software. (2026). *PantrySoft: Food pantry software*. Consultado a 22 de outubro de 2026, em https://www.pantrysoft.com',
    'Chen, P. P. (1976). The entity-relationship model – toward a unified view of data. *ACM Transactions on Database Systems, 1*(1), 9–36. https://doi.org/10.1145/320434.320440',
    'Clegg, D., & Barker, R. (1994). *Case Method Fast-Track: A RAD Approach*. Addison-Wesley.',
    'Cockburn, A. (2000). *Writing Effective Use Cases*. Addison-Wesley.',
    'GASC. (2026). *Relatório de análise organizacional – GASC, Grupo de Ação Social Cristã, Barcelos* [Documento interno].',
    'GASC, Câmara Municipal de Barcelos, & IPCA. (2026). *Barcelos Solidário – Desenvolvimento de uma plataforma de âmbito social para os cidadãos de Barcelos* [Apresentação].',
    'Google. (2026a). *Firebase documentation*. https://firebase.google.com/docs',
    'Google. (2026b). *Cloud Firestore – Data model*. https://firebase.google.com/docs/firestore/data-model',
    'Google. (2026c). *ML Kit – Barcode scanning*. https://developers.google.com/ml-kit/vision/barcode-scanning',
    'Google. (2026d). *Guide to app architecture*. Android Developers. https://developer.android.com/topic/architecture',
    'Google. (2026e). *Android\'s Kotlin-first approach*. Android Developers. https://developer.android.com/kotlin/first',
    'Google. (2026f). *Jetpack Compose*. Android Developers. https://developer.android.com/compose',
    'Gustavsson, J., Cederberg, C., Sonesson, U., van Otterdijk, R., & Meybeck, A. (2011). *Global food losses and food waste – Extent, causes and prevention*. Food and Agriculture Organization of the United Nations (FAO).',
    'ISO/IEC. (2023). *ISO/IEC 25010:2023 – Systems and software engineering – Systems and software Quality Requirements and Evaluation (SQuaRE) – Product quality model*. International Organization for Standardization.',
    'JetBrains. (2026). *Kotlin documentation*. https://kotlinlang.org/docs',
    'Larman, C. (2004). *Applying UML and Patterns* (3.ª ed.). Prentice Hall.',
    'Link2Feed. (2026). *Link2Feed: Client intake and management for food banks*. Consultado a 22 de outubro de 2026, em https://link2feed.ca',
    'Martin, R. C. (2017). *Clean Architecture: A Craftsman\'s Guide to Software Structure and Design*. Prentice Hall.',
    'Object Management Group. (2017). *OMG Unified Modeling Language (OMG UML), Version 2.5.1*. https://www.omg.org/spec/UML/2.5.1',
    'Parlamento Europeu e Conselho. (2004). Regulamento (CE) n.º 852/2004, relativo à higiene dos géneros alimentícios. *Jornal Oficial da União Europeia*, L 139.',
    'Parlamento Europeu e Conselho. (2011). Regulamento (UE) n.º 1169/2011, relativo à prestação de informação aos consumidores sobre os géneros alimentícios. *Jornal Oficial da União Europeia*, L 304.',
    'Parlamento Europeu e Conselho. (2016). Regulamento (UE) 2016/679, relativo à proteção das pessoas singulares no que diz respeito ao tratamento de dados pessoais (Regulamento Geral sobre a Proteção de Dados). *Jornal Oficial da União Europeia*, L 119.',
    'PlantUML. (2026). *PlantUML language reference guide*. https://plantuml.com',
    'Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner\'s Approach* (9.ª ed.). McGraw-Hill.',
    'Sommerville, I. (2016). *Software Engineering* (10.ª ed.). Pearson.',
    'Wiegers, K., & Beatty, J. (2013). *Software Requirements* (3.ª ed.). Microsoft Press.',
]


def bibliografia(r):
    r.empty(4)
    r.unnumbered_title('Bibliografia', toc=True)
    for b in BIB:
        p = r.doc.add_paragraph(style='Bibliography')
        from docx.shared import Cm
        p.paragraph_format.first_line_indent = Cm(-0.75)
        p.paragraph_format.left_indent = Cm(0.75)
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r.add_runs(p, b)
        for run in p.runs:
            run.font.name = 'Arial'
            run.font.size = __import__('docx').shared.Pt(11)


def anexos(r, D, UCS, RF):
    r.empty(10)
    r.unnumbered_title('ANEXOS', toc=True)
    r._section_break(r.sect[11])

    r.empty(1)
    r.unnumbered_title('Anexo A – Mapeamento do registo RGDHSA049', toc=True)
    r.para(f'O documento RGDHSA049 – *Monitorização do Controlo da Receção de Matérias-Primas* (Edição 1, Revisão 0, 12/2020) é um registo mensal com uma linha por produto recebido. A Tabela {r.next_tab()} indica a origem de cada coluna nos dados do sistema, o que permite gerá-lo automaticamente para qualquer intervalo de datas.')
    r.table(['Coluna do RGDHSA049', 'Origem no sistema'], [
        ['Mês/Ano', 'Intervalo pedido (cabeçalho; vários meses geram várias folhas).'],
        ['Dia', 'RECECAO.data_hora (dia).'],
        ['Produto / Fornecedor', 'PRODUTO.nome + marca / DOADOR.nome (ou "Particular anónimo").'],
        ['Documento de receção – Lote / N.º guia de remessa', 'LINHA_RECECAO.lote_fornecedor ou RECECAO.n_guia.'],
        ['Quantidade', 'LINHA_RECECAO.quantidade + apresentação (ex.: 1 palete / 30 UN).'],
        ['Condições de higiene (C / NC)', 'LINHA_RECECAO.higiene_c.'],
        ['Rotulagem / Data de validade (C / NC)', 'LINHA_RECECAO.rotulagem_c (e a validade registada).'],
        ['Características organoléticas (C / NC)', 'LINHA_RECECAO.organoleticas_c.'],
        ['Embalagem íntegra (C / NC)', 'LINHA_RECECAO.embalagem_c.'],
        ['Temperatura', 'LINHA_RECECAO.temperatura ou RECECAO.temperatura.'],
        ['Responsável (rubrica)', 'UTILIZADOR.nome de quem registou a receção.'],
        ['Observações', 'LINHA_RECECAO.observacoes (motivos de não conformidade, rejeição).'],
    ], 'Correspondência entre as colunas do RGDHSA049 e os dados do sistema.', widths=[4, 6])

    r.page_break()
    r.unnumbered_title('Anexo B – Exemplos de documentos de entrada', toc=True)
    r.para(f'A instituição forneceu exemplos de guias de transporte de cadeias de distribuição (Pingo Doce e Recheio) e de um resumo de doações diárias. São documentos tabulares com, entre outros, o código do artigo do fornecedor, a descrição, a quantidade e a unidade (UN ou KG), e no cabeçalho o número da guia, a data e o NIF do fornecedor. A Tabela {r.next_tab()} mostra a correspondência com os dados do sistema; esta estrutura regular fundamenta a melhoria futura F03.')
    r.table(['Campo da guia', 'Exemplo', 'Campo do sistema'], [
        ['Fornecedor / loja', 'Pingo Doce – Barcelos Alcaides de Faria', 'DOADOR (tipo EMPRESA).'],
        ['N.º da guia / Refª', 'DPM1/4101774379', 'RECECAO.n_guia.'],
        ['Data do documento', '23.03.2026', 'RECECAO.data_hora (referência).'],
        ['Artigo (código)', '0000262753', 'Correspondência futura código → PRODUTO.'],
        ['Descrição', 'ALFACE FRISADA EMB. PD', 'PRODUTO.nome / marca / formato.'],
        ['Quantidade e unidade', '1,324 KG ; 3,000 UN', 'LINHA_RECECAO.quantidade + APRESENTACAO.'],
    ], 'Correspondência entre os campos das guias de transporte e o sistema.', widths=[2.8, 3.6, 3.6])

    r.page_break()
    r.unnumbered_title('Anexo C – Matriz de rastreabilidade', toc=True)
    n = r.next_tab()
    r.para(f'A Tabela {n} relaciona cada requisito funcional com os casos de uso descritos na secção 4.1.3, com os *mockups* do Capítulo 6 que o concretizam e com os casos de teste de aceitação do Capítulo 8. Todos os requisitos do MVP têm pelo menos um *mockup*; os casos de uso descritos cobrem os fluxos principais, e os requisitos de consulta e de gestão de dados mestre são especificados diretamente pelos *mockups*.')
    import re
    from cap_mockups import DESC

    def expand(t):
        out = set(re.findall(r'RF-[A-Z]{3}-\d\d', t))
        for a, b in re.findall(r'(RF-[A-Z]{3}-\d\d) a (RF-[A-Z]{3}-\d\d)', t):
            out |= {f'{a[:7]}{i:02d}' for i in range(int(a[-2:]), int(b[-2:]) + 1)}
        return out
    uc, mk, ta = {}, {}, {}
    for uid, _, f in UCS:
        for x in expand(f['Requisitos']):
            uc.setdefault(x, []).append(uid)
    for mid, (_, req, _) in sorted(DESC.items()):
        for x in expand(req):
            mk.setdefault(x, []).append(mid)
    for tid, *_, req in TESTES:
        for x in expand(req):
            ta.setdefault(x, []).append(tid)
    rows = []
    for reqs in RF.values():
        for rid, _, _, fase in reqs:
            rows.append([rid, ', '.join(uc.get(rid, [])) or '–', ', '.join(mk.get(rid, [])) or '–',
                         ', '.join(ta.get(rid, [])) or '–', fase])
    r.table(['Requisito', 'Casos de uso', 'Mockups', 'Testes', 'Fase'], rows,
            'Matriz de rastreabilidade requisitos – casos de uso – mockups – testes.', widths=[1.5, 1.6, 3.6, 2.2, 1.1], size=8)
