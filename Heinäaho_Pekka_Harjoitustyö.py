from datetime import datetime, timedelta
import time

def tulosta_hitaasti(teksti, viive=0.1):
    for merkki in teksti:
        print(merkki, end='', flush=True)
        time.sleep(viive)

class paikka:
    def __init__(self, nimi, kuvaus, ovi, kohteliaisuus_annettu):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.ovi = ovi
        self.kohteliaisuus_annettu = kohteliaisuus_annettu
        self.itemit = []
        self.location = []

    def addItem(self, item):
        self.itemit.append(item)

    def removeItem(self, item):
        self.itemit.remove(item)

    def tulosta_paikka(self):
        tulosta_hitaasti(f'\nOlet paikassa: {self.nimi}.\n', viive=0.02)

    def katsele_paikka(self):
        if self.nimi == 'aula':
            tulosta_hitaasti(f'{self.kuvaus}\nTutkittuasi paikat, löydät:\n', viive=0.02)
        elif self.nimi == 'eteinen':
            tulosta_hitaasti(f'{self.kuvaus}\nOvi ulos on {self.ovi}. Tutkittuasi paikat, löydät vartijan pöydältä:\n', viive=0.02)
        else:
            tulosta_hitaasti(f'{self.kuvaus}\nOvi on {self.ovi}. Tutkittuasi paikat, löydät:\n', viive=0.02)
        if not self.itemit:
            tulosta_hitaasti('et mitään...\n', viive=0.02)
        else:
            tulosta_huoneen_itemit(self.itemit)


# kerros 1
ulkona = paikka('ulkona', 'Ulkona on raikas aamuilma.', 'kiinni', False)
eteinen = paikka('eteinen', 'Vartija lukee lehteä työpisteellään. \nEteisestä on ovi ulos, pohjoisessa on kulku käytävälle ja sivulla portaat ylös sekä idässä näkyy odotusaula.', 'kiinni', False)
aula = paikka('odotusaula', 'Lännessä on eteinen. Aulassa on iso divaanisohva ja kaksi isoa nojatuolta. Seinällä on tv sekä taideteos, jossa lukee "Unet päivässä pitää lääkärin loitolla". Alat myös itsekin tuntea hieman väsymystä.', 'auki', False)
kaytava1_kahvio = paikka('käytävä, kahvion ovi', 'Kahvion ovessa on ikkuna. Kahviossa näkyy olevat valot päällä. Käytävä jatkuu pohjoiseen ja etelässä on eteinen.', 'kiinni', False)
kahvio = paikka('kahvio', 'Kahviossa ei ole ketään. Seinällä on kello ja sen vieressä tulletusikkuna, josta tulee raikasta aamuilmaa sisälle.', 'kiinni', False)
kaytava1_varasto = paikka('käytävä, varaston ovi', 'Ovessa lukee "Varasto". Käytävä jatkuu pohjoiseen ja etelään.', 'kiinni', False)
varasto = paikka('varasto', 'Hyllyillä on arkistomappeja monelta eri vuodelta. Viimeisen kuukauden mappi puuttuu.', 'kiinni', False)
kaytava1_kokoushuone = paikka('käytävä, kokoushuoneen ovi', 'Ovessa lukee "Kokoushuone". Käytävä jatkuu pohjoiseen ja etelään.', 'kiinni', False)
kokoushuone = paikka('kokoushuone', 'Johtaja istuu pöydän takana ja nostaa katseensa sinuun.', 'kiinni', False)
kaytava1_toimisto = paikka('käytävä, toimiston ovi', 'Toimiston ovi on auki ja toimistossa näkyy pöydän takana istuvan sihteeri.', 'auki', False)
toimisto = paikka('toimisto', 'Toimistossa istuu sihteeri.\n"Johtaja odottaa sinua kokoushuoneessa"\n', 'auki', False)

