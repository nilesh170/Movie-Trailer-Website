# -*- coding: utf8 -*-
import fresh_tomatoes
import media
import webbrowser


def get_info():
    """
    This function gives user the details about the
    video like name, storyline etc
    """
    name = input("Which videos info you want to see:\nplease give the name"
                 "\n[The Names are :\nToy Story,\nAvatar,\nAvengers,\nBatman,"
                 "\nRise of The Guardians,\nHow to Train your Dragon,\nThe "
                 "Boss Baby,\nThe Angry Bird,\nKung fu Panda,\nCoco,\nNow You "
                 "See Me,\nThe Prestige,\nGame of Thrones,\nCastle Rock,\n"
                 "Orange Is The New Black,\nSuits,\nThe Flash,\nJessica Jones,"
                 "\nSherlock,\nThe Fall,\n13 Reasons Why]\n")
    if name.lower() == "toy story":
        return toy_story.show_info()
    elif name.lower() == "coco":
        return Coco.show_info()
    elif name.lower() == "suits":
        return Suits.show_info()
    elif name.lower() == "kung fu panda":
        return Kungfupanda.show_info()
    elif name.lower() == "now you see me":
        return Now_you.show_info()
    elif name.lower() == "the prestige":
        return The_Prestige.show_info()
    elif name.lower() == "game of thrones":
        return Game_of_thrones.show_info()
    elif name.lower() == "castle rock":
        return Castle_Rock.show_info()
    elif name.lower() == "orange is the new black":
        return Orange_Is_the_New_Black.show_info()
    elif name.lower() == "the flash":
        return The_Flash.show_info()
    elif name.lower() == "jessica jones":
        return Jessica_Jones.show_info()
    elif name.lower() == "sherlock":
        return Sherlock.show_info()
    elif name.lower() == "the fall":
        return The_Fall.show_info()
    elif name.lower() == "13 reasons why":
        return Reasons_Why.show_info()
    elif name.lower() == "avatar":
        return avatar.show_info()
    elif name.lower() == "avengers":
        return avengers.show_info()
    elif name.lower() == "batman":
        return batman.show_info()
    elif name.lower() == "rise of the guardians":
        return Rise_of_the_Guardians.show_info()
    elif name.lower() == "how to train your dragon":
        return How_to_Train_your_Dragon.show_info()
    elif name.lower() == "the boss baby":
        return The_Boss_Baby.show_info()
    elif name.lower() == "the angry bird":
        return The_Angry_Bird.show_info()
    else:
        print("Please provide the correct name \n")
        return 0


def get_abt():
    """
    This function gives a way to choose user want
    he/she wants to see on the website
    """
    vid = ''
    while vid.lower() not in ['videos', 'movies', 'tvshows']:
        # this function helps user to choose what he/she wants
        # to see on the website
        vid = input('\nWhat do you want to see in the website:'
                    '\nIf you like to see all the videos enter:'
                    ' videos\nIf you like to see all'
                    ' the movies collection enter: movies\nIf '
                    'you like to see'
                    ' all the tvshows enter: tvshows\n')
        if vid.lower() not in ['videos', 'movies', 'tvshows']:
            print('Sorry, I do not understand your input.')
        print('-'*80)
    return vid.lower()


