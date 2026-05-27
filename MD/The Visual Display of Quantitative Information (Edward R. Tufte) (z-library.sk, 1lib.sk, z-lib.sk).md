Edward R. Tufte

# The Visual Display of Quantitative Information

SECOND EDITION

Copyright © 2001 by Edward Rolf Tufte Published By Graphics Press LLC Post Office Box 430, Cheshire, Connecticut 06410

A pssion;yrolr p

## Contents

PART I GRAPHICAL PRACTICE   
1 Graphical Excellence 13   
2 Graphical Integrity 53   
3 Sources of Graphical Integrity and Sophistication 79   
PART II THEORY OF DATA GRAPHICS   
4 Data-Ink and Graphical Redesign 91   
5 Chartjunk: Vibrations, Grids, and Ducks 107   
6 Data-Ink Maximization and Graphical Design 123   
7 Multifunctioning Graphical Elements 139   
8 Data Density and Small Multiples 161   
9 Aesthetics and Technique in Data Graphical Design 177   
Epilogue: Designs for the Displayf Informatin 191

For my parents Edward E. Tufte and Virginia James Tufte

To the memory of

John W. Tukey (19152000)

## Introduction to the Second Edition

This new edition provides high-resolution color reproductions of the many graphics of William Playfair, adds color to other images where appropriate, and includes all the changes and corrections accumulated during the 17 printings of the first edition.

This book began in 1975 when Dean Donald Stokes of Princeton's Woodrow Wilson School asked me to teach statistics to a dozen journalists who were visiting that year to learn some economics. I annotated a collection of readings, with a long section on statistical graphics. The literature here was thin, too often grimly devoted to explaining use of the ruling pen and to promulgating "graphic standards" indifferent to the nature of visual evidence and quantitative reasoning. Soon I wrote up some ideas. Then John Tukey, the phenomenal Princeton statistician, suggested that we give a series of joint seminars. Since the mid-196os, Tukey had opened up the field, as his brilliant technical contributions made it clear that the study o statistical graphics was intellectually respectable and not just about pie charts and ruling pens.

After moving to Yale University, I finished the manuscript in 1982. A publisher was interested but planned to print only 2,000 copies and to charge a very high price, contrary to my hopes for a wide readership. I also sought to design the book so as to make it sel-exemplifying—that is, the physical object itself would reflect the intellectual principles advanced in the book. Publishers seemed appalled at the prospect that an author might govern design.

Consequently I investigated self-publishing. This required a firstrate book designer, a lot of money (at least for a young professor), and a large garage. I found Howard Gralla who had designed many museum catalogs with great care and craft. He was willing to work closely with this difficult author who was filled with all sorts of opinions about design and typography. We spent the summer in his studio laying out the book, page by page. We were able to integrate graphics right into the text, sometimes into the middle of a sentence, eliminating the usual separation of text and image— one of the ideas Visual Display advocated. To finance the book I took out another mortgage on my home. The bank officer said this was the second most unusual loan that she had ever made; first place belonged to a loan to a circus to buy an elephant!

My view on self-publishing was to go all out, to make the best and most elegant and wonderful book possible, without compromise. Otherwise, why do it?

Most of all, the book, as a thing in itself, gave to me fresh new eyes for the intellectual and aesthetic joy of visual evidence, visual reasoning, and visual understanding.

January 2001 Cheshire, Connecticut

## Introduction

Data graphics visually display measured quantities by means of the combined use of points, lines, a coordinate system, numbers, symbols, words, shading, and color.

The use of abstract, non-representational pictures to show numbers is a surprisingly recent invention, perhaps because of the diversity of skills required—the visual-artistic, empirical-statistical, and mathematical. It was not until 17501800 that statistical graphics— length and area to show quantity, time-series, scatterplots, and multivariate displays—were invented, long after such triumphs of mathematical ingenuity as logarithms, Cartesian coordinates, the calculus, and the basics of probability theory. The remarkable William Playfair (1759-1823) developed or improved upon nearly all the fundamental graphical designs, seeking to replace conventional tables of numbers with the systematic visual representations of his "linear arithmetic.

Modern data graphics can do much more than simply substitute for small statistical tables. At their best, graphics are instruments for reasoning about quantitative information. Often the most effective way to describe, explore, and summarize a set of numbers— even a very large set—is to look at pictures of those numbers. Furthermore, of all methods for analyzing and communicating statistical information, well-designed data graphics are usually the simplest and at the same time the most powerful.

The first part of this book reviews the graphical practice of the two centuries since Playfair. The reader will, I hope, rejoice in the graphical glories shown in Chapter 1 and then condemn the lapses and lost opportunities exhibited in Chapter 2. Chapter 3, on graphical integrity and sophistication, seeks to account for these differences in quality of graphical design.

The second part of the book provides a language for discussing graphics and a practical theory of data graphics. Applying to most visual displays of quantitative information, the theory leads to changes and improvements in design, suggests why some graphics might be better than others, and generates new types of graphics. The emphasis is on maximizing principles, empirical measures of graphical performance, and the sequential improvement of graphics through revision and editing. Insights into graphical design are to be gained, I believe, from theories of what makes for excellence in art, architecture, and prose.

This is a book about the design of statistical graphics and, as such, it is concerned both with design and with statistics. But it is also about how to communicate information through the simultaneous presentation of words, numbers, and pictures. The design of statistical graphics is a universal matter-like mathematics—and is not tied to the unique features of a particular language. The descriptive concepts (a vocabulary for graphics) and the principles advanced apply to most designs. I have at times provided evidence about the scope of these ideas, by showing how frequently a principle applies to (a random sample of) news and scientific graphics.

Each year, the world over, somewhere between 9oo billion (9×1011) and 2 trillion (2× 1012) images of statistical graphics are printed. The principles of this book apply to most of those graphics. Some of the suggested changes are small, but others are substantial, with consequences for hundreds of billions of printed pges.

But I hope also that the book has consequences for the viewers and makers of those images—that they will never view or create statistical graphics the same way again. That is in part because we are about to see, collected here, so many wonderful drawings, those of Playfair, of Minard, of Marey, and, nowadays, of the computer.

Mos the,h bok  celati  t ras.

Graphical Practice

PART I

## I Graphical Excellence

Excellence in statistical graphics consists of complex ideas communicated with clarity, precision, and efficiency. Graphical displays should

show the data

induce the viewer to think about the substance rather than about methodology, graphic design, the technology of graphic production, or something else

avoid distorting what the data havet y

present many numbers in a small space

make large data sets coherent

encourage the eye to compare different pieces of data

reveal the data at several levels of detail, from a broad overview to the fine structure

serve a reasonably clear purpose: description, exploration, tabulation, or decoration

be closely integrated with the statistical and verbal descriptions of a data set.

Graphics reveal data. Indeed graphics can be more precise and revealing than conventional statistical computations. Consider Anscombe's quartet: all four of these data sets are described by exactly the same linear model (at least until the residuals are examined).

<table><tr><td colspan="2"></td><td colspan="2">II</td><td colspan="2">III</td><td colspan="2">IV X Y</td><td></td><td></td></tr><tr><td>X</td><td>Y</td><td>X</td><td>Y</td><td>X</td><td>Y</td><td></td><td></td><td></td><td></td></tr><tr><td>10.0</td><td>8.04</td><td>10.0</td><td>9.14</td><td>10.0</td><td>7.46</td><td>8.0</td><td>6.58</td><td></td><td>N = 11</td></tr><tr><td>8.0</td><td>6.95</td><td>8.0</td><td>8.14</td><td>8.0</td><td>6.77</td><td>8.0</td><td>5.76</td><td></td><td>mean of X&#x27;s = 9.0</td></tr><tr><td>13.0</td><td>7.58</td><td>13.0</td><td>8.74</td><td>13.0</td><td>12.74</td><td>8.0</td><td>7.71</td><td></td><td>mean of Y&#x27;s = 7.5</td></tr><tr><td>9.0</td><td>8.81</td><td>9.0</td><td>8.77</td><td>9.0</td><td>7.11</td><td></td><td>8.0</td><td>8.84</td><td>equation of regression line:Y = 3+0.5X</td></tr><tr><td>11.0</td><td>8.33</td><td>11.0</td><td>9.26</td><td>11.0</td><td>7.81</td><td></td><td>8.0</td><td>8.47</td><td>standard error of estimate of slope = 0.118</td></tr><tr><td>14.0</td><td>9.96</td><td>14.0</td><td>8.10</td><td>14.0</td><td>8.84</td><td></td><td>8.0 7.04</td><td></td><td>t = 4.24</td></tr><tr><td>6.0</td><td>7.24</td><td>6.0</td><td>6.13</td><td>6.0</td><td>6.08</td><td>8.0</td><td>5.25</td><td></td><td>sum of squares X - X = 110.0</td></tr><tr><td>4.0</td><td>4.26</td><td>4.0</td><td>3.10</td><td>4.0</td><td>5.39</td><td></td><td>19.0 12.50</td><td></td><td>regression sum of squares = 27.50</td></tr><tr><td>12.0</td><td>10.84</td><td>12.0</td><td>9.13</td><td>12.0</td><td>8.15</td><td></td><td>8.0 5.56</td><td></td><td>residual sum of squares of Y = 13.75</td></tr><tr><td>7.0</td><td>4.82</td><td>7.0</td><td>7.26</td><td>7.0</td><td>6.42</td><td></td><td>8.0 7.91</td><td></td><td>correlation coefficient = .82</td></tr><tr><td>5.0</td><td>5.68</td><td>5.0</td><td>4.74</td><td>5.0</td><td>5.73</td><td></td><td>8.0</td><td>6.89</td><td>$r{2}=.67</td></tr></table>

And yet how they differ, as the graphical display of the data makes vividly clear:

F. J. Anscombe, "Graphs in Statistical Analysis," American Statistician, 27 (February 1973), 1721.

![](images/9345f6d4bb8c6b198fc39d0c1061cbf63a19c8fe081ffe574c18800bf58d48bc.jpg)

![](images/6475e1dfedb590bed34f8a5e45a483662dd04d26774f7113d5a8665f7f5d609b.jpg)

![](images/9918ad901d63bbf955e7e72a14aae76f555da69b73e864a11be55f7194bfacb2.jpg)

![](images/04d33619297eabbe0aaa5014c7b097c247c7028cc3b9940f91e75709f9a44bfa.jpg)

And likewise a graphic easily reveals point A, a wildshot observation that will dominate standard statistical calculations. Note that point A hides in the marginal distribution but shows up as clearly exceptional in the bivariate scatter.

![](images/c8e5df8443903c1ae3fe3cf9fc50fd2e78c9e7df0bf6e473f1a8ceba7e02c067.jpg)

Stephen S. Brier and Stephen E. Fienberg, "Recent Econometric Modelling of Crime and Punishment: Support for the Deterrence Hypothesis?" in Stephen E. Fienberg and Albert J. Reiss, Jr., eds., Indicators of Crime and Criminal Justice: Quantitative Studies (Washington, D.C., 1980), p. 89.

Of course, statistical graphics, just like statistical calculations, are only as good as what goes into them. An ill-specified or preposterous model or a puny data set cannot be rescued by a graphic (or by calculation), no matter how clever or fancy. A silly theory means a silly graphic:

Edward R. Dewey and Edwin F. Dakin, Cycles: The Science of Prediction (New York, 1947), p. 144.

![](images/d33af5adeaba085268e4035efb0c9dc34eeadbe539c279c3c8c586c1c51eccbc.jpg)  
Solar Radiation And Stock PricEs  
A. New York stock prices (Barron's average). B. Solar Radiation, inverted, and C. London stock prices, all by months, 1929 (after Garcia-Mata and Shaffner).

Let us turn to the practice of graphical excellence, the efficient communication of complex quantitative ideas. Excellence, nearly always of a multivariate sort, is illustrated here for fundamental graphical designs: data maps, time-series, space-time narrative designs, and relational graphics. These examples serve several purposes, providing a set of high-quality graphics that can be discussed (and sometimes even redrawn) in constructing a theory of data graphics, helping to demonstrate a descriptive terminology, and telling in brief about the history of graphical development. Most of all, we will be able to see just how good statistical graphics can be.

## Data Maps

These six maps report the age-adjusted death rate from various types of cancer for the 3,o56 counties of the United States. Each map portrays some 21,ooo numbers.1 Only a picture can carry such a volume of data in such a small space. Furthermore, all that data, thanks to the graphic, can be thought about in many different ways at many different levels of analysis—ranging from the contemplation of general overall patterns to the detection of very fine county-by-county detail. To take just a few examples, look at the

1 Each county's rate is located in two dimensions and, further, at least four numbers would be necessary to reconstruct the size and shape of each county. This yields 7× 3,056 entries in a data matrix sufficient to reproduce a map.

and around the Great Lakes

In highest decile, statistically significant

y

er rat r men than r we he outh, partuy Louisiana (cancers probably caused by occupational exposure, from working with asbestos in shipyards)

Significantly high, but not in highest decile

In highest decile, but not statistically significant

unusual hot spots, including northern Minnesota and a few counties in Iowa and Nebraska along the Missouri River

Not significantly different from U.S. as a whole

differences in types of cancer by region (for example, the high rate of stomac cancer in the north-central part of the country —probably the result of the consumption of smoked fish by Scandinavians)

Significantly lower than U.S. as a whole

rates in areas where you have lived.

The maps provide many leads into the causes—and avoidance— of cancer. For example, the authors report:

In certain situations . .  the unusual experience of a cnty warrants further investigation. For example, Salem County, New Jersey, leads the nation in bladder cancer mortality among white men. We attribute this excess risk to occupational exposures, since about 25 percent of the employed persons in this county work in the chemical industry, particularly the manufacturing of organic chemicals, which may cause bladder tumors. After the finding was communicated to New Jersey health officials, a company in the area reported that at least 330 workers in a single plant had developed bladder cancer during the last 5o years. It is urgent that surveys of cancer risk and programs in cancer control be initiated among workers and former workers in this area.2

2Robert Hoover, Thomas J. Mason, Frank W. McKay, and Joseph F. Fraumeni, Jr., "Cancer by County: New Resource for Etiologic Clues," Science, 189 (September 19, 1975), 1006.

Maps from Atlas of Cancer Mortality for U.S. Counties: 1950-1969, by Thomas J. Mason, Frank W. McKay, Robert Hoover, William J. Blot, and Joseph F. Fraumeni, Jr. (Washington, D.C.: Public Health Service, National Institutes of Health, 1975). The six maps shown here were redesigned and redrawn by Lawrence Fahey and Edward Tufte.

![](images/d2c2cfffacfa3288c2fff42baaeec607c39da9c01047901c5de2af7005c25e4a.jpg)

![](images/6c79563f3993c87823df271005a2474bde83d165a8f7d4b296d0a9b63b406690.jpg)

![](images/4824b1139dbb576f4a28d53173b0cf1c35021bc3de431ba47c2dbb91df384e28.jpg)

![](images/1c20b4f97cadb302d6e8f5777c3891f381bcf2e94276a1ea339b45c9ba08506e.jpg)

![](images/e59ad49f20c36496e51c0bb4147cece3153c79f8af0002a41d43de5e2c6465ce.jpg)

![](images/a547eee808e0426ebfc9b97a93233cae421349d3ad7f39ea688c60e61009d9d4.jpg)

The maps repay careful study. Notice how quickly and naturally our attention has been directed toward exploring the substantive content of the data rather than toward questions of methodology and technique. Nonetheless the maps do have their flaws. They wrongly equate the visual importance of each county with its geographic area rather than with the number of people living in the county (or the number of cancer deaths). Our visual impression of the data is entangled with the circumstance of geographic boundaries, shapes, and areas—the chronic problem afflicting shadedin-rea designs of such "blot maps" or "patch maps."

A further shortcoming, a defect of data rather than graphical composition, is that the maps are founded on a suspect data source, death certificate reports on the cause of death. These reports fall under the influence of diagnostic fashions prevailing among doctors and coroners in particular places and times, a troublesome adulterant of the evidence purporting to describe the already sometimes ambiguous matter of the exact bodily site of the primary cancer. Thus part of the regional clustering seen on the maps, as well as some of the hot spots, may reflect varying diagnostic customs and fads along with the actual differences in cancer rates between areas.

Data maps have a curious history. It was not until the seventeenth century that the combination of cartographic and statistical skills required to construct the data map came together, fully 5,ooo years after the first geographic maps were drawn on clay tablets. And many highly sophisticated geographic maps were produced centuries before the first map containing any statistical material was drawn.³ For example, a detailed map with a full grid was engraved during the eleventh century A.D. in China. The Yü Chi Thu (Map of the Tracks of Yü the Great) shown here is described by Joseph Needham as the

. . . most remarkable cartographic work of its age in any culture, carved in stone in + 1137 but probably dating from before + 1100. The scale of the grid is 100 li to the division. The coastal outline is relatively firm and the precisionof the network of river systems extraordinary.The size of theoriginal, which is now in the Pei Lin Museum at Sian, is about 3 feet square. The name of the geographer is not known. . .. Anyone who compares this map with the contemporary productions of European religious cosmography cannot but be amazed at the extent to which Chinese geographywas at that time ahead of the West. . . . There was nothing like it in Europe till the Escorial MS. map of about + 1550. . . .4

3 Data maps are usually described as thematic maps" in cartography. For a thorough account, see Arthur H. Robinson, Early Thematic Mapping in the History of Cartography (Chicago, 1982). On the history of statistical graphics, see H. Gray Funkhouser, "Historical Devel opment of the Graphical Representation of Statistical Data," Osiris, 3 (November 1937), 269404; and James R. Beniger and Dorothy L. Robyn, "Quantitative Graphics in Statistics: A Brief History," American Statistician, 32 (February 1978), 1-11.

4Joseph Needham, Science and Civilisation in China (Cambridge, 1959), vol. 3, 546-547.

![](images/477c7ed8f425536c6dcb15c5c96409bfdb2ff9aa6de532bb790722c6478ad71c.jpg)  
E. Chavannes, "Les Deux Plus Anciens Spécimens de la Cartographie Chinoise," Bulletin de I'École Française de l'Extréme Orient, 3 (1903), 135, Carte B.

# Ecce formulam,vfum,atque

turaabua o, qu du Ghi    .

SEPTENTRIO. pars uperior.

![](images/c3bf9aecde4b8eb08221e65f2d766441cc2708f94569a7f2adb616be8696a7a3.jpg)

![](images/607b3512ad83d6dc44b3f6d2388f2fe1213f0de0d48d27a1a3f27717a939a292.jpg)

The 1546 edition of Cosmographia by Petrus Apianus contained examples of map design that show how very close European cartography by that time had come to achieving statistical graphicacy, even approaching the bivariate scatterplot. But, according to the historical record, no one had yet made the quantitative abstraction of placing a measured quantity on the map's surface at the intersection of the two threads instead of the name of a city, let alone the more difficult abstraction of replacing latitude and longitude with some other dimensions, such as time and money. Indeed, it was not until 1786 that the first economic time-series was plotted.

![](images/7a118a1610fe63b7e20a105531b92d1adb8681270fac31f6ad2dd25bffc424fb.jpg)

One of the first data maps was Edmond Halley's 1686 chart showing trade winds and monsoons on a world map.5 The detailed section below shows the cartographic symbolization; with, as Halley wrote, the sharp end of each little stroak pointing that part of the Horizon, from whence the wind continually comes; and where there are Monsoons the rows of stroaks run alternately backwards and forwards, by which means they are thicker [denser] than elsewhere."

![](images/8f4c6cb9cdc0a89a596bb4734d08b050f0cd795c908ca1ac3ff37a313bc65d87.jpg)  
5Norman J. W. Thrower, "Edmond Halley as a Thematic Geo-Cartographer," Annals of the Association of American Geographers, 59 (December 1969), 652676.

Edmond Halley, "An Historical Account of the Trade Winds, and Monsoons, Observable in the Seas Between and Near the Tropicks; With an Attempt to Assign the Phisical Cause of Said Winds," Philosophical Transactions, 183 (1686), 153168.

An early and most worthy use of a map to chart patterns of disease was the famous dot map of Dr. John Snow, who plotted the location of deaths from cholera in central London for September 1854. Deaths were marked by dots and, in addition, the area's eleven water pumps were located by crosses. Examining the scatter over the surface of the map, Snow observed that cholera occurred almost entirely among those who lived near (and drank from) the Broad Street water pump. He had the handle of the contaminated pump removed, ending the neighborhood epidemic which had taken more than 5oo lives.6 The pump is located at the center of the map, just to the right of the D in BROAD sTREET. Of course the link between the pump and the disease might have been revealed by computation and analysis without graphics, with some good luck and hard work. But, here at least, graphical analysis testifies about the data far more efficiently than calculation.

6E. W. Gilbert, "Pioneer Maps of Health and Disease in England," Geographical Journal, 124 (1958), 172183. Shown here is a redrawing of John Snow's map. For a reproduction and detailed analysis of the original map, see Edward Tufte, Visual Explanations: Images and Quantities, Evidence and Narrative (Cheshire, Connecticut, 1997), Chapter 2. Ideally, see John Snow, On the Mode of Communication of Cholera (London, 1855).

![](images/0d288041d9c6a01d827ac248d19d8587cb32e89b588c88767fbc65cd860a9778.jpg)

Charles Joseph Minard gave quantity as well as direction to the data measures located on the world map in his portrayal of the 1864 exports of French wine:

![](images/b001e49f421676d5779c1bcd0cdc3af2e414f27a0a69d6f10a110ac810a644b2.jpg)

Computerized cartography and modern photographic techniques have increased the density of information some 5,ooo-fold in the best of current data maps compared to Halley's pioneering effort. This map shows the distribution of 1.3 million galaxies (including some overlaps) in the northern galactic hemisphere. The map divides the sky into 1,024 × 2,222 rectangles. The number of galaxies counted in each of the 2,275,328 rectangles is represented by ten gray tones; the darker the tone, the greater the number of galaxies counted. The north galactic pole is at the center. The sharp edge on the left results from the earth blocking the view from the observatory. In the area near the perimeter of the map, the view is obscured by the interstellar dust of the galaxy in which we live (the Milky Way) as the line of sight passes through the flattened disk of our galaxy. The curious texture of local clusters of galaxies seen in this truly new view of the universe was not anticipated by students of galaxies, who had, of course, microscopically examined millions of photographs of galaxies before seeing this macroscopic view. Although the clusters are clearly evident (and accounted for by a theory of galactic origins), the seemingly random filaments may be happenstance. The producers of the map note the "strong temptation to conclude that the gal axies are arranged in a remarkable filamentary pattern on scales of approximately 5° to 15°, but we caution that this visual impression may be misleading because the eye tends to pick out linear patterns even in random noise. Indeed, roughly similar patterns are seen on maps constructed from simulated catalogs where no linear structure has been built in. . . ."7

The most extensive data maps, such as the cancer atlas and the count of the galaxies, place millions of bits of information on a single page before our eyes. No other method for the display of statistical information is so powerful.

![](images/47d9c8acd6eb30e29733fce6def9d441eec860cf3e541145334b8286fa37c1ef.jpg)

7 Michael Seldner, B. H. Siebers, Edward J. Groth and P. James E. Peebles, "New Reduction of the Lick Catalog of Galaxies," Astronomical Journal, 82 (April 1977), 249-314. See Gillian R. Knapp, "Mining the Heavens: The Sloan Digital Sky Survey," Sky & Telescope (August 1997), 40-48; Margaret J. Geller and John P. Huchra, "Mapping the Universe," Sky & Telescope (Åugust 1991), 134-139.

![](images/d0c3d78d713efde19552d31e5e6efbb9c9c62e1bbb16e6c5aa1410bf7111c0eb.jpg)

## Time-Series

The time-series plot is the most frequently used form of graphic design.8 With one dimension marching along to the regular rhythm of seconds, minutes, hours, days, weeks, months, years, centuries, or millennia, the natural ordering of the time scale gives this design a strength and efficiency of interpretation found in no other graphic arrangement.

This reputed tenth- (or possibly eleventh-) century illustration of the inclinations of the planetary orbits as a function of time, apparently part of a text for monastery schools, is the oldest known example of an attempt to show changing values graphically. It appears as a mysterious and isolated wonder in the history of data graphics, since the next extant graphic of a plotted time-series shows up some 8oo years later. According to Funkhouser, the astronomical content is confused and there are difficulties in reconciling the graph and its accompanying text with the actual movements of the planets. Particularly disconcerting is the wavy path ascribed to the sun.9 An erasure and correction of a curve occur near the middle of the graph.

8 A random sample of 4,ooo graphics drawn from 15 of the world's newspapers and magazines published from 1974 to 198o found that more than 75 percent of all the graphics published were time-series. Chapter 3 reports more on this.

9H. Gray Funkhouser, "A Note on a Tenth Century Graph," Osiris, 1 (January 1936), 260262.

![](images/4481e5157637e4b8d90bfc0a7258a5414ecdf7e14b3cf1d49ea8956fc71345cf.jpg)

It was not until the late 17oos that time-series charts began to appear in scientific writings. This drawing of Johann Heinrich Lambert, one of a long series, shows the periodic variation in soil temperature in relation to the depth under the surface. The greater the depth, the greater the time-lag in temperature responsiveness. Modern graphic designs showing time-series periodicities differ little from those of Lambert, although the data bases are far larger.

![](images/9292f609cace2fa95b3c95a65a8ca67aae704880a1b7a356402900f3d0685252.jpg)  
J. H. Lambert, Pyrometrie (Berlin, 1779).

![](images/d69846a7d5716b8fade08292bbc99649f34ca337b9e9446b4775702f19d39286.jpg)

This plot of radio emissions from Jupiter is based on data collected by Voyager 2 in its pass close by the planet in July 1979. The radio intensity increases and decreases in a ten-hour cycle as Jupiter rotates. Maximum intensity occurs when the Jovian north magnetic pole is tipped toward the spacecraft, indicating a northern hemisphere source. A southern source was detected on July 7, as the spacecraft neared the equatorial plane. The horizontal scale shows the distance of the spacecraft from the planet measured in terms of Jupiter radii (R). Note the use of dual labels on the horizontal to indicate both the date and distance from Jupiter. The entire bottom panel also serves to label the horizontal scale, describing the changing orientation of the spacecraft relative to Jupiter as the planet is approached. The multiple time-series enforce not only comparisons within each series over time (as do all time-series plots) but also comparisons between the three different sampled radio bands shown. This richly multivariate display is based on 453,6oo instrument samples of eight bits each. The resulting 3.6 million bits were reduced by peak and average processing to the 18,9oo points actually plotted on the graphic.

D. A. Gurnett, W. S. Kurth, and F. L. Scarf, "Plasma Wave Observations Near Jupiter: Initial Results from Voyager $\overline { { 2 } } , \overline { { ^ { \circ } } }$ Science 206 (November 23, 1979), 987991; and letter from Donald A. Gurnett to Edward R. Tufte, June 27, 1980.

Time-series displays are at their best for big data sets with real variability. Why waste the power of data graphics on simple linear changes,

![](images/c526ce47754ae9eb2658508f8907f417da3194beeabf3ee0b849407543937f41.jpg)

which can usually be better summarized in one or two numbers? Instead, graphics should be reserved for the richer, more complex, more difficult statistical material. This New York City weather summary for 198o depicts 1,888 numbers. The daily high and low temperatures are shown in relation to the long-run average. The path of the normal temperatures also provides a forecast of expected change over the year; in the middle of February, for instance, New York City residents can look forward to warming at the rate of about 1.5 degrees per week all the way to July, the yearly peak. This distinguished graphic successfully organizes a large collection of numbers, makes comparisons between different parts of the data, and tells a story.

NEW YORK CITY'S WEATHER FOR 1980  
![](images/a6ee905ac29042d730c37dd708e857abc1743907fc54326fde487c569b5cd736.jpg)  
New York Times, January 11, 1981, p. 32.

![](images/012ac764f2d559f566e8403dcd1b1f5ad8fe8b980fe2e18baeb1441023ce6ee6.jpg)  
E. J. Marey, La méthode graphique (Paris, 1885), p. 20. The method is attributed to the French engineer, Ibry.

A design with similar strengths is Marey's graphical train schedule for Paris to Lyon in the 188os. Arrivals and departures from a station are located along the horizontal; length of stop at a station is indicated by the length of the horizontal line. The stations are separated in proportion to their actual distance apart. The slope of the line reflects the speed of the train: the more nearly vertical the line, the faster the train. The intersection of two lines locates the time and place that trains going in opposite directions pass each other.

In 1981 a new express train from Paris to Lyon cut the trip to under three hours, compared to more than nine hours when Marey published the graphical train schedule. The path of the modern TGV (train à grande vitesse) is shown, overlaid on the schedule of 100 years before:

![](images/9843a6847f917bf184f5f80dad8fa5edbe6d16db921282d24b0ed3a376816912.jpg)

The two great inventors of modern graphical designs were J. H. Lambert (17281777), a Swiss-German scientist and mathematician, and William Playfair (1759-1823), a Scottish political economist.10 The first known time-series using economic data was published in Playfair's remarkable book, The Commercial and Political Atlas (London, 1786). Note the graphical arithmetic, which shows the shifting balance of trade by the difference between the import and export time-series. Playfair contrasted his new graphical method with the tabular presentation of data:

10Laura Tilling, "Early Experimental Graphs," British Journal for the History of Science, 8 (1975), 193213.

Information, that is imperfectly acquired, is generally as imperfectly retained; and a man who has carefully investigated a printed table, finds, when done, that he has only a very faint and partial idea of what he has read; and that like a figure imprinted on sand, is soon totally erased and defaced. The amount of mercantile transactions in money, and of profit or loss, are capable of being as easily represented in drawing, as any part of space, or as the face of a country; though, till now, it has not been attempted. Upon that principle these Charts were made; and, while they give a simple and distinct idea, they are as near perfect accuracy as is any way useful. On inspecting any one of these Charts attentively, a sufficiently distinct impression will be made, to remain unimpaired for a considerable time, and the idea which does remain will be simple and complete, at once including the duration and the amount. [pages 3-4]

For Playfir, graphic were preferable t table because rais showed the shape of the data in a comparative perspective. Timeseries plots did this, and all but one of the 44 charts in the first edition of The Commercial and Political Atlas were time-series. That one exception is the first known bar chart, which Playfair invented because year-to-year data were missing and he needed a design to portray the one-year data that were available. Nonetheless he was skeptical about his innovation:

CHART of all the IMPORTS and EXPORTS o and Firem EN GLAND From the Year 1700 to 1782 by M. Playfair  
![](images/04120a35db0681e3745c086cd701b8f22c0d730ad27c059137f36e360c7b006b.jpg)  
The Divisions at the Bottom, expref YEARs, & thase on the Righthand,MILLroNs qPouNDS Iahialie Seale! Pubc  the d 20 78

This Chart is different from the others in principle, as it does not comprehend any portion of time, and it is much inferior in utility to those that do; for though it gives the extent of the different branches of trade, it does not compare the same branch of commerce with itself at different periods; nor does it imprint upon the mind that distinct idea, in doing which, the chief advantage of Charts consists: for as it wants the dimension that is formed by duration, there is no shape given to the quantities. [page 101]

He was right: small, noncomparative, highly labeled data sets usually belong in tables.

Exports and Importsof ScoTLanD tand from different part for one Year from Chritmas 8o to Chritmas 1781.  
![](images/7a3646796049cd90ad53b9f0ca2ca229f5a94deba3818ee3cf4b75058b33c4be.jpg)  
Dullidhad on dho

The chart does show, at any rate, the imports (cross-hatched lines) and exports (solid lines) to and from Scotland in 1781 for 17 countries, which are ordered by volume of trade. The horizontal scale is at the top, possibly to make it more convenient to see in plotting the points by hand. Zero values are nicely indicated both by the absence of a bar and by a "o." The horizontal scale mistakenly repeats "200." In nearly all his charts, Playfair placed the labels for the vertical scale on the right side of the page (suggesting that he plotted the data points using his left hand).

Playfair's last book addressed the question whether the price of wheat had increased relative to wages. In his Letter on our agricultural distresses, their causes and remedies; accompanied with tables and copper-plate charts shewing and comparing the prices of wheat, bread and labour, from 1565 to 1821, Playfair wrote:

You have before you, my Lords and Gentlemen, a chart of the prices of wheat for 250 years, made from official returns; on the same plate I have traced a line representing, as nearly as I can, the wages of good mechanics, such as smiths, masons, and carpenters, in order to compare the proportion between them and the price of wheat at every different period. . . . the main fact deserving of consideration is, that never at any former period was wheat so cheap, in proportion to mechanical labour, as it is at the present time. . . [pages 2931]

Here Playfair plotted three parallel time-series: prices, wages, and the reigns of British kings and queens.

![](images/9ff74dda5b88bacb1ca48ae1a3f665a6602c12282d732a6051bfab3237fd8c65.jpg)

The history and genealogy of royalty was long a graphical favorite. This superb construction of E. J. Marey brings together several sets of facts about English rulers into a time-series that conveys a sense of the march of history. Marey (1830-1904) als0 pioneered the development of graphical methods in human and animal physiology, including studies of horses moving at different paces, the moet a t e  m the bottom upwards),

