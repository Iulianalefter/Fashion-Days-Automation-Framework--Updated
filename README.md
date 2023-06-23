Fashion Days BDD Automation Framework

Site-ul testat: www.fashiondays.ro

Design pattern-ul folosit: Page Object Model

Metodologia: Behavior Driven Development

Instalați Google Chrome
Instalați Pycharm Community Edition: https://www.jetbrains.com/pycharm/download/
Instalați Python https://www.python.org/downloads/

Pentru a clona/importa proiectul:

Descărcați GIT: https://git-scm.com/downloads
Deschideți folderul unde doriți să clonați proiectul, dați click dreapta, selectați ”Git Bash Here”
In fereastra deschisă, copiati  urmatorea comandă: 
git clone https://Iulianalefter/Fashion-Days---BDD_Automation_Framework.git

Librarii de instalat:

pip install -U selenium

pip install behave

pip install behave-html-formatter

pip install webdriver-manager

În Terminal, run tests:

behave -f html -o behave-report.html
