> 来源：The Visual Display of Quantitative Information (Edward R. Tufte)
> 原始文件：C:\Users\lenovo\Documents\Codex\2026-05-29\书籍专著\The Visual Display of Quantitative Information (Edward R. Tufte)\The Visual Display of Quantitative Information (Edward R. Tufte).md
> 识别方式：强章节标记

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

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/c7957163b63bac8ace0d7147cfe76aeda07c474db043870afb2fa3dcac62616b.jpg)  
Department of Surveys, Ministry of Labour, Atlas of Israel (Jerusalem, 1956), vol. 8, p. 8.

1 On the design of tables, see A.S.C. Ehrenberg, "Rudiments of Numeracy," Journal of the Royal Statistical Society, A, 140 (1977), 277297.

Tables also work well when the data presentation requires many localized comparisons. In this 410-number table that I designed for the New York Times to show how different people voted in presidential elections in the United States, comparisons between the elections of 1980 and 1976 are read across each line; within-election analysis is conducted by reading downward in the clusters of three to seven lines. The horizontal rules divide the data into topical paragraphs; the rows are ordered so as to tell an ordered story about the elections. This type of elaborate table, a supertable, is likely to attract and intrigue readers through its organized, sequential detail and reference-like quality. One supertable is far better than a hundred little bar charts.

## How Different Groups Voted for President

Based on 12,782 interviews with voters at their polling places. Shown is how each group divided its vote for President and, in parentheses, the percentage of the electorate belonging to each group.

