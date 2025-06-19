import streamlit as st
import json
from datetime import datetime

# 📌 Configuration de la page Streamlit
st.set_page_config(page_title="Scénario 1 - Lecture Secouriste", layout="centered")

# === TITRE PRINCIPAL ===
st.title("🆘 Scénario 1 — Lecture des signes vitaux + antécédents par un secouriste")

# === CONTEXTE DU SCÉNARIO ===
st.markdown("**Contexte** : Le secouriste est devant une victime inconsciente après un séisme.")
st.markdown("Il prend les signes vitaux manuellement, puis tente d’accéder aux antécédents médicaux.")
st.divider()

# === ÉTAPE 1 : Lecture directe des signes vitaux (locale) ===
st.subheader("📍 Lecture locale des signes vitaux")

# Données simulées que le secouriste mesure lui-même
signes_vitaux = {
    "température": "38.6°C",
    "fréquence cardiaque": "110 bpm",
    "tension artérielle": "100/65 mmHg"
}
st.json(signes_vitaux)

# Résultat visuel
st.success("✅ Lecture locale autorisée — Le secouriste mesure lui-même les signes vitaux")

st.divider()

# === ÉTAPE 2 : Tentative d'accès aux antécédents médicaux ===
st.subheader("🔐 Consultation des antécédents médicaux")

# Le secouriste coche ces cases pour prouver les conditions d’urgence
urgence = st.checkbox("✅ Contexte d’urgence détecté", value=True)
certificat_valide = st.checkbox("✅ Certificat du secouriste vérifié", value=True)
aucun_medecin = st.checkbox("✅ Aucun médecin n’est disponible", value=True)

# Politique d'élévation temporaire : toutes les conditions doivent être vraies
if urgence and certificat_valide and aucun_medecin:
    st.success("🎯 Élévation temporaire accordée vers le rôle 'assistant médical'")
    
    # Affichage des antécédents autorisés grâce à l'élévation
    antecedents = {
        "antécédents médicaux": [
            "Diabète de type 1",
            "Allergie : Pénicilline",
            "Opération cardiaque (2019)"
        ]
    }
    st.json(antecedents)

    # Simuler une journalisation dans une blockchain locale
    st.info("📄 Action journalisée dans la blockchain locale")
    log = {
        "utilisateur": "secouriste_001",
        "action": "lecture antécédents",
        "heure": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        "rôle_temporaire": "assistant_médical",
        "motif": "urgence"
    }
    st.code(json.dumps(log, indent=4), language="json")

else:
    # Si l'une des conditions n'est pas cochée
    st.error("❌ Accès refusé — Condition d’élévation non remplie")
