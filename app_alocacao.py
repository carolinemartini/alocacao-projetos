import streamlit as st
import pandas as pd

AVALIADORES_POR_PROJETO = 5  # quantos avaliadores por projeto

def pode_avaliar(av, dist_projeto, cat_projeto):
    if av["Distrito"] == dist_projeto:
        return False
    if av[cat_projeto] != "SIM":
        return False
    if av["Carga"] >= av["MaxProjetos"]:
        return False
    return True

st.title("Alocação de Avaliadores para Projetos")

st.write("Faça upload dos arquivos CSV:")

uploaded_avaliadores = st.file_uploader("Upload avaliadores.csv", type=["csv"])
uploaded_projetos = st.file_uploader("Upload projetos.csv", type=["csv"])

if uploaded_avaliadores and uploaded_projetos:
    avaliadores = pd.read_csv(uploaded_avaliadores)
    projetos = pd.read_csv(uploaded_projetos)

    # Padroniza as respostas para maiúsculas e remove espaços
    for cat in ['Cat1','Cat2','Cat3','Cat4','Cat5','Cat6','Cat7','Cat8']:
        avaliadores[cat] = avaliadores[cat].str.strip().str.upper()

    avaliadores["Carga"] = 0
    alocacao = []

    if st.button("Rodar alocação"):
        for _, proj in projetos.iterrows():
            candidatos = [a for _, a in avaliadores.iterrows()
                          if pode_avaliar(a, proj["Distrito"], proj["Categoria"])]
            candidatos.sort(key=lambda x: x["Carga"])

            escolhidos = []
            for candidato in candidatos:
                if len(escolhidos) < AVALIADORES_POR_PROJETO:
                    escolhidos.append(candidato)
                else:
                    break

            if len(escolhidos) < AVALIADORES_POR_PROJETO:
                st.warning(f"Projeto {proj['Projeto']} tem apenas {len(escolhidos)} avaliadores possíveis.")

            for escolhido in escolhidos:
                idx = avaliadores.index[avaliadores["Avaliador"] == escolhido["Avaliador"]][0]
                avaliadores.at[idx, "Carga"] += 1
                alocacao.append({
                    "Projeto": proj["Projeto"],
                    "Categoria": proj["Categoria"],
                    "Avaliador": escolhido["Avaliador"]
                })

        alocacao_df = pd.DataFrame(alocacao)
        st.success("Alocação concluída!")

        st.subheader("Alocação detalhada (Projeto x Avaliador):")
        st.dataframe(alocacao_df)

        csv = alocacao_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV de alocação", csv, "alocacao_resultado.csv", "text/csv")

        agrupado = alocacao_df.groupby('Avaliador')['Projeto'].apply(list).reset_index()
        agrupado['Projetos'] = agrupado['Projeto'].apply(lambda x: ', '.join(x))
        agrupado = agrupado.drop(columns=['Projeto'])

        st.subheader("Alocação por Avaliador:")
        st.dataframe(agrupado)

        csv2 = agrupado.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV agrupado por avaliador", csv2, "alocacao_por_avaliador.csv", "text/csv")