![](images/13d45cf2ce024e20bd056b25669c11e784a7211a378129cb0929a3d8f902b027.jpg)

<table><tr><td rowspan="9"></td><td rowspan="9">5 O n</td><td rowspan="9">Q 2 walk.</td><td rowspan="9">Ordinary</td><td rowspan="9"></td><td rowspan="9">.- G© … $E</td><td rowspan="9">..- Ee </td><td rowspan="9"></td><td rowspan="9"></td><td rowspan="2">-…-</td><td colspan="2"></td><td rowspan="9">---</td><td rowspan="9">n</td><td rowspan="3"></td><td colspan="2"></td><td>E</td><td rowspan="9"></td><td rowspan="9"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td>… $$</td><td></td><td>-------</td></tr><tr><td rowspan="2">$$</td><td rowspan="2">..</td><td rowspan="2"></td><td rowspan="2">$</td><td></td><td rowspan="2">---_-</td></tr><tr><td></td></tr><tr><td></td><td></td><td></td><td></td><td>--</td><td rowspan="2"></td><td rowspan="4"></td><td></td><td></td></tr><tr><td>GE</td><td>0</td><td></td><td></td><td>$$</td><td></td><td rowspan="2">S</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan="2"></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan="5"></td></tr><tr><td></td><td>-</td><td></td><td></td><td>E</td><td></td><td></td><td></td><td rowspan="2">\</td></tr><tr><td>……----…-- E $</td><td></td><td></td><td></td><td></td><td></td><td>€--$</td><td rowspan="2"></td></tr><tr><td></td><td></td><td></td><td></td><td>$\$</td><td></td><td></td><td rowspan="2">Gullop.</td></tr><tr><td></td><td></td><td>Quicck</td><td></td><td>Amble.</td><td></td><td>Jog-trot.</td><td></td></tr></table>

E. J. Marey, La Méthode Graphique (Paris, 1885), p.6.  
E. J. Marey, Movement (London, 1895). Beginning with the tracks of the horse, the time-series are from pages 191, 224, 222, 265, 60, and 61.

![](images/a1653e0bd6de502a9c1fa4013025f30689b3ac5e7d9d4a2a1b25ffa937a80232.jpg)  
te l

![](images/b14d323b3c8e9a6061c887eeb3bd705b05c290772d2f6912d9eb89d671dcac14.jpg)  
as well as the advance of the gecko.

Mar'alavel orphegu became the time-series forerunner of Marcel Duchamp's Nude Descending a Staircase.

![](images/865128e1d8a935f9ea89682105caf9dc1cb37d52b04a67fa9e6375f1d7bc5009.jpg)

# " A

![](images/1feb0711c5a58c12d46db4d595e2c18d858a5e6055d20e2830a33171fc260df2.jpg)

The problem with time-series is that the simple passage of time is not a good explanatory variable: descriptive chronology is not causal explanation. There are occasional exceptions, especially when there is a clear mechanism that drives the Y-variable. This timeseries does testify about causality: the outgoing mail of the U.S. House of Representatives peaks every two years, just before the election day:

![](images/3beaaa188cc4cd84dd97cded347832c103a489865733aeee6c791d41ffdbab80.jpg)

# The graphic is worth at least 7oo words, the number used in a news report describing how incumbent representatives exploit their free mailing privileges to advance their re-election campaigns:

## FRANKED MAIL TIE TO YOTING SHOWN

Testimony Finds the Volume Rises Before Elections

WASHINGTON, June 1 (AP) New court testimony and documents show that much of the mail Congress sends at taxpayer expense is tied directly to the re-election campaigns of Senate and House members. According tomaterial filed in a lawsult inFederal Court:

¶Senate Republicans put two iema experts on the pubicpayroll to advise them on privileges to get votes.

qAn election manual prepared for Senate Democrats refers to newsletters as a "Iree forum," and sets up a timetable for sending them as an integral part of a model re-election campaign.

Senator John G. Tower, Republican of Texas, mailed more than 800,000 special-interest letters at taxpayer expense as part of his 1972 re-election effort and received campaign volunteer offers and donations in response.

¶Senator Jacob K. Javits, Republican of New York, gave written approval in 1973 for a tax-paid mail program intended to better his image and pay off at the polls. He focused his mail on areas where he needed votes.

qThe volume of "official" Congressional mail rises in election years and peaks just eo te enera lection

None of this activity necessarily violates any law or regulation, since Congress has wide discretion in the use of tax-paid mail. Congress gave itself the right to send official mail at Government expense at the founding of the republic, and only Congress polices against abuses of the free mailings.

Complaints of political use of the free-mailing privilege, called the franking privilege, are heard every election year. Recently, however, the volume and cost of franked mail has multiplied. A new Federal law will limit what out-of-office challengers can spend to unseat incumbents.

In 1972, Congress passed a law prohibiting mass franked mailings within 28 days before an election. The sponsor of that legislation, Representative Morris K. Udall. Democrat of Arizona, said in an interview that further changes were needed to curtail political abuse of the frank.

Mr. Udall urged a 60-day pre-election cutoff for mass mailings and said he favored closing a loophole that recently allowed defeated Representative Frank M. Clark, Democrat of Pennsylvania, to send a franked newsletter to his old constituents after he had left office. Mr. Clark is seeking to regain his old post.

## Practice Documented

Seldom has the political juse of franked mail been so well documented as in recent testimony and documents filed in a Federal Court by Common Cause, the lobby group, which. is suing for an end to tax-fi-Inanced mass mailings by Congress.

For example, Joyce P. Baker, a political mail specialist, said in a 1973 job proposal that she wanted to set up directmail programs for Republican Senators using franked mail.

"The purpose of such a program is to help an incumbent Senator et re-elected," she ssaid.

She was put on the Senate payroll at \$18,810 a year in 1973 and 1974 and testified that during that time she aided Republican Senators Robert J.

Dole of Kansas, Peter H. Domi-Coloado CharsMcC. Mathias Jr. of Maryland

Another political mail specialist, Lee W. MacGregor, wrote !a proposal for the use of franked mail by his chief, Senator Javits, in 1973.

The over-all objective of the franked mail program can be to get the recipient of the mail to identify positively with a particular stand you have taken or a bill you have introduced; the kind of identification that can be translated into a vote at the polls on election day Mr. MacGregor said.

Mr. Javits was out of the country and could not be reached. His administrative assistant, Donald Kellerman, defended the use of franked mail.

"It is a standard device to let voters, not voters but citizens, know what the Senator is doing here in Washington, be said.

. Senator Tower's use of franked mail in his 1972 cam. paign was documented by memorandums.

Tom Loeffler, a high-ranking campaign aide, wrote in a memorandum dated Oct. 27. 1972, that during the campaign Senator Tower had sent 31 pecl ne lett alin approximately 803,333 franked mailings.""

Mr. Tower was not available for comment. His administrative assistant, Elwin Skiles. said the Senator's use of franked mail in 1972 was within the law, and he defended the free-mailing privileges.

Postal Service figures show that in the 12 months before November, 1973, Congress sent 22.9 million franked pieces of mail. But in the next 12 months, covering the election season of 1974, Congress sent 350.6 million, a jump of 57 per cent about what's happening." Mr. Skiles said.

Time-series plots can be moved toward causal explanation by smuggling additional variables into the graphic design. For example, this decomposition of economic data, arraying 1,296 numbers, breaks out the top series into seasonal and trading-day fluctuations (which dominate short-term changes) to reveal the long-run trend adjusted for inflation. Note a significant defect in the design, however: the vertical grid conceals the height of the December peaks.) The next step would be to bring in additional variables to explain the transformed and improved series at the bottom.11

11See William S. Cleveland and Irma J. Terpenning, "Graphical Methods for Seasonal Adjustment," Journal of the American Statistical Association 77 (March 1982), 5262.

Julius Shiskin, "Measuring Current Economic Fluctuations," Statistical Reporter (July 1973), p. 3.

![](images/79eeb4c812ff54abc8cca6032e6c941cdccf98837697d32c78dc0fa322307dc0.jpg)

## A monopole?

Finally, a vivid design (with appropriate data) is the before-after time-series:

![](images/abb13914f7623dc0c4957fca982dff3d62b68b2a542aef7c223b2567742c2e30.jpg)  
Cabrera's candidate monopole signal looms over a disturbance caused by a liquid nitrogen transfer earlier in the day. The jump in magnetic flux through the superconducting detector loop (or equivalently, the jump in the loop's supercurrent) is just the right magnitude to be a monopole. Moreover, the current remained stable for many hours afterward.  
M. Mitchell Waldrop, "In Search of the Magnetic Monopole," Science (June 4, 1982), p. 1087.

And before and after the collapse of a bridge on the Rhòne in 1840:

Pont de Bourg-S.Andcol sur le Rhòne.

![](images/de0cd01154fd05d6e23a6a5ef42c6cfceb26ffde70e9e71557694542d981920b.jpg)

Charles Joseph Minard, "De la Chute des Ponts dans les grandes Crues," (October 24, 1856), Figure 3, in Minard, Collection de ses brochures (Paris, 1821 1869), held by the Bibliothèque de l'École Nationale des Ponts et Chaussées, Paris.

## Narrative Graphics of Space and Time

An especially effective device for enhancing the explanatory power of time-series displays is to add spatial dimensions to the design of the graphic, so that the data are moving over space (in two or three dimensions) as well as over time. Three excellent space-time-story graphics illustrate here how multivariate complexity can be subtly integrated into graphical architecture, integrated so gently and unobtrusively that viewers are hardly aware that they are looking into a world of four or five dimensions. Occasionally graphics are belligerently multivariate, advertising the technique rather than the data. But not these three.

The first is the classic of Charles Joseph Minard (1781-1870), the French engineer, which shows the terrible fate of Napoleon's army in Russia. Described by E. J. Marey as seeming to defy the pen of and time-series, drawn in 1869, portrays a sequence of devastating losses suffered in Napoleon's Russian campaign of 1812. Beginning at left on the Polish-Russian border near the Niemen River, the thick tan flow-line shows the size of the Grand Army (422,ooo) as it invaded Russia in June 1812. The width of this band indicates the size of the army at each place on the map. In September, the army reached Moscow, which was by then sacked and deserted, with 100,000 men. The path of Napoleon's retreat from Moscow is depicted by the darker, lower band, which is linked to a temperature scale and dates at the bottom of the chart. It was a bitterly cold winter, and many froze on the march out of Russia. As the graphic shows, the crossing of the Berezina River was a disaster, and the army finally struggled back into Poland with only 10,000 men remaining. Also shown are the movements of auxiliary troops, as they sought to protect the rear and the flank of the advancing army. Minard's graphic tells a rich, coherent story with its multivariate data, far more enlightening than just a single number bouncing along over time. Six variables are plotted: the size of the army, its location on a two-dimensional surface, direction of the army's movement, and temperature on various dates during the retreat from Moscow. At upper right we see Minard's French original, which was printed as a two-color lithograph in the form of a small poster. And at lower right, our English translation.

It may well be the best statistical graphic ever drawn.

12 E. J. Marey, La méde grahqe (Paris, 1885), p. 73. For more on Minard, see Arthur H. Robinson, "The Thematic Maps of Charles Joseph Minard," Imago Mundi, 21 (1967), 95-108.

Upper image from Charles Joseph Minard, Tableaux Graphiques et Cartes Figuratives de M. Minard, 1845-1869, Bibliothèque de l'École Nationale des Ponts et Chaussées, Paris, item 28 (62 by 25 cm, or 25 by 10 in). English translation by Dawn Finley and redrawing by Elaine Morse, completed August 2002.

![](images/f6767b58f2227f3a7b34a4aef83fe9619151f98a89f61cf6dd04c39506b2a187.jpg)  
dng.pur Ragain, I P02.54 Naric 5! 0h & Paris.

![](images/bb94c3e5b97fe44337d587c7a08c0330de26b878b0dc01c1184e2e54d3b265a2.jpg)

The next time-space graphic, drawn by a computer, displays the levels of three air pollutants located over a two-dimensional surface (six counties in southern California) at four times during the day. Nitrogen oxides (top row) are emitted by power plants, refineries, and vehicles. Refineries along the coast and Kaiser Steel's Fontana plant produce the post-midnight peaks shown in the first panel; traffic and power plants (with their heavy daytime demand) send levels up during the day. Carbon monoxide (second row) is low after midnight except out at the steel plant; morning traffic then begins to generate each day's ocean of carbon monoxide, with the greatest concentration at the convergence of five freeways in downtown Los Angeles. Reactive hydrocarbons (third row), like nitrogen oxides, come from refineries after midnight and then increase with traffic during the day. Each of the 12 time-spacepollutant slices summarizes pollutants for 2,40o spatial locations (2,400 squares five kilometers on a side). Thus 28,8oo pollutant readings are shown, except for those masked by peaks.

Los Angeles Times, July 22, 1979; based on work of Gregory J. McRae, California Institute of Technology.

The air pollution display is a small multiple. The same graphical design structure is repeated for each of the twelve slices or multiples. Small multiples are economical: once viewers understand the design of one slice, they have immediate access to the data in all the other slices. Thus, as the eye moves from one slice to the next, the constancy of the design allows the viewer to focus on changes in the data rather than on changes in graphical design.

![](images/7ba3d1d9f897b604e68f567388b44a6143062b238fff421b27a353d897619b3e.jpg)

Our third example of a space-time-story graphic ingeniously mixes space and time on the horizontal axis. This design moves well beyond the conventional time-series because of its clever plotting field, with location relative to the ground surface on the vertical axis and time/space on the horizontal. The life cycle of the Japanese beetle is shown.

L. Hugh Newman, Man and Insects (London, 1965), pp. 104105.

![](images/809c8cb34f0497d539faae7559558531fd6400e5ec26ebf5c2b784d25ae37f96.jpg)

## More Abstract Designs: Relational Graphics

The invention of data graphics required replacing the latitudelongitude coordinates of the map with more abstract measures not based on geographical analogy. Moving from maps to statistical graphics was a big step, and thousands of years passed before this step was taken by Lambert, Playfair, and others in the eighteenth century. Even so, analogies to the physical world served as the conceptual basis for early time-series. Playfair repeatedly compared his charts to maps and, in the preface to the first edition of The Commercial and Political Atlas, argued that his charts corresponded to a physical realization of the data:

Suppose the money we pay in any one year for the expence of the Navy were in guineas, and that these guineas were laid down upon a large table in a straight line, and touching each other, and those paid next year were laid down in another straight line, and the same continued for a number of years: these lines would be of different lengths, as there were fewer or more guineas; and they would make a shape, the dimensions of which would agree exactly with the amount of the sums; and the value of a guinea would be represented by the part of space which it covered. The Charts are exactly this upon a small scale, and one division represents the breadth or value of ten thousand or an hundred thousand guineas as marked, with the same exactness that a square inch upon a map may represent a square mile of country. And they, therefore, are a representation of the real money laid down in different lines, as it was originally paid away. [pages iiiiv]

Fifteen years later in The Statistical Breviary, his most theoretical book about graphics, Playfair broke free of analogies to the physical world and drew graphics as designs-in-themselves.

One of four plates in The Statistical Breviary, this graphic is distinguished by its multivariate data, the use of area to depict quantity, and the pie chart—in apparently the first application of these devices. The circle represents the area of each country; the line on the left, the population in millions read on the vertical scales; the line on the right, the revenue (taxes) collected in millions of pounds sterling read also on the vertical scale; and the "dotted lines drawn between the population and revenue, are merely intended to connect together the lines belonging to the same country. The ascent

## STATISTICAL BREVIARY;

SHEWING, ON A PRINCIPLE ENTIRELY NEW, THE RESOURCES

OF EVERY STATE AND KINGDOM IN EUROPE;

ILLUSTRATED WITHSTAINED COPPER-PLATE CHARTS,REPRESENTING THEPHYSICAL POWERS OF EACH DISTINCT NATIONWITH EASE AND PERSPICUITY.

By WILLIAM PLAYFAIR.

TO WHICN IE ADDED. A SIMILAR EXHIRITION OF THE RULING POWERS OF HINDOOSTAN.

1801.

LONDON: Paintod by T. Brnssa1, Bait Couit, Fist Suet, W  F R Ca Co Bn dPAAy,Leaal St adT dDroieA,  jeme's Street.

![](images/41050bc1d3d02886afd59b3c4639e7e0e03b40ed6ee536f64e29bc981ca3fc8e.jpg)

of those lines being from right to left, or from left to right, shews whether in proportion to its population the country is burdened with heavy taxes or otherwise" (pages 13-14). The slope of the dotted line is uninformative, since it is dependent on the diameter of the circle as well as the height of the two verticals. However, the sign of the slope does make sense, taking Playfair to his familiar point about what he regarded as excessive taxation in Britain (sixth circle from the right, with the slope running opposite to most countries). Playfair was enthusiastic about the multivariate arrangement because it fostered comparisons:

The author of this work applied the use of lines to matters of commerce and finance about fifteen years ago, with great success. His mode was generally approved of as not only facilitating, but rendering those studies more clear, and retained more easily by the memory. The present charts are in like manner intended to aid statistical studies, by shewing to the eye the sizes of different countries represented by similar forms, for where forms are not similar, the eye cannot compare them easily nor accurately. From this circumstance it happens, that we have a more accurate idea of the sizes of the planets, which are spheres, than of the nations of Europe which we see on the maps, all of which are irregular forms in themselves as well as unlike to each other. Size, Population, and Revenue, are the three principal objects of attention upon the general scale of statistical studies, whether we are actuated by curiosity or interest; I have therefore represented these three objects in one view. . . . [page 15]

But here Playfair had a forerunner—and one who thought more clearly about the abstract problems of graphical design than did Playfair, who lacked mathematical skills. A most remarkable and explicit early theoretical statement advancing the general (nonanalogical) relational graphic was made by J. H. Lambert in 1765, 35 years before The Statistical Breviary:

We have in general two variable quantities, x, y, which will be collated with one another by observation, so that we can determine for each value of x, which may be considered as an abscissa, the corresponding ordinate y. Were the experiments or observations completely accurate, these ordinates would give a number of points through which a straight or curved line should be drawn. But as this is not so, the line deviates to a greater or lesser extent from the observational points. It must therefore be drawn in such a way that it comes as near as possible to its true position and goes, as it were, through the middle of the given points.13

Lambert drew a graphical derivation of the evaporation rate of water as a function of temperature, according to Tilling. The analysis begins with two time-series: DEF, showing the decreasing height of water in a capillary tube as a function of time, and ABC, the temperature. The slope of the curve DEF is then taken (note the tangent DEG) at a number of places, yielding the rate of evaporation:

J. H. Lambert, "Essai d'hygrométrie ou sur la mesure de I'humidité," Mémoires de l'Académie Royale des Sciences et Belles-Lettres . . . 1769 (Berlin, 1771), plate 1, facing p. 126; from Tilling's article.

![](images/ee3d9f6726eae000d839a411ce8c251d09cc98614e757edb39ffe5fc5e50eb36.jpg)

To complete the graphical calculus, the measured rate is plotted against the corresponding temperature in this relational graphic:

![](images/3ca199e9a2171765859a831d478f0c7a9236fe8e6b1a0069c7bd5560990f0d8d.jpg)

Thus, by the early 18oos, graphical design was at last no longer dependent on direct analogy to the physical world—thanks to the work of Lambert and Playfair. This meant, quite simply but quite profoundly, that any variable quantity could be placed in relationship to any other variable quantity, measured for the same units of observation. Data graphics, because they were relational and not tied to geographic or time coordinates, became relevant to all quantitative inquiry. Indeed, in modern scientific literature, about 40 percent of published graphics have a relational form, with two or more variables (none of which are latitude, longitude, or time). This is no accident, since the relational graphic-in its barest form, the scatterplot and its variants—is the greatest of all graphical designs. It links at least two variables, encouraging and even imploring the viewer to assess the possible causal relationship between the plotted variables. It confronts causal theories that X causes Y with empirical evidence as to the actual relationship between X and Y, as in the case of the relationship between lung cancer and smoking:

## CRUDE MALE DEATH RATE FOR LUNG CANCER IN 1950 AND PER CAPITA CONSUMPTION OF CIGARETTES IN 1930 IN VARIOUS COUNTRIES.

![](images/6c6e5b2ba2343a1b7be6328ad348780d316f04bbe52835508259277645067bff.jpg)  
CIGARETTE CONSUMPTION

Report of the Advisory Committee to the Surgeon General, Smoking and Health (Washington, D.C., 1964), p. 176; based on R. Doll, "Etiology of Lung Cancer," Advances in Cancer Research, 3 (1955), 1-50.

These small-multiple relational graphs show unemployment and inflation over time in "Phillips curve" plots for nine countries, demonstrating the collapse of what was once thought to be an inverse relationship between the variables.

Paul McCracken, et al., Towards Full Employment and Price Stability (Paris, 1977), p. 106.

Inflation and Unemployment Rates  
![](images/6980bffbef33d8274e6dbc22eccf711504ce1fb3613df8134a6164ed099e9798.jpg)

Theory and measured observations diverge in the physical sciences, also. Here the relationship between temperature and the thermal conductivity of copper is assessed in a series of measurements from different laboratories. The connected points are from a single publication, cited by an identification number. The very different answers reported in the published literature result mainly from impurities in the samples of copper. Note how effectively the graphic organizes a vast amount of data, recording findings of hundreds of studies on a single page and, at the same time, enforcing comparisons of the varying results.

![](images/7b30fdd998aed8423b4b9ec840feec28fc1df379490e76765a12d5d605f1a307.jpg)  
C.Y. Ho, R. W. Powell, and P. E. Liley, Thermal Conductivity of the Elements: A Comprehensive Review, supplement no. 1, Journal of Physical and Chemical Reference Data, 3 (1974), I-244.

Finally, two relational designs of a different sort—wherein the data points are themselves data. Here the effect of two variables interacting is portrayed by the faces on the plotting field:

![](images/38d09193cc42329eee6ce3bb523fd24aece704268a1d3b4bec9dbf58ef710ac7.jpg)

E. C. Zeeman, "Catastrophe Theory," Scientific American, 234 (April 1976), 67; based on Konrad Z. Lorenz, King Solomon's Ring (New York, 1952).

And similarly, the varying sizes of white pine seedlings after growing for one season in sand containing different amounts of calcium, in parts per million in nutrient-sand cultures:

![](images/ff044eeceeeb4012672b59e70ed6159ea2b2e00aad65bac972328e246f38e7f7.jpg)

## Principles of Graphical Excellence

Gapi leei data—a matter of substance, of statistics, and of desgn.

Graphical excellence consists of complex ideas communicated with clarity, precision, and efficiency.

Graphical excellence is that which gives to the viewer the greatest number of ideas in the shortest time with the least ink in the smallest space.

![](images/ebb999d1e94badc1d0a105fc145d8407e45597953de1bc86070a8770ab1124c8.jpg)

Graphical excellence is nearly always multivariate.

And graphical excellence requires telling the truth about the data.

As to the propriety and justness of representing sums of money, and time, by parts of space, tho' very readily agreed to by most men, yet a few seem to apprehend that there may possibly be some deception in it, of which they are not aware. . . .

William Playfair, The Comercial and Political Atlas (London, 1786)

People said: " With the chart on the wall, with the figures published, let's emulate and rouse our enthusiasm in production."

State Statistical Bureau of the People's Republic of China, Statistical Work in the New China (Beijing, 1979)

Get it right or let it alone.

The conclusion you jump to may be your own.