<table><tr><td></td><td>CARTER</td><td>REAGAN ANDERSON</td><td>in 1976</td></tr><tr><td>Democrats (43%)</td><td></td><td>$34</td><td>$12rac{2$</td></tr><tr><td></td><td>30 </td><td></td><td>77-22 43-54</td></tr><tr><td>Independents (23%) Republicans (28%)</td><td>13</td><td>84 4</td><td>9-90</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>Liberals (17%)</td><td>57</td><td>27 11</td><td>70·26</td></tr><tr><td>Moderates (46%)</td><td>42</td><td>48 8 71</td><td>51-48</td></tr><tr><td>Conservatives (28%)</td><td>23</td><td>4</td><td>29-70</td></tr><tr><td>Liberal Democrats (9%)</td><td>70</td><td>14 13</td><td>86 -12</td></tr><tr><td>Moderate Democrats (22%)</td><td>66 28</td><td>6</td><td>77-22</td></tr><tr><td>Conservative Democrats (8%)</td><td>53 41</td><td> ∞</td><td>64 -35</td></tr><tr><td>Polticallyactiv Dt %)</td><td>72 19</td><td></td><td>—</td></tr><tr><td>Democrats favoring Kennedy</td><td>24</td><td></td><td></td></tr><tr><td>in primaries (13%)</td><td>66</td><td>8</td><td></td></tr><tr><td>Liberal Independents (4%)</td><td>$29</td><td>$1\fc{ $</td><td>64-29</td></tr><tr><td>Moderate ndependents (12%)</td><td></td><td></td><td>45-53</td></tr><tr><td>Conservative ndependents (%)</td><td>69</td><td>6</td><td>2672</td></tr><tr><td>Liberal Republicans (2%)</td><td>25 66</td><td>O IDN</td><td>17-82</td></tr><tr><td>Moderate Republicans 11%)</td><td>13 81</td><td></td><td>11-88</td></tr><tr><td>Conserativ Republicans 2%)</td><td>6 91</td><td></td><td>6-93</td></tr><tr><td>i %</td><td>5 89</td><td></td><td></td></tr><tr><td>East (32%)</td><td>43 47</td><td></td><td>51-47</td></tr><tr><td>South (27%)</td><td>44 51</td><td>∞M</td><td>54-45</td></tr><tr><td>Midwest ((20%)</td><td>41 51</td><td></td><td>48·50</td></tr><tr><td>Wt(11%)</td><td>35 52</td><td>10</td><td>46-51</td></tr><tr><td>Blacks (10%)</td><td>82</td><td>14</td><td>82-16</td></tr><tr><td>Hispanics (2%)</td><td>30 6</td><td>3 36</td><td>755- 24</td></tr><tr><td>Wtes(88%)</td><td></td><td>55 8</td><td>47-52</td></tr><tr><td>Female (49%)</td><td>$3\frac{ }$</td><td>46</td><td>50 - 48</td></tr><tr><td>Male M(51%)</td><td></td><td>~</td><td>50 - 48</td></tr><tr><td>Femae, os equ </td><td></td><td>54</td><td></td></tr><tr><td>amendment (22%)</td><td>54</td><td>32 11</td><td>−</td></tr><tr><td>Female,oses equal hts amendment (15%)</td><td>29 66</td><td>4</td><td></td></tr><tr><td></td><td></td><td></td><td>—</td></tr><tr><td>Catholic (25%) Jewish (5%)</td><td>40 51</td><td>7</td><td>54-44</td></tr><tr><td>Protestant (46%)</td><td></td><td>39 14</td><td>64-34</td></tr><tr><td>Born-again hite Protestant%)</td><td>$3frac }$</td><td>56 0 61</td><td>44.555</td></tr><tr><td></td><td>43</td><td></td><td>-</td></tr><tr><td>18 -21 years old (6%) 22 -29 years old (17%)</td><td>44 43</td><td>11</td><td>48-50 51-46</td></tr><tr><td>30 44 years old (31%)</td><td>43</td><td>11</td><td>49-49</td></tr><tr><td>45 -59 years old (23%)</td><td>37</td><td>54 7</td><td></td></tr><tr><td>60 years or older (18%)</td><td>40 </td><td>$54 0</td><td>47-52</td></tr><tr><td></td><td></td><td></td><td>47-52</td></tr><tr><td>Family income Less than $10,000 (13%)</td><td>41</td><td></td><td>58·40</td></tr><tr><td>$10,000 -$14,999 (14%)</td><td>50</td><td>6</td><td></td></tr><tr><td>$15,000 - $24,999 (30%)</td><td>47</td><td>42 ∞</td><td>55 - 43</td></tr><tr><td>$25,000 - $50,000 (24%)</td><td>38</td><td>53 58</td><td>48.50</td></tr><tr><td>Over $50,000 (5%)</td><td>32 25 65</td><td>8 8</td><td>36-62 </td></tr><tr><td></td><td>56</td><td></td><td></td></tr><tr><td>Professional omanager 40%) Clerical, sales or other</td><td>33</td><td>9</td><td>41·57</td></tr><tr><td>white-collar (11%)</td><td></td><td></td><td></td></tr><tr><td>Blue-collar worker (17%)</td><td>42 46</td><td>48 ∞ M 47</td><td>46-53 57-41</td></tr><tr><td>Agriculture (3%)</td><td>29 35 </td><td></td><td></td></tr><tr><td>Looking for work (3%)</td><td>55</td><td></td><td>65-34</td></tr><tr><td>Education</td><td></td><td></td><td></td></tr><tr><td>High school or less (39%)</td><td></td><td></td><td>57 - 43</td></tr><tr><td>Some college (28%) College graduate (27%)</td><td></td><td>48 ∞ 55</td><td>51-49</td></tr><tr><td></td><td></td><td>51 11</td><td>45-55</td></tr><tr><td>Labor union household (26%)</td><td>47 44</td><td>∞</td><td>59-39</td></tr><tr><td>No member household in union (62%)</td><td>35</td><td>55</td><td>43-55</td></tr><tr><td>Family finances</td><td></td><td></td><td></td></tr><tr><td>Betye g%</td><td></td><td>37</td><td>30 -70</td></tr><tr><td>Same (40%) Worseoff thn a year go (34%)</td><td></td><td>∞∞ 46 64</td><td>51-49</td></tr><tr><td></td><td>25</td><td></td><td>77-23</td></tr><tr><td>Fiy Democrats, better off</td><td></td><td></td><td></td></tr><tr><td>than a year ago (7%)</td><td></td><td></td><td></td></tr><tr><td>Democrats, worse off</td><td>77</td><td>16 6</td><td>69-31</td></tr><tr><td>than a year ago (13%)</td><td>47</td><td>39 10</td><td>94-6</td></tr><tr><td>Independents, better f (%)</td><td>45 36</td><td>12</td><td></td></tr><tr><td>dependentsworse of (9%)</td><td>21 65</td><td>11</td><td></td></tr><tr><td>Republicans, tt% Republicans, worse off (11%)</td><td>18</td><td>77 4</td><td>3-97</td></tr><tr><td></td><td>6</td><td>89</td><td>24.76</td></tr><tr><td>More important problem Unemployment (39%)</td><td></td><td></td><td>75 -25</td></tr><tr><td>Inflation (44%)</td><td>30 </td><td>40 0</td><td>35-65</td></tr><tr><td>e U..</td><td></td><td>60</td><td></td></tr><tr><td>dealing with Soviet Union evenould</td><td></td><td></td><td></td></tr><tr><td>s th is fr 5%</td><td></td><td>32 6</td><td>vee</td></tr><tr><td>Disagree (31%)</td><td>50 </td><td>10</td><td>—</td></tr><tr><td>Favor equal rights amendment (46%)</td><td></td><td>38 11</td><td>—</td></tr><tr><td>Oppose equal rights amendment (35%)</td><td>$20rac66$</td><td>68 4</td><td></td></tr><tr><td>When decided about choice</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>Knew all along (41%)</td><td>47</td><td>50 2 60 ∞</td><td>44 ·55 57·42</td></tr><tr><td>During the primaries (13%) During conventions (8%)</td><td>30</td></table>

