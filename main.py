stopwords = ['the', 'of', 'is', 'i', 'me', 'he', 'she', 'of', 'or', 'and', 'for', 'to']


def limpiar_stop_words(texto_a_limpiar):
    """
    :param texto_a_limpiar: Es un string que contiene palabras tanto en mayúsculas como minúsculas y algunas stopwords
    :return: Una nueva version el texto con todas sus palabras en minúscula y sin las stopwords

    El objetivo del ejercicio es hacer uso de comprensión de listas para generar una nueva version del texto en
    minúscula y sin stopwords.
    Pista: necesitaras las funciones .split() y .join() para convertir el texto a lista y viceversa
    """
    # Escribe tu código aquí.

    lower_text = texto_entrada.lower()
    list_words = lower_text.split()
    list_words = [ list_words[j] for j in range(len(list_words)) if list_words[j]  not in stopwords ]
    texto_a_limpiar =  " ".join(list_words)

    return texto_a_limpiar


if __name__ == '__main__':
    texto_entrada = "The NEW python prograMMER is a GREAT person. He is EXCEllent solving problems OF CODING anD " \
                    "writING scrIPts tO solve moDErn problems"
    texto_procesado = limpiar_stop_words(texto_entrada)
    texto_limpio = "new python programmer a great person. excellent solving problems coding writing scripts solve modern problems"
    assert texto_limpio == texto_procesado, "Tu función aun no limpia de forma correcta"
    print("Tu limpiador de texto funciona!. FELICITACIONES!!!")