# Baua Biocides Scraper
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

Scrapping the data from each page of biocides listed on the BAUA website (https://www.baua.de/DE/Biozid-Meldeverordnung/Offen/offen.html) into a csv file.  
A windows standalone client is avalaible in the [dist folder](https://github.com/3r1cd3ma/Baua-Biocides-Scraper/tree/main/dist)

## About the project

### What's the problem?

Baua website contains many usefull data for biocides domain, but the website only allows you to search product by product and it is not easy to find and get some informations with over 80,000 products listed

### The idea

Facilitate the data manipulation with providing a csv file with all data scraped from Baua website.  

## How does it work ?

1. The user start the program.
2. The program extract data from Baua website.
3. A csv file containing data are created.

## Roadmap

This project was created after a request and is not intended to evolve. Nevertheless you can fork the project to improve it by yourself and propose them via the [project pull requests](https://github.com/3r1cd3ma/Baua-Biocides-Scraper/pulls/). or make a suggestion via the [project issues](https://github.com/3r1cd3ma/Baua-Biocides-Scraper/issues/).

## Build with

 - Programming language : [Python 3.10.0](https://www.python.org/)
 - Scraping Framework : [Scrapy 2.5.1](https://scrapy.org/)
 - HTTP library : [Requests 2.26.0](https://docs.python-requests.org/en/latest/)
 - Standalone Builder : [PyInstaller 4.7](https://www.pyinstaller.org/)

## Demo

You can use the windows standalone client in the [dist folder](https://github.com/3r1cd3ma/Baua-Biocides-Scraper/tree/main/dist)

## Version management

We use a semantic version management, that is a version number MAJOR.MINOR.CORRECTIVE :
1. the MAJOR version number when there are non backward compatible changes,
2. the MINOR version number when there are backward compatible feature additions,
3. the FIX version number when there are backwards compatible bug fixes.

See [SignMail tags](https://github.com/3r1cd3ma/SignMail/tags)
For more info: [semver.org](http://semver.org/)

## Authors
[![contributors](https://contrib.rocks/image?repo=3r1cd3ma/Baua-Biocides-Scraper)](https://github.com/3r1cd3ma/Baua-Biocides-Scraper/graphs/contributors)

- [**Eric De Maria**](https://github.com/3r1cd3ma/) - [Numio](https://numio.eu) - _Initial work_

## License

This project is licensed under the GNU GPL 3 license - See the [LICENSE](LICENCE) file for more details.