def get_episodes():
    """
    This class provides a url which contain the list
    of the episodes of the tv show on google.com
    """
    tvshow = ""
    tvshows = {
              "game of thrones": "https://www.google.co.in/search?biw=1366&bih=662&ei=jUJfW_j2DISOvQTrmZHwBA&q=game+of+thrones+episodes&oq=game+o+episodes&gs_l=psy-ab.1.0.0i7i30k1l10.52520.53781.0.55237.6.6.0.0.0.0.362.529.0j1j0j1.2.0....0...1.1.64.psy-ab..4.2.523....0.07UT2XT-nX4",  # noqa
              "castle rock": "https://www.google.co.in/search?q=castle+rock+episodes&stick=H4sIAAAAAAAAAONgFuLVT9c3NEw2K8pKL042VkLlakllJ1vpl5QBUXxBUX56UWKuVWpBZnF-SmoxALHeYSM8AAAA&sa=X&ved=2ahUKEwj715fQpMfcAhWGro8KHSK3BIUQMTA5egQIDRBD&biw=1366&bih=662",  # noqa
              "orange is the new black": "https://www.google.co.in/search?biw=1366&bih=662&ei=eUNfW5nCEYjlvAS1ja6IDg&q=orange+is+the+new+black+episodes&oq=+oraepisodes&gs_l=psy-ab.3.0.0i7i30k1l3.73181.75732.0.77105.10.10.0.0.0.0.197.1249.0j7.7.0....0...1.1.64.psy-ab..3.6.1070...0i7i10i30k1j0i8i10i30k1j0i67k1.0.KKD0uo55zFc",  # noqa
              "suits": "https://www.google.co.in/search?biw=1366&bih=662&ei=1UNfW6mcGcXnvASp-45Y&q=suits+episodes&oq=Sulits+episodes&gs_l=psy-ab.3.0.0i13k1l10.100383.103892.0.105529.8.8.0.0.0.0.294.1276.0j3j3.6.0....0...1.1.64.psy-ab..2.6.1261...0i7i30k1j0i67k1.0.z7eTUNw7kI0",  # noqa
              "the flash": "https://www.google.co.in/search?biw=1366&bih=662&ei=RURfW5uVBcfivASXobjAAw&q=the+flash+episodes&oq=theflas+episodes&gs_l=psy-ab.3.0.0i13k1l10.121800.125333.0.127277.9.8.1.0.0.0.246.661.0j1j2.3.0....0...1.1.64.psy-ab..5.4.673...0i7i30k1j0i10k1.0.rNJJNmiWmeI",  # noqa
              "jessica jones": "https://www.google.co.in/search?biw=1366&bih=662&ei=0ERfW7u6IY7EvwSa-r-4Dw&q=jessica+jones+episodes&oq=Jess+episodes&gs_l=psy-ab.3.2.0i7i30k1l10.429044.431792.0.433171.4.4.0.0.0.0.285.915.0j2j2.4.0....0...1.1.64.psy-ab..0.4.906....0.bt0PY6CGPJs",  # noqa
              "sherlock": "https://www.google.co.in/search?biw=1366&bih=662&ei=ikZfW_B4xeG-BK7Pm7AP&q=sherlock+episodes&oq=sher+episodes&gs_l=psy-ab.3.0.0i7i30k1l10.115543.116200.0.117240.4.4.0.0.0.0.204.759.0j3j1.4.0....0...1.1.64.psy-ab..0.4.746....0.CGkqZHrozHk",  # noqa
              "the fall": "https://www.google.co.in/search?ei=rqRgW4ajF4O5rQHXt5jQDA&btnG=Search&q=the+fall+episodes",  # noqa
              "13 reasons why": "https://www.google.co.in/search?ei=3qRgW4CLBYX7rQHRvJKYDA&q=13+reasons+why+episodes&oq=13+reasons+why+episodes&gs_l=psy-ab.3...35.7078.0.7552.18.18.0.0.0.0.0.0..0.0....0...1c.1.64.psy-ab..18.0.0....0.VHfUUA_T0WQ"}  # noqa
    while tvshow.lower() not in tvshows.keys():
        tvshow = input("Which tv show you want to know about.\n"
                       "Please provide the name\n [The Names are:"
                       "\nGame of thrones,\nCastle Rock,\nOrange Is the"
                       " New Black,\nSuits,\nThe Flash,\nJessica Jones,"
                       "\nSherlock,\nThe Fall,\n13 Reasons Why]\n")
        if tvshow.lower() not in tvshows.keys():
            print("Please provide the correct name of the Show")
        else:
            tv = tvshows[tvshow.lower()]
        print('-'*80)
    return tv
# Toy Story movie: movie title, storyline, poster image, trailer,
# release date, director, cast, budget, collection, ratings
# duration
toy_story = media.Movie("Toy Story",
                        "Andy's favourite toy, Woody, is worried that\nafter "
                        "Andy receives his birthday gift, a new toy called "
                        "Buzz Lightyear,\nhis importance may get reduced."
                        "He thus hatches a plan to eliminate Buzz.\n",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "19 November 1995",
                        "John Lasseter",
                        "Tom Hanks,\nTim Allen,\nDon Rickles,\nJim Varney,"
                        "\nWallace Shawn,\nJohn Ratzenberger,\nAnnie Potts,"
                        "\nJohn Morris,\nErik von Detten\n",
                        "$30 million",
                        "$373.6 million",
                        "IMDb = 8.3/10|Facebook = 4.3/5|Metacritic = 95%",
                        "1hr 21min")
# Avatar movie: movie title, storyline, poster image, trailer,
# release date, director, cast, budget, collection, ratings
# duration
avatar = media.Movie("Avatar",
                     "Jake Sully, a paralyzed former Marine, becomes\n"
                     "mobile again through one Avatar and falls"
                     " in love with a Naavi woman. As\na bond "
                     "he is drawn into a battle for the "
                     "survival of her world.\n",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "18 December 2009",
                     "James Cameron",
                     "Sam Worthington,\nZoe Saldana,\nStephen Lang,"
                     "\nMichelle Rodriguez,\nSigourney Weaver\n",
                     "$237 million + (re-release = $9 million)",
                     "$2.788 billion",
                     "IMDb = 7.8/10|Metacritic = 83%|Rotten Tomatoes = 83%",
                     "2hr 42min")
