from config import PATH_TO_SAVE
from .dbpedia_journal import DBpediaJournal

# Создаём нужный журнал, который потому будем использовать в эксперименте
journal = DBpediaJournal(PATH_TO_SAVE)
