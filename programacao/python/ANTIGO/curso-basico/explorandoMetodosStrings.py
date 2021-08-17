episodio = "Boku no hero - TEmporada 1, episódio 12"
episodioFormatado = episodio\
    .lower()\
    .replace("episódio", "ep")\
    .upper()\
    .replace("temporada", "s")

print(episodioFormatado)