# Avengers movie: movie title, storyline, poster image, trailer,
# release date, director, cast, budget, collection, ratings
# duration
avengers = media.Movie("Avengers : Infinity War",
                       "Iron Man, Thor, the Hulk and the rest of\nthe"
                       " Avengers unite to battle their most powerful"
                       " enemy yet the evil Thanos.\nThe fate of the "
                       "planet and existence itself has never been "
                       "more uncertain.\n",
                       "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8",
                       "27 April 2018",
                       "Anthony Russo,\nJoe Russo",
                       "$316–400 million",
                       "$2.045 billion",
                       "Robert Downey Jr.,\nChris Hemsworth,\nMark Ruffalo,"
                       "\nChris Evans,\nScarlett Johansson,\nBenedict "
                       "Cumberbatch,\nDon Cheadle,\nTom Holland,\n"
                       "Chadwick Boseman,\nPaul Bettany,\nElizabeth Olsen,"
                       "\nAnthony Mackie,\nSebastian Stan,\nDanai Gurira,\n"
                       "Letitia Wright,\nDave Bautista,\nZoe Saldana,\n"
                       "Josh Brolin,\nChris Pratt\n",
                       "IMDb = 8.7/10|Metacritic = 68%|Rotten Tomatoes = 83%",
                       "2hr 40min")
# Batman movie: movie title, storyline, poster image, trailer,
# release date, director, cast, budget, collection, ratings
# duration
batman = media.Movie("Batman : The Dark Knight",
                     "Dent and Batman begin an assault on "
                     "Gotham's\norganised crime, the mobs hire the Joker, a"
                     " psychopathic criminal\nmastermind, who wants to bring"
                     " all the heroes down to his level\n",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # noqa
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY&t=31s",
                     "18 July 2008",
                     "Christopher Nolan",
                     "Christian Bale,\nMichael Caine,\nHeath Ledger,\n"
                     "Gary Oldman,\nAaron Eckhart,\n"
                     "Maggie Gyllenhaal,\nMorgan Freeman\n",
                     "$185 million",
                     "$1.005 billion",
                     "IMDb = 9/10|Metacritic = 82%|Rotten Tomatoes = 94%",
                     "2hr 32min")
# Rise of the Guardians movie: movie title, storyline, poster image, trailer,
# release date, director, cast, budget, collection, ratings
# duration
Rise_of_the_Guardians = media.Movie("Rise of the Guardians",
                                    "When Pitch, returns to planet Earth to"
                                    " assault\the children nand take over the "
                                    "world, some guardians with"
                                    " extraordinary\nabilities join forces to"
                                    " protect the world.\n",
                                    "https://upload.wikimedia.org/wikipedia/en/9/92/Rise_of_the_Guardians_poster.jpg",  # noqa
                                    "https://www.youtube.com/watch?v=aPLiBxhoug0",  # noqa
                                    "21 December 2012",
                                    "Peter Ramsey",
                                    "Chris Pine,\nAlec Baldwin,\nHugh Jackman"
                                    ",\nIsla Fisher,\nJude Law\n",
                                    "$145 million",
                                    "$306.9 million",
                                    "IMDb = 7.3/10|Rotten Tomatoes = 74%|"
                                    "Common Sense Media = 4/5",
                                    "1hr 37min")
# How to Train your Dragon movie: movie title, storyline,
# poster image, trailer, release date, director, cast,
# budget, collection, ratings, duration
How_to_Train_your_Dragon = media.Movie("How to Train your Dragon",
                                       "A Viking breaks all rules and "
                                       "befriends a\ndragon he is supposed "
                                       "to kill. He decides to call "
                                       "him Toothless. They join\nforces to"
                                       " put an end to the terror that "
                                       "wreaks havoc in their "
                                       "respective worlds.",
                                       "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",  # noqa
                                       "https://www.youtube.com/watch?v=oKiYuIsPxYk",  # noqa
                                       "16 April 2010",
                                       "Dean DeBlois,\nChris Sanders",
                                       "Jay Baruchel,\nGerard Butler,\nCraig"
                                       " Ferguson,\nAmerica Ferrera,\nJonah "
                                       "Hill,\nChristopher Mintz-Plasse,\n"
                                       "T.J. Miller,\nKristen Wiig\n",
                                       "$165 million",
                                       "$495.8 million",
                                       "IMDb = 8.1/10|Metacritic = 74%|"
                                       "Rotten Tomatoes = 98%",
                                       "1hr 38min")