# kerros 2
kaytava2_sahkohuone = paikka('käytävä, sähköhuoneen ovi', 'Näet oven, jossa lukee "Sähköpääkeskus". Pohjoisessa on käytävä ja sivulla portaat alas.', 'kiinni', False)
sahkohuone = paikka('sähköhuone', 'Huoneessa on iso sähkökaappi, jossa on sähkötaulu johdonsuojakytkimineen.', 'kiinni', False)
kaytava2_talonmies = paikka('käytävä, talonmiehen ovi', 'Huoneen ovi on auki ja kuulet jonkun hyräilevät huoneessa. Käytävä jatkuu pohjoiseen ja etelään.', 'auki', False)
talonmies = paikka('talonmiehen huone', 'Talonmies on työntouhussa korjaamassa rikkimennyttä laitetta. Astuttuasi huoneeseen talonmies hymyilee sinulle.', 'auki', False)
kaytava2_palvelinsali = paikka('käytävä, palvelinsalin ovi', 'Näet oven, jossa lukee "Palvelinsali - Pääsy Kielletty!". käytävä jatkuu pohjoiseen ja etelään.', 'kiinni', False)
palvelinsali = paikka('palvelinsali', 'Palvelinsalissa hyrrää palvelikoneet, pienet ledivalot vilkkuvat laitteissa ja piuhat ovat siististi niputetut.', 'kiinni', False)
kaytava2_siivouskomero = paikka('käytävä, siivouskomeron ovi', 'Ovessa ei lue mitään. Käytävä jatkuu pohjoiseen ja etelään.', 'kiinni', False)
siivouskomero = paikka('siivouskomero', 'Komeron nurkat ovat pölyisiä ja siivousvälineitä on ympäriinsä', 'kiinni', False)
kaytava2_tyohuone = paikka('käytävä, tyohuoneen ovi', 'Näet ovessa lukevan "Työhuone". Käytävä jatkuu pohjoiseen ja etelään.', 'kiinni', False)
tyohuone = paikka('tyohuone', 'Saavut huoneeseen ja huomaat, että ikkuna on jäänyt auki. Huone on todella kylmä yöllisen hallan vuoksi.', 'kiinni', False)
kaytava2_veijo = paikka('käytävä, Veijon huone ovi', 'Olet käytävän päässä. Käytävä jatkuu etelään.', 'lukossa', False)
veijo = paikka('Veijon huone', 'Veijon ahkeroi läppärillään. Veijo kiittää sinua avusta ja jatkaa töitään.', 'lukossa', False)

# itemit
eteinen.itemit = ['kolikko']
aula.itemit = ['unet', 'sohvatyyny', 'kaukosäädin']
kahvio.itemit = ['kahvinkeitin', 'pullapitko', 'seinäkello']
varasto.itemit = ['arkistomappi']
kokoushuone.itemit = ['työsopimus']
toimisto.itemit = ['henkilökortti-vierailija']
sahkohuone.itemit = ['ruuvimeisseli', 'verkkokaapeli']
talonmies.itemit = ['avain']
palvelinsali.itemit = ['käytöstä poistettu reititin']
siivouskomero.itemit = ['harja', 'puhdistusliinoja']
tyohuone.itemit = ['kynä', 'henkilökortti-keijo']
veijo.itemit = ['lompakko']

# paikannus
ulkona.location = [1,1,1]
eteinen.location = [2,1,1]
aula.location = [3,1,1]
kaytava1_kahvio.location = [2,2,1]
kahvio.location = [1,2,1]
kaytava1_varasto.location = [2,3,1]
varasto.location = [1,3,1]
kaytava1_kokoushuone.location = [2,4,1]
kokoushuone.location = [1,4,1]
kaytava1_toimisto.location = [2,5,1]
toimisto.location = [1,5,1]
kaytava2_sahkohuone.location = [2,1,2]
sahkohuone.location = [1,1,2]
kaytava2_talonmies.location = [2,2,2]
talonmies.location = [1,2,2]
kaytava2_palvelinsali.location = [2,3,2]
palvelinsali.location = [1,3,2]
kaytava2_siivouskomero.location = [2,4,2]
siivouskomero.location = [1,4,2]
kaytava2_tyohuone.location = [2,5,2]
tyohuone.location = [1,5,2]
kaytava2_veijo.location = [2,6,2]
veijo.location = [1,6,2]

kaikki_paikat = [ulkona, eteinen, aula, kaytava1_kahvio, kahvio, kaytava1_varasto, varasto, kaytava1_kokoushuone, kokoushuone, kaytava1_toimisto, toimisto, kaytava2_sahkohuone, sahkohuone, kaytava2_talonmies, talonmies, kaytava2_palvelinsali, palvelinsali, kaytava2_siivouskomero, siivouskomero, kaytava2_tyohuone, tyohuone, kaytava2_veijo, veijo]
tervetuloa = 'Tervetuloa peliin! Töypaikan löytäminen on haastavaa. Avoimia paikkoja on rajallisesti ja tekijöitä paljon. Kuinka sinä löydät oman paikkasi ja kuinka tulet palkatuksi? Tehtäväsi on yksinkertainen: Saada johtaja vakuuttumaan, että sinä olet heidän etsimänsä pätevä tekijä toimeen!'
alku_kuvaus = 'Aamusi on ollut kiireinen valmistautuessasi haastatteluun. Yön aikana polkupyöräsi oli hävinnyt kerrostalon pihalta, joten jouduit käyttämään bussia. Olet nyt saapunut ison ohjelmistotalon pihaan. Kello on 9:49 ja tapaamisesi on sovittu ajalle 10:00. Edessäsi on ohjelmistotalon pääovi.'

pelin_nimi = 'PAIKKA ON TEIDÄN!'
pelaaja = {'nimi': 'nimetön', 'pisteet': 0, 'sijainti': ulkona, 'salkku': ['ansioluettelo', 'tutkintotodistus', 'läppäri']}
aika = datetime(2025, 11, 4, 9, 49)
tapaaminen_aika = datetime(2025, 11, 4, 10, 00)
minuutti = timedelta(minutes=1)
kahvi_keitetty = False

print()
print(pelin_nimi.center(57, '='))
pelaaja['nimi'] = input('Pelaajan nimi: ')
tulosta_hitaasti(f'\n{tervetuloa}\n', viive=0.02)
tulosta_hitaasti(f'{alku_kuvaus}\n', viive=0.02)