James Thurber, Further Fables for Our Time (New York, 195

For many people the first word that comes to mind when they think about statistical charts is "lie." No doubt some graphics do distort the underlying data, making it hard for the viewer to learn the truth. But data graphics are no different from words in this regard, for any means of communication can be used to deceive. There is no reason to believe that graphics are especially vulnerable to exploitation by liars; in fact, most of us have pretty good graphical lie detectors that help us see right through frauds.

Much of twentieth-century thinking about statistical graphics has been preoccupied with the question of how some amateurish chart might fool a naive viewer. Other important issues, such as the use of graphics for serious data analysis, were largely ignored. At the core of the preoccupation with deceptive graphics was the assumption that data graphics were mainly devices for showing the obvious to the ignorant. It is hard to imagine any doctrine more likely to stifle intellectual progress in a field. The assumption led down two fruitless paths in the graphically barren years from 1930 to 197o: First, that graphics had to be "alive," "communicatively dynamic," overdecorated and exaggerated (otherwise all the dullards in the audience would fall asleep in the face of those boring statistics). Second, that the main task of graphical analysis was to detect and denounce deception (the dullards could not protect themselves).

Then, in the late 196os, John Tukey made statistical graphics respectable, putting an end to the view that-graphics were only for decorating a few numbers. For here was a world-class data analyst spinning off half a dozen new designs and, more importantly, using them effectively to explore complex data.1 Not a word about deception; no tortured attempts to construct more "graphical standards" in a hopeless effort to end all distortions. Instead, graphics were used as instruments for reasoning about quantitative information. With this good example, graphical work has come to flourish.

Of course false graphics are stll with us. Deception must always be confronted and demolished, even if lie detection is no longer at the forefront of research. Graphical excellence begins with telling the truth about the data.

Here are several graphics that fail to tell the truth. First, the case of the disappearing baseline in the annual report of a company that would just as soon forget about 197o. A careful look at the middle panel reveals a negative income in 1970, which is disguised by having the bars begin at the bottom at approximately minus \$4,200,000:

Day Mines, Inc., 1974 Annual Report, p. 1.  
![](images/d5acba575922b5306dbc711e3d27293da56f08e89b14d4aeed49a00d092cf35b.jpg)  
This pseudo-decline was created by comparing six months' worth of payments in 1978 to a full year's worth in 1976 and 1977, with the lie repeated four times over.

![](images/d0fb6660a420a0f06825986d226b04ac5e5bdcc4921645387ab1dc9423b310c7.jpg)

And sometimes the fact that numbers have a magnitude as well as an order is simply forgotten:

![](images/8240c3e989c67435062a6e82e952410b529498202b9d54a171b2f987fdafd3f3.jpg)

## What is Distortion in a Data Graphic?

A graphic does not distort if the visual representation of the data is consistent with the numerical representation. What then is the "visual representation" of the data? As physically measured on the surface of the graphic? Or the perceived visual effect? How do we know that the visual image represents the underlying numbers?

One way to try to answer these questions is to conduct experiments on the visual perception of graphics—having people look at lines of varying length, circles of different areas, and then recording their assessments of the numerical quantities.

![](images/a1aee84982befcfdb2c2492765d156d550f5069cf2896aed06a8f6ca1a369537.jpg)

Such experiments have discovered very approximate power laws relating the numerical measure to the reported perceived measure. For example, the perceived area of a circle probably grows somewhat more slowly than the actual (physical, measured) area: the reported perceived area = (actual area)x, where x = .8±.3, a discouraging result. Different people see the same areas somewhat differently; perceptions change with experience; and perceptions are context-dependent.² Particularly disheartening is the securely established finding that the reported perception of something as clear and simple as line length depends on the context and what other people have already said about the lines.3

Misperception and miscommunication are certainly not special to statistical graphics,

![](images/49a2a33673180aeaf23ad45d46dccb2deffe64eec4f30dcb114230a57476b38f.jpg)

but what is a poor designer to do? A different graphic for each perceiver in each context? Or designs that correct for the visual transformations of the average perceiver participating in the average psychological experiment?

One satisfactory answer to these questions is to use a table to show the numbers. Tables usually outperform graphics in reporting on small data sets of 20 numbers or less. The special power of graphics comes in the display of large data sets.

At any rate, given the perceptual difficulties, the best we can hope for is some uniformity in graphics (if not in the perceivers) and some assurance that percivrs havir ance o tig the numbers right. Two principles lead toward these goals and, in consequence, enhance graphical integrity:

The representation of numbers, as physically measured on the surface of the graphic itself, should be directly proportional to the numerical quantities represented.

Clear, detailed, and thorough labeling should be used to defeat graphical distortion and ambiguity. Write out explanations of the data on the graphic itself. Label important events in the data.

2The extensive literature is summarized in Michael Macdonald-Ross, "How Numbers Are Shown: A Review of Research on the Presentation of Quantitative Data in Texts," Audio-Visual Communication Review, 25 (1977), 359 409. In particular, H. J. Meihoefer finds great variability among perceivers; see The Utility of the Circle as an Effective Cartographic Symbol," Canadian Cartographer, 6 (1969), 105117; and "The Visual Perception of the Circle in Thematic Maps: Experimental Results," ibid., 10 (1973), 6384.

3S. E. Asch, "Studies of Independence and Submission to Group Pressure. A Minority of One Against a Unanimous Majority," Psychological Monographs (1956), 70.

Drawing by CEM; copyright 1961, The New Yorker.

Violations o the rst princple constitute one form of ahic misrepresentation, measured by the

$$
{ \mathrm { L i e ~ F a c t o r } } = { \frac { \mathrm { s i z e ~ o f ~ e f f e c t ~ s h o w n ~ i n ~ g r a p h i c } } { \mathrm { s i z e ~ o f ~ e f f e c t ~ i n ~ d a t a } } }
$$

If te Lie Factor is eual to e, then the raphic miht be doing a reasonable job of accurately representing the underlying numbers. Lie Factors greater than 1.05 or less than .95 indicate substantial distortion, far beyond minor inaccuracies in plotting. The logarithm of the Lie Factor can be taken in order to compare overstating (log LF > 0) with understating (log $\mathrm { L F } < 0 )$ errors. In practice almost all distortions involve overstating, and Lie Factors of two to five are not uncommon.

Here is an extreme example. A newspaper reported that the U.S. Congress and the Department of Transportation had set a series of fuel economy standards to be met by automobile manufacturers, beginning with 18 miles per gallon in 1978 and moving in steps up to 27.5 by 1985, an increase of 53 percent:

$$
\frac { 2 7 . 5 - 1 8 . 0 } { 1 8 . 0 } \times 1 0 0 = 5 3 \%
$$

These standards and the dates for their attainment were shown:

This line, representing 18 miles per gallon in 1978, is 0.6 inches long.

![](images/646b97397aaaf404d9c81776856f86ca46145cd5e5672378133bf0b72b380daf.jpg)  
This line, representing 27.5 miles per gallon in 1985, is 5.3 inches long.

The magnitude of the change from 1978 to 1985 is shown in the graph by the relative lengths of the two lines:

$$
\frac { 5 . 3 - 0 . 6 } { 0 . 6 } \times 1 0 0 = 7 8 3 \%
$$

Thus the numerical change of 53 percent is presented by some lines that changed 783 percent, yielding

$$
{ \mathrm { L i e ~ F a c t o r } } = { \frac { 7 8 3 } { 5 3 } } = 1 4 . 8
$$

which is too big.

The dispylsohas seveal peciarii  perpive:

On most roads the future is in front of us, toward the horizon, and the present is at our feet. This display reverses the convention so as to exaggerate the severity of the mileage standards.

Oddly enough, the dates on the left remain a constant size on the page even as they move along with the road toward the horizon.

The numbers on the right, as well as the width of the road itself, are shrinking because of two simultaneous effects: the change in the values portrayed and the change due to perspective. Viewers have no chance of separating the two.

It is easy enough to decorate these data without lying:

![](images/7b67e97aba5a8a63140177b9a3a79a13e84b9fce23524f568fe3c66d6c3fd9c7.jpg)

The non-lying version, in addition, puts the data in a context by comparing the new car standards with the mileage achieved by the mix of cars actually on the road. Also revealed is a side of the data disguised and mispresented in the original display: the fuel economy standards require gradual improvement at start-up, followed by a doubled rate from 1980 to 1983, and flattening out after that.

Sometimes decoration can help editorialize about the substance of the graphic. But it is wrong to distort the data measures—the ink locating values of numbers—in order to make an editorial comment or fit a decorative scheme. It is also a sure sign of the Graphical Hack at work. Here are many decorations but no lies:

![](images/56e7e9031fd02fa66f0294a57300b156d7da22048560d8a540ced1527ef94c6a.jpg)

## Design and Data Variation

Each part of a graphic generates visual expectations about its other parts and, in the economy of graphical perception, these expectations often determine what the eye sees. Deception results from the incorrect extrapolation of visual expectations generated at one place on the graphic to other places.

A scale moving in regular intervals, for example, is expected to continue its march to the very end in a consistent fashion, without the muddling or trickery of non-uniform changes. Here an irregular scale is used to concoct a pseudo-decline. The first seven increments on the horizontal scale are ten years long, masking the rightmost interval of four years. Consequently the conspicuous feature of the graphic is the apparent fall of curves at the right, particularly the decline in prizes won by people from the United States (the heavy, dark line) in the most recent period. This effect results solely from design variation. It is a big lie, since in reality (and even in extrapolation, scaling up each end-point by 2.5 to take the four years' worth of data up to a comparable decade), the U.S. curve turned sharply upward in the post-197o interval. A correction, with the actual data for 1971-80, is at the right:

National Science Foundation, Science Indicators, 1974 (Washington, D.C., 1976), p. 15.

Nobel Prizes Awarded in Science, for Selected Countries, 1901-1974  
![](images/0fc0e8539e016a5f9f29a43ef02a8356ea364f8dbf6ad19931f26ed73dcad5e2.jpg)  
Nobel Prizes Awarded in Science, for Selected Countries, 1901-1980

![](images/579ed63dffc286378da47cd1b9f4bf77cc4c0e1ac4680023c5d3329c9fc6f0cd.jpg)

The confounding of design variation with data variation over the surface of a graphic leads to ambiguity and deception, for the eye may mix up changes in the design with changes in the data. A steady canvas makes for a clearer picture. The principle is, then:

Show data variation, not design variation.

Design variation corrupts this display:

![](images/0c55e5bd38fd7886246690e5d1e140b3776a16ac69ddec32b4b3d8ca63dcb9cd.jpg)  
New York Times, December 19, 1978, p. D-7.  
The New York Times/Dec. 19, 1978

Five different vertical scales show the price:

<table><tr><td>During this time</td><td>one vertical inch equals</td></tr><tr><td>1973-1978</td><td>$8.00</td></tr><tr><td>January-March 1979</td><td>$4.73</td></tr><tr><td>April-June 1979</td><td>$4.37</td></tr><tr><td>July-September 1979</td><td>$4.16</td></tr><tr><td>October-December 1979</td><td>$3.92</td></tr></table>

And two different horizontal scales show the passage of time: During this time one horizontal inch equals 1973-1978 3.8 years 1979 0.57 years

As the two scales shift simultaneously, the distortion takes on multiplicative force. On the left of the graph, a price of \$1o for one year is represented by o.31 square inches; on the right side, by 4.69 square inches. Thus exactly the same quantity is 4.69/0.31 =15.1 times larger depending upon where it happens to fall on the surface of the graphic. That is design variation.

Time, April 9, 1979, p. 57.

Design variation infected similar graphics in other publications. Here an increase of 454 percent is depicted as an increase of $^ { 4 , 2 8 0 }$ percent, for a Lie Factor of 9.4:

![](images/39f4a063f57c7d6cca47e1a6939069f849e7ecb8d5552d8c039e2f10ac6bf456.jpg)

And an increase of 708 percent is shown as 6,700 percent, for a Lie Factor of 9.5:  
![](images/ccc3415666b081dea94f89a8e58df7a0da3b77fcf8d407c6c40a212147f06c68.jpg)  
Washington Post, March 28, 1979, p. A-18.

All these accounts of oil prices made a second error, by showing the price of oil in inflated (current) dollars. The 1972 dollar was worth much more than the 1979 dollar. Thus in sweeping from

Business Week, April 9, 1979, p. 99.

left to right over the surface of the graphic, the vertical scale in effect changes-design variation—because the value of money changes over the years shown. The only way to think clearly about money over time is to make comparisons using inflation-adjusted units of money. Several distinguished graphic designers did express the price in real dollars—and they also avoided other sources of design variation. The stars were Business Week, the Sunday Times (London), and The Economist.

![](images/62cba6ed5bbcd0cff1d17a5bc3ecbcf951c65a7611155cd4056f75a83303abe6.jpg)

In the graphic we saw first, the two sources of design variation covered up an intriguing, non-obvious aspect of the data: in the four years prior to the 1979-198o increases, the real price of oil had declined. Busy with decoration, the graphic had missed the news.

![](images/b754244f27ac52088a340273ffcbfc9b07d5d6d2671d8e7c7036a8691e40acd5.jpg)

![](images/b095b6b695570ce889344ecaa6be624e1f2d2a7c3df5e2027846237d2615745e.jpg)  
The Economist, December 29, 1979, p. 41.  
Sunday Times (London), December 16, 1979, p. 54.

![](images/f49baae823031b2501e2399d653c6a143b5f1ad3ea79dc28a5c485f872fad5c4.jpg)

![](images/4171971cedf1f9ff086e6d805772100aa20b4183122dadf6ed27ef33f00cae9d.jpg)  
The i theBote Year Shenthe Ri a

## The Case of Skyrocketing Government Spending

Probably the most frequently printed graphic, other than the daily weather map and stock-market trend line, is the display of government spending and debt over the years. These arrays nearly always create the impression that spending and debt are rapidly increasing.

As usual, Playfair was the first, publishing this finely designed graphic in 1786. Accompanied by his polemic against the "ruinous folly" of the British government policy of financing its colonial wars through debt, it is surely the first skyrocketing government debt chart, beginning the now 200-year history of such displays. This is one of the few Playfairs that is taller than wide; less than one-tenth of all his graphics (about 9o, drawn during 35 years of work) are longer on the vertical. The tall shape here serves to emphasize the picture of rapid growth. The money figures are not adjusted for inflation.

But Playfair had the integrity to show an alternative version a few pages later in The Commercial and Political Atlas. The interest on the national debt was plotted on a broad horizontal scale, diminishing the skyrocket effect. And, furthermore, "This is in real and not in nominal millions" (page 129):

Interest of the NATIONAL DEBT from the Revolution.  
![](images/826325543d9107172fb39ffd6950d8e6cbf57bdc8bb13f13d98cf15b5e1dcfac.jpg)

Although Playfair deflated money units over time in his work of 1786, the matter has proved difficult for many, eluding even modern scholars. This display helps its political point along by failing to discount for inflation and population growth and by using a tall and thin shape (the area covered by the data is 2.7 times taller than wide):

Morris Fiorina, Congress: Keystone of the Washington Establishment (New Haven, 1977), p. 92.

![](images/609aed20ebdcefaef1a00d23cf24f1d514581bc151abbad6e8183890a1e5e484.jpg)

Let us lok, in detail, a another graphicn overnet speng:  
![](images/60f5aa99ff5824c4047dc4b8f7869e569a5807d5c28af8df5c1ff821a361ab39.jpg)  
New York Times, February 1, 1976, p. IV-6.

Despite the appearance created by the hyperactive design, the state budget actually did not increase during the last nine years shown. To generate the thoroughly false impression of a substantial and continuous increase in spending, the chart deploys several visual and statistical tricks—all working in the same direction, to exaggerate the growth in the budget. These graphical gimmicks:

These three parallelepipeds have been placed on an optical plane in front of the other eight, creating the image that the newer budgets tower over the older ones.

This cluster of type emphasizes and stretches out the low value for 1966 1967, encouraging the impression that recent years have shot up from a small, stable base. Horizontal arrows provide similar emphasis. Total Ruda

![](images/b3bb9d586f806c357eb537c3b0dfaa4b42585caded0e9d4c792a880ba7c4b1f2.jpg)  
This squeezed-down block of type contributes to an image of small, squeezed-down budgets back in the good old days.  
Arrows pointing straight up emphasize recent growth. Compare with horizontal arrows at left.

Leaving behind the distortion in the chartjunk heap at the left yields a calmer view:

![](images/9d850a64f85491c435a0a96520f93cec9fbd8d44722b53e217ea2d93b599b7c7.jpg)

![](images/caee0b0939d5277048b22ced440b79697359d09d1c20161b95db494f5d032fc4.jpg)

Two statistical lapses also bias the chart. First, during the years shown, the state's population increased by 1.7 million people, or 10 percent. Part of the budget growth simply paralleled population growth. Second, the period was a time of substantial inflation; those goods and services that cost state and local governments \$1.00 to purchase in 1967 cost \$2.03 in 1977. By not deflating, the graphic mixes up changes in the value of money with changes in the budget.

Application of arithmetic makes it possible to take population and inflation into account. Computing expenditures in constant (real) dollars per capita reveals a quite different-and far more accurate-picture:

![](images/003ef83cc9f1297dbff7ea8b8ffa724f26484e346af8a70ee73d8b1f56573f6b.jpg)

![](images/9a5dc75d32ad0151215c1a43f5717d9e1d33cdac7de54da174405a40f73607c2.jpg)

Thus, in terms of real spending per capita, the state budget increased by about 20 percent from 1967 to 1970 and remained relatively constant from 1970 through 1976. And the 1977 budget represents a substantial decline in expenditures. That is the real news story of these data, and it was completely missed by the Graph of the Magical Parallelepipeds. Of course no small set of numbers is going to capture the complexities of a large budget—but, at any rate, why tell lies?

## The principle:

In time-series displays of money, deflated and standardized units of monetary measurement are nearly always better than nominal units.

## Visual Area and Numerical Measure

Another way to confuse data variation with design variation is to use areas to show one-dimensional data:

![](images/2193b89267484ae115c399b78228f19a46a6de81b6b791043b96cb5b8bbf098c.jpg)  
R. Satet, Les Graphiques (Paris, 1932), p. 12.

And here is the incredible shrinking doctor, with a Lie Factor of 2.8, not counting the additional exaggeration from the overlaid perspective and the incorrect horizontal spacing of the data:

## THE SHRINKING FAMILY DOCTOR In California

![](images/ae376cfe41cd03b80ccffe40b29c556f28dab839e3d59110f5667f2e5b03553a.jpg)

Many published efforts using areas to show magnitudes make the elementary mistake of varying both dimensions simultaneously in response to changes in one-dimensional data. Typical is the shrinking dollar fallacy. To depict the rate of inflation, graphs show currency shrinking on two dimensions, even though the value of money is one-dimensional. Here is one of hundreds of such charts:

![](images/cf031ae394a790e15a30b503a635660fb221c225597fcfc231400253de1a77c0.jpg)  
Washington Post, October 25, 1978, p. 1.

I then the 1978 dollar should be about twice as big as that shown.

There are considerable ambiguities in how people perceive a twodimensional surface and then convert that perception into a onedimensional number. Changes in physical area on the surface of a graphic do not reliably produce appropriately proportional changes in perceived areas. The problem is all the worse when the areas are tricked up into three dimensions:

By surface area, the Lie Factor for this graphic is 9.4. But, if one takes the barrel metaphor seriously and assumes that the volume of the barrels represents the price change, then the volume from 1973 to 1979 increases 27,000 percent compared to a data increase of 454 percent, for a Lie Factor of 59.4, which is a record.

Slarla one-dimensional data:

![](images/2b89eedeec835899fe866af756a376f9e80bf5aba31168f1da12bee90858b058.jpg)

![](images/070d14a4b442a426a2b37e487970b67f446748d10cf185a49befee06989ba0b9.jpg)  
New York Times, January 27, 1981, p.D-1.

The number of information-carrying (variable) dimensions depicted should not exceed the number of dimensions in the data.

Conclusion: The use of two (or three) varying dimensions to show one-dimensional data is a weak and inefficient technique, capable of handling only very small data sets, often with error in design and ambiguity in perception. These designs cause so many problems that they should be avoided:

# CASSE POSTALI DI RISPARMIO ITALIANE Numero dei Libretti, Libretto medio e Deposito totale al fine di ogni mese

![](images/a1af12d8ea33a14ebc3d0d810bbbbc301bb62c350e5cf98fc3d8c73ca0a81d45.jpg)

This multivariate history of the Italian post office uses two dimensions in a way nearly consistent with this principle, with the number of postal savings books issued and the average size of deposits multiplyingup t toal deposit at the en eacmonh from 1876 to 1881.

Antonio Gabaglio, Teoria Generale della Statistica (Milan, second edition, 1888).

But Playfair's circles, an early use of area to show magnitude, are not consistent with the principle, since the one-dimensional data (city populations) are represented by an areal data measure:

![](images/9d7ab1e323a81641ea5e3782435429f60aa2bb874e6e1703d2e6f18fd3b4fbf3.jpg)

Perhaps graphics that border on cartoons should be exempt from the principle. We certainly would not want to forgo the 4,340 pound chicken:

Scientific American Reference Book (New York, 1909), p. 280.

![](images/71308792a2702b565c88b61411623c9601a4789b43f6dc6bd5240db30dc37f54.jpg)

## Context is Essential for Graphical Integrity

To be truthful and revealing, data graphics must bear on the question at the heart of quantitative thinking: "Compared to what?" The emaciated, data-thin design should always provoke suspicion, for graphics often lie by omission, leaving out data sufficient for comparisons. The principle:

Graphics must not quote data out of context.

Nearly all the important questions are left unanswered by this display:

![](images/f012ae5b2c4eef5638186abfead4a2dbb51da48d2226ff593edcf9f09641439d.jpg)

A few more data points add immensely to the account:  
![](images/78d29ef21a6c9435ae13013d1b476ab708efd792c00398cfbc85023b937e2442.jpg)

Imagine the very different interpretations other possible timepaths surrounding the 1955-1956 change would have:

![](images/b146bbd259e3c600b0c3f20fb9784cd1c80c5869c74d3786cdfc1485c095a69e.jpg)

Comparisons with adjacent states give a still better context, revealing it was not only Connecticut that enjoyed a decline in traffic fatalities in the year of the crackdown on speeding:

![](images/5e65b533b845ba2e49f235f704f19d45e2798f8175f566a6f166b73436e34c86.jpg)  
Donald T. Campbell and H. Laurence Ross, "The Connecticut Crackdown on Speeding: Time Series Data in Quasi-Experimental Analysis," in Edward R. Tufte, ed., The Quantitative Analysis of Social Problems (Reading, Mass., 1970), 110-125.

## Conclusion

Lying graphics cheapen the graphical art everywhere. Since the lies often show up in news reports, millions of images are printed. When a chart on television lies, it lies tens of millions of times over; when a New York Times chart lies, it lies 9oo,ooo times over to a great many important and influential readers. The lies are told about the major issues of public policy-the government budget, medical care, prices, and fuel economy standards, for example. The lies are systematic and quite predictable, nearly always exaggerating the rate of recent change.

The main defense of the lying graphic is . . . "Well, at least it was approximately correct, we were just trying to show the general direction of change." But many of the deceptive displays we saw in this chapter involved fifteenfold lies, too large to be described as approximately correct. And in several cases the graphics were not even approximately correct by the most lax of standards, since they falsified the real news in the data. It is the special character of numbers that they have a magnitude as well as an order; numbers measure quantity. Graphics can display the quantitative iz o n  w hn.Tenar only the direction and not the magnitude right is the philosophy that informs the Pravda School of Ordinal Graphics. There, every chart has a crystal clear direction coupled with fantasy magnitudes.

![](images/90d3e56afb008a699436b24da8c201e4a7e7f6db021ab400ac12a6ba1a84f2d1.jpg)  
Poct npoAykyun npombwnehocth [1922 r. = I].  
Pravda, May 24, 1982, p. 2.

A second defense of the lying graphic is that, although the design itself lies, the actual numbers are printed on the graphic for those picky folks who want to know the correct size of the effects displayed. It is as if not lying in one place justified fifteenfold lies elsewhere. Few writers would work under such a modest standard of integrity, and graphic designers should not either.

Graphical integrity is more likely to result if these six principles are followed:

The representation of numbers, as physically measured on the surface of the graphic itself, should be directly proportional to the numerical quantities represented.

Clear, detailed, and thorough labeling should be used to defeat graphical distortion and ambiguity. Write out explanations of the data on the graphic itself. Label important events in the data.

Show data variation, not design variation.

In time-series displays of money, deflated and standardized units of monetary measurement are nearly always better than nominal units.

The number of information-carrying (variable) dimensions depicted should not exceed the number of dimensions in the data.

Graphics must not quote data out of context.

Why do artists draw graphics that lie? Why do the world's major newspapers and magazines publish them?1

Although bias and stereotyping are the origin of more than a few graphical distortions, the primary causes of inept graphical work are to be found in the skills, attitudes, and organizational structure prevailing among those who design and edit statistical graphics.

## Lack of Quantitative Skills of Professional Artists

Lurking behind the inept graphic is a lack of judgment about quantitative evidence. Nearly all those who produce graphics for mass publication are trained exclusively in the fine arts and have had little experience with the analysis of data. Such experience is essential for achieving precision and grace in the presence of statistics, but even textbooks of graphical design are silent on how to think about numbers. Illustrators too often see their work as an excluvely rnri—ortive,cet "syle" combine regularly in all possible permutations,a Big Think jargon for the small task of constructing a time-series a few data points long. Those who get ahead are those who beautify data, never mind statistical integrity.

## The Doctrine That Statistical Data Are Boring

Inept graphics also flourish because many graphic artists believe that statistics are boring and tedious. It then follows that decorated graphics must pep up, animate, and all too often exaggerate what evidence there is in the data. For example:

T ule char selis rhool , says that in his work, "The challenge is to present statistics as a visual idea rather than a tedious parade of numbers."2

The opening sentence of the chapter on statistical charts in Jan White's Graphic Idea Notebook: "Why are statistics so boring?" Sample illustrations supposedly reveal "Dry statistics turned

1"It is difficult to know why these same errors are being repeated. In Playfair's original work these kinds of mistakes were not made; moreover, these errors were not as widespread in the 1930 s as they are now. Perhaps the reason is an increase in the perceived need for graphs .. . without a concomitant increase in training in their construction. Evidence gathered by the committee on graphics of the American Statistical Association indicates that formal training in graphic presentation has had a marked decline at all levels of education over the last few decades." Howard Wainer, "Making Newspaper Graphs Fit to Print," in Paul A. Kolers, et al., eds. Processing of Visible Language 2 (New York, 1980), p. 139.

into symbolic graphics" and "Plain statistics embellished or humanized with pictures."3

A fine book on graphics, Herdeg's Graphis/Diagrams, is described by its publisher: "An international review demonstrating convincingly that statistical and diagrammatic graphics do not necessarily have to be dull."4

The doctrine of boring data serves political ends, helping to advance certain interests over others in bureaucratic struggles for control of a publication's resources. For if the numbers are dull dull dull, then an artist, indeed many artists, indeed an Art Department and an Art Director are required to animate the data, lest the eyes of the audience glaze over. Thus the doctrine encourages placing data graphics under control of artists rather than in the hands of those who write the words and know the substance. As the art bureaucracy grows, style replaces content. And the word people, having lost space in the publication to data decorators, console themselves with thoughts that statistics are really rather tedious anyway.

If the statistics are boring, then you've got the wrong numbers. Finding the right numbers requires as much specialized skill— statistical skill—and hard work as creating a beautiful design or covering a complex news story.

## The Doctrine That Graphics Are Only for the Unsophisticated Reader

Many believe that graphical displays should divert and entertain those in the audience who find the words in the text too difficult. For example:

• Consumer Reports describes the design of their new consumer magazine for children: "For the first test issue, CU's professional staff produced an article about sugar that was longer on graphics than on information. We had feared children might be overwhelmed by too many facts."5

An art director with overall responsibility for the design of some 3,ooo data graphics each year (yielding 2.5 billion printed images) said that graphics are intended more to lure the reader's attention away from the advertising than to explain the news in any detail. "Unlike the advertisements," he said, "at least we don't put naked women in our graphics."6

5 Consumer Reports, 45 (July 1980), 408.

6Louis Silverstein, "Graphics at the New York Times," presentation at the First General Conference on Social Graphics, Leesburg, Virginia, October 23, 1978.

A news director at a national television network said that graphics must be instantly understandable: "If you have to explain it, don't use it."7

This kind of graphical thinking leads to

7Interview with author, July 1980.

![](images/b08ebbc9c27f0b4906f007ad82b32e4590d0b550839198080ee5290fa4f53964.jpg)

Mary Eleanor Spear, Charting Statistics (New York, 1952), p. 5, who appropriately describes this as an "unnecessary chart."

## The Consequences

WWhi   l : "No one can write decently who is distrustful of the reader's intelligence, or whose attitude is patronizing."8 Contempt for graphics and their audience, along with the lack of quantitative skills among illustrators, has deadly consequences for graphical work: over-decorated and simplistic designs, tiny data sets, and big lies.

Like censorship, these constraints on graphical design lead to elliptical and eccentric communication. In seeking to avoid the subtleties of the scatterplot, artists drew up these convoluted specimens, forcing bivariate data into a univariate design:

![](images/13d9cdf1b3001158ba56a9eb150c9f9c137e4c5cdd464a6c45a0a36e1475218c.jpg)

8In William Strunk, Jr., and E. B. White, The Elements of Style (New York, 1959), p. 70.

New York Times, June 16, 1980, p. A-18.

Allen D. Manvel, "Taxation and Economic Growth," Taxation with Representation Newsletter, 9 (June 1980), p. 3.

![](images/9091d3f60de1e3d8e337d86725de73aeed5e420732ca6aa068021257b0e06702.jpg)

But beyond reviewing a few examples, let us look more systematically at the level of graphical sophistication prevailing at different publications. In order to make comparisons among a variety of newspapers, magazines, scientific journals, and books, I have compiled a rough measure of graphical sophistication-the share of a publication's graphics that are relational. Such a design links two or more variables but is not a time-series or a map. Relational graphics are essential to competent statistical analysis since they confront statements about cause and effect with evidence, showing how one variable affects another. The design idea is a simple one, although not quite as simple as the bar chart, timeseries plot, or data map. Relational graphics have been used since 1765 and are printed billions of times and ways every year; and there is evidence that twelve-year-old children understand the design.9

All these graphics count as sophisticated by our hardly demanding measure:10

![](images/256c2bee694d617dc6427984249742d18dc80d907cfbcb627b6a71f8f29eb57f.jpg)

![](images/4b9d23d0f7a660277e1e243e8a8eb5fc5f21cf058ec7bca054a316db3ae37c09.jpg)

The frequency of use of relational designs was counted for randomly selected issues from 1974 to 1980 of each of 15 news publications. A total of about 4,ooo graphics were examined in sampled issues. Scaling up the observed data by the frequency and circulation of the publication indicates that the sample represents a population of 250 to 300 billion printed graphical images.

Clara Francis Bamberger, "Interpretation of Graphs at the Elementary School Level," Catholic University of America Educational Research Monographs, 13 (May 1942). Additional data from textbooks and standardized tests are presented shortly.

10A variety of measures of graphical intelligence and com plexity are possible and another, data density, is discussed in Chapter 8.

![](images/d68a26a876dc3ac2a3dcf82c44edd86d33517ff5c389113de32bd6c1658adb5d.jpg)  
Ths New York Times/Feb. 29, 1976

# Pace of City Life Found 2.8 Feet per Second Faster

By BOYCE RENSBERGER

The pace of life in big cities is faster than it is in small towns—about 2.8 feet per second faster, according to a study by a Princeton University psychologist and his wife, who is an anthropologist.

By measuring how fast people walk along the main streets of municipalities of varying sizes, they have confirmed what most people have sensed informally. The inhabitants walk.

They found, for example, that on Flatbush Avenue in Brooklyn, people walk at a brisk 5 feet per second, only a little slower than their counterparts on Wenceslas Square in Prague, who bustle along at 5.8 feet per second.

In contrast to Brooklyn and Prague, both of which have a population of more than a million, the 365 citizens of Psychro, Greece, amble along at 2.7 feet per second and the people of Corte, France (population 5,500, move at 3.3 feet per second.

![](images/011e518a8368abd0574781b8beab366519472bc97f268920cb4a42b39eb8735f.jpg)

New York Times, February 29, 1976, p. 46.

Isao Sato and Miyohei Shinohara, New Politics and Economics (Tokyo, 1974), p. 113; a Japanese high school textbook.

Table 1 shows the results, ranking the 15 news publications by graphical sophistication. Seven of the papers, from Pravda to the Wall Street Journal, produced no relational graphics among those sampled and usually limited themselves to time-series. Other papers published more advanced graphics: the Japanese Asahi (a mass circulation daily), Akahata ("Red Flag," a Communist party paper that appears, from the data, to have employed a sophisticated and talented graphical designer in 1979), and Nihon Keizai (a financial daily), as well as Der Spiegel and The Economist. Although none reached the level of sophistication found in displays of scientific data (a random sample of 220 graphics from Science 19781980 had 42 percent of relational design), it is clear that some graphical intelligence is possible in news work, at least in Japan and at a few European weeklies.

Graphical Sophistication, World Press, 1974-1980

<table><tr><td></td><td>Percentage of statistical graphics based on more than one variable, but not a time-series or a map</td><td>Number of graphics in sample</td></tr><tr><td>Akahata (&quot;Red Flag&quot;) (Japan, daily, circulation 30,000)</td><td>9.3%</td><td>202</td></tr><tr><td>Asahi Shimbun (Japan, daily, 8,000,000)</td><td>7.6%</td><td>119</td></tr><tr><td>Der Spiegel (Germany, weekly, 1,000,000)</td><td>5.7%</td><td>454</td></tr><tr><td>The Economist (Britain, weekly, 170,000)</td><td>2.0%</td><td>342</td></tr><tr><td>Nihon Keizai Shimbun (Japan, daily financial paper, 1,700,000)</td><td>1.7%</td><td>297</td></tr><tr><td>Le Monde (French, daily, 440,000)</td><td>0.7%</td><td>144</td></tr><tr><td>Business Week (U.S., weekly, 800,000)</td><td>0.6%</td><td>726</td></tr><tr><td>New York Times (U.S., daily, 900,000; Sunday, 1,500,000)</td><td>0.5%</td><td>422</td></tr><tr><td>Pravda (USSR, daily, 10,500,000)</td><td>0.0%</td><td>54</td></tr><tr><td>Frankfurter Allgemeine (Germany, daily, 300,000)</td><td>0.0%</td><td>93</td></tr><tr><td>The Times (Britain, daily, 400,000)</td><td>0.0%</td><td>107</td></tr><tr><td>Washington Post (U.S., daily, 600,000; Sunday, 800,000)</td><td>0.0%</td><td>121</td></tr><tr><td>Time (U.S., weekly, 4,300,000)</td><td>0.0%</td><td>147</td></tr><tr><td>Die Zeit (Germany, weekly, 300,000)</td><td>0.0%</td><td>213</td></tr><tr><td>Wall Street Journal (U.S., daily, 2,000,000)</td><td>0.0%</td><td>449</td></tr></table>

Japanese graphical distinction is consistent with that country's heavy use of statistical techniques in the workplace and extensive quantitative training, even in the early years of school:

11 Andrew H. Malcolm, "Data-Loving Japanese Rejoice on Statistics Day," New York Times, October 28, 1977, p. A-1.

. . . no nation ranks higher in its collective passion for statistics. In Japan, statistics are the subject of a holiday, local and national conventions, awards ceremonies and nationwide statistical collection and graph-drawing contests. "This year," said Yoshiharu Takahashi, a Government statistician, "we had almost 30,000 entries. Actually, we had 29,836."

Entries in the [children's] statistical graph contest were screened three times by judges, who gave first prize this year to the work of five 7-year-olds. Their graph creation, titled Mom, play with us more often," was the result of a survey of 32 classmates on the frequency that mothers play with their offspring and the reasons given for not doing so. . . . Other children's work examined the frequency of family phone usage and correlated the day's temperature with cicada singing.11

Note the relational design of the last children's graphic mentioned.

The five U.S. publications examined rank toward the bottom of the world list, along with Pravda and a few European papers. Note, in Table 1, the complete dominance of non-relational designs at the lower-ranked newspapers and magazines. This is unfortunate because the relational graphic, unlike the simpler desis, is an explnaory grahi—sureynatural fo news rei and analysis.

The statistical graphics found in college and even high school textbooks are more sophisticated than those in news publications. Indeed, grade school children may experience a greater density of relational graphics than someone who reads only Business Week, the New York Times, Time, the Wall Street Journal, and the Washington Post. Tables 2 and 3 record the graphical sophistication of textbooks and of a variety of standardized educational tests. A comparison between these data and Table 1 suggests that most news publications outside of Japan operate at a pre-adult level of intelligence in graphical design.12

12Readers of news publications, particularly the elite press, have considerable educational and professional attainments, with the resulting graphical skills. About 80 percent of the 1.5 million readers of the Sunday New York Times attended college, according to a 198o Times market survey. The audience for statistical graphics is smarter than many illustrators believe.

Table 2 Graphical Sophistication, College and High School Textbooks
<table><tr><td></td><td>Percentage of statistical graphics based on more than one variable, but not Number of a time-series or a map</td><td>graphics</td></tr><tr><td>COLLEGE TEXTBOOKS: Medicine and public health: 11 articles in</td><td>82%</td><td>17</td></tr><tr><td>Judith Tanur, et al., Statistics: A Guide to the Unknown Introduction to Psychology, by Ernest</td><td>68%</td><td>82</td></tr><tr><td>Hilgard, et al. General Chemistry, by Linus Pauling</td><td>66%</td><td>53</td></tr><tr><td>Life on Earth, by Edward Wilson, et al.</td><td>47%</td><td>59</td></tr><tr><td>Weather, astronomy, engineering: 7 articles in Tanur, Statistics: A Guide</td><td>44%</td><td>9</td></tr><tr><td>to the Unknown Communication, work, education,</td><td>43%</td><td>35</td></tr><tr><td>economics: 20 articles in Tanur, Statistics: A Guide to the Unknown Political Behavior of the American Electorate, by William H. Flanigan</td><td>42%</td><td>43</td></tr><tr><td>and Nancy H. Zingale Economics, by Paul Samuelson</td><td>16%</td><td>57</td></tr><tr><td>Democracy in America, by Robert A. Dahl</td><td>8%</td><td>25</td></tr><tr><td>American Government, by James Q. Wilson</td><td>0%</td><td>39</td></tr><tr><td>HIGH SCHOOL TEXTBOOKS:</td><td></td><td></td></tr><tr><td>Chemical Principles, by William Masterton and Emil Slowinski</td><td>77%</td><td>27</td></tr><tr><td>The Project Physics Course, by Harvard Project Physics</td><td>48%</td><td>33</td></tr><tr><td>New Politics and Economics, by Isao Sato and Miyohei Shinohara (Japanese)</td><td>27%</td><td>22</td></tr><tr><td>Biological Science: An Ecological Approach, Biological Sciences Curriculum Study</td><td>18%</td><td>28</td></tr><tr><td>The American Economy, by Roy J. Sampson, et al.</td><td>5%</td><td>132</td></tr><tr><td>Sociology: The Study of Human Relationships, by LaVerne Thomas and Robert Anderson</td><td>0%</td><td>3</td></tr><tr><td>New Ethics and Social Science, by Yokichi Yajima, et al. (Japanese)</td><td>0%</td><td>5</td></tr><tr><td>Rise of the American Nation, by Lewis Paul Todd and Merle Curti</td><td>0%</td><td>39</td></tr><tr><td>Magruder&#x27;s American Government, revised by William McClenaghan</td><td>0%</td><td>70</td></tr></table>

Table 3 Graphical Sophistication, Educational Tests
<table><tr><td></td><td>Percentage of statistical graphics based on more than one variable, but not Number of a time-series or a map</td><td>graphics</td></tr><tr><td>National university entrance examinations, Japan, 1979 and 1980</td><td>100%</td><td>16</td></tr><tr><td>Review materials, Law School Admission Test, United States 1975</td><td>48%</td><td>29</td></tr><tr><td>Standardized tests for grade school, high school, and college; United States, 1970s:*</td><td></td><td></td></tr><tr><td>Science, 14 tests</td><td>67%</td><td>64</td></tr><tr><td>Arithmetic, mathematics, algebra, and analytic geometry; 21 tests</td><td>41%</td><td>37</td></tr><tr><td>Social studies, history, and</td><td>24%</td><td>49</td></tr><tr><td>government; 14 tests General ability, 5 tests</td><td>21%</td><td>47</td></tr></table>

\*Graphics collected in James R. Beniger, compiler, Selected Standardized Test Items that Measure Ability with Graphics (Washington, D.C.: Bureau of Social Science Research, 1975).

And so, just as there is a double standard of integrity at a good many news publications—one for words, another for graphics— so there is a double standard of sophistication. The statistical graphics are stupid; the prose is often serious and sometimes even demanding of expertise, as can be seen in these sentences from a single issue of the New York Times:

Recycling petrodollars may postpone the day of reckoning, but its effects would soon become intolerable without a steady depreciation in their purchasing power. Floating rates of exchange cannot restore even a semblance of equilibrium.

Numerous facets of the performance seem decidedly unfashionable if not downright eccentric: the square-toed instrumental phrasing and the frequent plodding tempos in the arias, the Romanticized treatment of the chorales, the generous retards at every cadence, the often intrusively elaborate continuo improvisations and an inconsistent attitude toward expression which ranges from heaving Mahlerian emphases to mechanical literalism.

The Court shows no sign of retreating from its view that a state government is protected by sovereign immunity against court orders to pay retroactive damages for past violations.

And Dr. Garth Graham, a medical director with Smithkline Corp., makers of Thorazine, noted that neuroleptics produce no euphoria, and are therefore unlikely to be abused by patients with a history of drug or alcohol dependence. "They are, if anything, dysphorogenic," Dr. Graham said.

## Conclusion

The conditions under which many data graphics are producedthe lack of substantive and quantitative skills of the illustrators, dislike of quantitative evidence, and contempt for the intelligence of the audience—guarantee graphic mediocrity. These conditions engender graphics that (1) lie; () employ only the simplest designs, often unstandardized time-series based on a small handful of data points; and (3) miss the real news actually in the data.

It wastes the tremendous communicative power of graphics to use them merely to decorate a few numbers. Moreover, much of the world these days is observed and assessed quantitatively—and well-designed graphics are far more effective than words in showing such observations.

How can graphic mediocrity be remedied?

Surely there is something to be said for rejecting once and for all the doctrines that data graphics are for the unintelligent and that statistics are boring. These doctrines blame the victims (the audience and the data) rather than the perpetrators.

Graphical competence demands three quite different skills: the substantive, statistical, and artistic. Yet now most graphical work, particularly at news publications, is under the direction of but a single expertise—the artistic. Allowing artist-illustrators to control the design and content of statistical graphics is almost like allowing typographers to control the content, style, and editing of prose. Substantive and quantitative expertise must also participate in the design of data graphics, at least if statistical integrity and graphical sophistication are to be achieved.

Theory of Data Graphics

PART II

Everyone spokeof an inforation overlad, but what there was in act was a noninformation overload.

Richard Saul Wurman, What-, Could-Be hiladelphia, 7

## Data-Ink and Graphical Redesign

Data graphics should draw the viewer's attention to the sense and substance of the data, not to something else. The data graphical form should present the quantitative contents. Occasionally artfulness of design makes a graphic worthy of the Museum of Modern Art, but essentially statistical graphics are instruments to help people reason about quantitative information.

Playfair's very first charts devoted too much of their ink to graphical apparatus, with elaborate grid lines and detailed labels. This time-series, engraved in August 1785, is from the early pages of The Commercial and Political Atlas:

CHART f IMPORTS and EXPORTS of ENGLAND t and from all NORTHAMERICA From the Year 1770 to 1782 by W. Playair  
![](images/d8f18e45e37799897f28a466d123146cc845d439f8693649ac2208910bf33990.jpg)  
J.Hinslie Sculp: Pb e

Within a year Playfair had eliminated much of the non-data detail in favor of cleaner design that focused attention on the time-series itself. He then began working with a new engraver and was soon producing clear and elegant displays:

Exports and Imports to and from DENMARK & NoRWAY from r7oo to 1780.  
![](images/643270f073135a7504b2eafc1e6f96be2c935ff0d763fdca0d98d03a2a33b74a.jpg)  
The Bottom line is divided into Years, the Right hand line into L1go00 each. Neele sculpr 352, Srand, London.  
This improvement in graphical design illustrates the fundamental principle of good statistical graphics: Above all else show the data.

The principle is the basis for a theory of data graphics.

## Data-Ink

A large share of ink on a graphic should present data-information, the ink changing as the data change. Data-ink is the non-erasable core of a graphic, the non-redundant ink arranged in response to variation in the numbers represented. Then,

<table><tr><td rowspan="3">Data-ink ratio =</td><td>data-ink</td></tr><tr><td>total ink used to print the graphic</td></tr><tr><td>= proportion of a graphic&#x27;s ink devoted to the non-redundant display of data-information</td></tr><tr><td rowspan="2"></td><td></td></tr><tr><td>= 1.o - proportion of a graphic that can be erased without loss of data-information.</td></tr></table>

A few graphics use every drop of their ink to convey measured quantities. Nothing can be erased without losing information in these continuous eight tracks of an electroencephalogram. The data change from background activity to a series of polyspike bursts. Note the scale in the bottom block, lower right:

LE-LMRF-MLM-LORM-RO

Kenneth A. Kooi, Fundamentals of Electroencephalography (New York, 1971), p. 110.

Most of the ink in this graphic is data-ink (the dots and labels on the diagonal), with perhaps 10-20 percent non-data-ink (the grid ticks and the frame):

![](images/5a686803943f80447c173d6b8bf40f34aa41a23aaf35309509fd4e67647e91d8.jpg)  
John Tyler Bonner, Size and Cycle: An Essay on the Structure of Biology (Princeton, 1965), p. 17.

In this display with nearly all its ink devoted to matters other than data, the grid sea overwhelms the numbers (the faint points scattered about the diagonal):

![](images/f6cf0553f4e33950fd10f718317e8b2e26aa8c32d45cc792558827f2f52e5b4b.jpg)

Another published version of the same data drove the share of data-ink up to about o.7, an improvement:

![](images/9f51a7056c59e04c739bb0a4d042f725a7d1051096ff8a4626bfc05c1cab67f6.jpg)  
Relationship of Actual Rates of Registration to Predicted Rates (104 cities 1960).

But a third reprint publication of the same figure forgot to plot the points and simply retraced the grid lines from the original, including the excess strip of grid along the top and right margins. The resulting figure achieves a graphical absolute zero, a null dataink ratio:

Figure 19.1 Relationship of Actual Rates of Registration to Predicted Rates (104 cities, 1960)  
![](images/23114be688f79b64df292949f0e8bbfb3b783e50b9fb33c9a03e74f4133208e4.jpg)

The three graphics were published in, respectively, Stanley Kelley, Jr., Richard E. Ayres, and William G. Bowen, "Registration and Voting: Putting First Things First," American Political Science Review, 61 (1967), 371; then reprinted in Edward R. Tufte, ed., The Quantitative Analysis of Social Problems (Reading, Mass., 1970), p. 267; and reprinted again in William J. Crotty, ed., Public Opinion and Politics: A Reader (New York, 1970), p. 364.

## Maximizing the Share of Data-ink

The larger the share of a graphic'ik devoted to data, the better (other relevant matters being equal):

## Maximize the data-ink ratio, within reason.

Evey b i  aphiu  on. Annear that reason should be that the ink presents new information.

The principl has a great many consequences for raphicl ig and design. The principle makes good sense and generates reasonable graphical advice--for perhaps two-thirds of all statistical aph.Forhehers he at  jut ot priate. Most important, however, is that other principles bearing on graphical design follow from the idea of maximizing the share of data-ink.

## Two Erasing Principles

The other side of increasing the proportion of data-ink is an erasing principle:

## Erase non-data-ink, within reason.

Ink that fails to depict statistical information does not have much interest to the viewer of a graphic; in fact, sometimes such nondata-ink clutters up the data, as in the case of a thick mesh of grid lines. While it is true that this boring ink sometimes helps set the stage for the data action, it is surprising, as we shall see in Chapter 7, how often the data themselves can serve as their own stage.

Redundant data-ink depicts the same number over and over. The labeled, shaded bar of the bar chart, for example,

![](images/68fda727499dca8212ba0e63f332aae234766edbc9af70076b650eec641b0906.jpg)  
unambiguously locates the altitude in six separate ways (any five of the six can be erased and the sixth will still indicate the height): as the (1) height of the left line, () height of shading, () heiht of right line, ) position of top horizontal line, (5) position (not content) of number at bar's top, and (6) the number itself. That is

![](images/c173bb10b1e308acd9b0692a3e547a8f490c5ad9a7c423b95a7e75d32079c433.jpg)

more ways than are needed. Gratuitous decoration and reinforcement of the data measures generate much redundant data-ink:

![](images/93c5ec71a680363ae376466a4a42853412bb344d326658d6464fcfae1f645470.jpg)

Bilateral symmetryo datameasures also creates redundancy, as in the box plot, the open bar, and Chernoff faces:

![](images/3154e03535124a1e348bc2420c253694aad95a032f280eabe4c82146f38817f3.jpg)

Half-faces carry the same information as ful faces. Halves may be easier to sort (by matching the right half of an unsorted face to the left half of a sorted face) than full faces. Or else an asymmetrical full face can be used to report additional variables.1

Bilateral symmetry doubles the space consumed by the design in a graphic, without adding new information. The few studies done on the perception of symmetrical designs indicate that "when looking at a vase, for instance, a subject would examine one of its symmetric halves, glance at the other half and, seeing that it was identical, cease his explorations. . . . The enjoyment of symmetry . . . lies not with the physical properties of the figure. At least eye movements suggest anything but symmetry, balance, or rest."2

![](images/501f8f2e5c5d141a755a034850982df433a705227872c6545bce80f026564fb5.jpg)

1 Bernhard Flury and Hans Riedwyl, "Graphical Representation of Multivariate Data by Means of Asymmetrical Faces," Journal of the American Statistical Association, 76 (December 1981), 757 765.

2Leonard Zusne, Visual Perception of Form (New York, 197o), pp. 256257.

Redundancy, upon occasion, has its uses: giving a context and order to complexity, facilitating comparisons over various parts of the data, perhaps creating an aesthetic balance. In cyclical timeseries, for example, parts of the cycle should be repeated so that thee can track y part  the c wiout havig t u back to the beginning. Such redundancy possibly improves Marey's 1880 train schedule. Those people leaving Paris or Lyon in the evening find that their trains run off the right-hand edge of the chart, to be picked up on the left again:

![](images/e652d4c73ac6bb4aed93b998ed20db8b644c1a71067ed248d2fe8e84ca65b5da.jpg)  
Atting an extra hal cycle makes every train in the first hours of the schedule a continuous line (as would mounting the original on a cylinder):

![](images/a17c3f572ffd8ceacd84f308c932fc6d3ce9441b470e2b05f6731396108caddb.jpg)

An sr wr of surface ocean currents, one and two-thirds times around is better:

![](images/4f7a30c60a238fb14177738059458dd23e9ae3f7d94738dea54bb0bc5c5295e7.jpg)

Kirk Bryan and Michael D. Cox, "The Circulation of the World Ocean: A Numerical Study. Part 1, A Homogeneous Model," Journal of Physical Oceanography, 2 (1972), 330.

![](images/d890d4d0ef0e4af7f3dd79f6419dd9edcc906b3369f811b3fe9d1f86fe86ef2f.jpg)

Most data representations, however, are of a single, uncomplicated number, and little graphical repetition is needed. Unless redundancy has a distinctly worthy purpose, the second erasing principle applies:

Erase redundant data-ink, within reason.

## Application of the Principles in Editing and Redesign

Just as a good editor of prose ruthlessly prunes out unnecessary words, so a designer of statistical graphics should prune out ink that fails to present fresh data-information. Although nothing can replace a good graphical idea applied to an interesting set of numbers, editing and revision are as essential to sound graphical design work as they are to writing. T. S. Eliot emphasized the "capital importance of criticism in the work of creation itself. Probably, indeed, the larger part of the labour of an author in composing his work is critical labour; the labour of sifting, combining, constructing, expunging, correcting, testing: this frightful toil is as much critical as creative."3

Consider this display, which compares each long bar with the adjacent short bar to show the viewer that, under the various experimental conditions, the long bar is longer:

3T. S. Eliot, "The Function of Criticism," in Selected Essays 1917-1932 (New York, 1932), p. 18.

![](images/af8bfbdae4d52ff8199027fb7042dea220c3a16ed00e8b37c6f99d0406a7af65.jpg)

Vigorous pruning improves the graphic immensely, while still retaining all the data of the original. It is remarkable that erasing alone can work such a transformation:

![](images/ce0984d82e2b613c11f88dac83bcb2ebd31d22c4686bad8c246cdbf8b27941ea.jpg)

The horizontals indicate the paired comparisons and would change if the experimental design changed—so they count as informationcarrying. All the asterisks are out since every paired comparison was statistically significant, a point that the caption can note. Here is the mix of non-data-ink and redundant data-ink that was erased, about $6 \varsigma$ percent of the original:

![](images/5e463eddd1e2080f3d96405049269ac2b4d7f0ef96e8cb97cd3ab6ddf645bd47.jpg)

T — equals the erased part plus the good part:

![](images/6ecff2cd7cad21840866f06cbbd0978c29fa64747b0d2a6b1e1e58c7e41b1b1d.jpg)

![](images/4ba45dbe4b6cdd19f94a828372e41dba84c7ea6b9fb4c6665a51235c7da94dcb.jpg)

![](images/9623c43a04088f45bc054a6677ed8eb7661e9e74e599d33c63f3fd09339c7144.jpg)

The next graphic, drawn by the distinguished science illustrator Roger Hayward, shows the periodicity of properties of chemical elements, exemplified by atomic volume as a function of atomic number. The data-ink ratio is less than $_ { 0 . 6 , }$ lowered because the 76 data points and the reference curves are obscured by the $6 3$ dark grid marks arrayed over the data plane like a precision marching band of $^ { 6 3 }$ mosquitoes:

![](images/dd6a4053734e608d29b41f3a153670b5a7ebda86a0607f2cdbcdfe59528edcfe.jpg)

T the curves tracing out the periods and the empirical observations. The little grid marks and part of the frame can be safely erased, removed from the denominator of the data-ink ratio:

<table><tr><td>2</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td></tr><tr><td></td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td></td><td>+</td></tr><tr><td>8</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>t</td><td>+</td><td>+</td></tr><tr><td></td><td>+</td><td>*</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td></tr><tr><td>8</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td></tr><tr><td></td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td></tr><tr><td>O</td><td>+</td><td>+</td><td>x</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td></tr><tr><td></td><td>10</td><td></td><td>30</td><td></td><td>50</td><td></td><td>70</td><td></td><td>90</td></tr></table>

The uncluttered display brings out another aspect of the data: several of the elements do not fit the smooth theoretical curves all that well. The data-ink ratio has increased to about .9, with only the frame lines remaining as pure non-information:

![](images/6cb693fb8af6e57a3e47180ddd49cb7392362274bdd8d9eaeaa0b7ed5e9155b0.jpg)

The reference curves prove essential for organizing the data to show the periodicity. The curves create a structure, giving an ordering, a hierarchy, to the fow of information from the page:

![](images/b7ee6db6fc65de8d2d21a8be644183fe95c064d2b5cfaecf2720d725f291342c.jpg)  
Restoring the grid fails to organize the data. The ticks are too powerful, and they also add a disconcerting visual vibration to the graphic. With the ticks, the reference curves become all the more necessary, since the eye needs some guidance through the maze of dots and crosses:

![](images/9b10aa9692ccc125f9dd8cd8620281e6924ffd73c5e57e3f0103532b3c9b6ebc.jpg)

The space opened up by erasing can be effectively used. Labels for the initial elements of each period, an alkali, show the beginning of each cycle in the periodic table of elements—and in the graphic. The unusual rare-earths are indicated. In addition, the label and numbers on the vertical axis are turned to read from left to right rather than bottom to top, making the graphic slightly more accessible, a little more friendly:

![](images/a899a090d3ee54e71a2a37dca15db803a8b4568f5d99225e87f473057f3b82a4.jpg)

## Conclusion

Five principles in the theory of data graphics produce substantial changes in graphical design. The principles apply to many graphics and yield a series of design options through cycles of graphical revision and editing.

Above all else show the data.

Maximize the data-ink ratio.

Erase non-data-ink.

Erase redundant data-ink.

Revise and edit.

With savage piures fill theps

And o'er unhabitable downs

Place elephants for want of towns.

Jonatan w en nury ar

5 Chartjunk: Vibrations, Grids, and Ducks

The interior decoration of graphics generates a lot of ink that does not tell the viewer anything new. The purpose of decoration varies —to make the graphic appear more scientific and precise, to enliven the display, to give the designer an opportunity to exercise artistic skills. Regardless of its cause, it is all non-data-ink or redundant data-ink, and it is often chartjunk. Graphical decoration, which prospers in technical publications as well as in commercial and media graphics, comes cheaper than the hard work required to produce intriguing numbers and secure evidence.

Sometimes the decoration is thought to reflect the artist's fundamental design contribution, capturing the essential spirit of the data and so on. Thus principles of artistic integrity and creativity are invoked to defend—even to advance—the cause of chartjunk. There are better ways to portray spirits and essences than to get them all tangled up with statistical graphics.

Fortunately most chartjunk does not involve artistic considerations. It is simply conventional graphical paraphernalia routinely added to every display that passes by: over-busy grid lines and excess ticks, redundant representations of the simplest data, the debris of computer plotting, and many of the devices generating design variation.

Like weeds, many varieties of chartjunk flourish. Here three widespread types found in scientific and technical research work are catalogued—unintentional optical art, the dreaded grid, and the self-promoting graphical duck. A hundred chartjunky examples from commercial and media graphics have been forgone so as to demonstrate the relevance of the critique to the professional scientific production of data graphics.

## Unintentional Optical Art

Contemporary optical art relies on moiré effects, in which the design interacts with the physiological tremor of the eye to produce the distracting appearance of vibration and movement.

##

The effect extends beyond the ink of the design to the whole page. When exploited by the experts, such as Bridget Riley and Victor Vasarely, op art effects are undoubtedly eye-catching.

But statistical graphics are also often drawn up so as to shimmer. This moiré vibration, probably the most common form of graphical clutter, is inevitably bad art and bad data graphics. The noise clouds the flow of information as these examples from technical and scientific publications illustrate:

Instituto de Expansão Commercial, Brasil: Graphicos Economicos—Estatisticas (Rio de Janeiro, 1929), p. 15.

![](images/a7dabeabc1826298fb8c13fc0488c44db7e7858d0a0c926c54fa12123856ed94.jpg)

![](images/2df2b01aa7e342f653eafa70678ff704afb1503287a51faeb6a24480ae90e626.jpg)  
Months after Operation  
utevrRguattra moderate; and 3.0, severe.

On this page, what should have been simple tables are turned into bad graphics published in major scientific journals. Above a duck moiré with an unintentional Necker Illusion, as the two back planes optically flip to the front. Some pyramids conceal others; and one variable (stacked depth of the stupid pyramids) has no label or scale. Below, we learn very little about data, but do discover that moiré vibration may well be at a maximum for equally spaced bars:

Nicholas T. Kouchoukos, et al., "Replacement of the Aortic Root with a Pulmonary Autograft in Children and Young Adults with Aortic-Valve Disease," The New England Journal of Medicine, 330 (January 6, 1994), p. 4.

![](images/493c0fe01a628a90e8b3185403f0cba522f61bda41c7284a9a1bc1be089ecf7e.jpg)

![](images/6fa356dd49047c6866bdc00de645e200513ae12486829c146ba760565db8bfd1.jpg)  
James T. Kuznicki and N. Bruce Mc-Cutcheon, "Cross-Enhancement of the Sour Taste on Single Human Taste Papillae," Journal of Experimental Psychology: General, 108 (1979), 76.  
Eain M. Cornford and Marie E. Huot, "Glucose Transfer from Male to Female Schistosomes," Science, 213 (September 11, 1981), 1270.

And, finally, from the style sheet once provided by the Journal of the American Statistical Association, a graphic described as p u e

A. Average Probabilities of W from N(1,1) with n = 10  
![](images/6f6674fc2635f8f5a108691190fe98bf05479e837a51caea661a19389e2935a8.jpg)  
"JASA Style Sheet," Journal of the American Statistical Association, 71 (March 1976), 260261.

The display required 131 line-strokes and 15 digits to communicate its simple information. The vibrating lines are poorly drawn, unevenly spaced, and misaligned with the vertical axis.

Vibrating chartjunk even frequents the graphic of major scientific journals:

<table><tr><td>The ten most frequently cited (footnoted) scientific journals: random sample of issues published 1980-1982</td><td>Percentage of graphics with moiré vibration</td><td>Number of graphics in sample</td></tr><tr><td>Biochemistry</td><td>2%</td><td>568</td></tr><tr><td>Journal of Biological Chemistry</td><td>2%</td><td>565</td></tr><tr><td>Journal of the American Chemical Society</td><td>3%</td><td>317</td></tr><tr><td>Journal of Chemical Physics</td><td>6%</td><td>327</td></tr><tr><td>Biochimica et Biophysica Acta</td><td>8%</td><td>432</td></tr><tr><td>Nature</td><td>11%</td><td>225</td></tr><tr><td>Proceedings of the National Academy of Sciences, U.S.A.</td><td>12%</td><td>438</td></tr><tr><td>Lancet</td><td>15%</td><td>364</td></tr><tr><td>Science</td><td>17%</td><td>311</td></tr><tr><td>New England Journal of Medicine</td><td>21%</td><td>338</td></tr></table>

Moéeffchave prola wi uerraphic (in programs such as Excel). Such unfortunate patterns were once generated by means of thin plastic transfer sheets; now the computer produces instant chartjunk. Shown here are a few of the many vibrating possibilities. Cross-hatching should be replaced with tint screens of shades of gray. Specific areas on a graphic should be labeled with words rather than encoded with hatching.

![](images/a206a54423e0a891bdf4f3a18346fa89717cf2cbae9064ff693ccc8622302f98.jpg)

This form of chartjunk is a twentieth-century innovation, and computer graphics are multiplying it more than ever. The handbooks and textbooks of statistical graphics, along with user's manuals for computer graphics programs, are flled up with vibrating graphics, presented as exemplars of design. Note the high

proportion of chartjunky graphics in the more recent publications. Computer graphics are particularly active:

<table><tr><td>Textbooks and handbooks of statistical graphics; and manuals for computer graphics programs (ordered by date of publication)</td><td>Percentage of graphics with moiré vibration of graphics</td><td>Total number</td></tr><tr><td>Willard C. Brinton, Graphic Methods for Presenting Facts (New York, 1914)</td><td>12%</td><td>255</td></tr><tr><td>R. Satet, Les Graphiques (Paris, 1932)</td><td>29%</td><td>28</td></tr><tr><td>Herbert Arkin and Raymond R. Colton, Graphs: How to Make and Use Then (New York, 1936)</td><td>17%</td><td>95</td></tr><tr><td>Mary Eleanor Spear, Charting Statistics (New York, 1952)</td><td>46%</td><td>134</td></tr><tr><td>Anna C. Rogers, Graphic Charts Handbook (Washington, D.C., 1961)</td><td>32%</td><td>201</td></tr><tr><td>F. J. Monkhouse and H. R. Wilkinson, Maps and Diagrams (London, third edition, 1971)</td><td>14%</td><td>322</td></tr><tr><td>Calvin F. Schmid and Stanton E. Schmid, Handbook of Graphic Presentation (New York, second edition, 1979)</td><td>22%</td><td>399</td></tr><tr><td>A. J. MacGregor, Graphics Simplified (Toronto, 1979)</td><td>34%</td><td>65</td></tr><tr><td>The user&#x27;s manual for a widely distributed computer graphics package: SAS/GRAPH User&#x27;s Guide (Cary, North Carolina, 1980)</td><td>68%</td><td>28</td></tr><tr><td>The manual for a very extensive computer graphics program: Tell-A-Graf User&#x27;s Manual (San Diego, 1981)</td><td>53%</td><td>459</td></tr></table>

Can optical art effects ever produce a better graphic? Bertin exhorts: "It is the designer's duty to make the most of this variation; to obtain the resonance [of moiré vibration] without provoking an uncomfortable sensation: to flirt with ambiguity without succumbing to it."1 But can statistical graphics successfully "flirt with ambiguity"? It is a clever idea, but no good examples are to be found. The key difficulty remains: moiré vibration is an undisciplined ambiguity, with an illusive, eye-straining quality that contaminates the entire graphic. It has no place in data graphical design.

1 Jacques Bertin, Semiology of Graphics: Diagrams, Networks, Maps (Madison, Wisconsin, 1983, translated by William J. Berg), p. 8o; this book is the English translation of Bertin's important work, Sémiologie graphique (Paris, 1967).

## The Grid

On  them at raphil ments, the rid shouly be muted or completely suppressed so that its presence is only implicit—lest it compete with the data. Grids are mostly for the i pottia oefirathr than ut into print. Dark grid lines are chartjunk. They carry no information, clutter up the graphic, and generate graphic activity unrelated to data information. This grid camouflages the profile of the data in the age-sex pyramid of the population of France in 1967:

![](images/4e59021b3f99b2c7402e7c399fd2275b4f4a6eae16ecec44e515eb960cb4a2e8.jpg)  
Military losses in World War I Deficit of births during Warld War I Mility losses in World War I Deficit of births during World War II Rise of births due to demobilization after World War II

A revision quiets the grid and gives emphasis to the data:  
![](images/2a7c5eb2e7a07c4f2f4ea8c523c6f23229d874fa072d22d81f0cfe522a3e8405.jpg)

The space occupied by the doubled grid lines consumes 18 percent of the area of this otherwise most ingenious design, a "multiwindow plot." Optical white dots appear at the intersections of the grid lines. (The plot shows the following: The large square contains $\mathrm { X } _ { 4 } , \mathrm { X } _ { 7 }$ scatterplots for the indicated levels of $\mathbf { X } _ { 1 }$ and ${ \bf { X } } _ { \mathfrak { s } }$ The marginal plots on the right are conditioned on $\mathrm { x } _ { \mathfrak { s } }$ and the plots at the top on ${ \bf X } _ { 1 }$ .The upper right corner shows the unconditional $\mathrm { X } _ { 4 } , \mathrm { X } _ { 7 }$ scatter.) Redrawing eliminates the vibration:

ULTIWINDOW PLOT OF PARTICLE PHYSICS MOMENTUM DATA  
![](images/0252b4f4a1a26d722d1f9294300a623bfcda84646889ebdc8547fba6f5dd4278.jpg)  
Paul A. Tukey and John W. Tukey, "Data-Driven View Selection; Agglomeration and Sharpening," in Vic Barnett, ed., Interpreting Multivariate Data (Chichester, England, 1981), 231232.

![](images/cf7d3c392bb0981372e0941f939230ffb60433f4a05a26e5af198d9c558dd097.jpg)

<table><tr><td rowspan=1 colspan=1>..</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>.:</td><td rowspan=1 colspan=1>.</td><td rowspan=1 colspan=1>·(5.v</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>s</td><td rowspan=1 colspan=1>*</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>.</td><td rowspan=1 colspan=1>.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>in.</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>•..</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>.</td></tr></table>

![](images/59b0f412e82d3434ef693b631a62bb8f0a1e766d5d1766f2f767f7b465f00de9.jpg)

The ri nhe cassic Mary trai sedule  veryve:

![](images/f6fed01c37062914a1b8ac75471e050309159ab3c9bd5c188bd1c6124b86a567.jpg)

Thinning the grid lines helps a little bit:  
![](images/b88613ebd22349a29a433528f3c9d92a027274b08615acbfa0139848bd9857f2.jpg)

A better treatment, however, is a gray rid:

![](images/25157dd347ec43ce7e7d4189e799b60ca8499dc9e39351091538a3a1785f19f9.jpg)

When a graphic serves as a look-up table, then a grid may help in reading and interpolating. But even in this case the grids should be muted relative to the data. A gray grid works well and, with a delicate line, may promote more accurate data reconstruction than a dark grid.

Most ready-made graph paper comes with a darkly printed grid. The reverse (unprinted) side should be used, for then the lines show through faintly and do not clutter the data. If the paper is heavily gridded on both sides, throw it out.

## Self-Promoting Graphics: The Duck

When a graphic is taken over by decorative forms or computer debris, when the data measures and structures become Design Elements, when the overall design purveys Graphical Style rather than quantitative information, then that graphic may be called a c in honor of the duckform store, Big Duck.For this buili the whole structure is itself decoration, just as in the duck data graphic. In Learning from Las Vegas, Robert Venturi, Denise Scott

Brown, and Steven Izenour write about the ducks of modern architecture—and their thoughts are relevant to the design of data graphics as well:

When Modern architects righteously abandoned ornament on buildings, they unconsciously designed buildings that were ornament. In promoting Space and Articulation over symbolism and ornament, they distorted the whole building into a duck. They substituted for the innocent and inexpensive practice of applied decoration on a conventional shed the rather cynical and expensive distortion of program and structure to promote a duck. . . . It is now time to reevaluate the once-horrifying statement of John Ruskin that architecture is the decoration of construction, but we should append the warning of Pugin: It is all right to decorate construction but never construct decoration.2

2Robert Venturi, Denise Scott Brown, and Steven Izenour, Learning from Las Vegas (Cambridge, revised edition, 1977), p. 163. The initial statement of the duck concept is found on pp. 87-103.

Big Duck, Flanders, New York; photograph by Edward Tufte, July 2000.

![](images/b336a3fff1419a64dede1f1abb0b4c8a7b4eadcaacc9f728f45a2dbee197f813.jpg)

The addition of a fake perspective to the data structure clutters many graphics. This variety of chartjunk, now at high fashion in the world of Boutique Data Graphics, abounds in corporate annual reports, the phony statistical studies presented in advertisements, the mass media, and the more muddled sorts of social science research.

A series of weird three-dimensional displays appearing in the magazine American Education in the 197os delighted connoisseurs of the graphically preposterous. Here five colors report, almost by happenstance, only five pieces of data (since the division within each year adds to 100 percent). This may well be the worst graphic ever to find its way into print:

![](images/cc0667ab5b8ecc48d1e8711b4c9f073584599a40165ca87be789ebbd69d480a0.jpg)

William L. Kahrl, et al., The California Water Atlas (Sacramento, 1978, 1979), p. 55.

![](images/602e17f983d82c1dfc7d2ea1782c8e3efd99f058ebea4c7ff1ae6e16f9d79036.jpg)

![](images/3f81348d628f06d81603ec02ea219702a9e389c85cb69e7426408fe9f9ec8301.jpg)

Occasionally designers seem to seek credit merely for possessing a new technology, rather than using it to make better designs. Computers and their affliated apparatus can do powerful things graphically, in part by turning out the hundreds of plots necessary for good data analysis. But at least a few computer graphics only evoke the response "Isn't it remarkable that the computer can be programmed to draw like that?" instead of "My, what interesting data."

![](images/8fc7e4852167c9365c486f60446ce6b34c03e16dbcea1f48212a8c3bf42e511d.jpg)

The symptoms of the We-Used-A-Computer-To-Build-A-Duck Syndrome appear in this display from a professional journal: the thin substance; the clotted, crinkly lettering all in upper-case sans serif; the pointlessly ordered cross-hatching; the labels written in computer abbreviations; the optical vibration—all these the by-products of the technology of graphic fabrication. The overly busy vertical scaling shows more percentage markers and labels than there are actual data points. The observed values of the percentages should be printed instead. Since the information consists of a few numbers and a good many words, it is best to pass up the computerized graphics capability this time and tell the story with a table:

Arthur H. Miller, Edie N. Goldenberg, and Lutz Erbring, "Type-Set Politics: Impact of Newspapers on Public Confidence," American Political Science Review, 73 (1979), 6784.

<table><tr><td>Content and tone of front-page articles in 94 U.S. newspapers, October and November, 1974</td><td>Number of articles</td><td>Percent of articles with negative criticism of specific person or policy</td></tr><tr><td>Watergate: defendants and prosecutors, Ford&#x27;s pardon of Nixon</td><td>537</td><td>49%</td></tr><tr><td>Inflation, high cost of living</td><td>415</td><td>28%</td></tr><tr><td>Government competence: costs, quality, salaries of public employees</td><td>322</td><td>30%</td></tr><tr><td>Confidence in government: power of special interests, trust in political</td><td>266</td><td>52%</td></tr><tr><td>leaders, dishonesty in politics Government power: regulation of business,</td><td>154</td><td>42%</td></tr><tr><td>secrecy, control of CIA and FBI Crime</td><td>123</td><td>30%</td></tr><tr><td>Race</td><td>103</td><td>25%</td></tr><tr><td>Unemployment</td><td>100</td><td>13%</td></tr><tr><td>Shortages: energy, food</td><td>68</td><td>16%</td></tr></table>

## Conclusion

Chartjunk does not achieve the goals of its propagators. The overwhelming fact of data graphics is that they stand or fall on their content, gracefully displayed. Graphics do not become attractive and interesting through the addition of ornamental hatching and false perspective to a few bars. Chartjunk can turn bores into disasters, but it can never rescue a thin data set. The best designs (for example, Minard on Napoleon in Russia, Marey's graphical train schedule, the cancer maps, the Times weather history of New York City, the chronicle of the annual adventures of the Japanese beetle, the new view of the galaxies) are intriguing and curiosity-provoking, drawing the viewer into the wonder of the data, sometimes by narrative power, sometimes by immense detail, and sometimes by elegant presentation of simple but interesting data. But no information, no sense of discovery, no wonder, no substance is generated by chartjunk.

Forgo chartjunk, including

moiré vibration,

the grid, and the duck.

Pael patteetatncnla for me, no physical action or social sport. As much consciousness as possible. Clarity, completeness, quintessence, quiet. No noise, no schmutz, no schmerz, no fauve schwärmerei. Perfection, passiveness, consonance, consummateness. No palpitations, no gesticulation, no grotesquerie. Spirituality, serenity, absoluteness, coherence. No automatism, no accident, no anxiety, no catharsis, no chance. Detachment, disinterestedness, thoughtfulness, transcendence. No humbugging, no buttonholing, no exploitation, no ixing thin up.

Ad Reinhardt, statement for the catalogue of the exhibition, "The New Decade: 35 American Painters and Sculptors," Whitney Museum of American Art, New York, 1955.

So far the principles of maximizing data-ink and erasing have helped to generate a series of choices in the process of graphical revision. This is an important result, but can the ideas reach beyond the details and particularities of editing? Is it possible to do what a theory of graphics is supposed to do, that is, to derive new graphical forms? In this chapter the principles are applied to many graphical designs, basic and advanced, including box plots, bar charts, histograms, and scatterplots. New designs result.

## Redesign of the Box Plot

Mary Eleanor Spear's "range bar

![](images/a994ae66bc14f0752e4e147b50dfbe78295b79b105e58cce830d95224d7109eb.jpg)

can be mostly erased without loss of information:

The revised design, a quartile plot, shows the same five numbers. It is easy to draw by hand or computer and, most importantly, can replace the conventional scatterplot frame. The straightedge need only be placed on the paper once to draw the quartile plot, compared to six separate placings for the box plot. An alternative is

but this design will not work effectively to frame a scatterplot.   
Nor does it look very good.

Perhaps special emphasis should be given to the middle half of the distribution, however, as in the box plot. This can be done by changing line weights

or, even better, by offsetting the middle half:

This latter de is the preerred form o the quartile pot. It us the ink effectively and looks good.

I s  o,he c data-ink has suggested a variety of designs, but the choice of the best overall arrangement naturally also rests on statistical and aesthetic criteria—in other words, the procedure is one of reasonable data-ink maximizing.

The same logic applies to many similar designs, such as this "parallel schematic plot." The original required 8o separate placings of the straightedge, 5o horizontals and 30 verticals:

![](images/dc1c274414c94a4b9f692a73ec8e2853b168875ddf41a8e21f4cc7581994aef1.jpg)

An erased version requires only 10 verticals to show the same information:

![](images/59128811e0d0f1c0c8868209f7366efe0e35a3fdeea5e01cd4c9f70703b44699.jpg)

The large reduction in the amount of drawing is relevant for the use of such designs in informal, exploratory data analysis, where the research worker's time should be devoted to matters other than drawing lines.

## Redesign of the Bar Chart/Histogram

Here is the standard model bar chart, with the design endorsed by the practices and the style sheets of many statistical and scientific publications:

![](images/7028a23655a4fba518b7de3599d27cc399b4ab24575173984727eb3882a0ea1c.jpg)

I  :

Exports nd ports ScoTLanD toand from difeent parts for n Yefromritua 78 to Chrims17
<table><tr><td rowspan=1 colspan=10>30 2030 40 50 60 70 80 90so</td><td rowspan=1 colspan=10>no   230   150  _170      20</td><td rowspan=1 colspan=6>0  200   240   26</td><td rowspan=1 colspan=4>0  280</td><td rowspan=1 colspan=1>1,300,000</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Nammes of Places.</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>o</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Jersey 8c.</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Ireland.</td></tr><tr><td rowspan=1 colspan=1>:</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Polond</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Iole of Man</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Grenland.</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Pruyfia</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Portugal</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Hollond</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Sweden</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Gnerly</td></tr><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Germany</td></tr><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Denmark and</td></tr><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Flonders</td></tr><tr><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>WeftIndres</td></tr><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>America.</td></tr><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Rufra</td></tr><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>*</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>breland.</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>—</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>—</td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td></tr></table>

The Upright divifions are Ten Thoufand Pounds each. The Black Lines are Exports the Ribbellines Imperts Aubbd  theAd funo WP Nede crp: 352 Strurd. Londen.

The box can be erased:

![](images/6958294a8b40b28f28e9786a946ab68d00ba031b7de677b425117cb40330478a.jpg)

And the vertical axis, except for the ticks:

![](images/9e19e46a0e887dd40faf07145fb68b87affc17309ee4dd22cb26082eb07be7f9.jpg)

Even part of the data measures can be erased, making a white grid, which shows the coordinate lines more precisely than ticks alone:

![](images/84813bdf4aa91113aa82fc7aedbbbb0ae22ed580041f6ef8f0759d055316fa78.jpg)

The white grid eliminates the tick marks, since the numerical labels on the vertical are tied directly to the white lines:

![](images/dca51dd86fb7240e63204a21cfb2e4b892d1009fb4d04671393ae3a5338a04f4.jpg)

Although the intersection of the thicker bar with the thinner baseline creates an attractive visual effect (but also the optical illusion of gray dots at the intersections), the baseline can be erased since the bars define the end-point at the bottom:

![](images/32c7a6d16f23e065b9c69a8ab4d2d9d9c5706e10d960c40406d98efa0a11b542.jpg)

Still, a thin baseline looks good:

![](images/f62e25de6f2beb14de6a666eba1794342563e66f4ef0dde3376e5126bf5ba76c.jpg)

Erasing and data-ink maximizing have induced changes in the plain old bar chart. The techniques—no frame, no vertical axis, no ticks, and the white grid—apply to other designs:

![](images/bfa21fb0162c2ee51c51123dbc6c04f04612d7475c90c77458bf8021f62596fb.jpg)  
Robert McGill, John W. Tukey, and Wayne A. Larsen, "Variations of Box Plots," American Statistician, 32 (1978), 12-16.

![](images/8ed4bc950929e65433a39bb48dfdd706fee9547c8a50871b9e871aad89721a05.jpg)

## Redesign of the Scatterplot

Consider the standard bivariate scatterplot:

![](images/30c034a12ce7b29072067b965009acbe806e7ee14013be7dc6b2fbb75f49a2db.jpg)

Ausel , brougt tonote by the maxiization n asg principles, is that the frame of a graphic can become an effective data-communicating element simply by erasing part of it. The frame lines should extend only to the measured limits of the data rather than, as is customary, to some arbitrary point like the next round number marking off the grid and grid ticks of the plot. That part of the frame exceeding the limits of the observed data is trimmed off:

![](images/66eeec86f7ecb9d3f963b8af9bacb4594ded7b4c44ad87933841bfd5dafc05ce.jpg)

The result, a range-frame, explicitly shows the maximum and minimum of both variables plotted (along with the range), information available only by extrapolation and visual estimation in the conventional design. The data-ink ratio has increased: some non-dataink has been erased, and the remainder of the frame, now carrying information, has gone over to the side of data-ink.

![](images/0d587a8171d914865adb43d04e94615b7f5dc7af110badf9d24d2565034e4fe1.jpg)  
Noting but hel  thefe ne hane:

![](images/690192aa17e1cc29d327d861e23413323411b8ec537b41ef77f9f045ba591aed.jpg)

A range-frame does not require any viewing or decoding instructions; it is not a graphical puzzle and most viewers can easily tell what is going on. Since it is more informative about the data in a clear and precise manner, the range-frame should replace the non-data-bearing frame in many graphical applications.

A small shift in the remaining ink turns each range-frame into a quartile plot:

![](images/f96adfcee8bc13980b85c7ef9a0cb0db7dc347599e682c0b4011d8495fd0868b.jpg)

Erasing and editing has led to the display of ten extra numbers (the minimum, maximum, two quartiles, and the median for both variables). The design is useful for analytical and exploratory data analysis, as well as for published graphics where summary characterizations of the marginal distributions have interest. The design is nearly always better than the conventionally framed scatterplot.

Range-frames can also present ranges along a single dimension. Here the historical high and low are shown in the vertical frame. This is an excellent practice and should be used widely in all sorts of displays, both scientific and unscientific:

![](images/1a567e47bb8f365b7427c2e6f94e266500bb43d7c3f828498198d0d51001a7d8.jpg)

Finally, the entire frame can be turned into data by framing the bivariate scatter with the marginal distribution of each variable. The dot-dash-plot results.1

1 The terminology follows tradition, for scatterplots were once called "dot diagrams"—for example, in R. A. Fisher's Statistical Methods for Research Workers (Edinburgh, 1925).

![](images/49f3aa5f0d425762fdbe1294bef2b4fc3a806935ae21490d8f2ca7527f47651e.jpg)

The dot-dash-plot combines the two fundamental graphical designs used in statistical analysis, the marginal frequency distribution and the bivariate distribution. Dot-dash-plots make routine what good data analysts do already—plotting marginal and joint distributions together.

An empirical cumulative distribution of residuals on a normal grid shows the outer 18 terms plus the 3oth term, with all 60 points plotted in the marginal distribution:

![](images/76d3b195e7ef3b589b0634bf2190ffd8a1b25ff2d625bc9ec9898e0da72428db.jpg)

Similarly, this data-rich graphic of signals from pulsars shows both marginal distributions:

![](images/6095f29359360e76d1feb8ebcaf94209a110d334902986db24c029590626caf4.jpg)

Timothy H. Hankins and Barney J. Rickett, "Pulsar Signal Processing," in Berni Alder, et al., eds., Methods in Computational Physics, Volume 14: Radio Astronomy (New York, 197s), p. 108.

Narrowband spectra of individual subpulses. Each point of the intensity $I _ { \mathfrak { q } } ( t )$ plotted on the right is the sum of the distribution of intensities across the receiver bandwidth shown in the center. At the top is plotted the spectrum averaged over the pulse. In the limit of many thousands of pulses this would show the receiver bandpass shape.

The fringe of dashes in the dot-dash-plot can connect a series of bivariate scatters in a rugplot (since it resembles a set of fringed rugs-and covers the statistical ground):

![](images/2d44fbbcbe57901b837a2e1e9008fbcb86f6d9d318bf20e9de8bd22ca5fa7a78.jpg)  
Reflecting the one-dimensional projections from each scatter, the dashes encourage the eye to notice how each plot filters and translates the data through the scatter from one adjacent plot to the next. Sometimes it is useful to think of each bivariate scatter as the imperfect empirical representation of an underlying curve that transforms one variable into another. In the rugplot, the sequence of variables can wander off as appropriate. The quantitative history of a single observation can be traced through a series of one- and two-dimensional contexts.

## Conclusion

The first part of a theory of data graphic is in place.The ide, as described in the previous three chapters, is that most of a graphic's ink should vary in response to data variation. The theory has something to say about a great variety of graphics—workaday scientific charts, the unique drawings of Roger Hayward, the exemplars of graphical handbooks, newspaper displays, computer graphics, standard statistical graphics, and the recent inventions of Chernoff and Tukey.

The observed increases in efficiency, in how much of the graphic's ink carries information, are sometimes quite large. In several cases, the data-ink ratio increased from .1 or .2 to nearly 1.0. The transformed designs are less cluttered and can be shrunk down more readily than the originals.

But, are the transformed designs better?

() They are necessarily better within the principles of the theory, for more information per unit of space and per unit of ink is displayed. And this is significant; indeed, the history of devices for communicating information is written in terms of increases in efficiency of communication and production.

() Graphics are almost always going to improve as they go througediting, revison, andtesting agaist diffrent des - tions. The principles of maximizing data-ink and erasing generate graphical alternatives and also suggest a direction in which revisions should move.

(3) Then there is the audience: will those looking at the new designs be confused? Some of the designs are self-explanatory, as in the case of the range-frame. The dot-dash-plot is more difficult, although it still shows all the standard information found in the scatterplot. Nothing is lost to those puzzled by the frame of dashes, and something is gained by those who do understand. Moreover, it is a frequent mistake in thinking about statistical graphics to underestimate the audience. Instead, why not assume that if you understand it, most other readers will, too? Graphics should be as intelligent and sophisticated as the accompanying text.

)Some of the new designs may appear odd, but this is probably because we have not seen them before. The conventional designs for statistical graphics have been viewed thousands of times by nearly every reader of this book; on the other hand, the rangeframe, the dot-dash-plot, the white grid, the quartile plot, the rugplot, and the half-face just a few times. With use, the new designs will come to look just as reasonable as the old.

Maximizing data ink (within reason) is but a single dimension of a complex and multivariate design task. The principle helps conduct experiments in graphical design. Some of those experiments will succeed. There remain, however, many other considerations in the design of statistical graphics—not only of efficiency, but also of complexity, structure, density, and even beauty.

# 7 Multifunctioning Graphical Elements

The same ink should often serve more than one graphical purpose. A graphical element may carry data information and also perform a design function usually left to non-data-ink. Or it might show several different pieces of data. Such multifunctioning graphical complex, multivariate data.1

Consider, for example, the multifunctioning blot of the blot map. It simultaneously locates the geographic unit on a twodimensional surface, describes the shape of the geographic unit, and indicates the level of the variable displayed by color or intensity of shading. That is a great deal of information for a small patch of ink—and the different pieces of information are not confounded and mixed together.

1 The idea of double-functioning elements appears in architectural criticism; see Robert Venturi, Complexity and Contradiction in Architecture (New York, second edition, 1977), ch. 5. Venturi in turn cites Wylie Sypher, Four Stages of Renaissance Style (Garden City, N.Y., 1955).

In contrast, the conventional graphical frame performs only a modest design function, the separation of the grid and data measures from the labels. And it is a place to hang the grid ticks. With all that ink doing so little, it is a prime candidate for mobilization as a double-functioning graphical element. Hence the range-frame, the quartile frame, and the dot-dash-plot.

The principle, then, is:

Mobilize every graphical element, perhaps several times over, to show the data.

The danger of multifunctioning elements is that they tend to generate graphical puzzles, with encodings that can only be broken by their inventor. Thus design techniques for enhancing graphical clarity in the face of complexity must be developed along with multifunctioning elements.

## Data-Built Data Measures

The graphical element that actually locates or plots the data is the data measure. The bars of a bar chart, the dots of a scatterplot, the dots and dashes of a dot-dash-plot, the blots of a blot map are data measures. The ink of the data measure can itself carry data; for example, the dots of the scatterplot can take on different shadings in response to a third variable.

Buildinur ce v detail and dimensionality of a graphic. The stem-and-leaf plot constructs the distribution of a variable with numbers themselves:

![](images/a3236cc8fcf353be69d092a2f7c54602e7ad0d3aa48e1d0a9c3cf738c78a1507.jpg)

The idea of making every graphical element effective was behind the design of the stem-and-leaf plot. In presenting his invention, John Tukey wrote: "If we are going to make a mark, it may as well be a meaningful one. The simplest—and most useful—meaningful mark is a digit."2

Here, too, the data form the data measure. Note the bimodal distribution i thehitogramcolle sudents arranged byheht.

2"Some Graphic and Semigraphic Displays," in T. A. Bancroft, ed., Statistical Papers in Honor of George W. Snedecor (Ames, Iowa, 1972), p. 296.

![](images/aa4393eb11d79d3241b9f86c0df57c355136b205772f6cf796621cdb164816d4.jpg)  
Brian L. Joiner, "Living Histograms," International Statistical Review, 43 (1975), 339-34o. But, for further developments, see Mark F. Schilling, Ann E. Watkins, and William Watkins, "Is Human Height Bimodal?" The American Statistician, 56 (August 2002), 223229.

A distinguished graphic that builds data measures out of data was designed by Colonel Leonard P. Ayres for his statistical history of World War I, a book with several notable graphics all done by typewriter and rule. Constructing the data measures out of each American division's name (a numerical designation) turns what might have been a routine time-series into an elegant display. (Note that the cumulative design depends on the fact that none of the divisions returned before October 1918.) The triple-functioning data measure shows: (1) the number of divisions in France for each month, June 1917 t0 October 1918; (2) what particular divisions were in France in each month; and (3) the duration of each division's presence in France.

![](images/81b8e3ffa74f4fb5e29e4a9d070b185c49c869bebec52853180b3d7662571e6a.jpg)

Encoding of data measures can be far more elaborate. The plotted points here are Chernoff faces, which reduce well, maintaining legibility even with individual areas of .o5 square inches as shown.3 The analyst would observe the standard X-Y scatterplot and then turn to the within-scatter detail, seeking clusters of similar observations over the X-Y plane. Outlying faces and those inconsistent with others in the neighborhood—they are, of course, strangers—should be identified by observation number or name.

3Herman Chernoff, "The Use of Faces to Represent Points in k-Dimensional Space Graphically," Journal of the American Statistical Association 68 (June 1973), 361-368. For an application of faces located over two dimensions, see Howard Wainer and David Thissen, "Graphical Data Analysis," Annual Review of Psychology, 32 (1981), 191241.

![](images/e5504959409233118ca9dca8652d427cd168825dd2dbb9140b13e6c56607059e.jpg)

With cartoon faces and even numbers becoming data measures, we would appear to have reached the limit of graphical economy of presentation, imagination, and, let it be admitted, eccentricity.

But let us consider this shaped poem, "Easter Wings" by George Herbert (1593-1633), which uses space—the length of each line— to depict quantity, all done 15o years before Playfair.4 The lines double-function: the longer lines describe wealth, plenty, largesse, and rising to flight; shorter lines tell of poverty and becoming o thine;nd entemedia gh idicate tran and change (decaying, rising, combining, becoming):

4 For a remarkable oTsoG-like tour of the many typographical variant shapes of "Easter Wings" in its long publication history, see te essay "FIAT LUX," y "Random Cloud" in Randall McLeod, ed., Crisis in Editing: Texts of the English Renaissance (New York, 1994), 61-172.

## Easter-wings.

Lord who, Though foolishly he lost the same,   
Decaying more and more,   
Till he became   
Most poore :   
With thee   
O let me rise   
As larks, harmoniously,   
And sing this day thy victories:   
Then shall the fall further the fight in me.   
My tender age in sorrow did beginne:   
And still with sicknesses and shame   
Thou didst so punish sinne,   
That I became   
Most thinne.   
With thee   
Let me combine   
And feel this day thy victorie :   
For, if I imp my wing on thine,   
Affliction shall advance the flight in me.

And the typographical delight of the statistician W. J. Youden:

THE

NORMAL

Law of ErrOr

stand8 out in the

EXPERIENCE OF MANKIND

As one of the Broadest

GENERALIZATIONS OF NATURAL

philosophy  it serves a8 thE

GuiDing instrumenT in Researches

IN THE PHYSICAL AND BOCIAL SCIENCE8 AND

IN MEDICINE AGRICULTURE AND ENGINEERING

it is an indispensable tool for the analysib and the

interpretation of the basic data obtained by observation and experiment

Flyl :il a e, as in the living histogram. The chart shows how states once differed in their engineering standards for painting lane stripes on road pavement. Some states marked the road lanes with short dashes and long gaps; others used only solid lines. Portrayed in the graphic is the actual physical pattern painted on the road, with 48 U.S. states ordered by the length of the painted mark:

Redrawn from A. R. Lauer, "Psychological Factors in Effective Traffic Control Devices," Traffic Quarterly, 5 (January 1951), 94.

<table><tr><td colspan="2"></td><td colspan="2">50</td><td colspan="2">100</td><td colspan="2">150</td><td colspan="2">200</td><td colspan="2">250 300</td><td></td><td colspan="2"></td></tr><tr><td>California</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>350</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Missouri Minnesota</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Alabama</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Arizona Colorado</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Florida</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Georgia</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Kentucky</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Louisiana</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Maine</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Massachusetts</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mississippi</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Nebraska</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Nevada</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New Hampshire</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New Mexico</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>New York</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>North Carolina</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Oregon</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Pennsylvania</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Washington</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Delaware Iowa</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Wyoming</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Connecticut</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Vermont</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Wisconsin</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rhode Island Kansas</td><td></td><td></td><td></td></table>

## Data-Based Grids

Very occasionally the grid can report directly on the data. This grid is formed by the location of measurement instruments; the plain dots register a zero reading, in contrast with the white background where no readings were taken. Erasing the grid would erase measured data (rather uneventful, to be sure). Such is not the case for most grid dots, ticks, and lines.

![](images/658d4c93998ee7537e8ec33ff44a83b9ebd171fd3b432b105e2b76dbfa7b531b.jpg)  
K. V. Roberts and D. E. Potter, "Magnetohydrodynamic Calculations," in Berni Alder, et al., eds., Methods in Computational Physics: Volume 9, Plasma Physics (New York, 197o), p. 402.

The arrangement of data in this table-graphic yields an internal grid, a rare example of data as grid:
<table><tr><td colspan="2">MID-PARENTS</td><td colspan="6">ADULT CHILDREN their Heights, and Deviations from 68inches.</td></tr><tr><td>Heights in</td><td>Deviates in</td><td colspan="6">64}$</td></tr><tr><td>inches 72</td><td>inches</td><td colspan="6">-4 I</td></tr><tr><td>71</td><td>+3</td><td colspan="6"></td></tr><tr><td></td><td>+2</td><td colspan="6"></td></tr><tr><td>70</td><td colspan="6">+1</td></tr></table>

Karl Pearson, The Life, Letters and Labours of Francis Galton (Cambridge, 1930), vol. MII-A, 14.

![](images/5efb475f0740eb0e99687d6d2617bff6279092402f107d289264501bcdf431e6.jpg)

Here the ri is theement  interet, rather than the map.

Lester J. Cappon, Barbara Bartz Petchenik, and John Hamilton Long, Atlas of Early American History (Princeton, 1976), p. 58.

The grid that follows presents the data on the surface of the rock; on the sides, the grid is conventional. The two displays compare the effect of religion, taking into account party affiliation, on a person's vote for president in 1956 and in 1960 (when a Catholic ran for president). Note there is no reliable slope associated with religion in 1956, once party is controlled; in 1960, a systematic effect is found. Reading the slopes in the other direction shows the persistent effect of party in both elections:

Philip E. Converse, "Religion and Politics: The 1960 Election," in Angus Campbell, Philip E. Converse, Warren E. Miller, and Donald E. Stokes, Elections and the Political Order (New York, 1966), 102103.

![](images/dfb6923ddd44bd47e04e2247f21bc9d618062bb4546d5807e867824914bfd61c.jpg)

![](images/b6eb5f2ab7a3df65d9b78d69080f6a9a7a101711f4d852241cec6566929f90f4.jpg)

Although the implicit plotting coordinates are based on regular intervals, the vertical rid lines in the published version are irrg ularly spaced, keyed to significant events. The data-based grid is a shrewd graphical device, serving rather than fighting with the data. It is a technique underused in contemporary graphical work.

![](images/27c14bc28b64a4896b1bd8e04c28dd1039cbb5a6d32dee1a50bcc613f641c003.jpg)

![](images/197ece271b9456ca3e47d5d76c2d6bb234f5f167845a080cd731b032da6bebfb.jpg)  
N2

## Double-Functioning Labels

Data-based coordinate lines lead to data-based labels, as, for example, at the bottom of Playfair's debt graphic. Again, the issue is the same: why not use the ink to show data? Beginning with conventionally labeled frame

<table><tr><td>Γ</td><td>1</td><td>T</td><td>T</td></tr><tr><td>0</td><td>10</td><td>20</td><td></td></tr></table>

and erasing to the range-frame
<table><tr><td>—</td><td>T</td><td>I</td><td>T</td><td>I</td></tr><tr><td>0</td><td>10</td><td>20</td><td>30</td><td>40</td></tr></table>

leaves those lonely ticks and numbers out on the tails, working to help the eye get a better reading on where the line of the rangeframe ends. But that job can be done better by investing the same ink in data: rather than showing the minimum round number and the maximum round number at the ends of the frame, show the actual minimum and maximum realized in the data:

<table><tr><td></td><td>T</td><td>T</td><td>T</td></tr><tr><td>4</td><td>10</td><td>20</td><td>30</td></tr></table>

With its greater precision and two tick-marks less of non-dataink, the range-frame with range-labels is superior to the rangeframe with round number labels. Both improve on the standard, passive frame.

Numbers also double-function when used both to name things (like an identification number) and to reflect an ordering. In this graphic (in which the circled numbers fail to double-function), each number identifies a particular study of the thermal conductivity of tungsten, ordered alphabetically by the last name of the first author. If that list were ordered by date of publication instead, then the code would also indicate the time order in which the various conductivity determinations were made. Thus "1" would indicate the earliest study, and so on—or, alternatively, "61c" would be the third study published in 1961. Such information has interest, since we could see which of the early studies got the right answer. In addition, the movement of the studies toward the "correct" recommended values could be tracked. This extra information requires no additional ink.

C.Y. Ho, R. W. Powell, and P. E. Liley, Thermal Conductivity of the Elements: A Comprehensive Review, supplement no. 1, Journal of Physical and Chemical Reference Data, 3 (1974), I692.

![](images/9b069c85c3136bcc641471f632695ec5ee0cee94168eda8657e33065600f483d.jpg)

In most graphics, the coordinate labels are far from the data measures. Consequently the eye of the viewer must move back and forth between the path formed by the data and the coordinate positions arrayed along the margins of the graphic. Sometimes this eye-work can be eliminated entirely by turning the coordinate labels into data measures, another double-functioning maneuver. Take the example from the style sheet of the Journal of the American Statistical Association:

![](images/344a4c28608131a0e2ce9b363aedb000ae6ea10a87fbee47783efdc88e7529c0.jpg)

The grid increments of the X-axis are relocated upward to mark the path of the data:

0   
.15 1   
.10 2   
.05 3 4 5 6   
.00 7 8 9 10 11 12 13 14 15

An since the ise  thi ispy is the proability t  ir value, the round-number Y-scale is replaced by exact values:

.114 1   
.075 2   
.052 3   
.034 4   
.025 5   
.004 6 7 8 9 10 11 12 13 14 15   
.002

The Y-scale now resembles the dashes of the dot-dash-plot, with the vertical column of data-positioned numbers serving as the dashes to indicate the marginal distribution.

The method of data-based markers for the marginal distributions suggests a further enhancement of the dot-dash-plot:

![](images/a063068c61b68a0cf17ffb8f28e36e97eb629ae551cd957db2107487b0059cee.jpg)

Now the numbers in the margin eliminate the standard frame and even a range-frame, replace the coordinate ticks, show the marginal distribution of both variables, and record the exact values of the two measurements made on each unit of observation. This graphical arrangement performs better for smaller data sets (say 30 observations or less) and when a fine level of detail is required.

Finally, a striking design with data-based labels:

![](images/e5a2f2258860253e4fca42dcd703feea92ea903b118380faeae58b7c3d754334.jpg)

## Puzzles and Hierarchy in Graphics

The complexity of multifunctioning elements can sometimes turn data graphics into visual puzzles, crypto-graphical mysteries for the viewer to decode. A sure sign of a puzzle is that the graphic must beepretrough averba rathr thanvisalps.

For exap, espi evenulndatee, formed by crossing two four-color grids, this is a puzzle graphic. Deployed here, in a feat of technological virtuosity, are 16 shades of color spread on 3,056 counties, a monument to a sophisticated computer graphics system.5 But it is surely a graphic experienced verbally, not visually. Over and over, the viewers must run little phrases through their minds, trying to maintain the right pattern of words to make sense out of the visual montage: "Now let's see, purple represents counties where there are both high levels of male cardiovascular disease mortality and 11.6 to 56.0 percent of the households have more than 1.01 persons per room.

. . . What does that mean anyway? . . . And the yellow-green counties. . . ." By contrast, in a non-puzzle graphic, the translation of visual to verbal is quickly learned, automatic, and implicit —so that the visual image flows right through the verbal decoder initially necessary to understand the graphic. As Paul Valéry wrote, "Seeing is forgetting the name of the thing one sees.

5 The technique is described in Vincent P. Barabba and Alva L. Finkner, "The Utilization of Primary Printing Colors in Displaying More than One Variable," in Bureau of the Census, Technical Paper No. 43, Graphical Presentation of Statistical Information (Washington, D.C., 1978), 14-21. The maps are assessed in Howard Wainer and C. M. Francolini, "An Empirical Inquiry Concerning Human Understanding of Two-Variable Color Maps," American Statistician, 34 (1980), 81-93.

![](images/3b3c69a37e62fe355b8e5501146510ab55f54b4baf89d46ea4b989adecc59755.jpg)

Color often generates graphical puzzles. Despite our experiences with the spectrum in science textbooks and rainbows, the mind's eye does not readily give a visual ordering to colors, except possibly for red to reflect higher levels than other colors, as in the hot spots of the cancer map. Attempts to give colors an order result in those verbal decoders and the mumbling of little mental phrases again—indeed, even mnemonic phrases about the phrases required for graphical decoding:

A method of coloring ingenious in idea but not very satisfactory in practice was used by L. L. Vauthier. It was called the mountain-to-the-sea method. White was used for the representation of the greatest intensity of the fact because it indicated the summit of a mountain with its eternal snow, next came green representing the forests farther down the slopes, then yellow for the grain of the plains, and finally for the minimum the blue of the waters at sea level.

Because they do have a natural visual hierarchy, varying shades of gray show varying quantities better than color. Ten gray shades worked effectively in the galaxies map:

6 H. Gray Funkhouser, "Historical Development of the Graphical Representation of Statistical Data," Osiris, 3 (1937), 326, who cites É. Cheysson, "Les mé- thodes de statistique graphique à l'Exposition universelle de 1878," Journal de la Société de Statistique de Paris, 19 (1878), 331.

![](images/c6de7dfd6a84026c4545cf842cd15e5dbc4e703a2e429a9952cbb31c0ea7255a.jpg)

The success of gray compared to the visually more spectacular color gives us a lead on how multifunctioning graphical elements can communicate complex information without turning into puzzles. The shades of gray provide an easily comprehended order to the data measures. This is the key. Central to maintaining clarity in the face of the complex are graphical methods that organize and order the flow of graphical information presented to the eye.

How can graphical architecture promote the ordered, sequenced, hierarchical flow of information from the graphic to the mind's eye? How can the data-information be arranged so that the viewer is able to peel back layer after layer of data from a graphic?

Multip lyeroration e crate byultievin depths and multiple viewing angles.

Graphics can be designed to have at least three viewing depths: () what is seen from a distance, an overall structure usually aggregated from an underlying microstructure; (2) what is seen up close and in detail, the fine structure of the data; and (3) what is seen implicitly, underlying the graphicthat which is behind the graphic. Look at all the differnt level of detail created by this population density map of the United States, a glory of modern cartography prepared by the Bureau of the Census. Each dot, except in urban centers, represents 5oo people. Note the corridors connecting the major urban complexes; the effects of landforms on the population distribution (the central valley of California, the valleys and ridges of Appalachia, and the clusters along rivers); and the small towns along the highways, linked like a string of pearls. The map arrays, in effect, some 400,oo0 points on its implicit grid.

Different visual angles for different aspects of the data also organize graphical information. Each separate line of sight should remain unchanging (preferably horizontal or vertical) as the eye watches for data variation off the flat of the line of sight. For multivariate work, several clear lines can be created. Recall Ayres' display of American divisions in France. Even with its complex, interwoven data, the graphic is not a puzzle. Three separate visual angles make the flow of information coherent: the profile of the horizon for the upward-moving time-series, the vertical for the composition of the bar, and the horizontal for each division's stay. Thus while every drop of ink serves three different data display functions, each of the three comes to the eye with its own independence and integrity.

![](images/c5a29c9286267b54f87efe20b4b286161481ea7dc3473070f354762e01cbdb52.jpg)

![](images/9731e07e9b428b1928d0cbad07c0073b79834d54679754bf951fbf37b421d150.jpg)

Current Receipts of Government as a Percentage of Gross Domestic Product, 1970 and 1979

![](images/be8bf4dc2349ec995e1adb84f96a99798b871605e86c151bab7ca1ca1f9e719e.jpg)

Similarly, this table-graphic organizes data for viewing in several directions. The chart, when read vertically, ranks 15 countries by government tax collections in 1970 and again in 1979, with the names spaced in proportion to the percentages. Across the columns, the paired comparisons show how the numbers changed over the years. The slopes are also compared by reading down the collection of lines, and lines of unusual slope stand out from the overall upward pattern. The information shown is both integrated and separated: integrated through its connected content, separated in that the eye follows several different and uncluttered paths in looking over the data:

<table><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>

Suu in creating and evaluating designs that organize complex information hierarchically.

I want to reach that state of condensation of sensations which constitutes a picture.

Henri Matisse

Our eyes can make a remarkable number of distinctions within a small area. With the use of very light grid lines, it is easy to locate 625 points in one square inch or, equivalently, 100 points in one square centimeter.

Or consider how an 8o by 8o grid over a square inch—about 30   
by 30 over a square centimeter—divides the space:1

With the help of considerable redundancy and context, our eyes make fine distinctions of this sort all the time. Measurement instruments used in engineering, architectural, and machine work are engraved with scales of 2o increments to the centimeter and 50 to the inch. Or consider the reading of fine print. The type in the U.S. Statistical Abstract is set at 12 lines per vertical inch, with each line running at about 23 characters per inch for a maximum density of 276 characters per square inch. The actual density, given the white space, is in this case 185 characters per square inch or 28 per square centimeter.

No. 1450. STEEL PRODUCTS—NET SHIPMENTS, BY MARKET CLASSES: 1960 TO 1978 Inhor tCs conlns t"me ecass

1 A square grid formed on each side by n parallel black and n-1 parallel white lines contains n2 intersections of two black lines (corners of squares), (n-1)2 intersections of two white lines (white squares), and 2n(n-1) intersections of a black and white line (sides of squares), for a total of (2n-1)2 line intersections or distinct locations.

25,281 distinctions

<table><tr><td>MARKET CLASS</td><td>1960</td><td>1965</td><td>1970</td><td>1973</td><td>1974</td><td>1975</td><td>1976</td><td>1977</td><td>1978</td></tr><tr><td>Totali...</td><td>71,149</td><td>92,666</td><td>90.798</td><td>111,430</td><td>109.472</td><td>79.957</td><td>89,447</td><td>91,147</td><td>97.935</td></tr><tr><td>Steel for converting and processing. Independent forgers, n.e.c.</td><td>2,928 841</td><td>3,932 1,250</td><td>3,443 1,048</td><td>4,714 1,213</td><td>4,486 1,339</td><td>3,255 1,098</td><td>4,036 952</td><td>3,679 998</td><td>4,612 1,192</td></tr><tr><td>Industrial fasteners Steel service centers, distributors..</td><td>1,071 11,125</td><td>1,234 14, 813</td><td>1,005 16,025</td><td>1,278 20 ,383</td><td>, 31 20, 0, 400</td><td>675 12,700</td><td>912 14,615</td><td>848 15,346</td><td>870 17,333</td></tr><tr><td>Construction, inci. maintenance_</td><td>9,664</td><td>11,836</td><td>8,913</td><td>10, 731</td><td>11,360</td><td>8,119</td><td>7,508</td><td>7,553</td><td>9,612</td></tr><tr><td>Contractors&#x27; products.</td><td>3,602</td><td>5,018</td><td>4,440</td><td>6,459</td><td>6,249</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>3,927</td><td>4,502</td><td>4,500</td><td>3,480</td></tr><tr><td>Automotive...</td><td>14,610</td><td>20,123</td><td>14,475</td><td>3,217</td><td>18,928</td><td>1 15, 214</td><td>21,351</td><td>21,490</td><td>21,253</td></tr><tr><td>Rail transportation......-</td><td>2,525</td><td>3,805</td><td>3,098</td><td>3,228</td><td>3,417</td><td>3,152</td><td>3,056</td><td></td><td></td></tr><tr><td>Freight cars, passenger cars,</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3,238</td><td>3,549</td></tr><tr><td>locomotives..</td><td>1,763</td><td>2,875</td><td>2,005</td><td>1,997</td><td>2,097</td><td>1,794</td><td>1,428</td><td>1,709</td><td>2,188</td></tr><tr><td>Rails and all other .</td><td>762</td><td>99300</td><td>1,093</td><td>1,231</td><td>1,320</td><td>1,358</td><td>1,628</td><td>1,529</td><td>1,,361</td></tr><tr><td>Shipbuilding and marine equip...</td><td>622 78</td><td>1,0051</td><td>859</td><td>1,019</td><td>1,339</td><td>1,413</td><td>969</td><td>869</td><td>845</td></tr><tr><td>Aircraft and aerospace.. Ofl and gas industries.....</td><td>1,759</td><td>94</td><td>56</td><td>69</td><td>79</td><td>69</td><td>59</td><td>63</td><td>60</td></tr><tr><td></td><td>288</td><td>1,936 392</td><td>3,550</td><td>3,405</td><td>4,210</td><td>4,171</td><td>2,653</td><td>3,650</td><td>4,140</td></tr><tr><td>Mining, quarrying, and lumbering.</td><td>1,003</td><td></td><td>4977</td><td>534</td><td>644</td><td>596</td><td>536</td><td>486</td><td>508</td></tr><tr><td>Agricultural, incl. machinery...</td><td></td><td>1,483</td><td>1,126</td><td>1,772</td><td>1,859</td><td>1,429</td><td>1,784</td><td>1,743</td><td>1,805</td></tr><tr><td>Machinery, industrial equip., tools</td><td>3,958</td><td>5,873</td><td>5,169</td><td>6,351</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Electrical equipment..</td><td>2078</td><td>2,985</td><td>$2,10 </td><td>3,348</td><td>6,440 3,242</td><td>5,173 2,173</td><td>5,180</td><td>5,566 2639</td><td>5,992</td></tr><tr><td>Appliances, utensils, and cutlery..-</td><td>1,760</td><td></td><td>160</td><td>2,747</td><td></td><td>1,653</td><td>2,671 1,9</td><td>2,129</td><td>2,811</td></tr><tr><td>Other domestic commercial equip.</td><td>1,959</td><td></td><td>778</td><td>1,990</td><td></td><td>1,390</td><td>1,813</td><td>1.846</td><td>2,094</td></tr><tr><td>Containers, packaging, shipping...</td><td>6,42</td><td></td><td>HN 775</td><td>7,11</td><td></td><td>6,053</td><td>6,914</td><td>6,714</td><td>1,889</td></tr><tr><td></td><td>4,976</td><td>5, 867</td><td>6,29</td><td>6,070</td><td>, 349</td><td></td><td></td><td>5,173</td><td>6,595</td></tr><tr><td>Cans and closures..</td><td>165</td><td>289</td><td>1; 222</td><td>918</td><td></td><td>4,859</td><td>5,2</td><td></td><td>4,950</td></tr><tr><td>Ordnance and other military.</td><td></td><td></td><td></td><td></td><td>654</td><td>405</td><td>219</td><td>193</td><td>207</td></tr><tr><td>Exports (reporting companies only)</td><td>2,563</td><td>2,078</td><td>5,985</td><td>3,138</td><td>3,961</td><td>1,755</td><td>1,839</td><td>1,076</td><td>1,224</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

![](images/7451c158e99e1d4a5bd0860cce71aea5017676e0b9bd597357ee87bf911bfd03.jpg)  
Totalincludes nonclassifed shipments, and beginning 0data include estimates or  relatively all e  compan hich repot  se poducion u ot hipmenBol ut , d ses. Includes railways, rapid transit systems, railroad rails, trackwork, and equipment.  
U.S. Bureau of the Census, Statistical Abstract of the United States: 1979 (Washington, D.C., 1979), p. 822.

Maps routinely present even finer detail. A cartographer writes that "the resolving power of the eye enables it to differentiate to 0.1 mm where provoked to do so. Clearly, therefore, conciseness is of the essence and high resolution graphics are a common denominator of cartography."2 Distinctions at o.1 mm mean 254 per inch.

2D. P. Bickmore, "The Relevance of Cartography," in John C. Davis and Michael J. McCullagh, eds., Display and Analysis of Spatial Data (London, 1975), p. 331.

How many statistical graphics take advantage of the ability of the eye to detect large amounts of information in small spaces? And how much information should graphics show? Let us begin by considering an empirical measure of graphical performance, the data density.

## Data Density in Graphical Practice

The numbers that go into a graphic can be organized into a data matrix of observations by variables. Taking into account the size of the graphic in relation to the amount of data displayed yields the data density:

$$
\mathrm { d a t a \ d e n s i t y \ o f \ a \ g r a p h i c = \frac { n u m b e r \ o f \ e n t r i e s \ i n \ d a t a \ m a t r i x } { a r e a \ o f \ d a t a \ g r a p h i c } }
$$

Data matrices and data densities vary enormously in practice. At one extreme, this overwrought display (originally printed in five colors) presents a data matrix of four entries, the names and the numbers for the two bars on the right. The left bar is merely the total of the other two. The graph covers 26.5 square inches (171 square centimeters), resulting in a data density of .15 numbers per square inch (.o2 numbers per square centimeter), which is thin indeed.

![](images/82d2ba38bc2914b8fd294c71cd8337b5976f2d990de3d7edad7715c49293b0ec.jpg)

The exemplar from the JASA style sheet comes in at a lightweight 3.8 numbers per square inch (o.6 numbers per square centimeter) and a small data matrix of 32 entries:

![](images/1b9c78f3bbf2f6e54cc5b010e0c8d5ac4a7d2decf0972631d7edcaf273637fde.jpg)

In contrast, the New York weather history, in this reduced version, does very well at 181 numbers per square inch (28 per square centimeter):

![](images/ca158e259b5016d2bcbf2fedac2230ee0061e62c7c4679f3a1b2ac752321ca5d.jpg)

An annual sunshine record reports about 1,00 numbers per square inch (160 per square centimeter):

F. J. Monkhouse and H. R. Wilkinson, Maps and Diagrams (London, third edition, 1971), pp. 242243.

![](images/23f6ae046c5d642ed591e133e48d4385d35814998db79df90396c6577ad2575c.jpg)

The visual metaphor corresponds appropriately to the data if the image is reversed, so that the light areas are the times when the sun shines:

![](images/03ac1323590988af9649953e0ee23d9966528d358ef7dd95328dbc71c69a4203.jpg)

Jacques Bertin, Semiologie Graphique (Paris, second edition, 1973), p. 152.

![](images/5e281c23bb0737a4aeeae3bc6931e7d377a82770cca90267eb373e6c739bee36.jpg)

This map (27 square inches, 175 square centimeters) shows the location and boundaries of 3o,ooo communes of France. It would require at least 240,ooo numbers to recreate the data of the map (30,0oo latitudes, 30,0oo longitudes, and perhaps six numbers describing the shape of each commune). Thus that data density is nearly 9,000 numbers per square inch, or 1,400 numbers per square centimeter.

The new map of the galaxies locates 2,275,328 encoded rectangles on a two-dimensional surface of 61 square inches (390 square centimeters). Each rectangle represents three numbers (two by its location, one by its shading), yielding a data density of 110,000 numbers per square inch or 17,o0o numbers per square centimeter. That is the current record.

![](images/c9229b20840ee456c14aee5403191ae69845602fd6645af9b9b4bd248625d06a.jpg)

## Data Density and the Size of the Data Matrix: Publication Practices

The table shows the data density and the size of the data matrix for graphics sampled from scientific and news publications. At least 20 graphics from each publication were examined.

The table records an enormous diversity of graphical performances both within and between publications. A few data-rich designs appear in nearly every publication. The opportunity is there but it is rarely exploited: the average published graphic is rather thin, based on about 5o numbers shown at the rate of 1o per square inch. Among the world's newspapers, the Wall Street Journal, The Times (London), and Asahi publish data-rich graphics, with data densities equal to those of the Journal of the American Statistical Association. Most of the American papers and magazines, along with Pravda, publish less data per graphic than the major papers of other industrialized countries.

Data Density and Size of Data Matrix, Statistical Graphics in Selected Publications, Circa 1979-1980
<table><tr><td></td><td colspan="3">Data Density (Numbers per square inch) median minimum maximum</td><td colspan="3">Size of Data Matrix median minimum maximum</td></tr><tr><td>Nature</td><td>48</td><td>3</td><td>362</td><td>177</td><td>15</td><td>3780</td></tr><tr><td>Journal of the Royal Statistical Society, B</td><td>27</td><td>4</td><td>115</td><td>200</td><td>10</td><td>1460</td></tr><tr><td>Science</td><td>21</td><td>5</td><td>44</td><td>109</td><td>26</td><td>316</td></tr><tr><td>Wall Street Journal</td><td>19</td><td>3</td><td>154</td><td>135</td><td>28</td><td>788</td></tr><tr><td>Fortune</td><td>18</td><td>5</td><td>31</td><td>96</td><td>42</td><td>156</td></tr><tr><td>The Times (London)</td><td>18</td><td>2</td><td>122</td><td>50</td><td>14</td><td>440</td></tr><tr><td>Journal of the American Statistical Association</td><td>17</td><td>4</td><td>167</td><td>150</td><td>46</td><td>1600</td></tr><tr><td>Asahi</td><td>13</td><td>2</td><td>113</td><td>29</td><td>15</td><td>472</td></tr><tr><td>New England Journal of Medicine</td><td>12</td><td>3</td><td>923</td><td>84</td><td>8</td><td>3600</td></tr><tr><td>The Economist</td><td>9</td><td>1</td><td>51</td><td>36</td><td>3</td><td>192</td></tr><tr><td>Le Monde</td><td>8</td><td>1</td><td>17</td><td>66</td><td>11</td><td>312</td></tr><tr><td>Psychological Bulletin</td><td>8</td><td>1</td><td>74</td><td>46</td><td>8</td><td>420</td></tr><tr><td>Journal of the American Medical Association</td><td>7</td><td>1</td><td>39</td><td>53</td><td>14</td><td>735</td></tr><tr><td>New York Times</td><td>7</td><td>1</td><td>13</td><td>35</td><td>6</td><td>580</td></tr><tr><td>Business Week</td><td>6</td><td>2</td><td>12</td><td>32</td><td>14</td><td>96</td></tr><tr><td>Newsweek</td><td>6</td><td>1</td><td>13</td><td>23</td><td>2</td><td>96</td></tr><tr><td>Annuaire Statistique de la France</td><td>6</td><td>1</td><td>25</td><td>96</td><td>12</td><td>540</td></tr><tr><td>Scientific American</td><td>5</td><td>1</td><td>69</td><td>46</td><td>14</td><td>652</td></tr><tr><td>Statistical Abstract of the United States</td><td>5</td><td>2</td><td>23</td><td>38</td><td>8</td><td>164</td></tr><tr><td>American Political Science Review</td><td>2</td><td>1</td><td>10</td><td>16</td><td>9</td><td>40</td></tr><tr><td>Pravda</td><td>0.2</td><td>0.1</td><td>1</td><td>5</td><td>4</td><td>20</td></tr></table>

Very few statistical graphics achieve the information display rates found in maps. Highly detailed maps portray 100,000 to 150,ooo bits per square inch. For example, the average U.S. Geological Survey topographic quadrangle (measuring 17 by 23 inches) is estimated to contain over 100 million bits of information, or about 250,000 per square inch (40,000 per square centimeter).3 Perhaps some day statistical graphics will perform as successfully as maps in carrying information.

## High-Information Graphics

Data graphics should often be based on large rather than small data matrices and have a high rather than low data density. More information is better than less information, especially when the marginal costs of handling and interpreting additional information are low, as they are for most graphics. The simple things belong in tables orin the text; graphics can give a sense of large and complex data sets that cannot be managed in any other way. If the graphic becomes overcrowded (although several thousand numbers represented may be just fine), a variety of data-reduction techniques—averaging, clustering, smoothing—can thin the numbers out before plotting.4 Summary graphics can emerge from high-information displays, but there is nowhere to go if we begin with a low-information design.

Data-rich designs give a context and credibility to statistical evidence. Low-information designs are suspect: what is left out, what is hidden, why are we shown so little? High-density graphics help us to compare parts of the data by displaying much information within the view of the eye: we look at one page at a time and the more on the page, the more effective and comparative our eye can be.5 The principle, then, is:

Maximize data density and the size of the data matrix, within reason.

High-information graphics must be designed with special care. As the volume of data increases, data measures must shrink (smaller dots for scatters, thinner lines for busy time-series). The clutter of chartjunk, non-data-ink, and redundant data-ink is even more costly than usual in data-rich designs.

The way to increase data density other than by enlarging the data matrix is to reduce the area of a graphic. The Shrink Principle has wide application:

## Graphics can be shrunk way down.

Many data graphics can be reduced in area to half their currently published size with virtually no loss in legibility and information. For example, Bertin's crisp and elegant line allows the display of 17 small-scale graphics on a single page along with extensive text. Repeated application of the Shrink Principle leads to a powerful and effective graphical design, the small multiple.

![](images/6725cd208c6ab0c35735456f80a2e251ac3544b2b321b462f1ab4b3d54b3b84d.jpg)

## PROBLEMES GRAPHIQUES POSES PAR LES CHRONIQUES

Un total sur deux cases (sur deux ans) doit etre divise par deux (1).   
Un total pour six mois sera multiplie par deux dans des cases annuelles.

Courbes trop pointues, reduire T'echelle des Q; la sensibilite angulaire sinscrit dans une zone moyenne autour de 70.

Si la courbe n'est pas réductible (grandes el petites variations) employer les colonnes remplies (5).

Courbes trop plates: augmenter echelle des Q.

Variations tres faibles par rapport au total. Celui-ci perd de limportance et le zero peut etre supprime, a condition que le lecteur voit sa suppression (9). Le graphique peut étre interprété comme une accelération si letude fine des variations est necessaire (echelle logarithmique (10) (v. p. 240).

Tres grande amplitude entre les valeurs extremes. I1 faut admettre :

) Soit de ne pas percevoir les plus petites variations.

2°) Soit de ne s'interesser qu'aux differences relatives (echelle logarithmique) sans connaitre la quantité absolue.

3)Soit admeure des periodes differentes dans la composante ordonnee et les traiter a des echelles differentes au-dessus de l'echelle commune (12).

## Cycles tres marques.

Si r'etude porte sur la comparaison des phases de chaque cycle, if est preferable de decomposer (13) de maniere à superposer les cycles (14). La construction polaire peut étre employee. de preference dans une forme spirale (15) (ne pas commencer par un trop petit cercle); pour spectaculaire qu'elle soit, elle est moins efficace que la construction orthogonale.

Courbes annuelles de pluie ou de temperature. Un cycle possede deux phases (17), pourquoi n'en offrir qu une à la perception du spectateur? (16).

## Small Multiples

Small multiples resemble the frames of a movie: a series of graphics, showing the same combination of variables, indexed by changes in another variable. Twenty-three hours of Los Angeles air pollution are organized into this display, based on a computer generated video tape. Shown is the hourly average distribution of reactive hydrocarbon emissions. The design remains constant through all the frames, so that attention is devoted entirely to shifts in the data:

From video tape by Gregory J. McRae, California Institute of Technology. The model is described in G. J. McRae, W. R. Goodin, and J. H. Seinfeld, "Development of a Second-Generation Mathematical Model for Urban Air Pollution. I. Model Formulation," Atmospheric Environment, 16 (1982), 679696.

![](images/6371235cd1a5e47f4433e4fd366289c6a3a97af00fc0cd9eb7b8100fb7863bcb.jpg)

These grim small multiples show the distribution of occurrence of the cancer melanoma. The sites of 269 primary melanomas are recorded, along with the distribution between men and women. Note the data graphical arithmetic, similar to that of the multiwindow plot.

Arthur Wiskemann, "Zur Melanoment stehung durch chronische Lichteinwirkung," Der Hautarzt, 25 (1974), 21.

![](images/478fd1dc00fd9783c74c934be9d37a6486d7f0a1eeabf6d134086c58be7a2855.jpg)  
Abb. 1. Verteilung von 269 primären Melanomen auf Kopf und Hals

![](images/b906f969d5ded263184d5b6cf2ece1014216ab59479baea72bf471c267e7ed89.jpg)  
Abb. 2

![](images/daa8c3551ca03e0fc54baac144be8849159a9fec1ad144d206f7c22d706b9260.jpg)  
Abb. 3  
Abb. 2 u. 3. Differenzierung der Melanomverteilung nach Geschlechtern

The effects of sampling errors are shown in these 12 distributions, each based on a sample of go random normal deviates:

Edmond A. Murphy, "One Cause? Many Causes? The Argument from the Bimodal Distribution," Journal of Chronic Diseases, 17 (1964), 309.

# IJY \$3vra}\$ O-15 10-

These six distributions show the age composition of herring catches each year from 1908 to 1913. A tremendous number of herring were spawned in 1904, and that class began to dominate the 1908 catch as four-year-olds, then the 19o9 catch as five-year-olds, and so on:

![](images/6fae72f09f3e9f8cfd3742fc58f7ac9f952aac4a12f0cd2bba4710f910dc7498.jpg)

This next design compares a complex set of data: shown are the chromosomes of (from left to right) man, chimpanzee, gorilla, and orangutan. The similarities between humans and the great apes are to be noted.

Johan Hjort, "Fluctuations in the Great Fisheries of Northern Europe," Rapports et Proces-Verbaux, 20 (1914), in Susan Schlee, The Edge of an Unfamiliar World (New York, 1973), p. 226.

Jorge J. Yunis and Om Prakash, "The Origin of Man: A Chromosomal Pictorial Legacy," Science, 215 (March 19, 1982), 1527.

<table><tr><td>1 0 101-4 I mI</td><td>a </td><td>14</td><td>BIE 3 I $\frac{ 3 }$ 15 a</td><td>b 4</td><td></td><td>- T 5</td><td>DI</td><td></td><td>6</td><td></td></tr><tr><td></td><td colspan="4"></td><td>10</td><td colspan="4">-m</td></tr><tr><td></td><td></td><td>8</td><td colspan="9">9 DI</td></tr></table>

And, finally, a visually similar small multiple, the Consumer Reports frequency-of-repair records for automobiles built from 1976 to 1981. This is a particularly ingenious mix of table and graphic, portraying a complex set of comparisons between manufacturers, types of cars, year, and trouble spots.

Consumer Reports, 47 (April 1982), 199207. Redrawn.

## uch bettr than averageBatter than averagAveragWorse than averagMuch worse than ave

<table><tr><td>Chevrolet Malibu, Chevelle 6, V6 76 77 78 79 80 81</td><td>Chevrolet Monza 4</td><td>Datsun 210, B210</td><td>Trouble Spots</td><td>Ford Granads 6</td><td>Ford pickup truck 6(2WD)</td><td>Honda Accord</td></tr><tr><td>o</td><td>76 77 78 79 80 81</td><td>76 77 78 79 80 81</td><td>Air-conditioning</td><td>76 77 78 79 80 81 O • O</td><td>77 78 79 80 81 • •</td><td>76 77 78 79 80 81</td></tr><tr><td></td><td>O O O</td><td>O</td><td>Body exterior (paint)</td><td>O •</td><td>O O</td><td>O O</td></tr><tr><td>•</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>•</td><td>Body exterior (rust)</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Body hardware</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>•</td><td>Body integrity</td><td>•</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Brakes</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Clutch</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>S</td><td>Driveline</td><td>0</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Electrical system (chassis)</td><td>o</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Engine cooling</td><td>•</td><td>0 O</td><td></td></tr><tr><td></td><td></td><td></td><td>Engine mechanical</td><td>O</td><td></td><td></td></tr><tr><td>0</td><td></td><td></td><td>Exhaust system</td><td>O</td><td>O</td><td></td></tr><tr><td></td><td></td><td>0</td><td>Fuel system</td><td>0</td><td></td><td></td></tr><tr><td></td><td></td><td>0</td><td>Ignition system</td><td>. •</td><td></td><td></td></tr><tr><td></td><td></td><td>• 0000</td><td>Suspension</td><td>o</td><td></td><td></td></tr><tr><td>00OOOO</td><td></td><td>00000 •</td><td>Transmission (manual)</td><td>•O 0•OOO</td><td>• o O 0 0 0000</td><td>O00O0 0O0</td></tr><tr><td>0O000</td><td></td><td>000000</td><td>Transmission (automatic) Trouble Index</td><td>0OOO0O</td><td>• OOOO0O</td><td></td></tr><tr><td></td><td></td><td>00000</td><td></td><td>00000</td><td></td><td>0OOOOO</td></tr><tr><td>00000</td><td></td><td></td><td>Cost Index</td><td></td><td>00000</td><td>000O0</td></tr></table>

<table><tr><td>Marcedes-Benz 300D 5{diesel) 76 77 78 79 80 81</td><td rowspan="8">Plymouth Volsre 6 00000</td><td rowspan="8">0</td><td>Suberu (except 4WD)</td><td>Trouble Spots</td><td>Toyota Corolia (exceptt Tercel)</td><td>Volkswagen Rabbit (diesel) 76 77 78 79 80 81</td><td rowspan="4">76 77 78 79 80 81 •.•</td><td rowspan="4">Volvo 240 series</td></tr><tr><td>76 77 78 79 80 81</td><td>76 77 78 79 80 81</td><td></td><td>76 77 78 79 80 81</td></tr><tr><td>00000 0000</td><td>000000</td><td>Air-conditioning</td><td>000 O O</td></tr><tr><td>00000</td><td>00O0</td><td>Body exterior (paint)</td><td>0 O 0 0000</td></tr><tr><td>0OOOO</td><td>0O0O</td><td>Body exterior (rust)</td><td>O 00 O</td></tr><tr><td>0000</td><td>0000</td><td>Body hardware</td><td>O</td></tr><tr><td>00000</td><td>O0O</td><td>Body integrity</td><td></td></tr><tr><td>00000</td><td>O•OO</td><td>Brakes</td><td></td></tr><tr><td></td><td>O</td><td>Clutch</td><td></td></tr><tr><td>00000</td><td>00000</td><td>Driveline</td><td></td></tr><tr><td>00000</td><td>• ••</td><td>Electrical system (chassis)</td><td></td></tr><tr><td>00000</td><td></td><td>000</td><td></td></tr><tr><td>0000</td><td>00000</td><td>0</td><td>Engine cooling</td><td></td><td></td></tr><tr><td>00000</td><td>000 O 0</td><td>O O</td><td>Engine mechanical Exhaust system</td><td></td><td></td></tr><tr><td>OOO0O</td><td>O</td><td>O O</td><td>Fuel system</td><td></td><td>00 0</td></tr><tr><td>00000</td><td></td><td>• o</td><td>Ignition system</td><td></td><td>O</td></tr><tr><td>00000</td><td></td><td>O O</td><td>Suspension</td><td></td><td>O 0</td></tr><tr><td></td><td>0</td><td>• O O OO</td><td>Transmission (manual)</td><td></td><td rowspan="2">00000 O O</td></tr><tr><td>00000</td><td>00000</td><td>0OOOOO</td><td>Transmission (automatic)</td><td></td></tr><tr><td>00000</td><td></td><td>000000</td><td>Trouble Index</td><td></td><td rowspan="2">00000 0000 OOOOO</td></tr><tr><td>O••••</td><td>00000</td><td>00000</td><td></td><td>0O</td></tr></table>

## Conclusion

Well-designed small multiples are

inevitably comparative

deftly multivariate

shrunken, high-density graphics

usually based on a large data matrix

drawn almost entirely with data-ink

efficient in interpretation

often narrative in content, showing shifts in the relationship between variables as the index variable changes (thereby revealing interaction or multiplicative effects).

Small ultpl rf muc te heory a h:

For data-ink, less is a bore.6

For non-data-ink, less is more.

6 The two aphorisms on the meaning of "less" are, respectively, credited to Ludwig Mies van der Rohe and to Robert Venturi, Complexity and Contradiction in Architecture (New York, second edition, 1977), p. 17.

<table><tr><td rowspan=1 colspan=10>CarteFigurae des pecteosuccsivo e homs alaame qu Onnibal conduidiepagne                 Legende.en Oralie en KraversamSes Gaules (sdon Lolybe ).Oresie pa M. OMinard, Supedn Geniral s Lonts hauiss jdaite<img src="images/db8f4bf80d431bdf58d36c40917fe8548902ae7832e9771b6e6c1b45aef57639.jpg"/></td></tr><tr><td rowspan=1 colspan=10>Carte Figurative des peto sucesive mbommeo de l&#x27;Cemic Fangaise ans la campagne  Russie 1812-A813.                            MOSCOCaes zons. Se ouge disiguelo bomume quiventienn Ruosi; le non cena ui m sortomSo rensiguement qui om seri i dreree la cate m ite quise C F C   L    Mhil O Wd,    Looc                           Polotrk8                                                                                                                         Moljarvorlia.c                                     ABeirin                    Orpr0090002          Heo             BolrShMohilowinsk</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>TABLEAU CRAPH</td><td rowspan=1 colspan=1>UE </td><td rowspan=1 colspan=1>a températn</td><td rowspan=1 colspan=1>c en desres </td><td rowspan=1 colspan=1>thermometre de caumur a dessous</td><td rowspan=1 colspan=2>e zéro.</td><td rowspan=4 colspan=1>ek s8</td></tr><tr><td rowspan=3 colspan=10>LesCasaqus pent aglople Nikmen geli.                                                     -1.- 21.1e14- 26.1e X          -30^1e6x^{}}$</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td></tr></table>

Aug,yo Ragnier, 2.Par.5" Karie 5 0t &Pari.

## 9 Aesthetics and Technique in Data Graphical Design

Along with the amazing graphic of the French losses in the Russiar invasion, Minard includes a second "Carte Figurative." It portrays Hannibal's fading elephant campaign in Spain, Gaul, and Northern Italy. Minard uses a light transparent color for flow-lines, allowing the underlying type to show through. This refined use of color to depict more information contrasts with the garish tones too often seen in modern graphics.

Charles Joseph Minard, Tableaux Graphiques et Cartes Figuratives de M. Minard, 1845-1869, a portfolio of his work held by the Bibliothèque de I'École Nationale des Ponts et Chaussées, Paris.

What makes for such graphical elegance? What accounts for the quality of Minard's graphics, of those of Playfair and Marey, and of some recent work, such as the new view of the galaxies? Good design has two key elements:

Graphical elegance is often found in simplicity of design and complexity of data.

Visually attractive graphics also gather power from content and interpretations beyond the immediate display of some numbers. The best graphics are about the useful and important, about life and death, about the universe. Beautiful graphics do not traffic with the trivial.

On rare occasions graphical architecture combines with the data content to yield a uniquely spectacular graphic. Such performances can be described and admired but there are no easy compositional principles on how to create that one wonderful graphic in millions. As Barnett Newman once said, "Aesthetics is for the artist like ornithology is for the birds."

What can be suggested, though, are some guides for enhancing the visual quality of routine, workaday designs. Attractive displays of statistical information

have a properly chosen format and design

use words, numbers, and drawing together

•reflect a balance, a proportion, a sense of relevant scale

display an accessible complexity of detail

oten have a narrative quality, a story to tell about the data

are drawn in a professional manner, with the technical details of production done with care

avoid content-free decoration, including chartjunk.

The Choice of Design: Sentences, Text-Tables, Tables, Semi-Graphics, and Graphics

The substantive content, extensiveness of labels, and volume and ordering of data all help determine the choice of method for the display of quantitative materials. The basic structures for showing data are the sentence, the table, and the graphic. Often two or three of these devices should be combined.

The conventional sentence is a poor way to show more than two numbers because it prevents comparisons within the data. The linearly organized flow of words, folded over at arbitrary points (decided not by content but by the happenstance of column width), offers less than one effective dimension for organizing the data. Instead of:

Nearly 53 percent of the type A group did something or other compared to 46 percent of B and slightly more than 57percentofC.

Arrange the type to facilitate comparisons, as in this text-table:

<table><tr><td>The three groups differed in how they did something or other:</td></tr><tr><td>Group A 53%</td></tr><tr><td>Group B 46%</td></tr><tr><td>Group C 57%</td></tr></table>

There are nearly always better sequences than alphabetical-for example, ordering by content or by data values:

<table><tr><td>Group B</td><td>46%</td></tr><tr><td>Group A</td><td>53%</td></tr><tr><td>Group C</td><td>$7%</td></tr></table>

Tables are clearly the best way to show exact numerical values, although the entries can also be arranged in semi-graphical form. Tables are preferable to graphics for many small data sets.1 A table is nearly always better than a dumb pie chart; the only worse design than a pie chart is several of them, for then the viewer is asked to compare quantities located in spatial disarray both within and between pies, as in this heavily encoded example from an atlas. Given their low data-density and failure to order numbers along a visual dimension, pie charts should never be used.2

![](images/c7957163b63bac8ace0d7147cfe76aeda07c474db043870afb2fa3dcac62616b.jpg)  
Department of Surveys, Ministry of Labour, Atlas of Israel (Jerusalem, 1956), vol. 8, p. 8.

1 On the design of tables, see A.S.C. Ehrenberg, "Rudiments of Numeracy," Journal of the Royal Statistical Society, A, 140 (1977), 277297.

Tables also work well when the data presentation requires many localized comparisons. In this 410-number table that I designed for the New York Times to show how different people voted in presidential elections in the United States, comparisons between the elections of 1980 and 1976 are read across each line; within-election analysis is conducted by reading downward in the clusters of three to seven lines. The horizontal rules divide the data into topical paragraphs; the rows are ordered so as to tell an ordered story about the elections. This type of elaborate table, a supertable, is likely to attract and intrigue readers through its organized, sequential detail and reference-like quality. One supertable is far better than a hundred little bar charts.

## How Different Groups Voted for President

Based on 12,782 interviews with voters at their polling places. Shown is how each group divided its vote for President and, in parentheses, the percentage of the electorate belonging to each group.

<table><tr><td></td><td>CARTER</td><td>REAGAN ANDERSON</td><td>in 1976</td></tr><tr><td>Democrats (43%)</td><td></td><td>$34</td><td>$12rac{2$</td></tr><tr><td></td><td>30 </td><td></td><td>77-22 43-54</td></tr><tr><td>Independents (23%) Republicans (28%)</td><td>13</td><td>84 4</td><td>9-90</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>Liberals (17%)</td><td>57</td><td>27 11</td><td>70·26</td></tr><tr><td>Moderates (46%)</td><td>42</td><td>48 8 71</td><td>51-48</td></tr><tr><td>Conservatives (28%)</td><td>23</td><td>4</td><td>29-70</td></tr><tr><td>Liberal Democrats (9%)</td><td>70</td><td>14 13</td><td>86 -12</td></tr><tr><td>Moderate Democrats (22%)</td><td>66 28</td><td>6</td><td>77-22</td></tr><tr><td>Conservative Democrats (8%)</td><td>53 41</td><td> ∞</td><td>64 -35</td></tr><tr><td>Polticallyactiv Dt %)</td><td>72 19</td><td></td><td>—</td></tr><tr><td>Democrats favoring Kennedy</td><td>24</td><td></td><td></td></tr><tr><td>in primaries (13%)</td><td>66</td><td>8</td><td></td></tr><tr><td>Liberal Independents (4%)</td><td>$29</td><td>$1\fc{ $</td><td>64-29</td></tr><tr><td>Moderate ndependents (12%)</td><td></td><td></td><td>45-53</td></tr><tr><td>Conservative ndependents (%)</td><td>69</td><td>6</td><td>2672</td></tr><tr><td>Liberal Republicans (2%)</td><td>25 66</td><td>O IDN</td><td>17-82</td></tr><tr><td>Moderate Republicans 11%)</td><td>13 81</td><td></td><td>11-88</td></tr><tr><td>Conserativ Republicans 2%)</td><td>6 91</td><td></td><td>6-93</td></tr><tr><td>i %</td><td>5 89</td><td></td><td></td></tr><tr><td>East (32%)</td><td>43 47</td><td></td><td>51-47</td></tr><tr><td>South (27%)</td><td>44 51</td><td>∞M</td><td>54-45</td></tr><tr><td>Midwest ((20%)</td><td>41 51</td><td></td><td>48·50</td></tr><tr><td>Wt(11%)</td><td>35 52</td><td>10</td><td>46-51</td></tr><tr><td>Blacks (10%)</td><td>82</td><td>14</td><td>82-16</td></tr><tr><td>Hispanics (2%)</td><td>30 6</td><td>3 36</td><td>755- 24</td></tr><tr><td>Wtes(88%)</td><td></td><td>55 8</td><td>47-52</td></tr><tr><td>Female (49%)</td><td>$3\frac{ }$</td><td>46</td><td>50 - 48</td></tr><tr><td>Male M(51%)</td><td></td><td>~</td><td>50 - 48</td></tr><tr><td>Femae, os equ </td><td></td><td>54</td><td></td></tr><tr><td>amendment (22%)</td><td>54</td><td>32 11</td><td>−</td></tr><tr><td>Female,oses equal hts amendment (15%)</td><td>29 66</td><td>4</td><td></td></tr><tr><td></td><td></td><td></td><td>—</td></tr><tr><td>Catholic (25%) Jewish (5%)</td><td>40 51</td><td>7</td><td>54-44</td></tr><tr><td>Protestant (46%)</td><td></td><td>39 14</td><td>64-34</td></tr><tr><td>Born-again hite Protestant%)</td><td>$3frac }$</td><td>56 0 61</td><td>44.555</td></tr><tr><td></td><td>43</td><td></td><td>-</td></tr><tr><td>18 -21 years old (6%) 22 -29 years old (17%)</td><td>44 43</td><td>11</td><td>48-50 51-46</td></tr><tr><td>30 44 years old (31%)</td><td>43</td><td>11</td><td>49-49</td></tr><tr><td>45 -59 years old (23%)</td><td>37</td><td>54 7</td><td></td></tr><tr><td>60 years or older (18%)</td><td>40 </td><td>$54 0</td><td>47-52</td></tr><tr><td></td><td></td><td></td><td>47-52</td></tr><tr><td>Family income Less than $10,000 (13%)</td><td>41</td><td></td><td>58·40</td></tr><tr><td>$10,000 -$14,999 (14%)</td><td>50</td><td>6</td><td></td></tr><tr><td>$15,000 - $24,999 (30%)</td><td>47</td><td>42 ∞</td><td>55 - 43</td></tr><tr><td>$25,000 - $50,000 (24%)</td><td>38</td><td>53 58</td><td>48.50</td></tr><tr><td>Over $50,000 (5%)</td><td>32 25 65</td><td>8 8</td><td>36-62 </td></tr><tr><td></td><td>56</td><td></td><td></td></tr><tr><td>Professional omanager 40%) Clerical, sales or other</td><td>33</td><td>9</td><td>41·57</td></tr><tr><td>white-collar (11%)</td><td></td><td></td><td></td></tr><tr><td>Blue-collar worker (17%)</td><td>42 46</td><td>48 ∞ M 47</td><td>46-53 57-41</td></tr><tr><td>Agriculture (3%)</td><td>29 35 </td><td></td><td></td></tr><tr><td>Looking for work (3%)</td><td>55</td><td></td><td>65-34</td></tr><tr><td>Education</td><td></td><td></td><td></td></tr><tr><td>High school or less (39%)</td><td></td><td></td><td>57 - 43</td></tr><tr><td>Some college (28%) College graduate (27%)</td><td></td><td>48 ∞ 55</td><td>51-49</td></tr><tr><td></td><td></td><td>51 11</td><td>45-55</td></tr><tr><td>Labor union household (26%)</td><td>47 44</td><td>∞</td><td>59-39</td></tr><tr><td>No member household in union (62%)</td><td>35</td><td>55</td><td>43-55</td></tr><tr><td>Family finances</td><td></td><td></td><td></td></tr><tr><td>Betye g%</td><td></td><td>37</td><td>30 -70</td></tr><tr><td>Same (40%) Worseoff thn a year go (34%)</td><td></td><td>∞∞ 46 64</td><td>51-49</td></tr><tr><td></td><td>25</td><td></td><td>77-23</td></tr><tr><td>Fiy Democrats, better off</td><td></td><td></td><td></td></tr><tr><td>than a year ago (7%)</td><td></td><td></td><td></td></tr><tr><td>Democrats, worse off</td><td>77</td><td>16 6</td><td>69-31</td></tr><tr><td>than a year ago (13%)</td><td>47</td><td>39 10</td><td>94-6</td></tr><tr><td>Independents, better f (%)</td><td>45 36</td><td>12</td><td></td></tr><tr><td>dependentsworse of (9%)</td><td>21 65</td><td>11</td><td></td></tr><tr><td>Republicans, tt% Republicans, worse off (11%)</td><td>18</td><td>77 4</td><td>3-97</td></tr><tr><td></td><td>6</td><td>89</td><td>24.76</td></tr><tr><td>More important problem Unemployment (39%)</td><td></td><td></td><td>75 -25</td></tr><tr><td>Inflation (44%)</td><td>30 </td><td>40 0</td><td>35-65</td></tr><tr><td>e U..</td><td></td><td>60</td><td></td></tr><tr><td>dealing with Soviet Union evenould</td><td></td><td></td><td></td></tr><tr><td>s th is fr 5%</td><td></td><td>32 6</td><td>vee</td></tr><tr><td>Disagree (31%)</td><td>50 </td><td>10</td><td>—</td></tr><tr><td>Favor equal rights amendment (46%)</td><td></td><td>38 11</td><td>—</td></tr><tr><td>Oppose equal rights amendment (35%)</td><td>$20rac66$</td><td>68 4</td><td></td></tr><tr><td>When decided about choice</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>Knew all along (41%)</td><td>47</td><td>50 2 60 ∞</td><td>44 ·55 57·42</td></tr><tr><td>During the primaries (13%) During conventions (8%)</td><td>30</td></table>