# The Boss Baby movie: movie title, storyline, poster image, trailer,
# release date, director, cast, budget, collection, ratings
# duration
The_Boss_Baby = media.Movie("The Boss Baby",
                            "Seven-year-old Tim gets jealous when his\nparents"
                            " give all their attention to his little"
                            " brother.\n",
                            "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=r8kE7rSzfQs",
                            "31 March 2017",
                            "Tom McGrath",
                            "Alec Baldwin,\nSteve Buscemi,\nMiles Bakshi,"
                            "\nJimmy Kimmel,\nLisa Kudrow\n",
                            "$125 million",
                            "$528 million",
                            "IMDb = 6.3/10|Rotten Tomatoes = 53%",
                            "1hr 37min")
# The Angry Bird movie: movie title, storyline, poster image, trailer,
# release date, director, cast, budget, collection, ratings
# duration
The_Angry_Bird = media.Movie("The Angry Birds",
                             "Red, Chuck and Bomb have always been the\n"
                             "outcasts within a community of flightless"
                             " birds on an island.\n",
                             "https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png",  # noqa
                             "https://www.youtube.com/watch?v=1U2DKKqxHgE",
                             "11 May 2016",
                             "Clay Kaytis,\nFergal Reilly",
                             "Jason Sudeikis,\nJosh Gad,\nDanny McBride,"
                             "\nMaya Rudolph,\nKate McKinnon,\nSean Penn,"
                             "\nTony Hale,\nKeegan-Michael Key,"
                             "\nBill Hader,\nPeter Dinklage\n",
                             "$73 million",
                             "$352.3 million",
                             "IMDb = 6.3/10|Metacritic = 43%|"
                             "Rotten Tomatoes = 43%",
                             "1hr 37min")
# Kung fu Panda movie: movie title, storyline, poster image, trailer,
# release date, director, cast, budget, collection, ratings
# duration
Kungfupanda = media.Movie("Kung Fu Panda",
                          "When an obese Po the Panda, a kung fu \n"
                          "enthusiast,gets selected as the Dragon"
                          " Warrior\n",
                          "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",  # noqa
                          "https://www.youtube.com/watch?v=PXi3Mv6KMzY",
                          "11 July 2008",
                          "Mark Osborne,\nJohn Stevenson",
                          "Jack Black,\nDustin Hoffman,\nAngelina Jolie,"
                          "\nIan McShane,\nSeth Rogen,\nLucy Liu,\nDavid "
                          "Cross,\nRandall Duk Kim,\nJames "
                          "Hong,\nJackie Chan\n",
                          "$130 million",
                          "$631.7 million",
                          "IMDb = 7.6/10|Metacritic = 73%|"
                          "Rotten Tomatoes = 87%",
                          "1hr 35min")
# Coco movie: movie title, storyline, poster image, trailer,
# release date, director, cast, budget, collection, ratings
# duration
Coco = media.Movie("Coco",
                   "Young Miguel dreams of becoming an accomplished \nmusician"
                   " like his idol Ernesto de la Cruz."
                   " Desperate to prove his talent\n",
                   "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",  # noqa
                   "https://www.youtube.com/watch?v=Ga6RYejo6Hk",
                   "27 October 2017",
                   "Lee Unkrich",
                   "Anthony Gonzalez,\nGael García Bernal,\nBenjamin Bratt,"
                   "\nAlanna Ubach,\nRenée Victor,\nAna Ofelia Murguía,"
                   "\nEdward James Olmos\n",
                   "$175–200 million",
                   "$807.1 million",
                   "IMDb = 8.4/10|Metacritic = 81%|Rotten Tomatoes = 97%",
                   "1hr 49min")
# Now you see me movie: movie title, storyline, poster image, trailer,
# release date, director, cast, budget, collection, ratings
# duration
Now_you = media.Movie("Now You See Me",
                      "The Horsemen, a group of four street magicians,\nrob a "
                      "huge sum of money that belongs to insurance magnate "
                      "Arthur Tressler.\nThe group is chased by FBI agent "
                      "Dylan Rhodes and Interpol agent Alma Dray.\n",
                      "https://upload.wikimedia.org/wikipedia/en/c/c7/Now_You_See_Me_Poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=4OtM9j2lcUA",
                      "21 May 2013",
                      "Louis Leterrier",
                      "\nJesse Eisenberg,\nMark Ruffalo,\nWoody Harrelson,"
                      "\nIsla Fisher,\nDave Franco,\nMélanie Laurent,"
                      "\nMichael Caine,\nMorgan Freeman\n",
                      "$75 million",
                      "$351.7 million",
                      "IMDb = 7.3/10|Metacritic = 50%|Rotten Tomatoes = 50%",
                      "1hr 55min")