def tulosta_huoneen_itemit(huoneen_itemit):
    for item in huoneen_itemit:
        print(item)

def tulosta_apua():
    print('_'*57)
    print(f"{'| Voit antaa komentoja:':<55}{'|'}")
    print(f"{'|':<55}{'|'}")
    print(f"{'| apua/help':<55}{'|'}")
    print(f"{'| lopeta':<55}{'|'}")
    print(f"{'| katsele':<55}{'|'}")
    print(f"{'| mukana':<55}{'|'}")
    print(f"{'| hymyile':<55}{'|'}")
    print(f"{'| kiitä':<55}{'|'}")
    print(f"{'| avaa ovi':<55}{'|'}")
    print(f"{'| avaa tv':<55}{'|'}")
    print(f"{'| mene ovesta/ovi/sisään':<55}{'|'}")
    print(f"{'| mene pohjoiseen/poh/p':<55}{'|'}")
    print(f"{'| mene etelään/ete/e':<55}{'|'}")
    print(f"{'| mene itään/itä/i':<55}{'|'}")
    print(f"{'| mene länteen/län/l':<55}{'|'}")
    print(f"{'| mene ylös/y':<55}{'|'}")
    print(f"{'| mene alas/a':<55}{'|'}")
    print(f"{'| ota (esine)':<55}{'|'}")
    print(f"{'| pudota (esine)':<55}{'|'}")
    print(f"{'| anna (esine)':<55}{'|'}")
    print(f"{'| piilota (esine)':<55}{'|'}")
    print(f"{'| käytä (esine)':<55}{'|'}")
    print(f"{'| näytä pisteet':<55}{'|'}")
    print(f"{'| näytä kartta':<55}{'|'}")
    print(f"{'| katso kello/kelloa':<55}{'|'}")
    print(f"{'| keitä kahvit/kahvia/sumpit/kahvi':<55}{'|'}")
    print(f"{'| juo kahvit/kahvia/sumpit/kahvi':<55}{'|'}")
    print(f"{'|':<55}{'|'}")
    print(f"{'|':<55}{'|'}")
    print(f"{'| TEHTÄVÄN VINKKI':<55}{'|'}")
    print(f"{'| Etsi Johtaja ja toimita hänelle hänen':<55}{'|'}")
    print(f"{'| pyytämät asiat.':<55}{'|'}")
    print(f"{'|':<55}{'|'}")
    print('_'*57)

def nayta_kartta():
    print()
    print(f'1krs    2krs')
    print(f'         X X')
    print(f'X X      X X')
    print(f'X X      X X')
    print(f'X X      X X')
    print(f'X X      X X')
    print(f'X X X    X X')
    print(f'  ^')
    print(f'  |')
    print(f'  eteinen')
    print()

def kaatuminen_eteisessa():
    tulosta_hitaasti('Avatessasi oven ja astuessasi sisään, tuuli tempaisee oven sepposen selälleen, salkkusi aukeaa ja salkussasi olevat dokumentit lentävät eteisaulan lattialle. Talon vartija auttaa sinua keräämään dokumenttisi ja ojentaa ne takaisin sinulle.', viive=0.02)
    pelaaja['salkku'].remove('ansioluettelo')
    
def poistutko():
    tulosta_hitaasti('Vartija: "Oletko jo lähdössä? Löysin vielä yhden pudottamasi dokumentin, tämä taitaa olla ansioluettelosi. Tässä ole hyvä. Sinä taidat olle se joku tuli haastatteluun."\n', viive=0.02)

def vartija_ohjaa_paikkaan_aula1():
    tulosta_hitaasti('"Johtaja odottaa sinua."\n\nVartija ohjaa sinut käytävälle.\n', viive=0.02)

def ovi_lukossa():
    print('Ovi on lukossa')

def ottaa_unet():
    tulosta_hitaasti('Oikaiset itsesi hetkeksi mukavalle sohvalle ja torkahdat viideksi minuutiksi...\n', viive=0.02)
    tulosta_hitaasti('...z...z...z...\n\n', viive=0.1)
    time.sleep(0.7)
    tulosta_hitaasti('Heräät ja huomaat että torkahdit!\n', viive=0.02)
    print(f'Kello näyttää {aika}')
    tulosta_hitaasti('Nyt on kiire!\n', viive=0.02)

def lompakko_vietiin():
    tulosta_hitaasti('"Hei! Veitkö lompakkoni?!?!"\nHuutaa Veijo perääsi.\n', viive=0.02)
    tulosta_hitaasti('...voi...ei...\n\n', viive=0.1)
    time.sleep(0.7)
    tulosta_hitaasti('Veijo hakee vartijan ja sinut saatetaan ulos talosta...\n', viive=0.02)
    game_over_teksti()

def epaselva():
    print('Epäselvä komento')

