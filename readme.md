# F1 Combinator
Inspired by Chain Bear's [2019 Remixed! - The 27399 ways Max Verstappen could win the 2019 season](https://www.youtube.com/watch?v=jfa5O8sg8g0&ab_channel=ChainBear) video.

The premise is that the F1 season is instead made up of a subset of the normal. Depending on which races are chosen, who would win?

Run `python3 f1.py`. This will print an update followed by the first 10 wins encountered by each driver (this should show some interesting seasons), the totals for each driver grouped by season length and finally the total championship wins.

As of the Bahrain GP, the results are as follows:
| Driver | Championships | Percentage |
| --| -- | -- |
| **Hamilton** | 32,530 | 99.28 |
| **Bottas** | 220 | 0.67 |
| **Verstappen** | 7 | 0.02 |
| **Gasly** | 4 | 0.01 |
| **Ties** | 6 | 0.02 |

Another dominant season for Hamilton!

Gasly's 4 wins are: {Italy} (unsurprisingly), {Eifel, Italy}, {Portugal, Italy}, and {Italy, Bahrain}, which are basically all the races where Gasly won and beat Hamilton's 7th place (+ fastest lap) in Italy.

No-one other than Hamilton can win a season of 8 or more races, although there are only three 7-race championships Bottas can win: Austria, Styria, 70th Anniversary, Italy, Russia, Belgium and one of Tuscany, Portugal and Emilia Romagna.

There are 6 ties, which are where the points and countbacks between the top two drivers are the same.