# The Prestige movie: movie title, storyline, poster image, trailer,
# release date, director, cast, budget, collection, ratings
# duration
The_Prestige = media.Movie("The Prestige",
                           "Two friends and fellow magicians become bitter\n"
                           "enemies after a sudden tragedy. As they devote"
                           " themselves to this rivalry,\nthey make sacrifices"
                           " that bring them fame but with terrible "
                           "consequences.\n",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Prestige_poster.jpg/220px-Prestige_poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=ijXruSzfGEc",
                           "17 October 2006",
                           "Christopher Nolan",
                           "Hugh Jackman,\nChristian Bale,\nMichael Caine,\n"
                           "Scarlett Johansson,\nRebecca Hall,\nAndy Serkis"
                           ",\nDavid Bowie\n",
                           "$40 million",
                           "$109.7 million",
                           "IMDb = 8.5/10|Metacritic = 66%|"
                           "Rotten Tomatoes = 75%",
                           "2hr 10min")
# Game of Thrones Tv Show: Show's title, Show's storyline, Show's poster image,
# Show's trailer, Show's release date, Show's writers, Show's cast,
# Show's budget, Show's collection, Show's ratings, Show's duration
Game_of_thrones = media.TvShow("Game of Thrones",
                               "Several royal families desire the Iron Throne"
                               "\nto gain control of Westeros. Whilst kingdoms"
                               " fight each other for power,\na sinister force"
                               " lurks beyond the Wall in the north.\n",
                               "https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_title_card.jpg",  # noqa
                               "https://www.youtube.com/watch?v=BpJYNVhGf1s",
                               "17 April 2011",
                               "David Benioff,\nD. B. Weiss",
                               "Emilia Clarke,\nKit Harington,\nSophie Turner,"
                               "\nPinker Dinklage,\nLena Headey,"
                               "\nMaisie Williams,\nNikolaj Coster-Waldau,"
                               "\nGwendoline Christie,\nAlfie Allen \n",
                               "8",
                               "HBO",
                               "IMDb = 9.5/10|TV.com = 9/10|"
                               "Rotten Tomatoes = 94%",
                               "67hr")
# Castle Rock Tv Show: Show's title, Show's storyline, Show's poster image,
# Show's trailer, Show's release date, Show's writers, Show's cast,
# Show's budget, Show's collection, Show's ratings, Show's duration
Castle_Rock = media.TvShow("Castle Rock",
                           "Henry returns to Castle Rock, Maine, unsettled by"
                           "\nthe place he once called home; based on the"
                           " literary canon of Stephen King.\n",
                           "https://upload.wikimedia.org/wikipedia/en/8/8a/CastleRock.png",  # noqa
                           "https://www.youtube.com/watch?v=gXsKCQenpt0",
                           "25 July 2018",
                           "Dustin Thomason,\nSam Shaw",
                           "André Holland,\nMelanie Lynskey,\nBill Skarsgård,"
                           "\nJane Levy,\nSissy Spacek\n",
                           "1",
                           "Hulu",
                           "IMDb = 8.8/10|Hulu = 4.7/5|Rotten Tomatoes = 79%",
                           "10hr")
# Orange Is The New Black Tv Show: Show's title, Show's storyline,
# Show's poster image, Show's trailer, Show's release date, Show's writers,
# Show's cast, Show's budget, Show's collection, Show's ratings
# Show's duration
Orange_Is_the_New_Black = media.TvShow("Orange Is The New Black",
                                       "Ten years after transporting drug "
                                       "money to Alex,\nPiper is imprisoned"
                                       " for the crime. The toughness of "
                                       "prison changes her\ndrastically as an"
                                       " individual, compelling her to do"
                                       " the unthinkable.\n",
                                       "https://upload.wikimedia.org/wikipedia/en/0/03/Orange_Is_the_New_Black_Season_1.jpg",  # noqa
                                       "https://www.youtube.com/watch?v=vY0qzXi5oJg",  # noqa
                                       "11 July 2013",
                                       "Jenji Kohan",
                                       "Taylor Schilling,\nLaura Prepon,\n"
                                       "Michael Harney,\nMichelle Hurst,\nKate"
                                       " Mulgrew,\nJason Biggs,\nUzo Aduba, "
                                       "\nDanielle Brooks,\nNatasha Lyonne,\n"
                                       "Taryn Manning,\nSelenis Leyva,\n"
                                       "Adrienne C. Moore,\nDascha Polanco,\n"
                                       "Nick Sandow,\nYael Stone,\nSamira"
                                       "Wiley,\nJackie Cruz,\nLea DeLaria,\n"
                                       "Elizabeth Rodriguez,\nJessica Pimen"
                                       "tel,\nLaura Gómez,\nMatt Peters,\nDale"
                                       " Soules\n",
                                       "6",
                                       "Netflix",
                                       "IMDb = 8.2/10|TV.com = 8.9/10|"
                                       "Rotten Tomatoes = 90%",
                                       "78hr")
