# Backend

Das Backend basiert auf Python und nutzt Flask für die REST-Schnittstelle.

## Neuen Crawler implementieren

Die Crawler liegen in dem Ordner [crawlers](crawlers) und müssen folgendes erfüllen:

* Abgeleitet von `BaseCrawler`
  * implementiert somit die Methode `def crawl(self, restaurant: RestaurantDto) -> Type[list[MenuDto]]`
* In [`crawlers/__register__.py`](crawlers/__register__.py) muss der neue Crawler registriert werden:
  * Ein *Identifier*, der auch in der Datenbank beim Restaurant für den Crawler hinterlegt wird
  * Der lamda-Aufruf des Crawlers

### Testen des Crawlers

Um den Crawler bei der Implementierung leichter zu testen, 
gibt es das CLI-Programm `crawler_cli.py`.

In diesem ersetzt man die globalen Variablen 

```python
restaurant_crawler_to_test = BioCateringSafranCrawler()
url_to_crawl = "https://biocatering-safran.de/"

```

mit dem zu testenden Crawler und gibt die URL zum crawlen an.

Das CLI-Programm gibt die Ergebnisse auf der Console aus und speichert noch nichts in der Datenbank.
