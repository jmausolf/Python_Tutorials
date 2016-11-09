###################################
###                             ###
###      Joshua G. Mausolf      ###
###   Department of Sociology   ###
###    University of Chicago    ###
###                             ###
###################################


from text_keyword_classifier import *

##########################################################
#Example 1: Keyword Categories with Keywords/Phrases
##########################################################

#Example

wall_street = ["lobby", "lobbying", "lobbies", "special interest", "special interests", "revolving door", "campaign donor", "campaign donation", "campaign donations", "bidder", "highest bidder", "campaign contributions", "loophole", "loopholes", "tax shelter", "tax evasion", "write their own rules", "own rules", "Wall Street", "bailout", "bailouts"]

corporate_greed = ["cheat", "cheating", "stacked against", "stacked up against", " stacked against", "good benefits", "decent salary", "stack the deck", "deck got stacked against", "exploit", "exploiting",  "protect workers", "protecting workers", "protect laborers", "protecting laborers", "protect Americans", "protecting Americans", "protect employee", "protect employees", "protecting employees", "work safe", "working safely", "safe at work", "work conditions", "innocent", "minimum wage", "pollute", "polluting", "regulate", "regulating", "federal oversight", "financial reform", "gambling", "derivative", "derivatives", "sub-prime", "risky investment", "risky investments", "bust unions", "union", "unions", "labor unions", "dirtiest air", "cheapest labor", "wages", "workplace safety", "Consumer Finance Protection Bureau", "consumer protection", "unions", "union label", "union workers", "CEO", "CEO's", "corporation", "corporations"]

inequality = ["wealth", "wealthy", "income equality", "income inequality", "inequality", "privileged", "rich", "1%", "1 percent", "one percent", "99%", "99 percent", "ninety-nine percent", "ninety nine percent", "fair", "unfair", "fairness", "unfairness", "middle-class", "middle class", "working class", "working-class", "lower class", "poor", "poverty", "rich", "upper class", "equity", "inequity", "egalitarian", "disparity", "unequal", "average American", "average Americans", "Wall Street", "Main Street", "main street", "50 million", " Warren Buffet", "Warren Buffett's secretary", "secretary", "class warfare", "class warefare", "warrior for the middle class", "Giving everybody a shot", "giving everybody a shot", "everybody a fair shot", "work your way up", "working your way up", "starting at the bottom", "blood, sweat and tears", "blood sweat and tears", "blood, sweat, and tears", "willing to work hard", "fair and just", "everybody is included", " folks at the top", "folks at the bottom"]

fair_share = ["fair shot", "fair shake", "gets a fair shake", "pay their fair share", "our fair share", "fair share"]

occupy = ["occupy", "occupying", "OWS", "Occupy Wall Street"]

combined_terms = wall_street+corporate_greed+inequality+fair_share+occupy


##########################################################
#Example 2: Keyword Categories with Keywords/Phrases
##########################################################

guns = ["_start", "firearm", "guns", "gun", "automatic weapons", "automatic weapon", "cheap handguns", "handguns", "shotgun", "shotguns", "rifle", "rifles", "Saturday night special", "high capacity magazines", "assualt rifles", "sawed off shotguns", "silencers", "AK-47s", "AR15", "AR-15s", "Glock", "Glocks"]

gun_laws = ["Second Amendment", "right to bear arms", "gunshow loophole", "gunshow", "gun dealer", "gun ownership", "gun sales", "gun manufacturers", "background check", "concealed carry", "ATF", "National Rifle Association", "NRA"]

gun_violence = ["mass shooting", "shootings", "guns don't kill people", "gun violence", "gunned down"]

shootings = ["Newtown", "San Bernardino", "Blacksburg", "Navy Yard", "Aurora", "Tucson", "Virginia Tech", "Fort Hood", "Charleston", "_end"]

gun_terms = guns+gun_laws+gun_violence+shootings


##########################################################
#Define Your Own Keyword Categories with Keywords/Phrases
#OCCUPY WALL STREET
##########################################################

wall_street = ["lobby", "lobbying", "lobbies", "special interest", "special interests", "revolving door", "campaign donor", "campaign donation", "campaign donations", "bidder", "highest bidder", "campaign contributions", "loophole", "loopholes", "tax shelter", "tax evasion", "write their own rules", "own rules", "Wall Street", "bailout", "bailouts"]

corporate_greed = ["cheat", "cheating", "stacked against", "stacked up against", " stacked against", "good benefits", "decent salary", "stack the deck", "deck got stacked against", "exploit", "exploiting",  "protect workers", "protecting workers", "protect laborers", "protecting laborers", "protect Americans", "protecting Americans", "protect employee", "protect employees", "protecting employees", "work safe", "working safely", "safe at work", "work conditions", "innocent", "minimum wage", "pollute", "polluting", "regulate", "regulating", "federal oversight", "financial reform", "gambling", "derivative", "derivatives", "sub-prime", "risky investment", "risky investments", "bust unions", "union", "unions", "labor unions", "dirtiest air", "cheapest labor", "wages", "workplace safety", "Consumer Finance Protection Bureau", "consumer protection", "unions", "union label", "union workers", "CEO", "CEO's", "corporation", "corporations"]

