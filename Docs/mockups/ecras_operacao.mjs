// Ecrãs de entregas, refeições, relatórios, administração, App Utente, painel web e PDF.
import { ic, appbar, bnav, field, li, chip, tag, btn, seg, cnc, stepper, phone, NAV_COZINHA, NAV_UTENTE } from './componentes.mjs';

const fefoRow = (n, nome, lote, val, tagv, qtd, extra = '') => `
  <div class="card outlined" style="padding:9px 12px">
    <div class="row sb"><span class="title-s">${nome}</span>${stepper(qtd)}</div>
    <div class="row" style="gap:6px;margin-top:3px"><span class="xs muted">${n}.º FEFO · ${lote} · val. ${val}</span>${tagv}</div>${extra}
  </div>`;

export const ecrasB = q => [
  // ---------------------------------------------------------------- Entregas
  { id: 'M22', grupo: 'Cabazes e outros bens', titulo: 'Entregas do dia', html: phone(`
    ${appbar({ title: 'Entregas', sub: 'Quinta-feira, 22 de outubro', lead: '', actions: ['calendar_month', 'qr_code_scanner'] })}
    <div class="row" style="padding:0 16px 10px;gap:6px">${chip('Hoje 7', true)}${chip('Amanhã 5')}${chip('Faltas 1')}</div>
    <div class="content np">
      <div class="list">
        ${li({ lead: '<span class="small b">09:30</span>', h: 'A-0119 · Sónia Martins', s: 'Cabaz quinzenal · 5 pessoas', trail: tag('Entregue', 'ok', 'check') })}
        ${li({ lead: '<span class="small b">10:00</span>', h: 'A-0131 · Carla Pereira', s: 'Cabaz mensal · 3 pessoas', trail: tag('Entregue', 'ok', 'check') })}
        ${li({ lead: '<span class="small b">10:30</span>', h: 'A-0142 · Maria Silva', s: 'Cabaz quinzenal · 4 pessoas · alergia', trail: tag('Agendado', 'info'), cls: 'sel' })}
        ${li({ lead: '<span class="small b">11:00</span>', h: 'A-0096 · Fernando Lopes', s: 'Outros bens · vestuário', trail: tag('Agendado', 'info') })}
        ${li({ lead: '<span class="small b">11:30</span>', h: 'A-0127 · Rui Almeida', s: 'Cabaz semanal · 2 pessoas', trail: tag('Suspenso', 'warn') })}
        ${li({ lead: '<span class="small b">14:30</span>', h: 'A-0088 · Helena Sousa', s: 'Cabaz quinzenal · 2 pessoas', trail: tag('Agendado', 'info') })}
        ${li({ lead: '<span class="small b">15:00</span>', h: 'A-0075 · Abel Marques', s: 'Cabaz mensal · 1 pessoa', trail: tag('Agendado', 'info') })}
      </div>
    </div>
    <div class="fab">${ic('qr_code_scanner')}Identificar</div>
    ${bnav('Entregas')}`) },

  { id: 'M23', grupo: 'Cabazes e outros bens', titulo: 'Identificação de quem levanta', html: phone(`
    ${appbar({ title: 'Identificação', sub: 'QR lido às 10:31', lead: 'arrow_back' })}
    <div class="content" style="padding-top:10px">
      <div class="card ok col" style="align-items:center;gap:6px;padding:18px">
        ${ic('verified', 'fill s48')}
        <div class="title-l" style="font-weight:500">Maria Silva</div>
        <div class="small">Titular · autorizada a levantar</div>
      </div>
      <div class="card outlined small" style="padding:10px 12px">
        <div class="row sb"><span class="muted">Agregado</span><span class="b">A-0142 · 4 pessoas</span></div>
        <div class="row sb" style="margin-top:4px"><span class="muted">Agendamento</span><span class="b">Hoje 10:30 · cabaz quinzenal</span></div>
        <div class="row sb" style="margin-top:4px"><span class="muted">Último cabaz</span><span class="b">15/10/2026</span></div>
      </div>
      <div class="card warn small row" style="gap:8px;align-items:flex-start">${ic('warning')}<div><b>Atenção na composição do cabaz</b><br>Alergia a glúten (1 membro) · sem carne de porco</div></div>
      <div class="spacer"></div>
      ${btn('Preparar cabaz', 'filled', 'shopping_basket', 'block lg')}
      <div class="row">${btn('Outros bens', 'outlined', 'checkroom', 'grow')}${btn('Não é esta pessoa', 'outlined', '', 'grow')}</div>
      <div class="xs muted center">Sem QR? Pesquise pelo nome: a identificação manual fica registada.</div>
    </div>`) },

  { id: 'M24', grupo: 'Cabazes e outros bens', titulo: 'Composição do cabaz com sugestão FEFO', html: phone(`
    ${appbar({ title: 'Cabaz · A-0142', sub: '4 pessoas · 9 artigos', lead: 'arrow_back', actions: ['add'] })}
    <div class="row" style="padding:0 16px 8px;gap:6px">${chip('Sugestão FEFO', true)}${chip('Todos')}${chip('Sem glúten', false, 'filter_alt')}</div>
    <div class="content" style="padding-top:2px;gap:8px">
      ${fefoRow(1, 'Iogurte natural', 'L-0912', '24/10', tag('2 dias', 'warn'), '4 UN')}
      ${fefoRow(1, 'Batata branca', 'L-0801', '30/10', tag('granel', 'neu'), '3 kg')}
      ${fefoRow(1, 'Arroz agulha 1 kg', 'L-0733', '02/12', '', '2 UN')}
      ${fefoRow(1, 'Leite meio-gordo 1 L', 'L-0790', '10/11', '', '4 UN')}
      ${fefoRow(1, 'Massa esparguete 500 g', 'L-0702', '15/03/27', '', '2 UN', `<div class="row small" style="gap:6px;margin-top:6px;color:var(--error)">${ic('warning', 's18')}Contém glúten · confirmar com o agregado</div>`)}
      ${fefoRow(1, 'Frango inteiro', 'L-0650', '10/01/27', tag('congelado', 'info'), '1 UN')}
    </div>
    <div class="bottombar">${btn('Rever entrega (9)', 'filled', 'arrow_forward')}</div>`) },

  { id: 'M25', grupo: 'Cabazes e outros bens', titulo: 'Confirmação da entrega', html: phone(`
    ${appbar({ title: 'Confirmar entrega', lead: 'arrow_back' })}
    <div class="content" style="padding-top:8px">
      <div class="card filled small" style="padding:10px 12px">
        <div class="row sb"><span class="muted">Agregado</span><span class="b">A-0142 · Silva</span></div>
        <div class="row sb" style="margin-top:4px"><span class="muted">Levanta</span><span class="b">Maria Silva (QR)</span></div>
        <div class="row sb" style="margin-top:4px"><span class="muted">Entrega</span><span class="b">Ana Costa</span></div>
      </div>
      <table class="t">
        <tr><th>Produto</th><th>Lote</th><th style="text-align:right">Qtd.</th></tr>
        <tr><td>Iogurte natural</td><td>L-0912</td><td style="text-align:right">4 UN</td></tr>
        <tr><td>Batata branca</td><td>L-0801</td><td style="text-align:right">3 kg</td></tr>
        <tr><td>Arroz agulha 1 kg</td><td>L-0733</td><td style="text-align:right">2 UN</td></tr>
        <tr><td>Leite meio-gordo 1 L</td><td>L-0790</td><td style="text-align:right">4 UN</td></tr>
        <tr><td>Grão-de-bico 845 g</td><td>L-0688</td><td style="text-align:right">2 UN</td></tr>
        <tr><td>Atum em óleo 120 g</td><td>L-0712</td><td style="text-align:right">3 UN</td></tr>
        <tr><td>Frango inteiro (cong.)</td><td>L-0650</td><td style="text-align:right">1 UN</td></tr>
        <tr><td>Maçã Gala 1,5 kg</td><td>L-0915</td><td style="text-align:right">1 UN</td></tr>
        <tr><td>Azeite 0,75 L</td><td>L-0601</td><td style="text-align:right">1 UN</td></tr>
      </table>
      <div class="card primary small row" style="gap:8px">${ic('event_repeat')}<span>Próximo cabaz agendado para <b>05/11/2026</b> (quinzenal).</span></div>
      <div class="spacer"></div>
      ${btn('Confirmar entrega', 'filled', 'done_all', 'block lg')}
    </div>`) },

  { id: 'M26', grupo: 'Cabazes e outros bens', titulo: 'Entrega de outros bens', html: phone(`
    ${appbar({ title: 'Outros bens · A-0096', sub: 'Fernando Lopes · 3 pessoas', lead: 'arrow_back' })}
    <div class="row" style="padding:0 16px 8px;gap:6px">${chip('Vestuário', true)}${chip('Higiene')}${chip('Limpeza')}</div>
    <div class="content" style="gap:8px;padding-top:2px">
      <div class="row" style="gap:6px">${chip('Homem', true)}${chip('Mulher')}${chip('Criança')}${chip('Tam. M', true)}</div>
      <div class="card outlined row" style="padding:10px 12px"><div class="grow"><div class="title-s">Casaco de inverno</div><div class="xs muted">Homem · M · 003-04-01 · 3 disponíveis</div></div>${stepper('1')}</div>
      <div class="card outlined row" style="padding:10px 12px"><div class="grow"><div class="title-s">Calças de ganga</div><div class="xs muted">Homem · M · 003-04-02 · 5 disponíveis</div></div>${stepper('2')}</div>
      <div class="card outlined row" style="padding:10px 12px"><div class="grow"><div class="title-s">Camisola de malha</div><div class="xs muted">Homem · M · 003-04-02 · 2 disponíveis</div></div>${stepper('0')}</div>
      <div class="section">Higiene (adicionados)</div>
      <div class="card outlined row" style="padding:10px 12px"><div class="grow"><div class="title-s">Gel de banho 750 ml</div><div class="xs muted">005-01-01 · 14 disponíveis</div></div>${stepper('1')}</div>
      <div class="card outlined row" style="padding:10px 12px"><div class="grow"><div class="title-s">Pasta de dentes 75 ml</div><div class="xs muted">005-01-02 · 22 disponíveis</div></div>${stepper('3')}</div>
    </div>
    <div class="bottombar">${btn('Confirmar entrega (7)', 'filled', 'done_all')}</div>`) },

  // ---------------------------------------------------------------- Refeições
  { id: 'M27', grupo: 'Refeições', titulo: 'Refeições do dia (cozinha)', html: phone(`
    ${appbar({ title: 'Refeições', sub: 'Quinta-feira, 22 de outubro', lead: '', actions: ['calendar_month'] })}
    <div class="content" style="padding-top:4px">
      <div class="card primary">
        <div class="row sb"><span class="title-m">Almoço</span>${tag('Aberto', 'ok')}</div>
        <div class="row" style="margin-top:8px;gap:18px">
          <div><div class="display" style="font-size:34px">38</div><div class="xs">a confecionar</div></div>
          <div><div class="display" style="font-size:34px">21</div><div class="xs">levantadas</div></div>
          <div><div class="display" style="font-size:34px">17</div><div class="xs">por levantar</div></div>
        </div>
        <div class="hbar" style="margin-top:8px;background:rgba(255,255,255,.6)"><div style="width:55%"></div></div>
      </div>
      <div class="card outlined row" style="padding:10px 12px"><div class="grow"><div class="title-s">Jantar</div><div class="small muted">Serviço fechado · abrir em dias excecionais</div></div><div class="switch"></div></div>
      <div class="row">${btn('Distribuir', 'filled', 'qr_code_scanner', 'grow')}${btn('Saída de produtos', 'tonal', 'outbox', 'grow')}</div>
      <div class="section">Amanhã (sex., 23/10)</div>
      <div class="card outlined small" style="padding:10px 12px">
        <div class="row sb"><span>Pedidos registados</span><span class="b">35 refeições · 19 agregados</span></div>
        <div class="row sb" style="margin-top:4px"><span>Hora limite para alterações</span><span class="b">hoje 16:00</span></div>
      </div>
      <div class="section">Sugestão para cozinhar hoje (FEFO)</div>
      <div class="row wrap" style="gap:6px">${tag('Peito de frango 3,2 kg · 1 dia', 'warn')}${tag('Alface 1,3 kg · 3 dias', 'warn')}${tag('Natas 4 UN · 2 dias', 'warn')}</div>
    </div>
    ${bnav('Refeições', NAV_COZINHA)}`) },

  { id: 'M28', grupo: 'Refeições', titulo: 'Saída de produtos para a cozinha', html: phone(`
    ${appbar({ title: 'Saída para a cozinha', sub: 'Almoço 22/10 · 38 refeições', lead: 'close' })}
    <div style="padding:0 16px 10px"><div class="search">${ic('search')}<span class="ph grow">Adicionar produto</span></div></div>
    <div class="content" style="gap:8px;padding-top:0">
      ${fefoRow(1, 'Peito de frango', 'L-0877', '23/10', tag('1 dia', 'err'), '3,2 kg')}
      ${fefoRow(1, 'Arroz agulha 1 kg', 'L-0733', '02/12', '', '4 UN')}
      ${fefoRow(1, 'Cenoura', 'L-0905', '29/10', tag('granel', 'neu'), '2 kg')}
      ${fefoRow(1, 'Cebola', 'L-0870', '15/11', tag('granel', 'neu'), '1,5 kg')}
      ${fefoRow(1, 'Azeite 0,75 L', 'L-0601', '01/06/27', '', '1 UN')}
      <div class="card info small row" style="gap:8px">${ic('info', 's20')}<span>Produtos a granel saem em kg: o saco de cenoura fica com 1 volume e 8 kg.</span></div>
    </div>
    <div class="bottombar">${btn('Registar saída (5)', 'filled', 'outbox')}</div>`) },

  { id: 'M29', grupo: 'Refeições', titulo: 'Levantamento de refeição', html: phone(`
    ${appbar({ title: 'Distribuição · Almoço', sub: '21 de 38 levantadas', lead: 'arrow_back' })}
    <div class="content" style="padding-top:8px">
      <div class="card ok row" style="gap:12px">${ic('verified', 'fill s40')}<div><div class="title-m">Paulo Silva</div><div class="small">A-0142 · autorizado · QR lido 12:41</div></div></div>
      <div class="card outlined" style="padding:12px">
        <div class="row sb"><span class="title-s">Pedido para hoje</span>${tag('Pedido', 'info')}</div>
        <div class="row sb" style="margin-top:8px"><span class="small">Refeições entregues</span>${stepper('2')}</div>
      </div>
      <div class="card primary" style="padding:12px">
        <div class="row" style="gap:8px">${ic('event_upcoming')}<span class="title-s">Pedido para amanhã (sex., 23/10)</span></div>
        <div class="row sb" style="margin-top:10px"><span class="small">N.º de refeições</span>${stepper('3')}</div>
        <div class="xs" style="margin-top:6px">Sugestão do pedido recorrente: 3 à sexta-feira</div>
      </div>
      <div class="spacer"></div>
      ${btn('Confirmar levantamento', 'filled', 'done', 'block lg')}
      <div class="row">${btn('Sem pedido amanhã', 'outlined', '', 'grow')}${btn('Exceção', 'outlined', 'report', 'grow')}</div>
    </div>`) },

  { id: 'M30', grupo: 'Refeições', titulo: 'Pedido de refeições recorrente', html: phone(`
    ${appbar({ title: 'Pedido de refeições', sub: 'A-0142 · Silva · 4 pessoas', lead: 'close' })}
    <div class="content" style="padding-top:12px">
      ${seg(['Um dia', 'Recorrente'], 'Recorrente')}
      <div class="row">${field('De', '26/10/2026', { trail: 'event' }).replace('class="field ', 'class="field grow ')}${field('Até', '20/11/2026', { trail: 'event' }).replace('class="field ', 'class="field grow ')}</div>
      <div class="label">Refeição</div>
      ${seg(['Almoço', 'Jantar'], 'Almoço')}
      <div class="label">N.º de refeições por dia da semana</div>
      <div class="card outlined" style="padding:4px 12px">
        ${[['Segunda', '2'], ['Terça', '2'], ['Quarta', '2'], ['Quinta', '2'], ['Sexta', '3'], ['Sábado', '0'], ['Domingo', '0']].map(([d, n]) =>
          `<div class="row sb" style="height:42px;${d !== 'Domingo' ? 'border-bottom:1px solid #e3e9e5' : ''}"><span class="small b">${d}</span>${stepper(n)}</div>`).join('')}
      </div>
      <div class="small muted">Serão criados 20 pedidos (44 refeições). O jantar só pode ser pedido em dias com serviço aberto.</div>
    </div>
    <div class="bottombar">${btn('Registar pedidos', 'filled', 'check')}</div>`) },

  // ---------------------------------------------------------------- Relatórios
  { id: 'M31', grupo: 'Relatórios e indicadores', titulo: 'Emissão do RGDHSA049', html: phone(`
    ${appbar({ title: 'RGDHSA049', sub: 'Controlo da receção de matérias-primas', lead: 'arrow_back' })}
    <div class="content" style="padding-top:12px">
      <div class="label">Período</div>
      <div class="row wrap" style="gap:6px">${chip('Este mês', true)}${chip('Mês anterior')}${chip('Personalizado', false, 'date_range')}</div>
      <div class="row">${field('De', '01/10/2026', { trail: 'event' }).replace('class="field ', 'class="field grow ')}${field('Até', '22/10/2026', { trail: 'event' }).replace('class="field ', 'class="field grow ')}</div>
      <div class="card filled" style="padding:12px">
        <div class="title-s">Pré-visualização</div>
        <div class="row sb small" style="margin-top:8px"><span>Receções</span><span class="b">31</span></div>
        <div class="row sb small" style="margin-top:4px"><span>Linhas de produto</span><span class="b">214</span></div>
        <div class="row sb small" style="margin-top:4px"><span>Linhas não conformes</span><span class="b" style="color:var(--error)">6</span></div>
        <div class="row sb small" style="margin-top:4px"><span>Responsáveis</span><span class="b">3</span></div>
      </div>
      <div class="card outlined small row" style="gap:8px">${ic('description', 's20')}<span>Formato A4 horizontal, igual ao modelo em papel (Edição 1, Revisão 0).</span></div>
      <div class="spacer"></div>
      ${btn('Gerar PDF', 'filled', 'picture_as_pdf', 'block lg')}
      ${btn('Exportar CSV', 'outlined', 'table_view', 'block')}
    </div>`) },

  { id: 'M32', grupo: 'Relatórios e indicadores', titulo: 'Painel de indicadores', html: phone(`
    ${appbar({ title: 'Indicadores', sub: 'Outubro de 2026', lead: 'arrow_back', actions: ['tune'] })}
    <div class="content" style="padding-top:4px">
      <div class="row"><div class="kpi"><div class="v">2 314</div><div class="l">Artigos recebidos</div></div><div class="kpi"><div class="v">96</div><div class="l">Cabazes entregues</div></div></div>
      <div class="row"><div class="kpi"><div class="v">812</div><div class="l">Refeições servidas</div></div><div class="kpi"><div class="v" style="color:var(--warn)">1,9%</div><div class="l">Desperdício</div></div></div>
      <div class="card outlined" style="padding:12px">
        <div class="row sb"><span class="title-s">Entradas vs. saídas por semana</span></div>
        <div class="bars">
          ${[[70, 55, 'S40'], [85, 72, 'S41'], [60, 66, 'S42'], [92, 80, 'S43']].map(([a, b, l]) => `<div><div class="row" style="align-items:flex-end;gap:3px;width:100%;height:90px"><div class="b1" style="height:${a}%"></div><div class="b2" style="height:${b}%"></div></div>${l}</div>`).join('')}
        </div>
        <div class="row xs muted" style="gap:12px;margin-top:6px"><span class="row" style="gap:4px"><span style="width:10px;height:10px;background:var(--primary);border-radius:2px"></span>Entradas</span><span class="row" style="gap:4px"><span style="width:10px;height:10px;background:#e0a458;border-radius:2px"></span>Saídas</span></div>
      </div>
      <div class="card outlined" style="padding:12px">
        <div class="title-s" style="margin-bottom:8px">Desperdício por categoria</div>
        ${[['Lacticínios', 38], ['Padaria', 27], ['Frutas e legumes', 22], ['Charcutaria', 13]].map(([c, p]) => `<div class="row small" style="gap:8px;margin-top:6px"><span style="width:110px">${c}</span><div class="hbar grow"><div style="width:${p}%"></div></div><span style="width:32px;text-align:right">${p}%</span></div>`).join('')}
      </div>
    </div>`) },

  // ---------------------------------------------------------------- Administração
  { id: 'M33', grupo: 'Administração', titulo: 'Células de prateleira', html: phone(`
    ${appbar({ title: 'Células', sub: '86 células · 6 colunas', lead: 'arrow_back', actions: ['print', 'more_vert'] })}
    <div class="row" style="padding:0 16px 10px;gap:6px">${chip('Todas', true)}${chip('Coluna 003')}${chip('Cheias 4')}${chip('Inativas')}</div>
    <div class="content np">
      <div class="list">
        ${li({ lead: 'grid_view', leadCls: 'sq', h: '<span class="mono">003-01-01</span>', s: 'Coluna 3 · Linha 1 · Andar 1 · Massas, Arroz', trail: tag('livre', 'ok') })}
        ${li({ lead: 'grid_view', leadCls: 'sq', h: '<span class="mono">003-01-02</span>', s: 'Coluna 3 · Linha 1 · Andar 2 · Arroz', trail: tag('cheia', 'err') })}
        ${li({ lead: 'grid_view', leadCls: 'sq', h: '<span class="mono">003-02-01</span>', s: 'Coluna 3 · Linha 2 · Andar 1 · Leguminosas', trail: tag('livre', 'ok') })}
        ${li({ lead: 'grid_view', leadCls: 'sq', h: '<span class="mono">003-02-02</span>', s: 'Coluna 3 · Linha 2 · Andar 2 · vazia', trail: tag('livre', 'ok') })}
        ${li({ lead: 'grid_view', leadCls: 'sq', h: '<span class="mono">004-01-01</span>', s: 'Coluna 4 · Linha 1 · Andar 1 · Leite', trail: tag('livre', 'ok') })}
      </div>
    </div>
    <div class="scrim" style="top:430px"></div>
    <div class="sheet">
      <div class="handle"></div>
      <div class="title-m">Criar células em série</div>
      <div class="row">${field('Coluna', '007').replace('class="field ', 'class="field grow ')}${field('Linhas', '1–4').replace('class="field ', 'class="field grow ')}${field('Andares', '1–3').replace('class="field ', 'class="field grow ')}</div>
      <div class="small muted">Serão criadas 12 células: 007-01-01 a 007-04-03 (formato xxx-xx-xx).</div>
      <div class="row" style="justify-content:flex-end;gap:8px">${btn('Cancelar', 'text')}${btn('Criar e imprimir QR', 'filled', 'print')}</div>
    </div>`) },

  { id: 'M34', grupo: 'Administração', titulo: 'Equipamento de frio e zonas', html: phone(`
    ${appbar({ title: 'ARCA1 · Arca 1', sub: 'Congelador · 6 zonas', lead: 'arrow_back', actions: ['edit'] })}
    <div class="content" style="padding-top:8px">
      <div class="label">Zonas (lado × nível)</div>
      <div class="zones">
        <div></div><div class="h">E · esquerda</div><div class="h">C · centro</div><div class="h">D · direita</div>
        <div class="h">1</div><div class="z">E1<small>2 lotes</small></div><div class="z full">C1<small>cheia</small></div><div class="z">D1<small>1 lote</small></div>
        <div class="h">2</div><div class="z">E2<small>vazia</small></div><div class="z">C2<small>3 lotes</small></div><div class="z">D2<small>2 lotes</small></div>
        <div class="h">3</div><div class="z none">—<small>não existe</small></div><div class="z none">—<small>não existe</small></div><div class="z none">—<small>não existe</small></div>
      </div>
      <div class="small muted">Os lados são sempre D, C ou E; o número de níveis varia por equipamento (RN-04).</div>
      <div class="label">Uso preferencial (sugestão, não restrição)</div>
      <div class="row wrap" style="gap:6px">${chip('Carne de aves', true)}${chip('Adicionar categoria', false, 'add')}</div>
      <div class="label">Outros equipamentos</div>
      <div class="card outlined" style="padding:0"><div class="list">
        ${li({ lead: 'kitchen', leadCls: 'sq', h: 'ARCA2 · Arca 2', s: 'Congelador · 2 zonas (E1, D1) · todos os congelados' })}
        ${li({ lead: 'kitchen', leadCls: 'sq', h: 'FRIG1 · Frigorífico', s: 'Refrigerado · 6 zonas · frescos' })}
      </div></div>
      ${btn('Imprimir etiquetas QR das zonas', 'tonal', 'print', 'block')}
    </div>`) },

  { id: 'M35', grupo: 'Administração', titulo: 'Categorias e tabela de congelação', html: phone(`
    ${appbar({ title: 'Categorias', sub: '18 categorias', lead: 'arrow_back', actions: ['add'] })}
    <div class="content np">
      <table class="t" style="margin:6px 0 0;font-size:12.5px">
        <tr><th style="padding-left:16px">Categoria</th><th>Cond.</th><th>Cong.</th><th>Aviso</th></tr>
        ${[['Carne de aves', 'Refrig.', '+90 d', '2 d'], ['Carne de vaca/porco', 'Refrig.', '+120 d', '2 d'], ['Peixe fresco', 'Refrig.', '+90 d', '1 d'], ['Pão e padaria', 'Ambiente', '+30 d', '1 d'], ['Lacticínios', 'Refrig.', '—', '3 d'], ['Frutas e legumes', 'Ambiente', '—', '3 d'], ['Massas e arroz', 'Ambiente', '—', '30 d'], ['Conservas', 'Ambiente', '—', '30 d'], ['Higiene pessoal', 'Ambiente', '—', '—'], ['Vestuário', 'Ambiente', '—', '—']].map(([a, b, c, d]) =>
          `<tr><td style="padding-left:16px">${a}</td><td>${b}</td><td>${c === '—' ? '<span class="muted">—</span>' : tag(c, 'info')}</td><td>${d}</td></tr>`).join('')}
      </table>
    </div>
    <div class="scrim" style="top:520px"></div>
    <div class="sheet">
      <div class="handle"></div>
      <div class="title-m">Carne de aves</div>
      <div class="row sb"><span class="small b">Congelável</span><div class="switch on"></div></div>
      <div class="row">${field('Extensão (dias)', '90', { cls: 'focus' }).replace('class="field ', 'class="field grow ')}${field('Aviso (dias)', '2').replace('class="field ', 'class="field grow ')}</div>
      <div class="row" style="justify-content:flex-end;gap:8px">${btn('Cancelar', 'text')}${btn('Guardar', 'filled')}</div>
    </div>`) },

  { id: 'M36', grupo: 'Administração', titulo: 'Utilizadores e perfis', html: phone(`
    ${appbar({ title: 'Utilizadores', sub: '9 ativos', lead: 'arrow_back', actions: ['search'] })}
    <div class="content np">
      <div class="list">
        ${li({ lead: 'AC', h: 'Ana Costa', s: 'Operador · Responsável', trail: tag('Ativo', 'ok') })}
        ${li({ lead: 'JR', h: 'Joana Reis', s: 'Técnico de ação social', trail: tag('Ativo', 'ok') })}
        ${li({ lead: 'MF', h: 'Manuel Fonseca', s: 'Cozinha', trail: tag('Ativo', 'ok') })}
        ${li({ lead: 'TP', h: 'Teresa Pinto', s: 'Administrador', trail: tag('Ativo', 'ok') })}
        ${li({ lead: 'VB', h: 'Vasco Brito', s: 'Operador (voluntário)', trail: tag('Inativo', 'neu') })}
      </div>
    </div>
    <div class="scrim" style="top:420px"></div>
    <div class="sheet">
      <div class="handle"></div>
      <div class="title-m">Perfis de Ana Costa</div>
      ${[['Administrador', false], ['Responsável da instituição', true], ['Técnico de ação social', false], ['Operador de armazém', true], ['Cozinha', false]].map(([p, on]) => `<div class="row" style="gap:12px;height:34px"><span class="check ${on ? 'on' : ''}"></span><span class="small b">${p}</span></div>`).join('')}
      <div class="row" style="justify-content:flex-end;gap:8px">${btn('Desativar', 'text')}${btn('Guardar', 'filled')}</div>
    </div>`) },

  // ---------------------------------------------------------------- App Utente
  { id: 'M37', grupo: 'App Utente', titulo: 'App Utente – entrada por telemóvel', html: phone(`
    <div class="content" style="padding:40px 28px 20px;gap:16px">
      <div class="col" style="align-items:center;gap:10px;margin-bottom:14px">
        <div style="width:84px;height:84px;border-radius:24px;background:var(--tertiary);display:flex;align-items:center;justify-content:center;color:#fff">${ic('family_restroom', 's48')}</div>
        <div class="title-l" style="font-weight:500">GASC Utente</div>
        <div class="muted small center">Espaço Social do GASC</div>
      </div>
      ${field('Número de telemóvel', '+351 912 345 678', { icon: 'smartphone' })}
      <div class="card info small">Enviámos um código por SMS. A conta tem de ser ativada primeiro pela sua técnica.</div>
      <div class="label center">Código de 6 dígitos</div>
      <div class="row" style="justify-content:center;gap:8px">${['4', '8', '1', '9', '', ''].map((d, i) => `<div style="width:40px;height:50px;border-radius:8px;border:${i === 4 ? '2px solid var(--primary)' : '1px solid var(--outline)'};display:flex;align-items:center;justify-content:center;font-size:22px">${d}</div>`).join('')}</div>
      <div class="center"><span class="btn text">Reenviar código (0:42)</span></div>
      <div class="spacer"></div>
      ${btn('Entrar', 'filled', '', 'block lg')}
    </div>`) },

  { id: 'M38', grupo: 'App Utente', titulo: 'App Utente – início e credencial', html: phone(`
    ${appbar({ title: 'Olá, Maria', sub: 'Agregado A-0142', lead: '', actions: ['notifications'] })}
    <div class="content" style="padding-top:4px;align-items:center">
      <div class="card elev col" style="width:100%;align-items:center;padding:16px;gap:6px">
        <div class="label">A MINHA CREDENCIAL</div>
        <div style="width:170px;height:170px">${q.utente}</div>
        <div class="small muted">Mostre este código ao levantar o cabaz ou as refeições</div>
      </div>
      <div class="card primary row" style="width:100%;gap:12px">${ic('shopping_basket', 's32')}<div class="grow"><div class="small">Próximo cabaz</div><div class="title-m">qui., 29 de outubro · 10:30</div></div></div>
      <div class="card outlined" style="width:100%;padding:10px 12px">
        <div class="row sb"><span class="title-s">Refeições desta semana</span><span class="btn text" style="height:28px">Alterar</span></div>
        <div class="row" style="gap:6px;margin-top:6px">${['Seg 2', 'Ter 2', 'Qua 2', 'Qui 2', 'Sex 3'].map(d => tag(d, 'prim')).join('')}</div>
      </div>
    </div>
    ${bnav('Início', NAV_UTENTE)}`) },

  { id: 'M39', grupo: 'App Utente', titulo: 'App Utente – pedidos de refeição', html: phone(`
    ${appbar({ title: 'Refeições', sub: 'Pedidos do agregado', lead: '' })}
    <div class="content" style="padding-top:4px">
      <div class="row sb"><span class="btn text">${ic('chevron_left')}</span><span class="title-s">26 out. – 1 nov.</span><span class="btn text">${ic('chevron_right')}</span></div>
      <div class="card outlined" style="padding:4px 12px">
        ${[['Seg 26', '2', 'Pedido'], ['Ter 27', '2', 'Pedido'], ['Qua 28', '2', 'Pedido'], ['Qui 29', '2', 'Pedido'], ['Sex 30', '3', 'Pedido'], ['Sáb 31', '–', ''], ['Dom 1', '–', '']].map(([d, n, s]) =>
          `<div class="row sb" style="height:44px;border-bottom:1px solid #e3e9e5"><span class="small b" style="width:60px">${d}</span><span class="small grow">Almoço${n !== '–' ? ` · <b>${n}</b> refeições` : ' · sem pedido'}</span>${s ? tag(s, 'info') : ''}</div>`).join('')}
      </div>
      <div class="card info small row" style="gap:8px">${ic('schedule', 's20')}<span>Pode alterar os pedidos até às 16:00 do dia anterior.</span></div>
      <div class="card warn small row" style="gap:8px">${ic('ac_unit', 's20')}<span>Jantar disponível a 28/10 (vaga de frio). Deseja pedir?</span></div>
    </div>
    <div class="fab">${ic('add')}Novo pedido</div>
    ${bnav('Refeições', NAV_UTENTE)}`) },
];

