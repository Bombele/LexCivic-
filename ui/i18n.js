// i18n.js
const DICT = {
  fr: {
    mission_title: "Documenter, classifier, mémoriser les abus pour la justice citoyenne.",
    mission_desc: "Interface sobre, multilingue et auditable pour la légitimité collective.",
    btn_declare: "Déclarer un abus",
    btn_memory: "Consulter la mémoire",
    btn_charter: "Accéder à la charte",
    declare_title: "Déclaration d’un abus",
    field_type: "Type d’abus",
    field_place: "Lieu",
    field_date: "Date",
    field_desc: "Description",
    field_file: "Preuve (optionnel)",
    btn_submit: "Envoyer",
    footer_rights: "Mémoire citoyenne et justice digitale",
    btn_home: "Accueil",
    charter_title: "Charte citoyenne et gouvernance",
    charter_point1_label: "Légitimité:",
    charter_point1: "Validation par juristes, ONG et diaspora.",
    charter_point2_label: "Transparence:",
    charter_point2: "Processus auditable, publication des métadonnées.",
    charter_point3_label: "Sécurité:",
    charter_point3: "Anonymisation par défaut, prudence opérationnelle.",
    charter_point4_label: "Multilinguisme:",
    charter_point4: "Bascule fluide FR/ES/LN.",
    memory_title: "Mémoire institutionnelle",
    btn_filter: "Filtrer",
    status_sending: "Envoi en cours...",
    status_success: "Dénonciation enregistrée.",
    status_error: "Erreur lors de l’envoi.",
  },
  es: {
    mission_title: "Documentar, clasificar y memorizar abusos para la justicia ciudadana.",
    mission_desc: "Interfaz sobria, multilingüe y auditable para la legitimidad colectiva.",
    btn_declare: "Declarar un abuso",
    btn_memory: "Consultar la memoria",
    btn_charter: "Acceder a la carta",
    declare_title: "Declaración de un abuso",
    field_type: "Tipo de abuso",
    field_place: "Lugar",
    field_date: "Fecha",
    field_desc: "Descripción",
    field_file: "Prueba (opcional)",
    btn_submit: "Enviar",
    footer_rights: "Memoria ciudadana y justicia digital",
    btn_home: "Inicio",
    charter_title: "Carta ciudadana y gobernanza",
    charter_point1_label: "Legitimidad:",
    charter_point1: "Validación por juristas, ONG y diáspora.",
    charter_point2_label: "Transparencia:",
    charter_point2: "Proceso auditable, publicación de metadatos.",
    charter_point3_label: "Seguridad:",
    charter_point3: "Anonimización por defecto, prudencia operativa.",
    charter_point4_label: "Multilingüismo:",
    charter_point4: "Cambio fluido FR/ES/LN.",
    memory_title: "Memoria institucional",
    btn_filter: "Filtrar",
    status_sending: "Enviando...",
    status_success: "Denuncia registrada.",
    status_error: "Error al enviar.",
  },
  ln: {
    mission_title: "Kokoma, kopona mpe kobomba babus mpo na bosembo ya bato.",
    mission_desc: "Interfás ya pete, ya malamu mpe oyo ekoki kosimbana, mpo na lolenge ya lisanga.",
    btn_declare: "Koteya abus",
    btn_memory: "Talela mémoire",
    btn_charter: "Kotɔnda na charte",
    declare_title: "Koteya abus",
    field_type: "Lolenge ya abus",
    field_place: "Esika",
    field_date: "Mokolo",
    field_desc: "Liyebisi",
    field_file: "Elembo (soki olingi)",
    btn_submit: "Tinda",
    footer_rights: "Memwa ya bato mpe bosembo ya digital",
    btn_home: "Libandeli",
    charter_title: "Charte ya bato mpe bokambi",
    charter_point1_label: "Lola ya bokonzi:",
    charter_point1: "Kopesa nzela na ba juristes, ONG, mpe diaspora.",
    charter_point2_label: "Koyebisa polele:",
    charter_point2: "Misala oyo ekoki kolandama, kobimisa metadata.",
    charter_point3_label: "Bobateli:",
    charter_point3: "Kobombama na kombo te, bokɛngɛli na mosala.",
    charter_point4_label: "Maloba ebele:",
    charter_point4: "Kokita/kokɔta malamu FR/ES/LN.",
    memory_title: "Memwa ya bapanzi",
    btn_filter: "Kopona",
    status_sending: "Kotinda...",
    status_success: "Rapɔrt esalaki malamu.",
    status_error: "Lokumu te na kotinda.",
  },
};

const LexCivicI18N = {
  lang: "fr",
  setLang(next) {
    this.lang = next;
    document.documentElement.lang = next;
    document.querySelectorAll("[data-i18n]").forEach(el => {
      const key = el.getAttribute("data-i18n");
      el.textContent = DICT[next][key] || DICT.fr[key] || el.textContent;
    });
  },
  init() {
    this.setLang(this.lang);
    document.querySelectorAll(".lang-switch .lang").forEach(btn => {
      btn.addEventListener("click", () => {
        document.querySelectorAll(".lang-switch .lang").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        this.setLang(btn.dataset.lang);
        localStorage.setItem("lexcivic_lang", btn.dataset.lang);
      });
    });
    const stored = localStorage.getItem("lexcivic_lang");
    if (stored) this.setLang(stored);
  },
};