For sets of highly labeled numbers, a wordy data graphic— coming close to straight text—works well. This table of numbers is nicely organized into a graphic:

![](images/4e494a4aa4c9342f51bd4815383cf7ba5e3e93121b8d17cf2e82669566fce1c1.jpg)  
New York Times, January 2, 1979, p. D-3.

## Making Complexity Accessible: Combining Words, Numbers, and Pictures

Explanations that give access to the richness of the data make graphics more attractive to the viewer. Words and pictures are sometimes jurisdictional enemies, as artists feud with writers for scarce space. An unfortunate legacy of these craft-union differences is the artificial separation of words and pictures; a few style sheets even forbid printing on graphics. What has gone wrong is that the techniques of production instead of the information conveyed have been given precedence.

Words and pictures belong together. Viewers need the help that words can provide. Words on graphics are data-ink, making effective use of the space freed up by erasing redundant and nondata-ink. It is nearly always helpful to write little messages on the plotting field to explain the data, to label outliers and interesting data points, to write equations and sometimes tables on the graphic itself, and to integrate the caption and legend into the design so that the eye is not required to dart back and forth between textual material and the graphic. (The size of type on and around graphics can be quite small, since the phrases and sentences are usually not too long-and therefore the small type will not fatigue viewers the way it does in lengthy texts.)

