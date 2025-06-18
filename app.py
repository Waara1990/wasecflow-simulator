import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulateur WaSec-Flow", layout="wide")
st.title("🔐 Simulateur interactif WaSec-Flow (version démo)")

utilisateur = st.selectbox("👤 Sélectionnez l'utilisateur :", ["Secouriste", "Médecin", "PDP"])
action = st.selectbox("🔍 Action demandée :", ["Lire les signes vitaux", "Modifier diagnostic", "Accéder au dossier complet"])

autorisations = {
    "Secouriste": ["Lire les signes vitaux"],
    "Médecin": ["Lire les signes vitaux", "Modifier diagnostic", "Accéder au dossier complet"],
    "PDP": []
}

if action in autorisations.get(utilisateur, []):
    resultat = "✅ Accès accordé"
else:
    resultat = "❌ Accès refusé"

st.subheader("🧭 Graphe d'accès dynamique")

G = nx.DiGraph()
G.add_node("Utilisateur", role=utilisateur)
G.add_node("PDP")
G.add_node("Ressource", action=action)
G.add_node("Blockchain")

G.add_edge("Utilisateur", "PDP", action="requête")
G.add_edge("PDP", "Ressource", action=resultat)
G.add_edge("PDP", "Blockchain", action="log décision")

pos = {
    "Utilisateur": (0, 0),
    "PDP": (1, 1),
    "Ressource": (2, 0),
    "Blockchain": (1, -1)
}

fig, ax = plt.subplots(figsize=(8, 5))
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="#AED6F1", edgecolors='black')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='-|>')
nx.draw_networkx_edge_labels(G, pos, edge_labels={
    ("Utilisateur", "PDP"): "requête",
    ("PDP", "Ressource"): resultat,
    ("PDP", "Blockchain"): "journalisation"
})

plt.axis('off')
st.pyplot(fig)

st.subheader("🔎 Résultat de la décision")
st.info(f"**{utilisateur}** → {action} → **{resultat}**")
