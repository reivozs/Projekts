# Projekts

# Problēma
Esmu sācis pats savu biznesu, kurā pārdodu paša dizainētas drēbes. Tā kā tās ražoju un uzglabāju pats savās mājās, man tās pašam ir
nepieciešams izvedāt līdz pakomātiem, lai iepakojumus nosūtītu pircējiem, tāpēc man ir nepieciešama mašīna. Vienmēr esmu gribējis
mašīnu "Ford Transit Connect", tāpēc tagad vēlos iegādāties to. Bet man nav laika nepārtraukti iet mājaslapā auto24.lv un skatīties vai ir jauni "Ford Transit Connect" par man atbilstošu cenu un ne pārāk lielu nobrauku.

# Uzdevums
Izveidot programu, kuru palaižot, nolasa visus pieejamos "Ford Transit Connect" modeļus no mājaslapas
"https://www.auto24.lv/kasutatud/nimekiri.php?bn=2&a=100&aj=&ssid=125727415&b=7&bw=2038&bi=EUR&ab=0&ab%5B%5D=-2&ae=1&af=50&otsi=mekl%C4%93t"
un ievietot tos failā "masinas.json", kuru cena ir līdz 7,000 eiro un nobraukums līdz 200,000 km.

# Izmantotās bibliotēkas
Selenium - izmanto, lai iegūtu datus no tīmekļa un veiktu 'web scraping'; <br/>
webdriver - izmanto, lai automātiski vadītu tīmekli; <br/>
Service - izmanto, lai veiktu tīmekļa programmu testēšanu; <br/>
By - izmanto, lai iegūtu datus no tīmekļa; <br/>
time - izmanto, lai veiktu darbības ar laiku, piemēram, liktu programmai gaidīt noteiktu laika intervālu; <br/>
json - izmanto, lai strādātu ar json tipa failiem; <br/>

# Izmantotās programmas metodes
Programmā netiek izmantotas funkcijas, taču programma sākumā nolasa datus no tīmekļa vietnes, atver json failu, iet cauri visiem datiem un pārbauda, vai tie ir attiecīgi pareizi un saglabā tos masīvā. Kad iziets cauri visiem datiem, programma saglabā datus json failā. Programmā
tiek izmantots Try Except princips, jo lapā, kurā meklēju mašīnas, vairāki elementi nav mašīnu sludinājumi vai arī sludinājumiem nav visa
nepieciešamā informācija, kas liek programmai nobrukt.

Attēli no programmas procesa: https://failiem.lv/u/gkd6bn5g26