The principle of data /text integration is

Data graphics are paragraphs about data and should be treated as such.

Words, graphics, and tables are different mechanisms with but a single purpose—the presentation of information. Why should the flow of information be broken up into different places on the page because the information is packaged one way or another? Sometimes it may be useful to have multiple story-lines or multiple levels of presentation, but that should be a deliberate design jugment, not something decided by conventional production requirements. Imagine if graphics were replaced by paragraphs of words and those paragraphs scattered over the pages out of sequence with the rest of the text—that is how graphical and tabular information is now treated in the layout of many published pages, particularly in scientific journals and professional books.

Tables and graphics should be run into the text whenever possible, avoiding the clumsy and diverting segregation of "See Fig. 2," (figures all too often located on the back of the adjacent page).3 If a display is discussed in various parts of the text, it might well be printed afresh near each reference to it, perhaps in reduced size in later showings. The principle of text/graphic/table integration also suggests that the same typeface be used for text and graphic and, further, that ruled lines separating different types of information be avoided. Albert Biderman notes that illustrations were once well-integrated with text in scientific manuscripts, such as those of Newton and Leonardo da Vinci, but that statistical graphics became segregated from text and table as printing technology developed:

The evolution of graphic methods as an element of the scientific enterprise has been handicapped by their adjunctive, segregated, and marginal position. The exigencies of typography that moved graphics to a segregated position in the printed work have in the past contributed to their intellectual segregation and marginality as well. There was a corresponding organizational segregation, with decisions on graphics often passing out of the hands of the original analyst and communicator into those of graphic specialists--the commercial artists and designers of graphic departments and audio-visual aids shops, for example, whose predilections and skills are usually more those of cosmeticians and merchandisers than of scientific analysts and communicators.4

