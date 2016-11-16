use "GSS2014.DTA", replace

// The GSS has several missing values in the data
// * .i == 	inaplicable (IAP). 
//			Respondents who are not asked to answer a specific question
// * .d == 	Don't Know (DK)
// * .n == 	No Answer (NA)


// In addition, there are some other missing values encoded, 

// .a == 	na
// .b == 	no answer
// .c == 	can't choose
// .u == 	uncodeable & iap

// We could make a judgement that .n, .a, and .b all mean no answer. However, in case there is any sort of unforseen differences, we will maintain discrete numeric values for these encodings for now.

// Although this data is "missing" (indicated by the .), for Machine Learning (ML) we don't want to throw away this data since it might be informative.

// We will recode it as follows:

mvencode _all, mv(.i = -1 \ .d = -2 \ .n = -3)
mvencode _all, mv(.a = -4 \ .b = -5 \ .c = -6 \ .u = -7)


// Check for missing values
// findit mdesc //to install if needed
mdesc

//Make Some Indicator (0/1) Variables to Investigate
tab partyid, gen(partyid)
ren partyid1 partyid_na
ren partyid2 partyid_dk
ren partyid3 partyid_strdem
ren partyid4 partyid_dem
ren partyid5 partyid_ind_dem
ren partyid6 partyid_ind
ren partyid7 partyid_ind_rep
ren partyid8 partyid_rep
ren partyid9 partyid_str_rep
ren partyid10 partyid_other


// Save Result
//Change to Data Directory
cd "../"
export delimited using "gss2014.csv", nolabel replace
cd "GSS_Source"
