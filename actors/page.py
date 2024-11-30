import streamlit as st
import pandas as pd
import datetime
from st_aggrid import AgGrid
from actors.service import ActorService

actors = [
  {
    'id': 1,
    'name': 'Da Vinci'
  },
  {
    'id': 2,
    'name': 'Stallone'
  },
  {
    'id': 3,
    'name': 'Chuck Norris'
  },
]


def show_actors():
  actor_service = ActorService()
  actors = actor_service.get_actors()

  if actors:
    st.write('Lista de Atores/Atores')

    actors_df = pd.DataFrame(actors)
    
    AgGrid(
      data=actors_df,
      reload_data=True,
      key='actors_grid'
    )
  else:
    st.warning('Nenhum autor cadastrado')

  st.title('Cadastrar novo(a) Ator/Atroz')

  name = st.text_input('Nome do Ator/Atroz')

  birthday = st.date_input(
    label='Data de Nascimento',
    value=datetime.today(),
    min_value=datetime(1600, 1, 1).date(),
    max_value=datetime.today(),
    format='DD/MM/YYYY'
  )

  nationality_dropdown = ['BRAZIL', 'USA']

  nationality = st.selectbox(
    label='Nacionalidade',
    options=nationality_dropdown
  )

  if st.button('Cadastrar'):
    new_actor = actor_service.create_actor(
      name=name,
      birthday=birthday,
      nationality=nationality
    )

    if new_actor:
      st.rerun()
    else:
      st.error('Erro ao cadastrar Ator/Atriz. Verifique os campos')
      
    st.success(f'Ator/Atriz {name} cadastrado com sucesso')

