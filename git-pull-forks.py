#!/usr/bin/env python3

forks = """
@kenesparta kenesparta / live-bootcamp-project-fork
@aldass aldass / live-bootcamp-project
@paragoner1 paragoner1 / live-bootcamp-project
@zainen zainen / rust-bootcamp-project
@Ripper53 Ripper53 / live-bootcamp-project
@rgruberski rgruberski / live-bootcamp-project
@raywu-hk raywu-hk / live-bootcamp-project
@mpdevilleres mpdevilleres / live-bootcamp-project
@MoonKraken MoonKraken / live-bootcamp-project
@mmcclatchy mmcclatchy / live-bootcamp-project
@mjohnson518 mjohnson518 / live-bootcamp-project
@MikhailSporyshev MikhailSporyshev / live-bootcamp-project
@mattjsharp mattjsharp / live-bootcamp-project
@MadMathMike MadMathMike / live-bootcamp-project
@luisgabrielmendez luisgabrielmendez / live-bootcamp-project
@luiscarlosjayk luiscarlosjayk / live-bootcamp-project
@lfbos lfbos / live-bootcamp-project
@kruzabasi kruzabasi / rust-project
@Kooriii Kooriii / lgr-bootcamp-project
@khinch khinch / lgr-live-bootcamp-project
@KalyniukV KalyniukV / live-bootcamp-project
@xue2sheng xue2sheng / initial-live-bootcamp-project
@WallyOxen WallyOxen / live-bootcamp-project
@VimCommando VimCommando / live-bootcamp-project
@vikramriyer vikramriyer / live-bootcamp-project
@verygreenboi verygreenboi / live-bootcamp-project
@TuinderJ TuinderJ / live-bootcamp-project
@tiberiumboy tiberiumboy / live-bootcamp-project
@thedrummeraki thedrummeraki / live-bootcamp-project
@The-Rabak The-Rabak / live-bootcamp-project
@tedkimdev tedkimdev / live-bootcamp-project
@tahoe tahoe / live-bootcamp-project
@Sweng0d Sweng0d / live-bootcamp-project
@Stavch Stavch / live-bootcamp-project1
@srih1rsh1 srih1rsh1 / live-bootcamp-project
@srevesnerol srevesnerol / live-bootcamp-project
@smk1992 smk1992 / live-bootcamp-project
@shafiquejamal shafiquejamal / live-bootcamp-project
@serbanrobu serbanrobu / live-bootcamp-project
@scopevale scopevale / live-bootcamp-project
@jwmurray jwmurray / axum_auth_server
@DUNNSEAN DUNNSEAN / live-bootcamp-project
@dpdresser dpdresser / live-bootcamp-project
@dobleuber dobleuber / live-bootcamp-project
@deanmiller deanmiller / live-bootcamp-project
@CyndieKamau CyndieKamau / live-bootcamp-project
@crttcr crttcr / live-bootcamp-project
@coolboole coolboole / live-bootcamp-project
@cj-zhukov cj-zhukov / live-bootcamp-project
@ciphercrunch1919 ciphercrunch1919 / live-bootcamp-project-forked
@chadangelelli chadangelelli / live-bootcamp-project
@cezarcrintea cezarcrintea / lgr-live-bootcamp-project
@bloodfeast bloodfeast / live-bootcamp-project
@BeyondJacob BeyondJacob / live-bootcamp-project
@andreinnanu andreinnanu / live-bootcamp-project
@alexlave100 alexlave100 / live-bootcamp-project
@aleanon aleanon / live-bootcamp-project
@adamNewell adamNewell / live-bootcamp-project
@acgetchell acgetchell / live-bootcamp-project
@0xdecr1pto 0xdecr1pto / live-bootcamp-project
@JWLee89 JWLee89 / live-bootcamp-project
@jocax jocax / live-bootcamp-project
@JiriMON JiriMON / live-bootcamp-project
@jasonpark94 jasonpark94 / live-bootcamp-project
@jakubsuchybio jakubsuchybio / live-bootcamp-project
@jakegny jakegny / live-bootcamp-project
@ipcasj ipcasj / live-bootcamp-project
@imding imding / lgr-live-bootcamp-project
@Idleness76 Idleness76 / live-bootcamp-project
@hnariman hnariman / live-bootcamp-project
@helloiamgp helloiamgp / live-bootcamp-project
@harryobas harryobas / live-bootcamp-project
@hank-butler hank-butler / live-bootcamp-project
@GuillemIscla GuillemIscla / live-bootcamp-project
@garikAsplund garikAsplund / live-bootcamp-project
@gabrielhsc95 gabrielhsc95 / live-bootcamp-project
@gaborzatik gaborzatik / live-bootcamp-project
@evanmiller2112 evanmiller2112 / live-bootcamp-project
@evalredacted evalredacted / live-bootcamp-project
"""

from pathlib import Path

def main(name):
    paths = [
        (parts[1], parts[3])
        for fork in forks.splitlines()
        if fork and (parts := fork.split(' ')) and name == parts[3]
    ]

    for user, project in paths:
        p = Path(f"~/workspace/forks/{project}/{user}/").expanduser()
        print(f"# {'-' * 30}")
        pp = str(p)
        clone_cmd = f"git clone https://github.com/{user}/{project}.git"
        print(f"(mkdir -p '{pp}' && cd '{pp}' && {clone_cmd})")


if __name__ == '__main__':
    main("live-bootcamp-project")