# Suits Tv Show: Show's title, Show's storyline, Show's poster image,
# Show's trailer, Show's release date, Show's writers, Show's cast,
# Show's budget, Show's collection, Show's ratings, Show's duration
Suits = media.TvShow("Suits",
                     "Mike Ross, a talented young college dropout, is\nhired"
                     "as an associate by Harvey Specter, one of New York's"
                     " best lawyers.\nThey must handle cases while "
                     "keeping Mike's qualifications a secret.\n",
                     "https://upload.wikimedia.org/wikipedia/commons/c/cc/Suits_Logo.png",  # noqa
                     "https://www.youtube.com/watch?v=85z53bAebsI",
                     "11 July 2013",
                     "Aaron Korsh",
                     "Gabriel Macht,\nPatrick J. Adams,\nRick Hoffman,"
                     "\nMeghan Markle,\nSarah Rafferty,\nGina Torres,"
                     "\nAmanda Schull,\nDulé Hill,\nKatherine Heigl\n",
                     "8",
                     "USA Network",
                     "IMDb = 8.6/10|TV.com = 8.5/10|Rotten Tomatoes = 91%",
                     "80hr 16min")
# The Flash Tv Show: Show's title, Show's storyline, Show's poster image,
# Show's trailer, Show's release date, Show's writers, Show's cast,
# Show's budget, Show's collection, Show's ratings, Show's duration
The_Flash = media.TvShow("The Flash",
                         "Barry Allen, a forensic scientist with the Central\n"
                         "City police force, is struck by lightning in a "
                         "freak accident. When he\nwakes up after nine months,"
                         " he discovers that he can achieve great speeds.",
                         "https://upload.wikimedia.org/wikipedia/en/9/98/The_Flash_Intertitle.png",  # noqa
                         "https://www.youtube.com/watch?v=Yj0l7iGKh8g",
                         "7 October 2014",
                         "Greg Berlanti,\nAndrew Kreisberg,\nGeoff Johns",
                         "Grant Gustin,\nCandice Patton,\nDanielle Panabaker,"
                         "\nRick Cosnett,\nCarlos Valdes,\nTom Cavanagh,\n"
                         " Jesse L. Martin,\nKeiynan Lonsdale, "
                         "\nNeil Sandilands\n",
                         "5",
                         "The CW Television Network,\nTV Puls",
                         "IMDb = 8/10|TV.com = 7.8/10|Rotten Tomatoes = 86%",
                         "68hr 12min")
# Jessica Jones Tv Show: Show's title, Show's storyline, Show's poster image,
# Show's trailer, Show's release date, Show's writers, Show's cast,
# Show's budget, Show's collection, Show's ratings, Show's duration
Jessica_Jones = media.TvShow("Jessica Jones",
                             "Jessica settles in New York City and opens her\n"
                             "own detective agency, called Alias"
                             " Investigations, which seems to be\ncalled"
                             " into cases involving people who have"
                             " special abilities.\n",
                             "https://upload.wikimedia.org/wikipedia/en/8/8e/Jessica_Jones_Netflix.jpg",  # noqa
                             "https://www.youtube.com/watch?v=nWHUjuJ8zxE",
                             "20 November 2015",
                             "Melissa Rosenberg",
                             "Krysten Ritter,\nMike Colter,\nRachael Taylor,\n"
                             "Wil Traval,\nErin Moriarty,\nEka Darville,\n"
                             "Carrie-Anne Moss,\nDavid Tennant,\nJ.R. Ramirez,"
                             "\nTerry Chen,\nLeah Gibson,\nJanet McTeer\n",
                             "2",
                             "Netflix",
                             "IMDb = 8.1/10|TV.com = 8.5/10|"
                             "Rotten Tomatoes = 88%",
                             "22hr 32min")
# Sherlock Tv Show: Show's title, Show's storyline, Show's poster image,
# Show's trailer, Show's release date, Show's writers, Show's cast,
# Show's budget, Show's collection, Show's ratings, Show's duration
Sherlock = media.TvShow("Sherlock",
                        "Dr. Watson, a former army doctor, finds himself\n"
                        "sharing a flat with Sherlock Holmes, an eccentric"
                        " individual with a knack\nfor solving crimes. "
                        "Together, they take on the most unusual cases.\n",
                        "https://upload.wikimedia.org/wikipedia/en/4/4d/Sherlock_titlecard.jpg",  # noqa
                        "https://www.youtube.com/watch?v=xK7S9mrFWL4",
                        "25 July 2010",
                        "Mark Gatiss,\nSteven Moffat",
                        "Benedict Cumberbatch,\nMartin Freeman,\nRupert"
                        " Graves,\nUna Stubbs,\nMark Gatiss,\nLouise "
                        "Brealey,\nAndrew Scott,\nAmanda Abbington\n",
                        "4",
                        "BBC One,\nBBC HD,\nPublic Broadcasting Service",
                        "IMDb = 9.2/10|TV.com = 8.9/10|Rotten Tomatoes = 83%",
                        "18hr")