For sets of highly labeled numbers, a wordy data graphic— coming close to straight text—works well. This table of numbers is nicely organized into a graphic:

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/4e494a4aa4c9342f51bd4815383cf7ba5e3e93121b8d17cf2e82669566fce1c1.jpg)  
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

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/500ec661586f7645624c65bf1fbef33040d8d34631381aacdcb1964f9eff8460.jpg)

In contrast, this next desig is heavy handed, with neary every element out of balance: the clotted ink, the poor style of lettering, the puffed-up display of a small data set, the coarse texture of the entire graphic, and the mismatch between drawing and surrounding text:

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/bd401517a75e1fda0b0d6c15be0ebe733ac3cb5d24c580b0874d2d89a29237b1.jpg)

Edward R. Tufte, "The Relationship Between Seats and Votes in Two-Party Systems," American Political Science Review, 67 (June 1973), 551.

Lines in data graphics should be thin. One reason eighteenthand nineteenth-century graphics look so good is that they were engraved on copper plates, with a characteristic hair-thin line. The drafting pens of twentieth-century mechanical drawing thickened linework, making it clumsy and unattractive.

An effective aesthetic device is the orthogonal intersection of lines of different weights:

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/6c9c20e911f314071a313960d0feaf4c0102a196601ebdb23d3d407beaf13fb5.jpg)

Poster for the exhibition "Mondrian and Neo-Plasticism in America," Yale University Art Gallery, October 18 to December 2, 1979. The original painting was done in 1941 by Diller; see Nancy J. Troy, Mondrian and Neo-Plasticism in America (New Haven, 1979), p. 28.

Nearly every intersection of the lines in this design (based on a painting by Burgoyne Diller) involves lines of differing weights, and it makes a difference, for the painting's character is diluted with lines of constant width:

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/ce48c107f4fe82b13390d242656336515d792a04aa45df480575b7ed287813c6.jpg)

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/cb5122acbb043d78b0b5af7ad9051a2d754d7e2eb8ff83f02d82f16777fcbd21.jpg)

Likewise, data graphics can be enhanced by the perpendicular intersections of lines of differing weights. The heavier line should be a data measure. In a time-series, for example:

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/b3b63326920007e9c6d11b9256adf030134989f26859fd70d9b68a4cdec0918d.jpg)  
The contrast in line weight represents contrast in meaning. The greater meaning is given to the greater line weight; thus the data line should receive greater weight than the connecting verticals. The logic here is a restatement, in different language, of the principle of data-ink maximization.

## Proportion and Scale: The Shape of Graphics

Graphics should tend toward the horizontal, greater in length than height:

lesser height

Several eoigvororiznal ververtil dipys.

First, analogy to the horizon. Our eye is naturally practiced in detecting deviations from the horizon, and graphic design should take advantage of this fact. Horizontally stretched time-series are more accessible to the eye:

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/836356e60fe91c9c2bc55231d871a6d674eb3143cd20fab95c8cec2aa0fb58a6.jpg)

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/c9790dd6caf6dc21a7be7196c7efbc7505d7a6bcdf55af4276be686090b27f21.jpg)