3 "Fig.," often used to refer to graphics, is an ugly abbreviation and is not worth the two spaces saved.

4 Albert D. Biderman, "The Graph as a Victim of Adverse Discrimination and Segregation," Information Design Journal, 1 (1980),238.

Page after page of Leonardo's manuscripts have a gentle but thorough integration of text and figure, a quality rarely seen in modern work:

:234.

Leonardo da Vinci, Treatise on Painting [Codex Urbinas Latinus 1270], vol. 2, facsimile (Princeton, 1956), p. 234, paragraph 827.

chevai le cosc ucdutt ciere ranro miaime che noche le membva ma il tuto guasi tipara impossibile a potev figuvare Come selfocchio fussc.o, c'la busa dun guavto di braccio cguak alla tua tauola dipintv sia,a br disosta.m n. dal 'ochio mezo Gvaccio allova tu ucdrai per esospacio tutte le cose che 6 a. weder si posffi demivo alla lungheta .o. dnns orizonte di cento miglia in tanca confusa diminuttione chens che figurar di guelle alcuna pavte chabbia figutra ma apena potrai porve si piccolo punto di pencllo che non sia maggione chogm gran'casamento posto in dia migla di distantia

Perche li moni in longha dintantial si dimostramo pin saun nolla cima che mlla basa -

