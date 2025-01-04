import flet as ft
import requests
import pywhatkit as kit
from datetime import datetime

api_key = '7bd2db39af9e690736f560776a771f26'
genre_codes = [
    {'code': '28', 'genre': 'Ação'},
    {'code': '12', 'genre': 'Aventura'},
    {'code': '16', 'genre': 'Animação'},
    {'code': '35', 'genre': 'Comédia'},
    {'code': '80', 'genre': 'Crime'},
    {'code': '99', 'genre': 'Documentário'},
    {'code': '18', 'genre': 'Drama'},
    {'code': '10751', 'genre': 'Família'},
    {'code': '14', 'genre': 'Fantasia'},
    {'code': '36', 'genre': 'História'},
    {'code': '27', 'genre': 'Terror'},
    {'code': '104002', 'genre': 'Música'},
    {'code': '9648', 'genre': 'Mistério'},
    {'code': '10749', 'genre': 'Romance'},
    {'code': '878', 'genre': 'Ficção científica'},
    {'code': '53', 'genre': 'Thriller'},
    {'code': '37', 'genre': 'Faroeste'},
    {'code': '10770', 'genre': 'Cinema TV'},
    {'code': '10752', 'genre': 'Guerras'}
]

def check_actor(actor_name):
    url = f'https://api.themoviedb.org/3/search/person?api_key={api_key}&query={actor_name}&language=pt-BR'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            actor_id = data['results'][0]['id']
            return actor_id

        else:
            return None

    else:
        return None

def get_movies_list(genre_code, year, actor):
    final_movies = []
    url_genre_and_year = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&primary_release_date.gte={year}&with_genres={genre_code}&sort_by=popularity.desc&page=1&language=pt-BR"
    url_actor = f"https://api.themoviedb.org/3/person/{actor}/movie_credits?api_key={api_key}&vote_average.gte=7"
    response_genre_and_year = requests.get(url_genre_and_year)
    response_actor = requests.get(url_actor)
    if response_genre_and_year.status_code == 200 and response_actor.status_code == 200:
        movies_group_a = response_genre_and_year.json()
        movies_group_b = response_actor.json()
        for movie_a in movies_group_a['results']:
            if len(final_movies) <= 7:
                for genre in genre_codes:
                    if int(genre.get('code')) == int(movie_a.get('genre_ids')[0]):
                        final_movies.append({'title': movie_a['title'], 'release_date': movie_a['release_date'], 'genres': genre['genre'], 'poster_path': movie_a['poster_path'], 'overview': movie_a['overview']})

            else:
                break

        for movie_b in movies_group_b['cast']:
            if len(final_movies) <= 10:
                for genre in genre_codes:
                    if int(genre.get('code')) == int(movie_b.get('genre_ids')[0]):
                        final_movies.append({'title': movie_b['title'], 'release_date': movie_b['release_date'], 'genre': genre['genre'], 'poster_path': movie_b['poster_path'], 'overview': movie_b['overview']})

            else:
                break

        return final_movies

    else:
        return None

def send_movies_list(name, whatsapp, final_movies):
    hour = datetime.today().hour
    minute = datetime.today().minute
    messages = [f"_Olá **{name}** muito obrigado por testar o meu sistema, aproveite a sua lista com 10 filmes que você vai amar._"]
    for n, movie in enumerate(final_movies):
        messages.append(f'https://image.tmdb.org/t/p/w500{movie.get("poster_path")}\n\n{n+1}º {movie.get("title")}\nLançamento: {movie.get("release_date")}.\n\n\n{movie.get("overview")}')

    final_message = ''.join(messages)
    kit.sendwhatmsg(whatsapp, final_message, hour, minute + 2)

