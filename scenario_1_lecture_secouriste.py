import streamlit as st                  # Streamlit pour l'interface utilisateur
import time                            # Pour simuler le temps de traitement
import datetime                        # Pour afficher l'heure d'accès

# Configuration de l'application Streamlit
st.set_page_config(page_title="Scénario 1 : Lecture Secouriste", layout="wide")
st.title("📘 Scénario 1 : Lecture des signes vitaux par un secouriste")

# --- Informations simulées ---
utilisateur = "Secouriste"
ressource = "Signes vitaux (température, pouls, saturation, etc.)"
role_autorisé = "Secouriste"
autorisé = True  # Oui, dans ce scénario, le secouriste a le droit de lire

# --- Affichage des détails de la requête ---
st.subheader("🧾 Détails de la requête d'accès")
st.write(f"👤 Utilisateur : **{utilisateur}**")
st.write(f"📄 Ressource demandée : **{ressource}**")
st.write(f"🔐 Rôle requis : **{role_autorisé}**")

# --- Simulation de passage au PDP (Policy Decision Point) ---
st.subheader("⚙️ Traitement de la requête par le PDP")
with st.spinner("Analyse des règles de sécurité en cours..."):
    time.sleep(2)  # Pause pour effet de traitement
    if autorisé:
        st.success("✅ Accès accordé par le PDP")
    else:
        st.error("❌ Accès refusé par le PDP")

# --- Journalisation dans la Blockchain (simulation) ---
st.subheader("🧾 Journalisation dans la Blockchain")
horodatage = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"📅 Action : Lecture des signes vitaux")
st.write(f"👤 Par : {utilisateur}")
st.write(f"🕒 À : {horodatage}")
st.info("🛡️ L'action a été consignée dans la Blockchain (simulation)")

# --- Affichage des données (lecture autorisée) ---
st.subheader("📊 Données visibles par le secouriste")
signes_vitaux = {
    "Température corporelle": "37.1°C",
    "Pouls": "78 bpm",
    "Pression artérielle": "120/80 mmHg",
    "Saturation O₂": "97%",
    "Fréquence respiratoire": "16 rpm"
}

# Affichage dans une boîte claire
st.json(signes_vitaux)