The analogy to the horizon also suggests that a shaded, high contrast display might occasionally be better than the floating snake. The shading should be calm, without moiré effects.

Second, ease of labeling. It is easier to write and to read words that read from left to right on a horizontally stretched plottingfield:

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/12f7db55d29cc01b3b1ae27b2817c5f68a3ac945bda0b5429a0f0c98de1ffd52.jpg)

T  o

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/668e4456755997b7dbf6d97c6f89bdd40482cf1d8c1d4aadcd6191ac19cf87ca.jpg)

and a longer horizontal helps to elaborate the workings of the causal variable in more detail.

Fourth, Tukey's counsel.

Most diagnostic plots involve either a more or less definite dependence that bobbles around a lot, or a point spatter. Such plots are rather more often better made wider than tall. Widerthan-tall shapes usually make it easier for the eye to follow from left to right.

7John W. Tukey, Exploratory Data Analysis (Reading, Mass., 1977), p. 129.

Perhaps the most general guidance we can offer is that smoothly-changing curves can stand being taller than wide, but a wiggly curve needs to be wider than tall. . . .7

And, finally, Playfair's example. Of the 89 graphics in six different books by William Playfair, most (92 percent) are wider than tall. Several of the exceptions are his skyrocketing government debt displays. This plot shows the dimensions of each of those 89 graphics:

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/4f20b60bf6844dc5fe771f3817541119c21aef5211379a117ddccdc120299a58.jpg)

If graphics should tend toward the horizontal rather than the vertical, then how much so? A venerable (fifth-century B.c.) but dubious rule of aesthetic proportion is the Golden Section, a "divine division" of a line.8 A length is divided such that the smaller is to the greater part as the greater is to the whole:

8 The combination of geometry and mysticism surrounding the Golden Rectangle can be seen in Miloutine Borissavlièvitch, The Golden Number and the Scientific Aesthetics of Architecture (New York, 1958) and Tons Brunés, The Secrets of Ancient Geometry (Copenhagen, 1967), vols. 1 and 2.

$$
{ \frac { \mathsf { a } } { \mathsf { b } } } = { \frac { \mathsf { b } } { \mathsf { a } + { \mathsf { b } } } }
$$

Solving the quadratic when a = 1 yields ${ \mathfrak { b } } = { \frac { { \sqrt { 5 } } + 1 } { 2 } } = { \mathfrak { r } } . 6 1 8 \dots .$

In turn the Golden Rectangle is

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/c1b619db5f54a871f2d447fa45624e01100b8c2e122c750194b2e99f05353541.jpg)

The nice geometry of the Golden Rectangle is not unique; Birkhoff points out that at least five other rectangles (including the square) have one simple mathematical property or another for which aesthetic claims might be made:9

9George D. Birkhoff, Aesthetic Measure (Cambridge, 1933), pp. 2730.

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/b45025dce974727fb8d7f483595b023ca30e6d49fba94a7b98f394101e054604.jpg)

Playfair favored proportions between 1.4 and 1.8 in about twothirds of his published graphics, with most of the exceptions moving more toward the horizontal than the golden prescription:

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/c5a065cde6156dad45d7f915431d2e7421d209f8f1c1ad99a1dbb558cc2b8aab.jpg)

Visual preferences for rectangular proportions have been studied by psychologists since 186o, but, even given the implausible assumption that such studies are relevant to graphic design, the findings are hardly decisive. A mild preference for proportions near to the Golden Rectangle is found among those taking part in the experiments, but the preferred height/length ratios also vary a great deal, ranging between

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/7d251eee35fe274be02ac48ed8681705874674b70e18804b8e938f813e824948.jpg)

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/710309ffa450c5250b1f9afbfad0dba52738425d8bd31a158987b809d66fdb56.jpg)

And, as is nearly always the case in experiments in graphical perception, viewer responses were found to be highly contextdependent.10

The conclusions:

10I have relied on Leonard Zusne, Visual Perception of Form (New York, 1970), ch. 10, for a summary of the immense literature.

I follow that suggestion.

Otherwise, move toward horizontal graphics about o percent wider than tall:

![](../../The Visual Display of Quantitative Information (Edward R. Tufte)/images/afd42124a49e3fb09234ad8d57324d00ed00642e33e0b366158274707f553e45.jpg)

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