# The Fall Tv Show: Show's title, Show's storyline, Show's poster image,
# Show's trailer, Show's release date, Show's writers, Show's cast,
# Show's budget, Show's collection, Show's ratings, Show's duration
The_Fall = media.TvShow("The Fall",
                        "The psychological thriller examines the lives\n"
                        "of two hunters\n",
                        "https://upload.wikimedia.org/wikipedia/en/e/e1/The_Fall_%28TV_Series%29.png",  # noqa
                        "https://www.youtube.com/watch?v=dyFrBC1rAcg",
                        "13 May 2013",
                        "Jakob Verbruggen,\nAllan Cubitt",
                        "Gillian Anderson,\nJamie Dornan,\nLaura Donnelly,\n"
                        "Bronagh Waugh,\nBen Peel,\nMichael McElhatton,\n"
                        "Niamh McGrady,\nFrank McCusker,\nIan McElhinney,\n"
                        "John Lynch,\nArchie Panjabi,\nStuart Graham,\n"
                        "Aisling Franciosi,\nValene Kane,\nKaren Hassan,\n"
                        "Emmett J. Scanlan,\nBronágh Taggart,\nNick Lee,\n"
                        "Jonjo O'Neill,\nColin Morgan,\nBrian Milligan,\n"
                        "Séainín Brennan,\nSeán McGinley,\nRichard Coyle,\n"
                        "Aisling Bea,\nBarry Ward,\nGenevieve O'Reilly,\n"
                        "Aidan McArdle,\nRuth Bradley,\nDenise Gough,\n"
                        "Martin McCann\n",
                        "3",
                        "BBC Two,\nRTÉ One",
                        "IMDb = 8.2/10|TV.com = 8.8/10|Rotten Tomatoes = 89%",
                        "16hr 19min")
# 13 Reasons Why Tv Show: Show's title, Show's storyline, Show's poster image,
# Show's trailer, Show's release date, Show's writers, Show's cast,
# Show's budget, Show's collection, Show's ratings, Show's duration
Reasons_Why = media.TvShow("13 Reasons Why",
                           "Hannah, a young woman who takes\nher own life."
                           "Two weeks after her tragic death, a classmate\n"
                           "named Clay finds a mysterious box on his porch.\n",
                           "https://upload.wikimedia.org/wikipedia/en/7/73/Netflix%27s_13_Reasons_Why_title_screen.png",  # noqa
                           "https://www.youtube.com/watch?v=JebwYGn5Z3E",
                           "31 March 2017",
                           "Brian Yorkey",
                           "Dylan Minnette,\nKatherine Langford,\n"
                           "Christian Navarro,\nAlisha Boe,\nBrandon"
                           " Flynn,\nJustin Prentice,\nMiles Heizer,\nRoss "
                           "Butler,\nDevin Druid,\nAmy Hargreaves,"
                           "\nDerek Luke,\nKate Walsh,\nBrian d'Arcy James\n",
                           "2",
                           "Netflix",
                           "IMDb = 8.1/10|TV.com = 8.1/10|"
                           "Rotten Tomatoes = 53%",
                           "23hr 50min")
# Set the videos that will be passed to the media file
movies = [toy_story, avatar, avengers, batman, Rise_of_the_Guardians,
          How_to_Train_your_Dragon, The_Boss_Baby, The_Angry_Bird,
          Kungfupanda, Coco, Now_you, The_Prestige]
tv_shows = [Game_of_thrones, Castle_Rock,
            Orange_Is_the_New_Black, Suits, The_Flash,
            Jessica_Jones, Sherlock, The_Fall, Reasons_Why]
videos = [toy_story, avatar, avengers, batman, Rise_of_the_Guardians,
          How_to_Train_your_Dragon, The_Boss_Baby, The_Angry_Bird,
          Kungfupanda, Coco, Now_you, The_Prestige, Game_of_thrones,
          Castle_Rock, Orange_Is_the_New_Black, Suits, The_Flash,
          Jessica_Jones, Sherlock, The_Fall, Reasons_Why]
video = get_abt()
if video == "videos":
    # this will open the all the videos(movies & tvshows) on the website
    fresh_tomatoes.open_movies_page(videos)
elif video == "movies":
    # this will open only movies on the website
    fresh_tomatoes.open_movies_page(movies)