// ---------------------------------------------------------------- Painel web (ecrã de parede)
export const painelWeb = () => ({ id: 'M40', grupo: 'Painel web', titulo: 'Painel de agenda para ecrã de parede', wide: true, html: `
<div class="wide">
  <div style="height:86px;background:var(--primary);color:#fff;display:flex;align-items:center;padding:0 36px;gap:18px">
    ${ic('volunteer_activism', 'fill s40')}<div class="grow"><div style="font-size:28px;font-weight:500">Espaço Social · Entregas de hoje</div><div style="opacity:.85;font-size:16px">Quinta-feira, 22 de outubro de 2026</div></div>
    <div style="font-size:46px;font-weight:300">10:42</div>
  </div>
  <div style="display:flex;gap:24px;padding:24px 36px;flex:1">
    <div style="flex:2;background:#fff;border-radius:18px;padding:18px 24px;box-shadow:0 1px 3px rgba(0,0,0,.12)">
      <table class="t" style="font-size:20px">
        <tr><th style="font-size:16px">Hora</th><th style="font-size:16px">Agregado</th><th style="font-size:16px">Tipo</th><th style="font-size:16px">Estado</th></tr>
        ${[['09:30', 'A-0119', 'Cabaz', ['Entregue', 'ok']], ['10:00', 'A-0131', 'Cabaz', ['Entregue', 'ok']], ['10:30', 'A-0142', 'Cabaz', ['A decorrer', 'warn']], ['11:00', 'A-0096', 'Outros bens', ['Agendado', 'info']], ['11:30', 'A-0127', 'Cabaz', ['Suspenso', 'neu']], ['14:30', 'A-0088', 'Cabaz', ['Agendado', 'info']], ['15:00', 'A-0075', 'Cabaz', ['Agendado', 'info']]].map(([h, a, t, [s, k]]) =>
          `<tr><td style="padding:12px 4px;font-weight:500">${h}</td><td>${a}</td><td>${t}</td><td><span class="tag ${k}" style="font-size:16px;height:30px;padding:0 12px">${s}</span></td></tr>`).join('')}
      </table>
    </div>
    <div style="flex:1;display:flex;flex-direction:column;gap:18px">
      <div style="background:var(--primary-container);border-radius:18px;padding:20px 24px"><div style="font-size:16px">Entregas hoje</div><div style="font-size:54px">2 / 7</div><div class="hbar" style="height:12px;background:#fff"><div style="width:29%;height:12px"></div></div></div>
      <div style="background:#fff;border-radius:18px;padding:20px 24px;box-shadow:0 1px 3px rgba(0,0,0,.12)"><div style="font-size:16px;color:var(--on-surface-var)">Almoço</div><div style="font-size:40px">21 / 38 <span style="font-size:18px;color:var(--on-surface-var)">levantadas</span></div></div>
      <div style="background:#fff;border-radius:18px;padding:20px 24px;box-shadow:0 1px 3px rgba(0,0,0,.12);flex:1"><div style="font-size:16px;color:var(--on-surface-var);margin-bottom:8px">Amanhã</div>
        <div style="font-size:18px;line-height:1.7">5 entregas agendadas<br>35 refeições pedidas</div></div>
    </div>
  </div>
  <div style="padding:0 36px 14px;font-size:13px;color:var(--on-surface-var)">Apenas códigos de agregado são mostrados (sem nomes), por questões de privacidade. Atualização automática em tempo real.</div>
</div>` });

