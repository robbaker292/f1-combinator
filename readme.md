# F1 Combinator
Inspired by Chain Bear's [2019 Remixed! - The 27399 ways Max Verstappen could win the 2019 season](https://www.youtube.com/watch?v=jfa5O8sg8g0&ab_channel=ChainBear) video.

The premise is that the F1 season is instead made up of a subset of the normal. Depending on which races are chosen, who would win?

For example, if the 2020 season was just 1 race long, there's (as of the Sakhir GP) 16 possible seasons, with Hamilton winning 11 of them, Bottas 2, and Verstappen, Perez & Gasly one each. What about if the season was five races long? There's 4368 of these, with Hamilton winning 4217 and Bottas 151. And so on.

Run `python3 f1.py results.csv`. This will print an update followed by the first 10 wins encountered by each driver (this should show some interesting seasons), the totals for each driver grouped by season length and finally the total championship wins.

As of the Bahrain GP, the results are as follows:
| Driver | Championships | Percentage |
| --| -- | -- |
| **Hamilton** | 64890 | 99.02 |
| **Bottas** | 575 | 0.88 |
| **Perez** | 30 | 0.05 |
| **Verstappen** | 12 | 0.02 |
| **Sainz** | 8 | 0.01 |
| **Gasly** | 4 | 0.01 |
| **Stroll** | 4 | 0.01 |
| **Ocon** | 2 | 0.00 |
| **Ties** | 10 | 0.00 |

Another dominant season for Hamilton!

Interestingly, both Sainz, Stroll and Ocon all win championships depsite not winning a race. Sainz manages to win two four-race Championships:

| Driver | Wins |
| -- | -- | 
| **Sainz** | `Italy, Sakhir`, `Italy, Sakhir` and one of `Austria, Bahrain, Emilia Romagna, Portugal or Eifel`, |
| | `Austria, Italy, Bahrain, Sakhir`, and `Austria, Italy, Eifel, Sakhir` |
| **Gasly** | `Italy` (unsurprisingly), `Eifel, Italy`, `Portugal, Italy`, and `Italy, Bahrain` |
| **Stroll** | `Italy, Sakhir` and one of `Spain, Hungary, 70th Anniversary, or Styria` |
| **Ocon** | `Belgium, Sakhir` or `Britain, Sakhir` |

No-one other than Hamilton can win a season of 9 or more races.

There are 10 ties, which are where the points and countbacks between the top two drivers are the same.