elif(video == "tvshows"):
    # this will open only tvshows on the website
    fresh_tomatoes.open_movies_page(tv_shows)
vl = "True"
while vl == "True":
    epi = input("Do you want to see the list of Number"
                " of\nEpisodes with season details"
                " of Tv Series\nof your like on google,\nPlease give your"
                " response as yes or no\n")
    if epi.lower() == "yes":
        vl = "True"
        gt = get_episodes()
        webbrowser.open(gt)
        print('-'*80)
    else:
        vl = "False"
        print("Ok, No Problem")
        print('-'*80)
vt = "True"
while vt == "True":
    m = input("Do you want to see the data"
              " of movies or\ntvshows like "
              "storyline etc\n"
              "Give your response as yes or no\n")
    if m.lower() == "yes":
        vt = "True"
        gh = get_info()
        print('-'*80)
    else:
        vt = "False"
        print("Ok, No Problem")
        print('-'*80)
mov = input("Do you want to search for related videos to a movie or"
            " tv show on youtube,\nGive your response as yes or no :\n")
if mov.lower() == "yes":
    telk = input("Which type of show you want to search about : ")
    # This will help you to search for related videos to anything,
    # including movies & tv shows
    webbrowser.open("https://www.youtube.com/results?search_query=related%3A"+telk)  # noqa
print("-"*80)
mv = input("Do you want to search for Movies or shows on google\n"
           " you can do that right from there,\nGive your respo"
           "nse as yes or no :\n")
if mv.lower() == "yes":
    te = input("Which you want to search about : ")
    # this will help you to search for related things to anything,
    # including movies & tv shows
    webbrowser.open("https://www.google.com/search?source=hp&ei=UDBpW8aCL4v9vASe0rjACA&q="+te+"&oq=avengers&gs_l=psy-ab.3..35i39k1l2j0i67k1l3j0i131i67k1j0i131k1j0i67k1l3.9836.10951.0.11265.10.9.0.0.0.0.366.893.2-2j1.4.0....0...1.1.64.psy-ab..6.4.1104.6...213.LAy7FPS26d0")  # noqa
print("-"*80)
tl = input("Are you planning to watch a movie of your "
           "like,\nGive your response as yes or no\n")
if tl.lower() == "yes":
    # this is a suggestion
    print("I will prefer Netfix, Amazon Prime & Hulu Plus for watching\n"
          "movies as you can get almost all the movies\nwhich"
          " are available\n")
    nel = input("Do you want to open Netfix, Give response as yes or no : ")
    if nel.lower() == "yes":
        # opens netflix on the webbrowser
        webbrowser.open("https://www.netflix.com/in/")
    ap = input("Do you want to open Amazon Prime Website, "
               "Give response as yes or no : ")
    if ap.lower() == "yes":
        # opens amazon prime on the webbrowser
        webbrowser.open("https://www.amazon.com/Prime-Movies/b?ie=UTF8&node=7613704011")  # noqa
    hp = input("Do you want to open Hulu Plus Website, Give"
               " response as yes or no : ")
    if hp.lower() == "yes":
        # opens hulu on the webbrowser
        webbrowser.open("https://www.hulu.com/welcome?orig_referrer=https%3A%2F%2Fwww.google.co.in%2F")  # noqa
print("-"*80)
tell = input("Are you planning to watch a tv show of your "
             "like,\nGive your response as yes or no\n")
if tell.lower() == "yes":
    print("I am getting you to a site on \nwhich you can "
          "search for you tv show & \nget how much time it"
          " will take to\nyou to watch the whole seasons"
          " & episodes\n")
    # opens a site where you can check for how much
    # time show will take you to see the whole session
    webbrowser.open("http://tiii.me/")
    print("I will prefer Netfix, HBO, Hulu for watching\ntv "
          "shows as you can get almost all the shows\nwhich"
          " are available\n")
    netfl = input("Do you want to open Netfix, Give response as yes or no : ")
    if netfl.lower() == "yes":
        # opens netflix on the webbrowser
        webbrowser.open("https://www.netflix.com/in/")
    hbo = input("Do you want to open HBO website, Give response as"
                " yes or no : ")
    if hbo.lower() == "yes":
        # opens HBO on the webbrowser
        webbrowser.open("https://www.hbo.com/")
    hul = input("Do you want to open Hulu, Give response as yes or no : ")
    if hul.lower() == "yes":
        # opens Hulu on the webbrowser
        webbrowser.open("https://www.hulu.com/welcome?orig_referrer=https%3A%2F%2Fwww.google.co.in%2F")  # noqa
    print("!!!Enjoy your Show!!!")
    print("-"*80)
else:
    print("No Problem, Enjoy your Show!!!")
    print("-"*80)