def avaa_tv():
    if 'kaukosäädin' in aula.itemit or 'kaukosäädin' in pelaaja['salkku']:
        tulosta_hitaasti('TV:stä tulee aamu-uutiset, joissa on aiheena ICT-alan työllisyystilanne. Toimittaja lukee uutisia:\n', viive=0.02)
        time.sleep(0.7)
        tulosta_hitaasti('"Vain seniori tason paikkoja tuntuu olevan tarjolla tällä hetkellä ICT-alalla.\n', viive=0.02)
        tulosta_hitaasti('Ehdoton suositus on olla valmiina heti, jos töitä tarjotaan. Ja kuten aina, muistakaa hymyillä toisillenne!......"\n', viive=0.02)
        time.sleep(0.7)
        tulosta_hitaasti('\nSuljet TV:n ja aiot itsekin olla juuri tänään skarppina!\n', viive=0.02)
    else:
        tulosta_hitaasti('Et löydä kaukosäädintä\n', viive=0.02)

def kahvin_keitto():
    tulosta_hitaasti('Kahvipannu tiputtaa kahvia...\n', viive=0.02)
    time.sleep(0.7)
    print('tip...')
    time.sleep(0.7)
    print('tip...')
    time.sleep(0.7)
    print('tip...')
    time.sleep(0.7)
    print('tip...')
    time.sleep(0.7)
    print('tip...')
    time.sleep(0.7)
    tulosta_hitaasti('\nTuore keskiafrikkalainen kahvipavun aromi tuoksahtaa nenääsi. Kahvi on valmista.\n', viive=0.02)

def juo_kahvi():
    print('Juot kahvin ja olosi piristyy!')

def sihteeri_kysyy():
    tulosta_hitaasti('Toimistossa istuva sihteeri sanoo sinulle:\n"Onhan sinulla ansioluettelosi mukana? Jos ei ole, niin sinun pitää hakea se."\n', viive=0.02)    

def sihteerin_soitto(p):     
    tulosta_hitaasti('Johtajan pöydällä oleva puhelin soi.\n', viive=0.02)
    time.sleep(2.5)
    print('ring')
    time.sleep(0.5)
    print('ring')
    time.sleep(0.5)
    print('ring')
    time.sleep(0.5)
    print('ring')
    time.sleep(0.5)
    tulosta_hitaasti('Johtajan puhui lyhyen puhelun ja sulki puhelimen.\n', viive=0.02)
    time.sleep(1.0)
    if p >= 300:
        tulosta_hitaasti('"Sihteerikin soitti ja kertoi että olet ollut hyvin mukava tänä aamuna henkilökunnallemme."\n', viive=0.02)
    else:
        tulosta_hitaasti('"Sihteeri soitti ja kertoi että olet ollut etäisen oloinen tänä aamuna henkilökunnallemme."\n', viive=0.02)
    if kahvi_keitetty == True:
        tulosta_hitaasti('"Kahvin olit tainnut keittää heille."\n', viive=0.02)

def voitto_palvelinsalissa():
    tulosta_hitaasti('\nPääsit sisään yrityksen palvelimelle. Näet kaikki henkilöstön tiedot ja pääset käsiksi tietokantaan.\n', viive=0.02)
    time.sleep(1.0)
    tulosta_hitaasti('Näppärillä IT-taidoillasi onnistut lisäämään itsesi yrityksen henkilöstöön ja asetat kuukausipalkaksesi 12 000 €/kk\n', viive=0.02)
    time.sleep(1.0)
    tulosta_hitaasti('Olet onnistuneesti läpäissyt "PAIKKA ON TEIDÄN" pelin vilunkikonstein!!!\n', viive=0.02)
    time.sleep(1.0)
    voitto_teksti()

def voitto_teksti():
    print('.')
    time.sleep(0.1)
    print('.')
    time.sleep(0.1)
    print('.')
    time.sleep(0.1)
    print('.')
    time.sleep(0.1)
    print('.')
    time.sleep(0.1)
    print('.')
    time.sleep(0.1)
    print('.')
    time.sleep(0.1)
    print(pelin_nimi.center(50, '='))
    print('\n\nLäpäisit pelin!\n\n')
    loppu_pisteet_ja_tulokset()
    quit()

def game_over_teksti():
    tulosta_hitaasti('Game Over\n' * 5, viive=0.02)
    loppu_pisteet_ja_tulokset()
    quit()

def loppu_pisteet_ja_tulokset():
    print(f"{'Pelaaja':.<45}{pelaaja['nimi']}")
    print(f"{'Pisteet':.<45}{kokonais_pisteet()}")
    print(f"{'Ajoissa':.<45}{aika <= tapaaminen_aika}")
    print(f"{'Ansioluettelo':.<45}{onko_cv()}")
    print(f"{'henkilökortti-vierailija':.<45}{onko_henkilokortti_vierailija()}")

