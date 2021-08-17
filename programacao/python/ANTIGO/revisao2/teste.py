from modelo import Filme, Serie, Playlist

if __name__ == '__main__':

    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)
    tmep = Filme('todo mundo em panico', 1999, 100)
    demolidor = Serie('Demolidar', 2016, 2)


    vingadores.dar_like()
    tmep.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()

    # print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Durção: {vingadores.duracao} - Like: {vingadores.likes}")
    # print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}")

    filmes_e_series = [vingadores, atlanta, demolidor, tmep]

    playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

    print(vingadores in playlist_fim_de_semana)

    print(f'Tamanho da playlist {len(playlist_fim_de_semana)}')

    for programa in playlist_fim_de_semana: # Polimorfismo
        # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
        # print(f"Nome: {programa.nome} - Ano: {programa.ano} - D: {detalhes} - Likes: {programa.likes}")
        print(programa)