lovo basa o nella uicimita che nella vemotione, Pro nasi,s. p.,d.s,.C, V. a.k, sano gradi delbawia cherempve sasoriglian guano pin s'inalzans, a f. f. h., h.k. sono G alivi gradi transursal dore Caria agista

Finally, a caveat: the use of words and pictures together requires a special sensitivity to the purpose of the design-in particular, whether the graphic is primarily for communication and illustration of a settled finding or, in contrast, for the exploration of a data set. Words on and around graphics are highly effective— sometimes all too effective—in telling viewers how to allocate their attention to the various parts of the data display.5 Thus, for graphics in exploratory data analysis, words should tell the viewer how to read the design (if it is a technically complex arrangement) and not what to read in terms of content.

5 Experiments in visual perception indicate that word instructions substantially determine eye movements in viewing pictures. See John D. Gould, "Looking at Pictures," in Richard A. Monty and John W. Senders, eds., Eye Movements and Psychological Processes (Hillsdale, N.J., 1976), 323343.

## Accessible Complexity: The Friendly Data Graphic

An occasional data graphic displays such care in design that it is particularly accessible and open to the eye, as if the designer had the viewer in mind at every turn while constructing the graphic. This is the friendly data graphic.

There are many specific differences between friendly and unfriendly graphics:

