import random

def load_phrases():
    phrases = {
        "adjectives": ["sparkly", "mischievous", "sunshiny", "brilliant", "cozy", "radiant", "charming", "delightful", "vibrant", "lively"],
        "nouns": ["laugh", "sparkle", "brain", "energy", "vibe", "smile", "heart", "spirit", "wit", "charm"],
        "verbs": ["light up", "spark", "tickle", "warm", "buzz", "shine", "dance", "glow", "ignite", "sprinkle"],
        "compliments": [
            "You've got this incredible sparkle in your eyes that always makes me smile.",
            "Your laugh is seriously the best sound ever. It's like sunshine in my ears.",
            "Your brain is just... wow. You're so quick and witty, it's amazing.",
            "You have this amazing ability to just light up a room. It's like you carry your own personal sunshine.",
            "You're like a cozy blanket on a chilly night – warm, comforting, and just perfect.",
            "That smile of yours? It's downright contagious. Seriously, try to frown around you, it's impossible.",
            "Your energy is something else. You're like a human power-up!",
            "You have the best vibe. Its so positive.",
            "Your wit is so sharp, I'm always on my toes.",
            "Your charm is undeniable."
        ],
        "expressions": [
            "Just thinking about you makes my day a million times better.",
            "You know, you're pretty much my favorite person ever. Just saying.",
            "I'm kinda obsessed with how awesome you are. No pressure, though.",
            "Every time I talk to you, I get this goofy grin. It's your fault.",
            "You're the kind of person who makes even Mondays feel like a Friday.",
            "I'm pretty sure you're a superhero in disguise. You're just too amazing to be normal.",
            "I'm really glad I met you. You make everything better.",
            "You have this amazing way of making me feel like I can do anything.",
            "I could talk to you for hours, and it would still feel like five minutes.",
            "You make my heart do a little happy dance."
        ],
        "dad_jokes": [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a fish with no eyes? Fsh!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "Why did the bicycle fall over? Because it was two tired!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Did you hear about the restaurant on the moon? Great food, no atmosphere!",
            "Why did the coffee go to the police? It got mugged!",
            "What do you call cheese that isn't yours? Nacho cheese!",
            "Want to hear a joke about construction? I'm still working on it!",
            "How do you organize a space party? You planet!",
            "What do you call a lazy kangaroo? A pouch potato!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "What do you call a sad strawberry? A blueberry!",
            "Why don't eggs tell jokes? They'd crack each other up!"
        ],
        "personal_traits": [
            "I love how you're always up for an adventure. You're so spontaneous!",
            "You're so incredibly kind and thoughtful. It's one of my favorite things about you.",
            "You've got this amazing ability to just roll with whatever life throws at you.",
            "I'm seriously impressed by how passionate you are about everything you do.",
            "You're so genuine and down-to-earth. It's really refreshing.",
            "You're so good at making people feel comfortable. It's like a superpower.",
            "I love your sense of humor. You always know how to make me laugh.",
            "Your creativity is off the charts. You're always coming up with the coolest ideas.",
            "You're so supportive and encouraging. You always believe in me.",
            "I love that you're always unapologetically yourself. It's inspiring."
        ],
        "funny_encouragement": [
            "You're so awesome, you could probably parallel park a train. Go you!",
            "Remember, you're not a taco. You can handle anything! Unless it involves being eaten, then maybe not.",
            "Don't worry, even a broken pencil can still draw a straight line... or something like that. You got this!",
            "If at first you don't succeed, blame gravity. Or try again. But blaming gravity is funnier.",
            "You're like a fine cheese: getting better with age... or at least more interesting.",
            "Just remember, even if you fall on your face, you're still moving forward. And that's something!",
            "You're not perfect, but you're definitely not a potato. And that's a win!",
            "When life gives you lemons, throw them back and ask for chocolate. Or just make lemonade. Your choice.",
            "You're so talented, you could probably convince a squirrel to share its nuts. That's talent!",
            "You're not just a snack, you're a whole buffet of awesomeness. Go get 'em!",
            "You're so bright, you make lightbulbs jealous.",
            "If you were a vegetable, you'd be a cute-cumber.",
            "You are the reason for the season... of awesomeness.",
            "You are so smart, you could teach a rock to do math.",
            "You are a force to be reckoned with, like a squirrel with a nut."
        ]
    }
    return phrases

def get_random_phrase(category):
    phrases = load_phrases()
    return random.choice(phrases[category])