def main(page: ft.Page):
    def get_started_page():
        start_view = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text('Olá, seja bem vindo!', size=30, weight=ft.FontWeight.BOLD, italic=True, text_align=ft.TextAlign.CENTER),
                    ft.Text('Vamos descubrir quais são os melhores filmes para você assistir baseado nas suas respostas a questões triviais que faremos para você e com a integração com  API oficial da TMDb, enviaremos os resultados ao seu whatsapp!', size=20, font_family='Consolas', selectable=True, text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton(text='Bora Começar!', bgcolor=ft.Colors.GREY, color=ft.Colors.BLUE_50, width=200, height=30, on_click=questions_page)
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            expand=True,
            padding=20
        )

        page.add(start_view)

    def questions_page(e):
        def validate_form(e):
            submit_form_btn.text = 'Aguarde um momento...'
            submit_form_btn.disabled = True
            error_message = ''
            if not name_field.value or not all(a.isalpha() or a.isspace() for a in name_field.value):
                error_message = 'Este campo não pode estar vazio ou conter números e símbolos.'

            if error_message:
                name_field.error_text = error_message
                page.update()
                raise Exception(error_message)

            else:
                name_field.error_text = ''
                page.update()

            if not whatsapp_field.value or not all(b.isnumeric() for b in whatsapp_field.value):
                error_message = 'Este campo não pode estar vazio ou conter espaços, deve conter apenas um número de whatsapp válido.'

            if error_message:
                whatsapp_field.error_text = error_message
                page.update()
                raise Exception(error_message)

            else:
                whatsapp_field.error_text = ''
                page.update()

            country_code = code_field.value[0:4].split()
            for data in genre_codes:
                if data['genre'] == genre_field.value:
                    genre_final = data['code']

            if not year_field.value or not all(c.isnumeric() for c in year_field.value):
                error_message = 'Este campo não pode estar vazio ou conter espaços, deve conter apenas um ano entre 2008 e 2023.'

            elif not (2008 < int(year_field.value) < 2023):
                error_message = 'Este campo não pode estar vazio ou conter espaços, deve conter apenas um ano entre 2008 e 2023.'

            if error_message:
                year_field.error_text = error_message
                page.update()
                raise Exception(error_message)

            else:
                year_field.error_text = ''
                page.update()

            if not actor_field.value or not all(d.isalpha() or d.isspace() for d in actor_field.value):
                error_message = 'Este campo não pode estar vazio ou conter números e símbolos.'

            if error_message:
                actor_field.error_text = error_message
                page.update()
                raise Exception(error_message)

            else:
                actor_field.error_text = ''
                page.update()

            actor_id = check_actor(actor_field.value)
            if actor_id:
                movies_list = get_movies_list(genre_code=genre_final, year=year_field.value, actor=actor_id)
                if not movies_list:
                    page.open(modal_request_error)

                else:
                    submit_form_btn.disabled = False
                    submit_form_btn.text = 'Enviar novamente'
                    page.open(success_modal)
                    send_movies_list(name=name_field.value, whatsapp=f'{country_code}{whatsapp_field.value}', final_movies=movies_list)

            else:
                page.open(modal_actor_id_error)

        page.clean()
        questions_lv = ft.ListView(expand=True, spacing=10, padding=20)
        questions_lv.controls.append(ft.Text('Responda as questões abaixo e em seguida vamos te enviar uma mensagem para o seu whatsapp com os resultados da busca!', size=20, weight=ft.FontWeight.BOLD, italic=True))
        questions_lv.controls.append(ft.Text('Informe seu nome'))
        name_field = ft.TextField(label='Nome', expand=True)
        questions_lv.controls.append(ft.Row(controls=[name_field], expand=True, width=150))
        questions_lv.controls.append(ft.Text('Informe seu whatsapp'))
        whatsapp_field = ft.TextField(label='Whatsapp', expand=True)
        questions_lv.controls.append(ft.Row(controls=[whatsapp_field], expand=True, width=150))
        questions_lv.controls.append(ft.Text('Informe o código do seu país'))
        code_field = ft.Dropdown(
            label='Código',
            expand=True,
            options=[
                ft.dropdown.Option('+55 (Brasil)'),
                ft.dropdown.Option('+244 (Angola)'),
                ft.dropdown.Option('+351 (Portugal)'),
                ft.dropdown.Option('+258 (Moçambique)'),
                ft.dropdown.Option('+238 (Cabo Verde)'),
                ft.dropdown.Option('+245 (Guiné-Bissau)'),
                ft.dropdown.Option('+239 (São Tomé e Príncipe)'),
                ft.dropdown.Option('+670 (Timor Leste)'),
                ft.dropdown.Option('+240 (Guiné Equatorial)')
            ]
        )

        questions_lv.controls.append(ft.Row(controls=[code_field], expand=True))
        questions_lv.controls.append(ft.Text('Qual gênero de filmes você mais gosta?'))
        genre_field = ft.Dropdown(
            expand=True,
            label='Gênero',
            options=[
                ft.dropdown.Option('Ação'),
                ft.dropdown.Option('Aventura'),
                ft.dropdown.Option('Animação'),
                ft.dropdown.Option('Comédia'),
                ft.dropdown.Option('Crime'),
                ft.dropdown.Option('Documentário'),
                ft.dropdown.Option('Drama'),
                ft.dropdown.Option('Família'),
                ft.dropdown.Option('Fantasia'),
                ft.dropdown.Option('História'),
                ft.dropdown.Option('Terror'),
                ft.dropdown.Option('Música'),
                ft.dropdown.Option('Mistério'),
                ft.dropdown.Option('Romance'),
                ft.dropdown.Option('Ficção científica'),
                ft.dropdown.Option('Thriller'),
                ft.dropdown.Option('Faroeste'),
                ft.dropdown.Option('Cinema TV'),
                ft.dropdown.Option('Guerras'),
            ]
        )

        questions_lv.controls.append(ft.Row(controls=[genre_field], expand=True, width=150))
        questions_lv.controls.append(ft.Text('Filmes lançados após o ano:'))
        year_field = ft.TextField(label='Ano', expand=True)
        questions_lv.controls.append(ft.Row(controls=[year_field], expand=True, width=150))
        questions_lv.controls.append(ft.Text('Informe seu ator favorito?'))
        actor_field = ft.TextField(label='Ator', expand=True)
        questions_lv.controls.append(ft.Row(controls=[actor_field], expand=True, width=150))
        submit_form_btn = ft.ElevatedButton(text='Enviar', bgcolor=ft.Colors.GREY, color=ft.Colors.BLUE_50, expand=True, on_click=validate_form)
        questions_lv.controls.append(ft.Row(controls=[submit_form_btn], expand=True, width=100))
        page.add(questions_lv)

    page.title = 'YourNextFilm - Seu Próximo Filme'
    page.appbar = ft.AppBar(
        title=ft.Text('YourNextFilms', color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
        center_title=False,
        bgcolor=ft.Colors.RED_400,
        actions=[ft.IconButton(ft.Icons.QUESTION_MARK_OUTLINED, on_click=lambda e: page.open(modal_info))]
    )

    modal_actor_id_error = ft.AlertDialog(title=ft.Text('Ator não encontrado', size=30, weight=ft.FontWeight.BOLD), content=ft.Text('Não foi possível encontrar o ator especificado na base de dados do TMDb, ou talvez tenha tido uma falha na requesição. Verifique se está conectado a internet estável e se o campo com o nome do ator está correto e tente novamente porfavor.', font_family='Consolas', selectable=True, size=20))
    modal_request_error = ft.AlertDialog(title=ft.Text('Falha na requesição', size=30, weight=ft.FontWeight.BOLD), content=ft.Text('Verifique se a sua conexão com a internet está estavel e inicie sessão no whatsapp web para enviarmos a mensagem.', font_family='Consolas', selectable=True, size=20))
    success_modal = ft.AlertDialog(title=ft.Text('Sucesso!', size=30, weight=ft.FontWeight.BOLD), content=ft.Text('A requesição foi feita com sucesso dentro de alguns minutos as mensagens vão cair no número fornecido. Não feche o programa!', font_family='Consolas', selectable=True, size=20))
    modal_info = ft.AlertDialog(title=ft.Text('Descrição', size=30, weight=ft.FontWeight.BOLD), content=ft.Text('Este programa tem um foco em demonstrar meus conhecimentos em programação desktop com Flutter usando o Python e habilidades de conexão com APIs exemplificando aqui fazendo uma conexão gratuita com a TMDb (The Movie Database) com o objetivo de obter dados de filmes para usar como base na construção de uma lista de recomendações que se adequam as suas respostas e essa mesma lista será enviada para o Whatsapp de um número forncido por si através de um Bot.\nOBS: TESTE O PROGRAMA COM UM NÚMERO DE WHATSAPP DE TESTE OU ENVIE SIMPLESMENTE MENSAGENS PARA SI POIS O WHATSAPP PODE BLOQUEAR SEU NÚMERO SE ESTA AUTOMAÇÃO FOR USADA VÁRIAS VEZES.\n\nCopyright © 2025 Manassés Ndombele - Programador Pleno', font_family='Consolas', selectable=True, size=20))
    get_started_page()

ft.app(target=main)