def tulosta_arkistomappi():
    tulosta_hitaasti('Nostat arkistomapin, mutta se on liian painava mukaan otettavaksi.\nSen sijaan vilkaiset, mitä siinä lukee.\n\n', viive=0.02)
    tulosta_hitaasti('Joulu 2025 - ICT-Palvelut\nProduct id: 2290121225\n"Ohjelmointipalvelujen jatkosuunnitelmat" tilaus\ntilaus nro: 2290010126\nkehitystunnus: kkitc28\ntarget command: hashed command\npass: seikkailu\ndeadline: 31.21.2025\nHead Leader: Veijo Valpas\nTeam: Keijo Mäki, Sanna Koivu, Sami Kuusikko, Ilari Isomäki\nLanguage: Python\nToteutus: Human Code\n.....\n....\n...\n..\n.\n\n', viive=0.02)
    time.sleep(1.0)
    tulosta_hitaasti('Laitat mapin takaisin.\n\n', viive=0.02)

def onko_cv():
    if 'ansioluettelo' in pelaaja['salkku']:
        return True
    else:
        return False
    
def onko_henkilokortti_vierailija():
    if 'henkilökortti-vierailija' in pelaaja['salkku']:
        return True
    else:
        return False
    
def onko_henkilokortti_keijo():
    if 'henkilökortti-keijo' in pelaaja['salkku']:
        return True
    else:
        return False
    
def paivita_sijainti(koordinaatit):
    for i in kaikki_paikat:
        if i.location == koordinaatit:
            return i

def kokonais_pisteet():
    palauta_pisteet = pelaaja['pisteet']
    for p in kaikki_paikat:
        if p.kohteliaisuus_annettu == True:
            palauta_pisteet += 100
    return palauta_pisteet

komento = input('\n> ')

