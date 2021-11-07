# F1 Combinator
Inspired by Chain Bear's [2019 Remixed! - The 27399 ways Max Verstappen could win the 2019 season](https://www.youtube.com/watch?v=jfa5O8sg8g0&ab_channel=ChainBear) video.

The premise is that the F1 season is instead made up of a subset of the normal. Depending on which races are chosen, who would win?

For example, if the 2020 season was just 1 race long, there's 17 possible seasons, with Hamilton winning 11 of them, Bottas and Verstappen 2, and Perez & Gasly one each. What about if the season was five races long? There's 6188 of these, with Hamilton winning 5813, Bottas 307, and Verstappen 62. And so on.

Run `python3 f1.py 2020.csv`. This will print an update followed by the first 10 wins encountered by each driver (this should show some interesting seasons), the totals for each driver grouped by season length and finally the total championship wins.

The results are as follows:
| Driver | Championships | Percentage |
| --| -- | -- |
| **Hamilton** | 129419 | 98.74 |
| **Bottas** | 1389 | 1.06 |
| **Verstappen** | 181 | 0.14 |
| **Perez** | 32 | 0.02 |
| **Sainz** | 12 | 0.01 |
| **Gasly** | 5 | 0.00 |
| **Stroll** | 4 | 0.00 |
| **Ocon** | 2 | 0.00 |
| **Ties** | 27 | 0.00 |

Another dominant season for Hamilton!

Interestingly, both Sainz, Stroll and Ocon all win championships despite not winning a race.

| Driver | Wins |
| -- | -- | 
| **Sainz** | `Italy, Sakhir`, `Italy, Sakhir` and one of `Austria, Bahrain, Emilia Romagna, Portugal, Eifel or Abu Dhabi`, |
| | `Italy, Sakhir`, and  a pair of `Eifel, Abu Dhabi`, `Eifel, Sakhir`, `Turkey, Abu Dhabi`, or `Austria, Bahrain` |
| **Gasly** | `Italy` (unsurprisingly), `Eifel, Italy`, `Portugal, Italy`, `Italy, Bahrain` and `Italy, Abu Dhabi` |
| **Stroll** | `Italy, Sakhir` and one of `Spain, Hungary, 70th Anniversary, or Styria` |
| **Ocon** | `Belgium, Sakhir` or `Britain, Sakhir` |


Sainz (5) and Perez (8) win four-race championships, along with the top 3.
No-one other than Hamilton can win a season of 10 or more races, while Stroll can only win a three-race season.

| Season Length | HAM | BOT | VER | PER | SAI | GAS | STR | OCO |
| -- | -- | -- | -- | -- | -- | -- | -- | -- |
| 1 | 11 | 2 | 2 | 1 | - | 1 | - | - |
| 2 | 84 | 19 | 7 | 11 | 1 | 4 | - | 2 | 
| 3 | 559 | 66 | 26 | 12 | 6 | - | 4 | - |
| 4 | 2132 | 181 | 48 | 8 | 5 | - | - | - |
| 5 | 5813 | 307 | 62 | - | - | - | - | - |
| 6 | 11998 | 346 | 32 | - | - | - | - | - |
| 7 | 19171 | 273 | 4 | - | - | - | - | - |
| 8 | 24168 | 142 | - | - | - | - | - | - |
| 9 | 24257 | 53 | - | - | - | - | - | - |
| 10 | 19448 | - | - | - | - | - | - | - |
| 11 | 12376 | - | - | - | - | - | - | - |
| 12 | 6188 | - | - | - | - | - | - | - |
| 13 | 2380 | - | - | - | - | - | - | - |
| 14 | 680 | - | - | - | - | - | - | - |
| 15 | 136 | - | - | - | - | - | - | - |
| 16 | 17 | - | - | - | - | - | - | - |
| 17 | 1 | - | - | - | - | - | - | - |

There are 27 ties, which are where the points and countbacks between the top two drivers are the same.
