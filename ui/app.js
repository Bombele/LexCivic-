// app.js
document.addEventListener("DOMContentLoaded", () => {
  LexCivicI18N.init();

  const API = {
    base: "", // ex: https://api.lexcivic.org
    abuseTypes(lang) { return fetch(`${this.base}/abuse-types?lang=${lang}`).then(r => r.json()); },
    createReport(payload) {
      return fetch(`${this.base}/reports?lang=${payload.idioma}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      }).then(r => r.json());
    },
    listReports(lang) { return fetch(`${this.base}/stats?lang=${lang}`).then(r => r.json()); },
  };

  const lang = document.documentElement.lang || "fr";
  const tipoSelect = document.getElementById("tipo_abuso");
  if (tipoSelect) {
    API.abuseTypes(lang).then(data => {
      const types = data.types || {};
      tipoSelect.innerHTML = "";
      Object.keys(types).forEach(code => {
        const opt = document.createElement("option");
        opt.value = code;
        opt.textContent = `${types[code]} (${code})`;
        tipoSelect.appendChild(opt);
      });
    }).catch(() => {
      // Fallback minimal si API indisponible
      tipoSelect.innerHTML = `
        <option value="abuse_of_power">Abus de pouvoir (abuse_of_power)</option>
        <option value="administrative_corruption">Corruption administrative (administrative_corruption)</option>
        <option value="procedural_delay">Retards procéduraux (procedural_delay)</option>
        <option value="extortion">Extorsion (extortion)</option>
        <option value="medical_neglect">Négligence médicale (medical_neglect)</option>`;
    });
  }

  const form = document.getElementById("report-form");
  const status = document.getElementById("form-status");
  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      status.textContent = DICT[LexCivicI18N.lang].status_sending;
      const payload = {
        texto: document.getElementById("desc").value.trim(),
        tipo_abuso: document.getElementById("tipo_abuso").value,
        idioma: LexCivicI18N.lang,
        source: "web",
      };
      if (payload.texto.length < 10) {
        status.textContent = "Le texte est trop court.";
        return;
      }
      try {
        const res = await API.createReport(payload);
        status.textContent = DICT[LexCivicI18N.lang].status_success;
        form.reset();
      } catch (err) {
        status.textContent = DICT[LexCivicI18N.lang].status_error;
      }
    });
  }

  // Timeline placeholder
  const timeline = document.getElementById("timeline");
  if (timeline) {
    const typeSelect = document.getElementById("filter-type");
    API.abuseTypes(lang).then(data => {
      const types = data.types || {};
      typeSelect.innerHTML = `<option value="">Tous les types</option>`;
      Object.keys(types).forEach(code => {
        const opt = document.createElement("option");
        opt.value = code;
        opt.textContent = `${types[code]} (${code})`;
        typeSelect.appendChild(opt);
      });
    });

    const renderItems = (items) => {
      timeline.innerHTML = "";
      items.forEach((it) => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${it.type}</strong> — ${it.text} <br><span class="muted">${it.date}</span>`;
        timeline.appendChild(li);
      });
    };

    document.getElementById("apply-filters").addEventListener("click", () => {
      // Placeholder: remplacer par appel à /stats ou /reports list
      renderItems([
        { type: "Retards procéduraux", text: "Le procès a été retardé", date: "2025-11" },
        { type: "Extorsion", text: "Demande d'argent par un agent", date: "2025-10" },
      ]);
    });
  }
});