while komento != 'lopeta':    
    if len(komento.split()) == 2:

        # ota komennot
        if komento.split()[0] == 'ota':
            if komento.split()[1] == 'unet' and pelaaja['sijainti'] == aula:
                aika += (minuutti * 5)
                ottaa_unet()
            elif komento.split()[1] == 'arkistomappi' and pelaaja['sijainti'] == varasto:
                tulosta_arkistomappi()                
            elif komento.split()[1] in pelaaja['sijainti'].itemit:
                pelaaja['sijainti'].itemit.remove(komento.split()[1])
                pelaaja['salkku'].append(komento.split()[1])
                print(f'{komento.split()[1]} on nyt mukanasi.')
            else:
                print(f'Esinettä {komento.split()[1]} ei ole')

        # pudota komennot
        elif komento.split()[0] == 'pudota':
            if komento.split()[1] in pelaaja['salkku']:
                pelaaja['salkku'].remove(komento.split()[1])
                pelaaja['sijainti'].itemit.append(komento.split()[1])
                print(f'Pudotit: {komento.split()[1]}.')
            else:
                print(f'Esinettä {komento.split()[1]} ei ole mukanasi')

        # anna komennot
        elif komento.split()[0] == 'anna':
            if komento.split()[1] == 'avain' and 'avain' in pelaaja['salkku'] and pelaaja['sijainti'] == kaytava2_veijo:
                pelaaja['salkku'].remove(komento.split()[1])
                tulosta_hitaasti('Talonmieheltä löytämäsi avain sopii Veijon oveen. Veijo iloitsee avustasi ja pääsee työhuoneeseensa.\n', viive=0.02)
                pelaaja['pisteet'] += 300
                pelaaja['sijainti'].ovi = 'auki'
            elif komento.split()[1] in pelaaja['salkku']:
                if pelaaja['sijainti'] == eteinen or pelaaja['sijainti'] == toimisto or pelaaja['sijainti'] == talonmies:
                    pelaaja['salkku'].remove(komento.split()[1])
                    pelaaja['sijainti'].itemit.append(komento.split()[1])
                    print(f'Annoit: {komento.split()[1]}.')
                    print('Saat vastaukseksi kiitoksen.')
                else:
                    print(f'Ei ole ketään kelle antaa {komento.split()[1]}')
            else:
                print(f'Esinettä {komento.split()[1]} ei ole mukanasi')

        # piilota komennot
        elif komento.split()[0] == 'piilota':
            if komento.split()[1] in pelaaja['salkku']:
                pelaaja['salkku'].remove(komento.split()[1])
                eteinen.itemit.append(komento.split()[1])
                print(f'Piilotit: {komento.split()[1]}.')
            else:
                print(f'Esinettä {komento.split()[1]} ei ole mukanasi')

        # käytä komennot
        elif komento.split()[0] == 'käytä':
            if komento.split()[1] == 'verkkokaapeli' and 'verkkokaapeli' in pelaaja['salkku'] and 'läppäri' in pelaaja['salkku'] and pelaaja['sijainti'] == palvelinsali:
                tulosta_hitaasti('Yhdistät läppärisi verkkokaapelia käyttäen palvelinkoneelle. Palvelin pyytää salasanaa.\n', viive=0.02)
                syotetty_salasana = input('salasana? > ')
                if syotetty_salasana == 'seikkailu':
                    pelaaja['pisteet'] += 1000
                    voitto_palvelinsalissa()
                else:
                    tulosta_hitaasti('Salasana ei kelpaa. Et onnistunut pääsemään palvelimelle.\n', viive=0.02)
            elif komento.split()[1] == 'kaukosäädin' and 'kaukosäädin' in pelaaja['salkku']:
                if pelaaja['sijainti'] == aula:
                    avaa_tv()
                else:
                    print('Et löydä TV:tä täältä')
            elif komento.split()[1] in pelaaja['salkku']:
                tulosta_hitaasti(f'Pyörittelet hetken {komento.split()[1]} käsissäsi, mutta et löydä sopivaa käyttötarkoitusta.\n', viive=0.02) 
            else:
                print(f'Esinettä {komento.split()[1]} ei ole mukanasi')

        # näytä komennot
        elif komento.split()[0] == 'näytä':
            if komento.split()[1] == 'pisteet':
                print(kokonais_pisteet())
            elif komento.split()[1] == 'kartta':
                nayta_kartta()
            else:
                epaselva()

        # avaa komennot
        elif komento.split()[0] == 'avaa':
            if komento.split()[1] == 'ovi':
                if pelaaja['sijainti'].ovi == 'kiinni':
                    pelaaja['sijainti'].ovi = 'auki'
                    print('Ovi aukeaa')
                elif pelaaja['sijainti'].ovi == 'auki':
                    print('Ovi on jo auki')
                else:
                    print('Ovi on lukossa')
            elif komento.split()[1] == 'tv':
                if pelaaja['sijainti'] == aula:
                    avaa_tv()
                else:
                    print('Et löydä TV:tä täältä')
            else:
                epaselva()

        # mene komennot
        elif komento.split()[0] == 'mene':
            if komento.split()[1] in ['ovesta', 'ovi', 'sisään']:
                if pelaaja['sijainti'].ovi == 'kiinni':
                    print('Ovi on kiinni')                    
                else:
                    # tarkistetaan sijainnista lähtö-triggerit                    
                    if pelaaja['sijainti'] == eteinen:
                        if onko_cv() == False:
                            poistutko()
                            pelaaja['salkku'].append('ansioluettelo')
                        vartija_ohjaa_paikkaan_aula1()
                        pelaaja['sijainti'] = kaytava1_kahvio
                    elif pelaaja['sijainti'] == veijo and 'lompakko' in pelaaja['salkku']:
                        lompakko_vietiin()
                    else:
                        if pelaaja['sijainti'] == ulkona:
                            kaatuminen_eteisessa()
                        if pelaaja['sijainti'].location[0] == 2:
                            pelaaja['sijainti'] = paivita_sijainti([1,pelaaja['sijainti'].location[1],pelaaja['sijainti'].location[2]])                        
                        else:
                            pelaaja['sijainti'] = paivita_sijainti([2,pelaaja['sijainti'].location[1],pelaaja['sijainti'].location[2]])
                            
                    # huoneiden saapumis triggerit
                    if pelaaja['sijainti'] == toimisto:
                        if onko_cv() == False:
                            sihteeri_kysyy()
                    elif pelaaja['sijainti'] == kokoushuone:
                        if onko_henkilokortti_keijo() == True:
                            tulosta_hitaasti('Johtaja hätääntyy:\n "Kuka olet? Miksi sinulla on Keijon henkilökortti?\nOlet varmasti Cyber-rikollinen!"\n"Vartija!!! Vartija!!!"\n', viive=0.02)
                            tulosta_hitaasti('Vartija tulee juosten ja heittää sinut ulos rakennuksesta...\n', viive=0.02)
                            game_over_teksti()            
                        if onko_henkilokortti_vierailija() == True:
                            tulosta_hitaasti('Vierailijakorttisi kertoo, että olet varmaankin odotettu haastateltava.\n', viive=0.02)
                            if onko_cv() == False:
                                tulosta_hitaasti('Johtaja kysyy ensimmäisenä onko sinulla ansioluettelo mukana?\nKatsot salkustasi, eikä sitä ole siellä.\n\nJohtaja: "Palaa hakemaan se!"\n\nJohtaja ohjaa sinut takaisin käytävälle.\n', viive=0.02)
                            elif aika <= tapaaminen_aika:
                                pelaaja['pisteet'] += 100
                                tulosta_hitaasti(f'Johtaja: "Olen odottanut sinua {pelaaja["nimi"]}. Saavuit ajoissa paikalle. Olet täsmällinen kaveri!"\n', viive=0.02)
                            elif aika > tapaaminen_aika:
                                pelaaja['pisteet'] -= 200
                                tulosta_hitaasti(f'Johtaja: "Olen odottanut sinua {pelaaja["nimi"]}. Olet myöhässä. Yhtiössämme täsmällisyys on ensisijaisen tärkeää."\n', viive=0.02)
                            if onko_cv() == True:
                                time.sleep(2.0)
                                tulosta_hitaasti('Johtaja: "Näytähän sitä ansioluetteloasi."\n', viive=0.02)
                                time.sleep(2.0)
                                tulosta_hitaasti(f'"Hmmm............ {pelaaja["nimi"]}.......... Ahaa........... vai niin............."\n', viive=0.1)
                                time.sleep(2.0)
                                tulosta_hitaasti('"Olisitko valmis aloittamaan heti ensi kuussa?"\n', viive=0.02)
                                vastaus = input('> ')
                                while vastaus not in ['kyllä', 'olen', 'joo', 'totta kai', 'ehdottomasti', 'kyllä olen', 'valmis', 'olen valmis', 'olisin valmis', 'olisin', 'ei', 'en ole', 'en']:
                                    if vastaus == 'lopeta':
                                        quit()
                                    tulosta_hitaasti('"En ymmärtänyt. Mitä tarkoitit?"\n', viive=0.02)
                                    vastaus = input('> ')
                                if vastaus in ['kyllä', 'olen', 'joo', 'totta kai', 'ehdottomasti', 'kyllä olen', 'valmis', 'olen valmis', 'olisin valmis', 'olisin']:
                                    if aika <= tapaaminen_aika:                                        
                                        tulosta_hitaasti('Johtaja: "Vaikutat kyllä pätevältä tyypiltä.\nLuulen että sopisit tiimiimmen hyvin."\n', viive=0.02)
                                        time.sleep(1.5)
                                        tulosta_hitaasti('"Hmmm............ "\n', viive=0.1)
                                        time.sleep(1.5)
                                        sihteerin_soitto(kokonais_pisteet())
                                        tulosta_hitaasti('"Sinulta varmaan syntyy koodiakin ajallaan kun tulit ajoissakin."\n', viive=0.02)
                                        tulosta_hitaasti('"Hmmm............ "\n', viive=0.1)
                                        time.sleep(1.5)
                                        if kokonais_pisteet() < 300:
                                            tulosta_hitaasti('"Sopisitko sittenkään henkilökuntaamme..."\n', viive=0.1)
                                            tulosta_hitaasti('"En uskalla ottaa riskiä. Et saanut paikkaa parempi onni ensi kerralla."\n', viive=0.02)
                                            game_over_teksti()
                                        else:
                                            tulosta_hitaasti('"Tämä on selvä tapaus................... Paikka on teidän!"\n', viive=0.1)
                                            voitto_teksti()
                                    elif aika > tapaaminen_aika:
                                        tulosta_hitaasti('Johtaja: "Minun pitää hieman miettiä.\nOletkohan oikea henkilö tiimiimme. Tulit hieman myöhässäkin..."\n', viive=0.02)
                                        time.sleep(1.5)
                                        tulosta_hitaasti('"Hmmm............ "\n', viive=0.1)
                                        sihteerin_soitto(kokonais_pisteet())
                                        if kokonais_pisteet() >= 300:
                                            tulosta_hitaasti('"Henkilökuntamme tosin piti sinusta."\n', viive=0.02)
                                            tulosta_hitaasti('"Hmmm............ "\n', viive=0.1)
                                            tulosta_hitaasti('"Okei, toivottavasti en tee virhettä tässä................... Paikka on teidän!"\n', viive=0.1)
                                            voitto_teksti()
                                        else:
                                            tulosta_hitaasti('"Henkilökuntammekaan ei saanut sinusta edes hymyä irti..."\n', viive=0.02)
                                            tulosta_hitaasti('"Hmmm............ "\n', viive=0.1)
                                            tulosta_hitaasti('"Olen pahoillani, mutta et ole hakemamme henkilö tämän tiimiin"\n', viive=0.1)
                                            game_over_teksti()
                                elif vastaus in ['ei', 'en ole', 'en']:
                                    tulosta_hitaasti('"Siinä tapauksessa emme voi palkata sinua tähän tehtävään. Tarvitsemme heti tekijää."\n', viive=0.02)
                                    game_over_teksti()

                        elif onko_henkilokortti_vierailija() == False:
                            tulosta_hitaasti('"Kuka olet? Sinulla pitää olla kulkukortti täällä liikkuaksesi!"\n\nJohtaja ohjaa sinut takaisin käytävälle.\n', viive=0.02)

                        aika+= minuutti
                        pelaaja['sijainti'] = kaytava1_kokoushuone

                    # huoneen ovi asetetaan auki astuessa ovesta
                    pelaaja['sijainti'].ovi = 'auki'
                    time.sleep(0.2)
                    pelaaja['sijainti'].tulosta_paikka()                    
                    aika+= minuutti

            # liikkumiset pohjoiseen, etelään, itään, länteen, ylös ja alas
            elif komento.split()[1] in ['pohjoiseen', 'poh', 'p']:
                if pelaaja['sijainti'].location[2] == 1 and pelaaja['sijainti'].location[1] < 5 and pelaaja['sijainti'].location[0] != 1:
                    pelaaja['sijainti'] = paivita_sijainti([pelaaja['sijainti'].location[0],pelaaja['sijainti'].location[1]+1,pelaaja['sijainti'].location[2]])
                    pelaaja['sijainti'].tulosta_paikka()
                elif pelaaja['sijainti'].location[2] == 2 and pelaaja['sijainti'].location[1] < 6 and pelaaja['sijainti'].location[0] != 1:
                    pelaaja['sijainti'] = paivita_sijainti([pelaaja['sijainti'].location[0],pelaaja['sijainti'].location[1]+1,pelaaja['sijainti'].location[2]])                       
                    pelaaja['sijainti'].tulosta_paikka()
                else:
                    print('Et pääse pohjoiseen päin')
                if pelaaja['sijainti'] == kaytava2_veijo and pelaaja['sijainti'].ovi == 'lukossa':
                    tulosta_hitaasti('\nOvessa lukee Veijo.\nNäet miehen, joka selvästikin on hukannut jotain.\n', viive=0.02)
                    if 'avain' in pelaaja['salkku']:
                        tulosta_hitaasti('Mietit, voisitko jotenkin auttaa Veijoa... hmm...\n', viive=0.02)
                    else:
                        tulosta_hitaasti('Veijo etsii taskujaan ja mutisee, mihin on hukannut avaimensa...\n', viive=0.02)
            elif komento.split()[1] in ['etelään', 'ete', 'e']:
                if pelaaja['sijainti'].location[1] > 1 and pelaaja['sijainti'].location[0] != 1:
                    pelaaja['sijainti'] = paivita_sijainti([pelaaja['sijainti'].location[0],pelaaja['sijainti'].location[1]-1,pelaaja['sijainti'].location[2]])
                    pelaaja['sijainti'].tulosta_paikka()
                else:
                    print('Et pääse etelään päin')
            elif komento.split()[1] in ['itään', 'itä', 'i']:
                if pelaaja['sijainti'] == eteinen:
                    pelaaja['sijainti'] = paivita_sijainti([pelaaja['sijainti'].location[0]+1,pelaaja['sijainti'].location[1],pelaaja['sijainti'].location[2]])
                    pelaaja['sijainti'].tulosta_paikka()
                else:
                    print('Et pääse itään')
            elif komento.split()[1] in ['länteen', 'län', 'l']:
                if pelaaja['sijainti'] == aula:
                    pelaaja['sijainti'] = paivita_sijainti([pelaaja['sijainti'].location[0]-1,pelaaja['sijainti'].location[1],pelaaja['sijainti'].location[2]])
                    pelaaja['sijainti'].tulosta_paikka()
                else:
                    print('Et pääse länteen')
            elif komento.split()[1] in ['ylös', 'y']:
                if pelaaja['sijainti'] == eteinen or pelaaja['sijainti'] == kaytava2_sahkohuone:
                    if pelaaja['sijainti'].location[2]== 1:
                        print('Saavut toiseen kerrokseen')
                        pelaaja['sijainti'] = paivita_sijainti([pelaaja['sijainti'].location[0],pelaaja['sijainti'].location[1],2])
                        pelaaja['sijainti'].tulosta_paikka()
                        aika+= minuutti
                    else:
                        print('Et pääse ylemmäs')
                else:
                    print('Et löydä portaita')                                 
            elif komento.split()[1] in ['alas', 'a']:
                if pelaaja['sijainti'] == eteinen or pelaaja['sijainti'] == kaytava2_sahkohuone:
                    if pelaaja['sijainti'].location[2]== 2:
                        print('Saavut ensimmäiseen kerrokseen')
                        pelaaja['sijainti'] = paivita_sijainti([pelaaja['sijainti'].location[0],pelaaja['sijainti'].location[1],1])
                        pelaaja['sijainti'].tulosta_paikka()
                        aika+= minuutti
                    else:
                        print('Et pääse alemmas')
                else:
                    print('Et löydä portaita')
            else:
                epaselva()
                        
        # katso komennot
        elif komento.split()[0] == 'katso':
            if komento.split()[1] in['kello', 'kelloa']:
                print(f'Kello näyttää {aika}')
            else:
                epaselva()

        # keitä kahvi
        elif komento.split()[0] == 'keitä':
            if komento.split()[1] in ['kahvit', 'kahvia', 'sumpit', 'kahvi']:
                if pelaaja['sijainti'] == kahvio:
                        kahvin_keitto()
                        pelaaja['pisteet'] += 100
                        kahvi_keitetty = True
            else:
                epaselva()

        # juo kahvi
        elif komento.split()[0] == 'juo':
            if komento.split()[1] in ['kahvit', 'kahvia', 'sumpit', 'kahvi']:
                if pelaaja['sijainti'] == kahvio and kahvi_keitetty == True:
                        juo_kahvi()
            else:
                epaselva()               
        else:
            epaselva()
        
    elif len(komento.split()) == 1:
        if komento == 'katsele':
            pelaaja['sijainti'].katsele_paikka()
        elif komento == 'mukana':
            print()
            for i in pelaaja['salkku']:
                print(f' * {i}')
        elif komento == 'help' or komento == 'apua':
            tulosta_apua()
        elif komento in ['hymyile', 'kiitä']:
            if pelaaja['sijainti'] in [eteinen, toimisto, veijo, talonmies]:
                pelaaja['sijainti'].kohteliaisuus_annettu = True
                print('Saat vastaukseksi hymyn! =)')
        else:
            epaselva()
    else:
        epaselva()
            
    komento = input('\n> ')

print('Kiitos pelistä')
game_over_teksti()