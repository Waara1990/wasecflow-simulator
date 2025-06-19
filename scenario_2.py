# === Import des bibliothèques nécessaires ===
import streamlit as st
import json
from datetime import datetime

# === Configuration de la page Streamlit ===
st.set_page_config(page_title="Scénario 2 - Écriture du décès", layout="centered")

# === Titre principal ===
st.title("⛔ Scénario 2 — Tentative d’écriture du statut 'décès' par un secouriste")

# === Présentation du contexte ===
st.markdown("**Contexte** : Le secouriste tente d’enregistrer que le patient est décédé.")
st.markdown("⚠️ **Attention** : ce champ critique est **réservé uniquement aux médecins**, selon les règles RBAC de l’hôpital.")
st.divider()

# === Informations sur l'utilisateur simulé ===
role = "Secouriste"
action = "Écriture du statut décès"
autorisé = False  # Refusé selon la politique

# === Affichage des détails de la tentative ===
st.subheader("🔍 Détail de la tentative d'accès")
st.write(f"👤 **Utilisateur** : {role}")
st.write(f"📝 **Action demandée** : {action}")
st.write("📜 **Politique** : Écriture d’un décès = médecin uniquement")

# === Évaluation de la demande par le PDP local ===
st.subheader("🧠 Décision du PDP")
if autorisé:
    st.success("✅ Accès autorisé — Le statut 'décès' a été mis à jour.")
else:
    st.error("❌ Accès refusé — Le rôle 'Secouriste' n’a pas les droits nécessaires pour cette action critique.")

# === Journalisation dans les logs ===
st.subheader("🗂️ Journal d’audit")
log = {
    "utilisateur": "secouriste_001",
    "rôle": role,
    "action": action,
    "statut": "refusé",
    "raison": "Action critique réservée au médecin",
    "horodatage": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}
st.code(json.dumps(log, indent=4), language="json")