// ---------------------------------------------------------------- PDF RGDHSA049
export const pdfRgdhsa = () => {
  const rows = [
    ['01', 'Leite m/g 1 L / Pingo Doce', 'DPM1/4100…', '12 UN', 1, 1, 1, 1, '5,0', '', 'AC'],
    ['01', 'Arroz agulha 1 kg / Particular anónimo', '—', '10 UN', 1, 1, 1, 1, '—', '', 'AC'],
    ['06', 'Alface frisada / Pingo Doce', 'DPM1/4101…', '1,324 kg', 1, 1, 1, 1, '4,0', '', 'AC'],
    ['06', 'Leite Agros 35 cl / Pingo Doce', 'DPM1/4101…', '1 palete (30 UN)', 1, 1, 1, 0, '5,5', '2 emb. amolgadas', 'AC'],
    ['06', 'Fiambre perna 200 g / Pingo Doce', 'DPM1/4101…', '2 UN', 1, 1, 1, 0, '6,0', 'Rejeitado', 'AC'],
    ['09', 'Fiambre perna extra / Recheio', 'DRM1/3029…', '7 UN', 1, 1, 1, 1, '4,5', '', 'VB'],
    ['09', 'Bacon naco 200 g / Recheio', 'DRM1/3029…', '8 UN', 1, 1, 1, 1, '4,5', '', 'VB'],
    ['14', 'Feijão preto / Irmãdona', 'DON7004…', '1 UN', 1, 1, 1, 1, '—', '', 'AC'],
    ['20', 'Frango inteiro / Mercadona', 'GT 2026/88…', '6 UN', 1, 1, 1, 1, '-18', 'Congelado', 'JR'],
    ['20', 'Pescada congelada / Mercadona', 'GT 2026/88…', '4 kg', 1, 1, 1, 1, '-18', 'Congelado', 'JR'],
    ['21', 'Massa esparguete 500 g / Campanha escola', '—', '24 UN', 1, 1, 1, 1, '—', '', 'AC'],
    ['21', 'Grão-de-bico 845 g / Campanha escola', '—', '12 UN', 1, 1, 1, 1, '—', '', 'AC'],
    ['21', 'Atum em óleo 120 g / Campanha escola', '—', '30 UN', 1, 1, 1, 1, '—', '', 'AC'],
    ['22', 'Iogurte natural ×4 / Pingo Doce', 'DPM1/4101…', '6 UN', 1, 1, 1, 1, '4,0', '', 'AC'],
    ['22', 'Maçã Gala 1,5 kg / Pingo Doce', 'DPM1/4101…', '3 UN', 1, 1, 1, 1, '—', '', 'AC'],
    ['22', 'Pão de forma / Padaria Central', 'Lote 2210', '8 UN', 1, 1, 0, 1, '—', 'Bolor em 1 UN (rejeitada)', 'AC'],
    ['22', 'Azeite 0,75 L / Particular (J. Ferreira)', '—', '2 UN', 1, 1, 1, 1, '—', '', 'AC'],
    ['22', 'Cenoura granel / Produtor local', '—', '1 saco (10 kg)', 1, 1, 1, 1, '—', '', 'VB'],
  ];
  const cn = v => `<td style="text-align:center">${v ? 'X' : ''}</td><td style="text-align:center">${v ? '' : 'X'}</td>`;
  return { id: 'M41', grupo: 'Documentos gerados', titulo: 'RGDHSA049 gerado em PDF', wide: true, html: `
<div class="a4">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;border-bottom:2px solid #000;padding-bottom:8px">
    <div style="font-size:12px"><b>MEDIDA DE CONTROLO</b><br>Monitorização do Controlo da Receção de Matérias-Primas</div>
    <div style="font-size:12px;text-align:center"><b>Mês/Ano: 10/2026</b><br>Período: 01/10/2026 a 22/10/2026</div>
    <div style="font-size:11px;text-align:right">Edição 1 · Revisão 0<br>12/2020</div>
  </div>
  <table style="width:100%;border-collapse:collapse;font-size:10.5px;margin-top:12px" border="1" cellpadding="4">
    <tr style="background:#eee;text-align:center"><th rowspan="2">Dia</th><th rowspan="2">Produto / Fornecedor</th><th rowspan="2">Doc. receção<br>Lote / N.º guia</th><th rowspan="2">Quantidade</th>
      <th colspan="2">Cond. higiene</th><th colspan="2">Rotulagem / validade</th><th colspan="2">Caract. organoléticas</th><th colspan="2">Embalagem íntegra</th><th rowspan="2">Temp. (ºC)</th><th rowspan="2">Observações</th><th rowspan="2">Resp.</th></tr>
    <tr style="background:#eee;text-align:center">${'<th>C</th><th>NC</th>'.repeat(4)}</tr>
    ${rows.map(r => `<tr><td style="text-align:center">${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td>${cn(r[4])}${cn(r[5])}${cn(r[6])}${cn(r[7])}<td style="text-align:center">${r[8]}</td><td>${r[9]}</td><td style="text-align:center">${r[10]}</td></tr>`).join('')}
  </table>
  <div style="font-size:10px;margin-top:10px">C – produto conforme, dentro das propriedades pretendidas. NC – produto não conforme. Documento gerado automaticamente pelo sistema GASC Gestão em 22/10/2026 10:44 · página 1 de 12.</div>
  <div style="display:flex;justify-content:space-between;font-size:11px;margin-top:26px"><span>Elaborado por: ____________________</span><span>Aprovado por: Equipa HACCP</span></div>
  <div style="font-size:10px;text-align:right;margin-top:24px">RGDHSA049</div>
</div>` };
};
