Dataset:
I used a dataset called tmdb_5000_movies.xlsx which comes from Kaggle, and you can download from the website: https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system/input?select=tmdb_5000_movies.csv. You can directly use my dataset that’s in the repository. I specifically used the columns title and overview for our purpose.

Setup:
pip install pandas numpy scikit-learn

Running: Run the Recommendation System
python3 /Users/yukashimazaki/Desktop/movie4.py --file /Users/yukashimazaki/Desktop/tmdb_5000_movies.xlsx --query "I love sci-fi action movies set in space."
Please update the location of the py file and the excel file in your local machine.


Results:
Top Movie Recommendations:
Top Movie Recommendations (Ranked by Similarity Score):
1. Deep Impact (Score: 0.1591)
   Overview: seven mile wide space rock hurtle earth threaten obliterate planet s president united states save world appoint tough nail veteran astronaut lead joint american russian crew space destroy comet impact enterprise reporter use smart uncover scoop century
2. Hard Rain (Score: 0.1503)
   Overview: sweep action armored car driver christian slater try elude gang thief lead morgan freeman flood ravage countryside hard rain wild thrilling chill action ride fill close call uncertain loyalty heart stop heroic
3. Bandits (Score: 0.1498)
   Overview: bank robber fall love girl ve kidnap
4. Star Trek Beyond (Score: 0.1264)
   Overview: uss enterprise crew explore furth reach uncharted space encounter mysterious new enemy put federation stand test
5. The 6th Day (Score: 0.1264)
   Overview: futuristic action man meet clone stumble grand conspiracy clone take world
   
Salary expectation: $1500 per month
   
Video link: https://www.youtube.com/watch?v=hRLTryYhuVc


