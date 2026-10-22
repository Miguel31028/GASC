// Componentes reutilizáveis dos mockups (geram HTML).
export const ic = (n, cls = '') => `<span class="ms ${cls}">${n}</span>`;

export const statusbar = (dark = false) => `
<div class="statusbar" ${dark ? 'style="background:#171d1b;color:#fff"' : ''}>
  <span>10:42</span><span>${ic('signal_cellular_4_bar')}${ic('wifi')}${ic('battery_5_bar')}</span>
</div>`;

export const gesture = (dark = false) => `<div class="navbar-gesture" ${dark ? 'style="background:#171d1b"' : ''}></div>`;

export function appbar({ title, sub = '', lead = 'arrow_back', actions = [], cls = '' }) {
  return `<div class="appbar ${cls}">
    ${lead ? `<div class="ib">${ic(lead)}</div>` : '<div style="width:10px"></div>'}
    <div class="title"><h1>${title}</h1>${sub ? `<p>${sub}</p>` : ''}</div>
    ${actions.map(a => `<div class="ib">${a.startsWith('<') ? a : ic(a)}</div>`).join('')}
  </div>`;
}

export function bnav(active, items = NAV_GESTAO) {
  return `<div class="bnav">${items.map(([icon, label, badge]) => `
    <div class="${label === active ? 'on' : ''}"><div class="pill">${ic(icon, label === active ? 'fill' : '')}${badge ? `<span class="badge">${badge}</span>` : ''}</div>${label}</div>`).join('')}
  </div>`;
}
export const NAV_GESTAO = [['home', 'Início'], ['move_to_inbox', 'Receção'], ['shelves', 'Stock'], ['volunteer_activism', 'Entregas'], ['menu', 'Mais']];
export const NAV_COZINHA = [['home', 'Início'], ['restaurant', 'Refeições'], ['shelves', 'Stock'], ['menu', 'Mais']];
export const NAV_UTENTE = [['home', 'Início'], ['restaurant', 'Refeições'], ['event', 'Agenda'], ['person', 'Perfil']];

export const field = (label, value, o = {}) => `
<div class="field ${o.cls || ''}">
  ${o.lab === false ? '' : `<span class="lab">${label}</span>`}
  ${o.icon ? ic(o.icon) : ''}
  <span class="val ${o.ph ? 'ph' : ''}">${value}</span>
  ${o.trail ? (o.trail.startsWith('<') ? o.trail : ic(o.trail)) : ''}
</div>${o.support ? `<div class="support ${o.supportErr ? 'err' : ''}">${o.support}</div>` : ''}`;

export const li = ({ lead = '', leadCls = '', h, s = '', trail = '', cls = '' }) => `
<div class="li ${cls}">
  ${lead ? `<div class="lead ${leadCls}">${/^[a-z_]+$/.test(lead) ? ic(lead) : lead}</div>` : ''}
  <div class="txt"><div class="h">${h}</div>${s ? `<div class="s">${s}</div>` : ''}</div>
  ${trail ? `<div class="trail">${trail}</div>` : ''}
</div>`;

export const chip = (t, sel = false, icon = '') => `<span class="chip ${sel ? 'sel' : ''}">${sel && !icon ? ic('check') : icon ? ic(icon) : ''}${t}</span>`;
export const tag = (t, kind = 'neu', icon = '') => `<span class="tag ${kind}">${icon ? ic(icon) : ''}${t}</span>`;
export const btn = (t, kind = 'filled', icon = '', cls = '') => `<span class="btn ${kind} ${cls}">${icon ? ic(icon) : ''}${t}</span>`;
export const seg = (opts, on) => `<div class="seg">${opts.map(o => `<div class="${o === on ? 'on' : ''}">${o === on ? ic('check') : ''}${o}</div>`).join('')}</div>`;
export const cnc = (ok = true) => `<div class="cnc"><div class="c ${ok ? 'on' : ''}">C</div><div class="nc ${ok ? '' : 'on'}">NC</div></div>`;
export const stepper = v => `<div class="stepper"><div>${ic('remove')}</div><div class="v">${v}</div><div>${ic('add')}</div></div>`;

export function phone(inner, { dark = false } = {}) {
  return `<div class="screen">${statusbar(dark)}${inner}${gesture(dark)}</div>`;
}
