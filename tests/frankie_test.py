import unittest
from frankie import frankie


class TestFrankie(unittest.TestCase):
    """
    Does a series of tests on frankie's functions
    """

    def test_retrieve_episode_url(self):
        link = "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/lintegrale-jack-london-210818-rediffusion-3737456"
        result = frankie.retrieve_episode_url(link)
        self.assertEqual(
            result,
            "https://cdn-europe1.lanmedia.fr/audio/emissions/Au-coeur-de-l-histoire-24212/L-integrale-Jack-London-21-08-18-rediffusion-2695985.mp3",
        )

    def test_negative_retrieve_episode_url(self):
        link = "https://google.com"
        result = frankie.retrieve_episode_url(link)
        self.assertEqual(result, None)

    def test_format_page_link(self):
        page_number = 2
        result = frankie.format_page_link(page_number)
        self.assertEqual(
            result, "http://www.europe1.fr/emissions/Au-coeur-de-l-histoire/2"
        )

    def test_fetch_title(self):
        link = "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/lintegrale-jack-london-210818-rediffusion-3737456"
        result = frankie.fetch_title(link)
        self.assertEqual(result, "lintegrale-jack-london-210818-rediffusion-3737456")

    def retrieve_episode_links(self):
        link = "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire"
        link_lst = [
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/le-mystere-de-lassassinat-des-moines-de-tibhirine-3824003",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/la-folle-histoire-de-la-chasse-aux-sorcieres-de-salem-3820760",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/jean-sans-terre-le-roi-maudit-a-lorigine-dun-texte-fondateur-de-la-democratie-3819329",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/loi-de-1905-le-jour-ou-la-france-a-divorce-de-leglise-3815678",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/crise-des-otages-americains-quand-liran-a-fait-plier-les-etats-unis-3814274",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/les-nu-pieds-ancetres-de-gilets-jaunes-racontes-par-fabrice-dalmeida-3811121",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/la-bataille-darcole-racontee-par-fabrice-dalmeida-3809747",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/adieu-solferino-raconte-par-fabrice-dalmeida-3806096",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/vous-aimez-les-recits-decouvrez-notre-serie-originale-3h56-le-premier-homme-sur-la-lune-3762944",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/lintegrale-la-conquete-du-pole-nord-260818-rediffusion-3740531",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/le-recit-la-conquete-du-pole-nord-260518-3740516",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/lintegrale-francois-xavier-et-les-jesuites-250818-rediffusion-3740063",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/le-recit-francois-xavier-et-les-jesuites-250818-rediffusion-3740057",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/le-recit-abbas-ier-le-grand-rediffusion-3739511",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/lintegrale-la-perse-eternelle-24082018-rediffusion-3739508",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/lintegrale-limperatrice-wu-zetian-et-autres-empereurs-de-la-chine-23082018-rediffusion-3738719",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/le-recit-wu-zetian-seule-et-unique-imperatrice-de-chine-rediffusion-3738713",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/lintegrale-tamerlan-et-la-route-de-la-soie-22082018-rediffusion-3738035",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/le-recit-tamerlan-conquerant-des-steppes-rediffusion-3738032",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/le-recit-jack-london-lappel-de-laventure-rediffusion-3737459",
            "https://www.europe1.fr/emissions/Au-coeur-de-l-histoire/lintegrale-jack-london-210818-rediffusion-3737456",
        ]
        self.assertEqual(result, lst)


if __name__ == "__main__":
    unittest.main()
