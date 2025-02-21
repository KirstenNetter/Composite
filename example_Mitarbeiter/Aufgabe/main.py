from src.arbeiter import Arbeiter
from src.leitenderAngestellter import LeitenderAngestellter

"""
In src/stelle.py ist die Methode nenne_anzahl definiert.
Sie soll die Anzahl der Arbeiter zurückliefern, die der jeweiligen Stelle zu- bzw. untergeordnet sind.
Auf einen Arbeiter angewandt, gibt dieser nur sich selbst zurück.
Auf einen leitenden Angestellten angewandt, wird die Gesamtzahl aller ihm unterstellten Arbeiter zurückgegeben, wobei die leitenden Angestellten selbst nicht mitgezählt werden.
--------------
Deine Aufgabe:
--------------
Implementiere die entsprechenden Methodenkörper in src/arbeiter.py und src/leitenderAngestellter.py.
Führe dann diese main.py aus, um zu testen, ob alles funktioniert.
"""

if __name__ == "__main__":
   
    ceo = LeitenderAngestellter("CEO")

    anton       = LeitenderAngestellter("Anton") 
    berta       = LeitenderAngestellter("Berta")   
    charlotte   = LeitenderAngestellter("Charlotte")
    dora        = Arbeiter("Dora")
    emil        = Arbeiter("Emil")
    friedrich   = Arbeiter("Friedrich")
    gustav      = Arbeiter("Gustav")
    heinrich    = Arbeiter("Heinrich")
    ida         = Arbeiter("Ida")
    julius      = Arbeiter("Julius")

    # Aufbau der Hierarchie
    ceo.add(anton)
    ceo.add(berta)

    anton.add(charlotte)
    anton.add(dora)
    anton.add(emil)
       
    berta.add(friedrich)
    berta.add(gustav)
    berta.add(heinrich)

    charlotte.add(ida)
    charlotte.add(julius)

    ceo.display()
  
    print("\nGesamtanzahl Arbeiter:", ceo.nenne_anzahl())
    print("\nAnzahl Arbeiter unter Anton:", anton.nenne_anzahl())