inequality = ["wealth", "wealthy", "income equality", "income inequality", "inequality", "privileged", "rich", "1%", "1 percent", "one percent", "99%", "99 percent", "ninety-nine percent", "ninety nine percent", "fair", "unfair", "fairness", "unfairness", "middle-class", "middle class", "working class", "working-class", "lower class", "poor", "poverty", "rich", "upper class", "equity", "inequity", "egalitarian", "disparity", "unequal", "average American", "average Americans", "Wall Street", "Main Street", "main street", "50 million", " Warren Buffet", "Warren Buffett's secretary", "secretary", "class warfare", "class warefare", "warrior for the middle class", "Giving everybody a shot", "giving everybody a shot", "everybody a fair shot", "work your way up", "working your way up", "starting at the bottom", "blood, sweat and tears", "blood sweat and tears", "blood, sweat, and tears", "willing to work hard", "fair and just", "everybody is included", " folks at the top", "folks at the bottom"]

fair_share = ["fair shot", "fair shake", "gets a fair shake", "pay their fair share", "our fair share", "fair share"]

occupy = ["occupy", "occupying", "OWS", "Occupy Wall Street"]

#Top Keywords Listed by OWS Protestors
#Keywords kepts if >=5 responses for first, second, and third, choices
#These were pooled, and duplicates removed.
#http://occupyresearch.net/orgs/
OWS_survey = ["income inequality", "inequality", "economic conditions", "corruption", "justice", "corporate influence in politics", "corporations", "corporate personhood", "injustice", "social justice", "corporate greed", "anti-capitalism", "greed", "unemployment", "citizens united", "equality", "money in politics", "government corruption", "poverty", "environmental concerns", "democracy", "fairness", "freedom", "change", "inequity", "jobs", "money out of politics", "health care", "financial reform", "solidarity", "war", "movement building", "foreclosures", "frustration", "banks", "politics", "curiosity", "money", "campaign finance reform", "climate change", "education", "disparity", "bailouts", "future", "anger", "hope", "revolution", "humanity", "equity", "children", "police brutality", "rights", "community", "Oligarchy", "0.99", "fascism", "freedom of speech", "food", "civil liberties", "taxes", "peace", "plutocracy", "love", "corporate corruption", "joblessness", "campaign finance", "fraud", "Wall Street", "human rights", "compassion", "accountability", "NDAA", "debt", "tax the rich", "lobbyists", "broken political system", "agreement", "inequality", "corruption", "economy", "justice", "environment", "income inequality", "economic inequality", "healthcare", "capitalism", "corporatism", "economics", "social injustice", "income disparity", "political corruption", "government", "economic justice", "economic disparity", "economic injustice", "civil rights", "wealth disparity", "oppression", "racism", "patriarchy", "sustainability", "homelessness", "corporate power", "workers rights", "student loans", "wall street", "corrupt government", "exploitation", "accountability", "housing", "patriotism", "apathy", "responsibility", "corporations"]

other_terms = ["jobs", "economy", "unemployment"]

occupy_terms = wall_street+corporate_greed+inequality+fair_share+occupy+OWS_survey+other_terms


##########################################################
#Run
##########################################################

"""
---------------------------------------------------------------------
	INSTRUCTIONS TO RUN THE PROGRAM
---------------------------------------------------------------------

	-	(1) To run the function, first define your full keyword list.
		Several examples are above.

---------------------------------------------------------------------

	- 	(2) Next, select the folder with the speech files.
---------------------------------------------------------------------
	- 	(3) Outline the string slice that contains the date for your
		text file.

		Your text file should contain a date of the file
		for example, 2011-09-17_ID1.txt or CREC-2015-01-03.txt.

	- 	ds1:ds2 	= - date slices of filenames
					E.g. the filename "2011-09-17_ID1.txt"
						would want date slices of
						ds1 = 0 and ds2 = 10
						This takes the string slice 0:10
						and provides a date = 2011-09-17

---------------------------------------------------------------------
	- 	(4) Specify the name of the output file.
---------------------------------------------------------------------
	- 	(5) Specify other options if desired.
			See further documentation under speech_classifier
			documentation.

	speech_classifier(folder_name, ds1, ds2, output_file, terms,
					metric=0, addtime=0, addloc=0, addcite=0):

---------------------------------------------------------------------
"""

#Occupy
#speech_classifier("Congressional_Records_Text", 5, 15, "Congressional_Records_data.csv", occupy_terms, 1)
speech_classifier("data/president", 0, 10, "White_House_data.csv", combined_terms, 1)
