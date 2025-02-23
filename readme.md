{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 ArialMT;\f1\froman\fcharset0 Times-Roman;\f2\fswiss\fcharset0 Arial-ItalicMT;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red24\green25\blue27;\red238\green240\blue241;
\red16\green60\blue192;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c12549\c12941\c14118;\cssrgb\c94510\c95294\c95686;
\cssrgb\c6667\c33333\c80000;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs32 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Dataset:
\f1\fs24 \

\f0\fs32 I used a dataset called tmdb_5000_movies.xlsx which\cf3 \cb4 \strokec3  \cf0 \cb1 \strokec2 comes from Kaggle, and you can download from the website: {\field{\*\fldinst{HYPERLINK "https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system/input?select=tmdb_5000_movies.csv"}}{\fldrslt \cf5 \ul \ulc5 \strokec5 https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system/input?select=tmdb_5000_movies.csv}}. You can directly use my dataset that\'92s in the repository. I specifically used the columns 
\f2\i title
\f0\i0  and 
\f2\i overview 
\f0\i0 for our purpose.
\f1\fs24 \
\

\f0\fs32 Setup:
\f1\fs24 \

\f0\fs32 pip install pandas numpy scikit-learn
\f1\fs24 \
\

\f0\fs32 Running: Run the Recommendation System
\f1\fs24 \

\f0\fs32 python3 /Users/yukashimazaki/Desktop/movie4.py --file /Users/yukashimazaki/Desktop/tmdb_5000_movies.xlsx --query "I love sci-fi action movies set in space."
\f1\fs24 \

\f0\fs32 Please update the location of the py file and the excel file in your local machine.
\f1\fs24 \
\
\

\f0\fs32 Results:
\f1\fs24 \

\f0\fs32 Top Movie Recommendations:
\f1\fs24 \
\pard\pardeftab720\partightenfactor0

\f0\fs22\fsmilli11333 \cf0 Top Movie Recommendations (Ranked by Similarity Score):
\f1\fs24 \

\f0\fs22\fsmilli11333 1. Deep Impact (Score: 0.1591)
\f1\fs24 \

\f0\fs22\fsmilli11333 \'a0\'a0\'a0Overview: seven mile wide space rock hurtle earth threaten obliterate planet s president united states save world appoint tough nail veteran astronaut lead joint american russian crew space destroy comet impact enterprise reporter use smart uncover scoop century
\f1\fs24 \

\f0\fs22\fsmilli11333 2. Hard Rain (Score: 0.1503)
\f1\fs24 \

\f0\fs22\fsmilli11333 \'a0\'a0\'a0Overview: sweep action armored car driver christian slater try elude gang thief lead morgan freeman flood ravage countryside hard rain wild thrilling chill action ride fill close call uncertain loyalty heart stop heroic
\f1\fs24 \

\f0\fs22\fsmilli11333 3. Bandits (Score: 0.1498)
\f1\fs24 \

\f0\fs22\fsmilli11333 \'a0\'a0\'a0Overview: bank robber fall love girl ve kidnap
\f1\fs24 \

\f0\fs22\fsmilli11333 4. Star Trek Beyond (Score: 0.1264)
\f1\fs24 \

\f0\fs22\fsmilli11333 \'a0\'a0\'a0Overview: uss enterprise crew explore furth reach uncharted space encounter mysterious new enemy put federation stand test
\f1\fs24 \

\f0\fs22\fsmilli11333 5. The 6th Day (Score: 0.1264)
\f1\fs24 \

\f0\fs22\fsmilli11333 \'a0\'a0\'a0Overview: futuristic action man meet clone stumble grand conspiracy clone take world
\f1\fs24 \
}