<table><tr><td>Friendly</td><td>Unfriendly</td></tr><tr><td>words are spelled out, mysterious and elaborate encoding avoided</td><td>abbreviations abound, requiring the viewer to sort through text to decode abbreviations</td></tr><tr><td>words run from left to right, the usual direction for reading occidental languages</td><td>words run vertically, particularly along the Y-axis; words run in several different directions</td></tr><tr><td>little messages help explain data</td><td>graphic is cryptic, requires repeated references to scattered text</td></tr><tr><td>elaborately cncoded shadings, cross- hatching, and colors are avoided; instead, labels are placed on the graphic itself; no legend is required</td><td>obscure codings require going back and forth between legend and graphic</td></tr><tr><td>graphic attracts viewer, provokes curiosity</td><td>graphic is repellent, filled with chartjunk</td></tr><tr><td>colors, if used, are chosen so that the color-deficient and color-blind (5 to 10 percent of viewers) can make sense of the graphic (blue can be distin- guished from other colors by most</td><td>design insensitive to color-deficient viewers; red and green used for essential contrasts</td></tr><tr><td>color-deficient people) type is clear, precise, modest; lettering may be done by hand</td><td>type is clotted, overbearing</td></tr><tr><td>type is upper-and-lower case, with serifs</td><td>type is all capitals, sans serif</td></tr></table>

## With regard to typography, Josef Albers writes:

The concept that "the simpler the form of a letter the simpler its reading" was an obsession of beginning constructivism. It became something like a dogma, and is still followed by "modernistic" typographers. . . . Ophthalmology has disclosed that the more the letters are differentiated from each other, the easier is the reading. Without going into comparisons and details, it should be realized that words consisting of only capital letters present the most difficult reading—because of their equal height, equal volume, and, with most, their equal width. When comparing serif letters with sans-serif, the latter provide an uneasy reading. The fashionable preference for sans-serif in text shows neither historical nor practical competence.6

6Josef Albers, Interaction of Color (New Haven, 1963, revised edition 1975), p. 4.

## Proportion and Scale: Line Weight and Lettering

Graphical elements look better together when their relative proportions are in balance. An integrated quality, an appropriate visual linkage between the various elements, results. This musical score of Karlheinz Stockhausen exhibits such a visual balance:

Karlheinz Stockhausen, Texte, vol. 2 (Cologne, 1964), p. 82, from the score $\cot ^ { \ast } z _ { \mathrm { y } } ^ { \bar { \mathrm { y } } }$ klus für einen Schlagzeuger."

![](images/500ec661586f7645624c65bf1fbef33040d8d34631381aacdcb1964f9eff8460.jpg)

In contrast, this next desig is heavy handed, with neary every element out of balance: the clotted ink, the poor style of lettering, the puffed-up display of a small data set, the coarse texture of the entire graphic, and the mismatch between drawing and surrounding text:

![](images/bd401517a75e1fda0b0d6c15be0ebe733ac3cb5d24c580b0874d2d89a29237b1.jpg)

Edward R. Tufte, "The Relationship Between Seats and Votes in Two-Party Systems," American Political Science Review, 67 (June 1973), 551.

Lines in data graphics should be thin. One reason eighteenthand nineteenth-century graphics look so good is that they were engraved on copper plates, with a characteristic hair-thin line. The drafting pens of twentieth-century mechanical drawing thickened linework, making it clumsy and unattractive.

An effective aesthetic device is the orthogonal intersection of lines of different weights:

![](images/6c9c20e911f314071a313960d0feaf4c0102a196601ebdb23d3d407beaf13fb5.jpg)

Poster for the exhibition "Mondrian and Neo-Plasticism in America," Yale University Art Gallery, October 18 to December 2, 1979. The original painting was done in 1941 by Diller; see Nancy J. Troy, Mondrian and Neo-Plasticism in America (New Haven, 1979), p. 28.

Nearly every intersection of the lines in this design (based on a painting by Burgoyne Diller) involves lines of differing weights, and it makes a difference, for the painting's character is diluted with lines of constant width:

![](images/ce48c107f4fe82b13390d242656336515d792a04aa45df480575b7ed287813c6.jpg)

![](images/cb5122acbb043d78b0b5af7ad9051a2d754d7e2eb8ff83f02d82f16777fcbd21.jpg)

Likewise, data graphics can be enhanced by the perpendicular intersections of lines of differing weights. The heavier line should be a data measure. In a time-series, for example:

![](images/b3b63326920007e9c6d11b9256adf030134989f26859fd70d9b68a4cdec0918d.jpg)  
The contrast in line weight represents contrast in meaning. The greater meaning is given to the greater line weight; thus the data line should receive greater weight than the connecting verticals. The logic here is a restatement, in different language, of the principle of data-ink maximization.

## Proportion and Scale: The Shape of Graphics

Graphics should tend toward the horizontal, greater in length than height:

lesser height

Several eoigvororiznal ververtil dipys.

First, analogy to the horizon. Our eye is naturally practiced in detecting deviations from the horizon, and graphic design should take advantage of this fact. Horizontally stretched time-series are more accessible to the eye:

![](images/836356e60fe91c9c2bc55231d871a6d674eb3143cd20fab95c8cec2aa0fb58a6.jpg)

![](images/c9790dd6caf6dc21a7be7196c7efbc7505d7a6bcdf55af4276be686090b27f21.jpg)

The analogy to the horizon also suggests that a shaded, high contrast display might occasionally be better than the floating snake. The shading should be calm, without moiré effects.

Second, ease of labeling. It is easier to write and to read words that read from left to right on a horizontally stretched plottingfield:

![](images/12f7db55d29cc01b3b1ae27b2817c5f68a3ac945bda0b5429a0f0c98de1ffd52.jpg)

T  o

![](images/668e4456755997b7dbf6d97c6f89bdd40482cf1d8c1d4aadcd6191ac19cf87ca.jpg)

and a longer horizontal helps to elaborate the workings of the causal variable in more detail.

Fourth, Tukey's counsel.

Most diagnostic plots involve either a more or less definite dependence that bobbles around a lot, or a point spatter. Such plots are rather more often better made wider than tall. Widerthan-tall shapes usually make it easier for the eye to follow from left to right.

7John W. Tukey, Exploratory Data Analysis (Reading, Mass., 1977), p. 129.

Perhaps the most general guidance we can offer is that smoothly-changing curves can stand being taller than wide, but a wiggly curve needs to be wider than tall. . . .7

And, finally, Playfair's example. Of the 89 graphics in six different books by William Playfair, most (92 percent) are wider than tall. Several of the exceptions are his skyrocketing government debt displays. This plot shows the dimensions of each of those 89 graphics:

![](images/4f20b60bf6844dc5fe771f3817541119c21aef5211379a117ddccdc120299a58.jpg)

If graphics should tend toward the horizontal rather than the vertical, then how much so? A venerable (fifth-century B.c.) but dubious rule of aesthetic proportion is the Golden Section, a "divine division" of a line.8 A length is divided such that the smaller is to the greater part as the greater is to the whole:

8 The combination of geometry and mysticism surrounding the Golden Rectangle can be seen in Miloutine Borissavlièvitch, The Golden Number and the Scientific Aesthetics of Architecture (New York, 1958) and Tons Brunés, The Secrets of Ancient Geometry (Copenhagen, 1967), vols. 1 and 2.

$$
{ \frac { \mathsf { a } } { \mathsf { b } } } = { \frac { \mathsf { b } } { \mathsf { a } + { \mathsf { b } } } }
$$

Solving the quadratic when a = 1 yields ${ \mathfrak { b } } = { \frac { { \sqrt { 5 } } + 1 } { 2 } } = { \mathfrak { r } } . 6 1 8 \dots .$

In turn the Golden Rectangle is

![](images/c1b619db5f54a871f2d447fa45624e01100b8c2e122c750194b2e99f05353541.jpg)

The nice geometry of the Golden Rectangle is not unique; Birkhoff points out that at least five other rectangles (including the square) have one simple mathematical property or another for which aesthetic claims might be made:9

9George D. Birkhoff, Aesthetic Measure (Cambridge, 1933), pp. 2730.

![](images/b45025dce974727fb8d7f483595b023ca30e6d49fba94a7b98f394101e054604.jpg)

Playfair favored proportions between 1.4 and 1.8 in about twothirds of his published graphics, with most of the exceptions moving more toward the horizontal than the golden prescription:

![](images/c5a065cde6156dad45d7f915431d2e7421d209f8f1c1ad99a1dbb558cc2b8aab.jpg)

Visual preferences for rectangular proportions have been studied by psychologists since 186o, but, even given the implausible assumption that such studies are relevant to graphic design, the findings are hardly decisive. A mild preference for proportions near to the Golden Rectangle is found among those taking part in the experiments, but the preferred height/length ratios also vary a great deal, ranging between

![](images/7d251eee35fe274be02ac48ed8681705874674b70e18804b8e938f813e824948.jpg)

![](images/710309ffa450c5250b1f9afbfad0dba52738425d8bd31a158987b809d66fdb56.jpg)

And, as is nearly always the case in experiments in graphical perception, viewer responses were found to be highly contextdependent.10

The conclusions:

10I have relied on Leonard Zusne, Visual Perception of Form (New York, 1970), ch. 10, for a summary of the immense literature.

I follow that suggestion.

Otherwise, move toward horizontal graphics about o percent wider than tall:

![](images/afd42124a49e3fb09234ad8d57324d00ed00642e33e0b366158274707f553e45.jpg)

Design is choice. The theory of the visual display of quantitative information consists of principles that generate design options and that guide choices among options. The principles should not be applied rigidly or in a peevish spirit; they are not logically or mathematically certain; and it is better to violate any principle than to place graceless or inelegant marks on paper. Most principles of design should be greeted with some skepticism, for word authority can dominate our vision, and we may come to see only through the lenses of word authority rather than with our own eyes. What is to be sought in designs for the display of information is the clear portrayal of complexity. Not the complication of the simple; rather the task of the designer is to give visual access to the subtle and the difficult—that is,

Epilogue: Designs for the Display of Information

the revelation of the complex.

Index

aesthetics, graphical 177191

air pollution 42, 170

Boutique Data Graphics 118

Bowen, William G. 95

constant dollars 65-68

Akahata ("Red Flag"83

box plot 97, 123, 129

Consumer Reports 80, 174

Albers, Josef 183

context 74-75

Brier, Stephen S. 14

Converse, Philip E. 147

Alder, Berni 134, 145

Brinton, Willard C. 112

American Education 118

copper, conductivity of 49

Brown, Denise Scott 116117

American Political Science Review 167

Brunés, Tons 189

Cornford, Eain M. 109

Annuaire Statistique de la France 167

Bryan, Kirk 99

Cosmographia 22

Anscombe, F. J. 14

Business Week 63, 83, 167

county maps 1620, 153

Anscombe's quartet 13-14

Cox, Michael D. 99

area and quantity 6973

Arkin, Herbert 112

Crotty, William J. 95

Asahi 83, 167, 168

calculus 9

Asch, S. E. 56

calculus, graphical 46

astronomical graphics 2629, 154, 166

California Water Atlas 119

Ayres, Leonard P. 141, 155

Campbell, Angus 147

Ayres, Richard E. 95

Campbell, Donald T. 75

cancer 1620, 47, 171

Bamburger, Clara Francis 82

Bancroft, T. A. 53,140

cancer maps 1620, 121

bar chart 9697, 126128, 129

Barabba, Vincent P. 153

Barnett, Vic 114, 168

Cappon, Lester J. 146

cars, frequency of repair 174

before-after time-series 39

Curti, Merle 85

Beniger, James R. 20, 86

'Big Duck' 116, 117

Cartesian coordinates 9

Biochemistry 110

Bertin, Jacques 112, 166, 169, 178

bilateral symmetry 97

Bickmore, D. P. 162

cause and effect 37, 47, 82, 187

Birkhoff, George D. 189

blot maps 20, 139

Biderman, Albert D. 181

chemical elements 102-105

CEM 56

chartjunk 107-121

Biochimica et Biophysica Acta 110

Chavannes, E. 21

Blot, William J. 16

Bonner, John Tyler 94

Chernoff faces 97, 142

Chernoff, Herman 136, 142

boring statistics 7980, 87

Cheysson, É. 154

chicken, 4,340-pound 73

Cleveland, William S. 38, 168

cholera map 24

chromosomes 172-173

color 153154, 183

Borissavlièvitch, Miloutine 189

color-deficient viewers 183

Colton, Raymond R. 112

computer graphics 2627, 29, 42, 112,

116, 120121, 136, 153, 170

Connecticut speeding 74-75

Dahl, Robert A. 85

Dakin, Edwin F. 15

Daniel, Cuthbert 133

data-based grid 148

data-based labels 149152

data-built data-measures 139-144

data density 161-169

data-ink 91-105

data-ink maximization 96105, 123137, 175, 186, 187

data-ink ratio 93-96

data maps 1627

data matrix 167-169

data measures 139-144

data/text integration 180-182

data variation 6061

Davis, John C. 162

Day Mines, Inc. 54

decoder, visual 153154

deflating money 65-68

Der Spiegel 83

design variation 6063

Dewey, Edward R. 15

Die Zeit 83

Diller, Burgoyne 185

distortion, graphical 55-59

dogs so

Doll, R. 47, 82

gray shades 154

Kolers, Paul A. 79

dollars, constant 6568

grids 112-116

Kooi, Kenneth 93

dot-dash-plot 133, 136, 139, 152

grids, data-based 145148

Kouchoukos, Nicholas 109

double-functioning labels 149-152

grids, gray 116

Kuznicki, James T. 100, 109

Duchamp, Marcel 36

grids, white 127-129, 136

ducks116-121

Groth, Edward J. 26

labels on graphics 180182, 183, 187

Gurnett, Donald A. 29

'Easter Wings'143

Lambert, Johann Heinrich 29, 32, 45-46

economic data 15, 3234, 38, 54-55, 6168, 70, 9192, 108, 126, 148, 152, 158, 161, 180

half-face 97, 136

Lancet 110

Halley, Edmond 23

Hankins, Timothy H. 134

lane stripes 144

Larsen, Wayne A. 129

The Economist 63, 83, 167

Hannibal's campaign 176177

Lauer, A. R. 144

educational tests, graphics86

Hayward, Roger 102, 136

Ehrenberg, A. S. C. 178

Herbert, George 143

Law School Admission Test, graphics 86

election graphics 147, 179

Herdeg, Walter 80, 152

Learning from Las Vegas 116117

electroencephalogram 93

herring catches 172

Leonardo da Vinci 181-182

elegance, graphical 177

hierarchy in graphics 153-159

less is a bore 175

Eliot, T. S. 100

high-information graphics 168-169

less is more 175

encodings 178, 183

Hilgard, Emest 85

lettering 184

erasing principles 96100, 136

histogram 126-128

Lie Factor 57

Erbring, Lutz 120

histogram, living 140

lies, defense of 7677

excellence, graphical 13-51

Hjort, Johan 172

Liley, P. E. 49,150

Ho, C. Y. 49, 150

line weight 185

Hoover, Robert 16

living histogram 140

Fienberg, Stephen E. 14

horizon, analogy to 186187

Long, John Hamilton 146

'Fig.' 181

horse paces 34-35

Los Angeles smog 42, 170

Finkner, Alva L. 153

House of Representatives 37

Los Angeles Times 42, 69

Fiorina, Morris 66

Huot, Marie E. 109

lung cancer 1620, 47

Fisher, R. A.133

lying graphics 7677

Flanigan, William H. 85

identification numbers 149150

Flury, Bernhard 97

Israel, Atlas of 178

Fortune 167

Macdonald-Ross, Michael 56

MacGregor, A. J. 112

Francolini, C. M. 153

Italian post office 72

Frankfurter Allgemeine 83

magnetic monopole 39

Izenour, Steven 117

Fraumeni, Joseph F. 16

mail, House of Representatives 37

French communes 166

Japan, graphics in university entrance exams 86

Malcolm, Andrew H. 84

French wine map 25-26

Manvel, Allen D. 81

friendly data graphics 183

map, blot 20, 139

fuel economy graphic 57-59

Japanese beetle 43, 121

map, cancer 1620

Japanese graphics 82-84

JASA style sheet 110, 150151, 164

Funkhouser, H. Gray 20, 28, 154

map, cholera 24

map, data 1627

Gabaglio, Antonio 72

Joiner, Brian L. 140

galaxies map 2627, 154, 166

Journal of the American Chemical Society 110

map, French wine 25-26

gecko 36

map, galaxies 2627, 154, 166

Geological Survey maps 168

Journal of American Medical Association 167

Gilbert, E. W. 24

map, Israel 178

Goldenberg, Edie N. 120

map, patch 20

map, thematic 1627

Journal of the American Statistical Association 110, 150151, 164, 167-168

Goodin, W. R. 170

map, Yü Chi Thu 2021

Gould, John D. 182

Marey, E. J. 31, 3436, 40, 115116, 121

Journal of Biological Chemistry 110

grade school graphics 86

Graphical Hack 59

government spending 64-68, 158

Mason, Thomas J. 16

Journal of Chemical Physics 110

gray grid 116

Masterton, William 85

Journal of the Royal Statistical Society 167

Graph of Magical Parallelepipeds 68

Matisse, Henri 160

Jupiter graphic 29

Kahrl, William L. 119

Kelley, Stanley 95

maximizing data-density 168

maximizing data-ink 96105, 123137, 175, 186, 187

McClenaghan, William 85

McCracken, Paul 48

parallel schematic plot 125

McCullagh, Michael J. 162

Satet, R. 69, 112

patch maps 20

Sato, Isao 82, 85

McCutcheon, N. Bruce 100, 109

Pauling, Linus 85, 102

Scarf, F. L. 29

McGill, Robert 129

Pearson, Karl 145

scatterplot 130-135

McKay, Frank W. 16

Peebles, P. James E. 26

Schlee, Susan 172

McRae, Gregory J. 42, 170

periodicity of elements 102-105

Schmid, Calvin F. 112

Meihoefer, H. J. 56

perpendicular lines 185-186

Schmid, Stanton E. 112

melanoma 171

Petchenik, Barbara Bartz 146

Science 39, 83, 109, 110, 167, 173

Mies van der Rohe, Ludwig 175

Phillips curve 48

Science Indicators, 1974 60

Miller, Arthur H. 120

pie chart 178

Scientific American 50, 73, 167

Miller, Warren E. 147

Pittsburgh Civic Commission 55

sea-horse 36

Minard, Charles Joseph 2425, 39, 4041, 51, 121, 176177

Playfair, William 9, 3234, 4345, 52, 6465, 73, 9192, 126, 148, 188189

Seinfeld, J. H. 170

Mitchell, H. L. 50

Seldner, Michael 26

population density map 155-157

semi-graphics 178-180

moiré vibration 107-112

Potter, D. E. 145

Senders, John W. 168, 182

Le Monde 83, 167

Powell, R. W. 49, 150

Shahn, Ben 177

Mondrian, Piet 185

Prakash, Om 172

shape, graphical 186-190

Monkhouse, F.J. 112, 165

Pravda 83, 167

Shinohara, Miyohei 82, 85

Monty, Richard A. 168, 182

Pravda School of Ordinal Graphics 76

Shiskin, Julius 38

Moore, Carol 152

presidential vote graphics 147, 179

Shrink Principle 169

Moscow, Napoleon's campaign 4041 121, 176177

press, graphical sophistication 8284

Shryock, Henry S. 113

mountain-to-the-sea 154

Proceedings of the National Academy of Sciences, U.S.A. 110

Siebers, B. H. 26

Siegel, Jacob S. 113

multifunctioning elements 139-159

Psychological Bulletin 167

Silverstein, Louis 80

multiple viewing angles 154-155

psychological experiments 55-56

Slowinski, Emil 85

multiple viewing depths 154155

Pugin 117

small multiple 42, 48, 170175

multiwindow plots 114, 171

puzzle graphics 153

smog 42, 170

Murphy, Edmond A. 172

Snow, Dr. John 24

Museum of Modern Art 91

quartile plot 124, 136, 139

Social Indicators, 1973 163

Napoleon's march 4041, 51, 121, 176177

sophistication, graphical 8286

range-frame 130, 136, 139, 149, 152

narrative graphics 40-43

Spear, Mary Eleanor 81, 112, 123

redundant data-ink 96100

starfish 36

National Science Foundation 60

Nature 110, 167

Reinhardt, Ad 122

Statistical Abstract of the United States 161, 167

Needham, Joseph 20

Reiss, Albert J. 14

relational graphics 43-50

New England Journal of Medicine 110, 167

stem-and-leaf plot 140

Rickett, Barney J. 134

Stockhausen, Karlheinz 184

Newman, Barnett 177

Rhône bridge 39

stock prices 15

Newman, L. Hugh 43

Riedwyl, Hans 97

Stokes, Donald E. 147

Newsweek 167

Riley, Bridget 108

Newton, Isaac 181

strangers 142

road stripes 144

Strunk, William 81

New York City weather 30, 121, 164

Roberts, K. V. 145

New York Times 30, 54, 57, 61, 66, 71, 76, 8083, 86, 121, 164, 167, 179, 180

Sunday Times (London) 63

Robinson, Arthur H. 20, 40

sunshine, British 165

Nihon Keizai 83

Robyn, Dorothy L. 20

Rogers, Anna C. 112

non-data-ink 96, 107

supertable 179

optical dots 114

Ross, H. Laurence 75

royalty, genealogy 34-35

Sypher, Wylie 139

Swift, Jonathan 106

Nude Descending a Staircase 36

outliers 142

ocean currents 99

orthogonal lines 185-186

rugplot 135, 136

optical art 107-108

table-graphic 145, 158159

oil prices 61-63

Ruskin, John 117

tables 56, 178180

Tanur, Judith 85

sampling error 172

sans serif 183

Sampson, Roy J. 85

television graphics 76, 81

SAS/CRAPH 112

Samuelson, Paul 85

Tell-A-Graf 112

Terpenning, Irma J. 38

textbooks 84-85

textbooks, statistical graphics 112

text-tables 178180   
Thissen, David 142   
Thomas, Edward Llewellyn 168   
Thomas, LaVerne 85   
Thompson, Morris M. 168   
Thrower, Norman J. W. 23   
Thurber, James 52   
tick marks 127129, 149   
Tilling, Laura 32, 4546   
Time 62, 71, 79, 83   
The Times (London) 83, 167   
time-series 28-39   
time-series, before-after 39   
Todd, Lewis Paul 85   
train schedule 31, 98, 115116, 121   
Troy, Nancy J. 185   
Tufte, Edward R. 29, 53, 75, 95, 184   
Tukey, John W. 53, 114, 123, 125,   
129, 136, 140, 168, 188   
Tukey, Paul A. 114, 168   
tungsten, conductivity of 150   
typography 178-183

The following illustrations are reprinted by permission: CHAPTER 1. Anscombe's quartet © 1973 American Statistical Association. Map of the galaxies, P. James E. Peebles, Princeton University. Radio emissions of Jupiter, Donald A. Gurnett, @ 1979 American Association for the Advancement of Science. New York City weather history @ 1981 The New York Times Company. Text on franked mail © 1975 The New York Times Company. Magnetic monopole © 1982 American Association for the Advancement of Science. Bridge on Rhône, Bibliothèque de l'École Nationale des Ponts et Chaussées. Los Angeles smog, by Bob Allen © 1979 The Los Angeles Times, based on data from Gregory J. McCrae, California Institute of Technology. Japanese beetle  1965 Aldus Books, London. Phillips curve, Organisation for Economic Cooperation and Development, Paris. Dogs © 1976 Scientific American, Inc. CHAPTER 2. Payments to travel agents © 1978 The New York Times Company. Drawing by CEM @ 1961 The New Yorker Magazine, Inc. Fuel economy standards © 1978 The New York Times Company. opEC oil prices © 1978 The New York Times Company. Oil prices @ 1979 Time, Inc. Oil prices 1979 The Washington Post. Real price of oil, Business Week, 1979 McGraw-Hill, Inc. Real price of oil @ 1979 The Sunday Times, London. Real price of oil © 1979 The Economist. Growth of government © 1977 Yale University Press. New York budget © 1976 The New York Times Company. Shrinking doctor, by Bob Allen and Pete Bentevoja, © 1979 The Los Angeles Times. Shrinking dollar @ 1978 The Washington Post. Picture of oil derricks @ 1981 The New York Times Company. CHAPTER 3. Views on economy © 198o The New York Times Company. Pace of city life @ 1976 The New York Times Company. CHAPTER 4. Electroencephalogram © 1971 Harper & Row. Generation time @ 1965 Princeton University Press. Registration rates © 1967 American Political Science Association. Registration rates @ 197o Addison-

Valéry, Paul 153   
Vasarely, Victor 108   
Vauthier, L. L. 154   
Venturi, Robert 117, 139, 175   
viewing architecture 159   
Wainer, Howard 79, 142, 153   
Waldrop, M. Mitchell 39   
Wall Street Journal 83, 167-168   
Washington Post 62, 70, 83   
White, E. B. 81   
white grid 127129, 136   
White, Jan 7980   
white pines 50   
Wilk, Martin B. 53   
Wilkinson, H. R. 112, 165   
Wilson, James Q. 85   
Wiskenmann, Arthur 171   
World War I graphic 141   
Wurman, Richard Saul 90   
Yajima, Yokichi 85   
Youden, W.J. 143   
Yü Chi Thu map 2021   
Yunis, Jorge J. 172   
Zeeman, E. C. 50   
Zingale, Nancy H. 85   
Zusne, Leonard 97, 190

Wesley Publishing Company. Registration rates @ 1970 Holt, Rinehart and Winston. Ocean currents, Kirk Bryan, Princeton University and the American Meteorological Society. Bar chart, taste experiment, James T. Kuznicki, Proctor & Gamble Company. Roger Hayward drawing of periodic properties of elements, Linus Pauling. CHAPTER 5. Vertical bars, glucose transfer, Eain M. Cornford, © 1981 American Association for the Advancement of Science. Multiwindow plot, Paul A. Tukey. Big Duck, Peter Blake. California crops, State of California, Office of Planning and Research. Newspaper content © 1979 American Political Science Association. CHAPTER 6. Parallel schematic plot © 1977 Addison-Wesley Publishing Company. Box plot variation @ 1978 American Statistical Association. Pulsar signals @ 1975 Academic Press. Empirical cumulative distribution © 1976 John Wiley. CHAPTER 7. Stem-and-leaf plot @ 1972 The Iowa State University Press. Living histogram, Brian Joiner. Magnetohydrodynamics © 1970 Academic Press. 1783 map © 1976 Princeton University Press. 1956 and 1960 elections © 1966 John Wiley. CHAPTER 8. French communes © 1973 Mouton and Gauthier-Villars. Bertin small multiple © 1973 Mouton and Gauthier-Villars. Melanoma © 1972 Springer-Verlag. Normal dis tributions © 1964 Pergamon Press, Ltd. Chromosomes, Jorge J. Yunis, © 1982 American Association for the Advancement of Science. Automobile frequency of repair @ 1982 Consumers Union of the United States, Inc. CHAPTER 9. How different groups voted for president © 198o The New York Times Company. Forecasting © 1979 The New York Times Company. Leonardo da Vinci drawing, facsimile @ 1956 Princeton University Press. Musical score, Karlheinz Stockhausen, © 1964 Verlag M. DuMont Schauberg. Seats-votes graph @ 1973 American Political Science Association. Poster illustration based on Burgoyne Diller, Geometrical Composition in Black, Red, and White, Yale University Art Gallery, Collection Société Anonyme.

# Acknowledgments, Second Edition

In preparing this new edition, I am grateful to Michael Arsenault, Michael and Winifred Bixler, Nicholas Cox, Inge Druckrey, Howard Gralla, Graham Larkin, MaryBeth Uryga, Carolyn Williams, and to GHP.

The wonderful staff of Graphics Press continues with their very special care: Kate Atkinson, Karen Bass, Cynthia Bill, Donna Karosi, Elaine Morse, Kathy Orlando, Peter Taylor, and Carolyn Williams.

January 2001

Cheshire, Connecticut

## Acknowledgments

I am indebted to many for their advice and assistance with this book.

For leave and research support during several academic years, the Center for Advanced Study in the Behavioral Sciences, the John Simon Guggenheim Foundation, the Woodrow Wilson School of Princeton University, and Yale University.

For providing access to their superb collections, the Bibliothèque Nationale and the Bibliothèque de l'École Nationale des Ponts et Chaussées in Paris, and, at Yale University, the Historical Medical Library and the Beinecke Rare Book and Manuscript Library.

For helping me appreciate the practicalities in the production of statistical graphics, several members of the art department at the New York Times and my students in Graphic Design and in the Department of Statistics at Yale.

For assistance in establishing Graphics Press, Peter B. Cooper, Earle E. Jacobs, Jr., and Trudy Putsche.

For design and artwork, Howard I. Gralla and Minoru Nijima. For their help and hospitality in Paris during my work on the Minard drawings, Michel Balinski, Jean Dubout, André Jammes, and Claudine Kleb.

For providing examples and for suggesting improvements in the manuscript, James Beniger, Inge Druckrey, Timothy Gregoire, Joanna Hitchcock, Joseph LaPalombara, Kathryn Scholle, Stephen Stigler, Howard Wainer, and Ellen Woodbury.

For their reviews of the manuscript and for their inspiration and encouragement through all the years of this enterprise, Frederick Mosteller and John W. Tukey.

June 1982 Cheshire, Connecticut