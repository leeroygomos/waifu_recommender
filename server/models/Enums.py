from sqlalchemy.dialects import postgresql

genre = postgresql.ENUM('action', 'adventure', 'comedy', 'drama', 'fantasy', 'horror', 'mystery', 'romance', 'sci-fi', 'slice-of-life', 'music', 
                        name='genre', 
                        create_type=False)

trait = postgresql.ENUM('Energetic', 'Determined', 'Stern', 'Focused', 'Clever', 'Ambitious', 'Cowardly', 'Imaginative', 'Passionate', 'Protective', 
                        'Hot-headed', 'Loyal', 'Intellectual', 'Cautious', 'Calculated', 'Mysterious', 'Brooding', 'Cool-headed', 'Skilled', 'Shy', 
                        'Gentle', 'Lazy', 'Analytical', 'Serious', 'Disciplined', 'Driven', 'Impulsive', 'Compassionate', 'Resilient', 'Bored', 
                        'Overpowered', 'Arrogant', 'Powerful', 'Competitive', 'Caring', 'Free-spirited', 'Reserved', 'Talented', 'Supportive', 'Reliable', 
                        'Intellectual', 'Thoughtful',
                        name='trait',
                        create_type=False)

gender = postgresql.ENUM('Male', 'Female', 'Other', 
                         name='gender', 
                         create_type=False)

role = postgresql.ENUM('Main', 'Supporting', 'Antagonist', 
                       name='role', 
                       create_type=False)