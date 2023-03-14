planets = {
    "Mercury": ["intellectual", "adaptable", "inquisitive", "communicative", "nervous", "fickle"],
    "Venus": ["sensual", "romantic", "harmonious", "artistic", "luxurious", "lazy"],
    "Mars": ["assertive", "energetic", "courageous", "competitive", "impulsive", "aggressive"],
    "Jupiter": ["expansive", "optimistic", "generous", "philosophical", "excessive", "overconfident"],
    "Saturn": ["disciplined", "practical", "ambitious", "reserved", "inhibited", "pessimistic"],
    "Uranus": ["innovative", "unconventional", "rebellious", "eccentric", "erratic", "detached"],
    "Neptune": ["dreamy", "intuitive", "mystical", "idealistic", "confused", "illusory"],
    "Pluto": ["transformative", "intense", "powerful", "renewing", "obsessive", "destructive"],
    "Sun": ["vital", "creative", "radiant", "confident", "self-centered", "dominating"],
    "Moon": ["emotional", "nurturing", "intuitive", "moody", "sensitive", "attached"],
}
houses = {
    1: ["Identity", "Appearance", "Approach", "Temperament", "Individuality", "Instinct"],
    2 : ["Possessions", "Value", "Security", "Self-Worth", "Money", "Resources"],
    3: ["Communication", "Learning", "Siblings", "Short Trips", "Curiosity", "Adaptability"],
    4: ["Home", "Family", "Ancestry", "Roots", "Private Life", "Nurture"],
    5: ["Creativity", "Play", "Pleasure", "Children", "Romance", "Self-Expression"],
    6: ["Health", "Service", "Daily Work", "Routine", "Purification", "Detail"],
    7 : ["Partnership", "Relationship", "Marriage", "Negotiation", "Projection", "Balance"],
    8: ["Transformation", "Shared Resources", "Intimacy", "Death", "Taboo", "Regeneration"],
    9: ["Philosophy", "Higher Education", "Travel", "Expansion", "Belief", "Vision"],
    10: ["Career", "Public Life", "Achievement", "Recognition", "Authority", "Purpose"],
    11: ["Friendship", "Community", "Groups", "Goals", "Innovation", "Idealism"],
    12: ["Surrender", "Sacrifice", "Psychological Shadows", "Retreat", "Spirituality", "Karma"],
}

### SIGNS BB ᓚᘏᗢ
sun_signs_dict = {
    'Aries': ['adventurous', 'bold', 'competitive', 'confident', 'energetic', 'impatient', 'impulsive', 'passionate'],
    'Taurus': ['dependable', 'determined', 'grounded', 'loyal', 'patient', 'practical', 'sensual', 'stubborn'],
    'Gemini': ['adaptable', 'charming', 'curious', 'intellectual', 'nervous', 'playful', 'social', 'versatile'],
    'Cancer': ['caring', 'emotional', 'intuitive', 'loyal', 'moody', 'nurturing', 'sensitive', 'supportive'],
    'Leo': ['charismatic', 'confident', 'dramatic', 'generous', 'loyal', 'passionate', 'proud', 'radiant'],
    'Virgo': ['analytical', 'detail-oriented', 'helpful', 'modest', 'practical', 'reliable', 'reserved', 'sensitive'],
    'Libra': ['charming', 'diplomatic', 'gracious', 'harmonious', 'idealistic', 'indecisive', 'romantic', 'social'],
    'Scorpio': ['determined', 'intense', 'mysterious', 'passionate', 'powerful', 'private', 'resilient', 'resourceful'],
    'Sagittarius': ['adventurous', 'curious', 'enthusiastic', 'idealistic', 'independent', 'optimistic', 'philosophical', 'spontaneous'],
    'Capricorn': ['ambitious', 'disciplined', 'focused', 'patient', 'practical', 'reliable', 'responsible', 'serious'],
    'Aquarius': ['eccentric', 'friendly', 'independent', 'intellectual', 'original', 'quirky', 'rebellious', 'unpredictable'],
    'Pisces': ['compassionate', 'creative', 'dreamy', 'empathetic', 'imaginative', 'intuitive', 'mysterious', 'sensitive']
}
### SIGN QUALITIES ᓚᘏᗢ
qualities_dict = {
    'Cardinal': ['assertive', 'driven', 'innovative', 'enterprising', 'inspiring'],
    'Fixed': ['committed', 'loyal', 'resilient', 'determined', 'passionate'],
    'Mutable': ['adaptable', 'versatile', 'curious', 'flexible', 'resourceful']
}
### SIGN ELEMENTS BB ᓚᘏᗢ
sign_elements_dict = {
    "earth": ["practical", "realistic", "grounded", "patient", "hardworking", "dependable", "loyal", "sensual", "materialistic", "cautious", "conservative", "traditional"],
    "air": ["intellectual", "communicative", "analytical", "objective", "social", "creative", "independent", "unconventional", "logical", "detached", "fickle", "superficial"],
    "fire": ["passionate", "energetic", "spontaneous", "enthusiastic", "optimistic", "courageous", "inspirational", "assertive", "dramatic", "arrogant", "impulsive", "reckless"],
    "water": ["emotional", "intuitive", "compassionate", "imaginative", "nurturing", "creative", "mysterious", "sensitive", "psychic", "moody", "secretive", "easily overwhelmed"]
}
# but also CHAKRAS ᓚᘏᗢ
chakra_elements_dict = {
    "earth_chakra": ["grounding", "stability", "foundation", "security", "nourishment", "health", "prosperity", "patience", "endurance", "determination", "resilience", "physicality"],
    "water_chakra": ["emotions", "creativity", "pleasure", "sexuality", "intimacy", "fluidity", "change", "adaptability", "fertility", "imagination", "sensitivity", "healing"],
    "fire_chakra": ["willpower", "confidence", "courage", "action", "passion", "energy", "transformation", "power", "assertiveness", "self-esteem", "drive", "motivation"],
    "air_chakra": ["love", "compassion", "forgiveness", "balance", "harmony", "connection", "empathy", "self-love", "trust", "acceptance", "peace", "healing"]
}
### PLANETS BABE ᓚᘏᗢ
planets_dict = {
    'Sun': ['leadership', 'creativity', 'vitality', 'confidence', 'individuality', 'strength', 'willpower', 'radiance'],
    'Moon': ['emotions', 'intuition', 'nurturing', 'femininity', 'instinct', 'imagination', 'reflection', 'sensitivity'],
    'Mercury': ['communication', 'intellect', 'adaptability', 'curiosity', 'logic', 'versatility', 'precision', 'dexterity'],
    'Venus': ['love', 'beauty', 'harmony', 'sensuality', 'pleasure', 'grace', 'romance', 'elegance'],
    'Mars': ['action', 'courage', 'drive', 'passion', 'masculinity', 'assertiveness', 'challenge', 'perseverance'],
    'Jupiter': ['expansion', 'optimism', 'abundance', 'generosity', 'luck', 'philosophy', 'humor', 'adventure'],
    'Saturn': ['discipline', 'responsibility', 'hard work', 'structure', 'limitations', 'patience', 'wisdom', 'organization'],
    'Uranus': ['innovation', 'freedom', 'change', 'rebellion', 'originality', 'eccentricity', 'independence', 'progress'],
    'Neptune': ['imagination', 'mysticism', 'intuition', 'dreams', 'compassion', 'spirituality', 'creativity', 'idealism'],
    'Pluto': ['transformation', 'power', 'death and rebirth', 'intensity', 'obsession', 'regeneration', 'renewal', 'empowerment']
}
### PLANET RULERSHIP
planet_ruler_dict = {
    'sun_ruler': ['confident', 'ambitious', 'enthusiastic', 'creative', 'dramatic', 'charismatic', 'generous', 'loyal'],
    'moon_ruler': ['empathetic', 'intuitive', 'nurturing', 'sensitive', 'moody', 'imaginative', 'protective', 'family-oriented'],
    'mercury_ruler': ['intellectual', 'analytical', 'communicative', 'adaptable', 'curious', 'logical', 'detail-oriented', 'versatile'],
    'venus_ruler': ['romantic', 'harmonious', 'sensual', 'artistic', 'affectionate', 'graceful', 'peaceful', 'pleasure-seeking'],
    'mars_ruler': ['assertive', 'courageous', 'determined', 'passionate', 'competitive', 'impulsive', 'energetic', 'adventurous'],
    'jupiter_ruler': ['optimistic', 'expansive', 'generous', 'philosophical', 'adventurous', 'lucky', 'wise', 'benevolent'],
    'saturn_ruler': ['responsible', 'practical', 'organized', 'patient', 'ambitious', 'serious', 'disciplined', 'reliable'],
    'uranus_ruler': ['innovative', 'rebellious', 'original', 'eccentric', 'independent', 'progressive', 'unconventional', 'freedom-loving'],
    'neptune_ruler': ['dreamy', 'compassionate', 'imaginative', 'mystical', 'sensitive', 'artistic', 'spiritual', 'intuitive'],
    'pluto_ruler': ['transformative', 'powerful', 'intense', 'secretive', 'obsessive', 'regenerative', 'renewal-seeking', 'profound']
}
### planets IN DA HAUS ᓚᘏᗢ
sun_in_house = {
    "sun_in_house_1": ["leadership", "self-confidence", "individuality", "initiative", "courage", "willpower"],
    "sun_in_house_2": ["materialism", "stability", "sensuality", "values", "self-worth", "acquisition"],
    "sun_in_house_3": ["communication", "curiosity", "intellect", "adaptability", "learning", "sibling"],
    "sun_in_house_4": ["nurturing", "emotional security", "roots", "home", "family", "tradition"],
    "sun_in_house_5": ["creativity", "self-expression", "entertainment", "romance", "pleasure", "children"],
    "sun_in_house_6": ["health", "work", "service", "routine", "organization", "efficiency"],
    "sun_in_house_7": ["partnerships", "harmony", "diplomacy", "balance", "equality", "compromise"],
    "sun_in_house_8": ["transformation", "intensity", "mystery", "power", "regeneration", "sexuality"],
    "sun_in_house_9": ["philosophy", "travel", "higher education", "expansion", "optimism", "religion"],
    "sun_in_house_10": ["career", "ambition", "public image", "status", "achievement", "authority"],
    "sun_in_house_11": ["social groups", "friendship", "innovation", "idealism", "altruism", "community"],
    "sun_in_house_12": ["spirituality", "introspection", "compassion", "sacrifice", "seclusion", "karma"]
}
moon_in_house = {
    "moon_in_house_1": ["emotions", "nurturing", "sensitivity", "intuition", "instincts", "receptivity"],
    "moon_in_house_2": ["material security", "values", "emotional attachment", "possessiveness", "comfort", "nourishment"],
    "moon_in_house_3": ["communication", "curiosity", "imagination", "learning", "moodiness", "restlessness"],
    "moon_in_house_4": ["home", "family", "roots", "security", "tradition", "nostalgia"],
    "moon_in_house_5": ["creativity", "romance", "entertainment", "children", "self-expression", "drama"],
    "moon_in_house_6": ["health", "work", "routine", "anxiety", "service", "sensitivity"],
    "moon_in_house_7": ["partnerships", "harmony", "balance", "projection", "emotional mirroring", "codependency"],
    "moon_in_house_8": ["intensity", "transformation", "sexuality", "psychology", "obsession", "fears"],
    "moon_in_house_9": ["philosophy", "travel", "higher education", "adventure", "optimism", "seeking"],
    "moon_in_house_10": ["public image", "career", "ambition", "status", "responsibility", "maternal authority"],
    "moon_in_house_11": ["social groups", "friendship", "rebellion", "innovation", "altruism", "eccentricity"],
    "moon_in_house_12": ["spirituality", "introspection", "compassion", "sacrifice", "seclusion", "karma"]
}
mercury_in_house = {
    "mercury_in_house_1": ["mental agility", "communication", "youthful", "versatile", "curious", "adaptability"],
    "mercury_in_house_2": ["financially astute", "practical", "resourceful", "detailed", "materialistic", "observant"],
    "mercury_in_house_3": ["communicative", "inquisitive", "versatile", "learning", "restless", "adaptable"],
    "mercury_in_house_4": ["familial", "nostalgic", "sentimental", "practical", "domestic", "shrewd"],
    "mercury_in_house_5": ["creative", "dramatic", "playful", "romantic", "communicative", "spontaneous"],
    "mercury_in_house_6": ["analytical", "practical", "problem-solver", "detailed", "critical", "health-conscious"],
    "mercury_in_house_7": ["communicative", "harmonious", "diplomatic", "partner-oriented", "relational", "fair"],
    "mercury_in_house_8": ["intuitive", "deep-thinking", "psychological", "mysterious", "skeptical", "suspicious"],
    "mercury_in_house_9": ["philosophical", "explorative", "expansive", "travel-loving", "optimistic", "educational"],
    "mercury_in_house_10": ["strategic", "ambitious", "career-driven", "professional", "focused", "intellectual"],
    "mercury_in_house_11": ["innovative", "unconventional", "collaborative", "networking", "progressive", "visionary"],
    "mercury_in_house_12": ["introspective", "imaginative", "dreamy", "mystical", "unconscious", "meditative"]
}
venus_in_house = {
    "venus_in_house_1": ["attractive", "charming", "harmonious", "diplomatic", "graceful", "artistic"],
    "venus_in_house_2": ["financially indulgent", "materialistic", "pleasure-seeking", "sensual", "romantic", "possessive"],
    "venus_in_house_3": ["charming", "communicative", "versatile", "social", "inquisitive", "literary"],
    "venus_in_house_4": ["homely", "nurturing", "family-oriented", "sentimental", "artistic", "decorative"],
    "venus_in_house_5": ["romantic", "creative", "playful", "luxurious", "dramatic", "flirtatious"],
    "venus_in_house_6": ["service-oriented", "health-conscious", "organized", "detail-oriented", "helpful", "harmonious"],
    "venus_in_house_7": ["harmonious", "diplomatic", "relational", "charming", "artistic", "partnership-oriented"],
    "venus_in_house_8": ["intense", "emotional", "passionate", "erotic", "transformational", "mysterious"],
    "venus_in_house_9": ["philosophical", "adventurous", "expansive", "optimistic", "travel-loving", "educational"],
    "venus_in_house_10": ["career-oriented", "professional", "ambitious", "status-conscious", "diplomatic", "artistic"],
    "venus_in_house_11": ["social", "charismatic", "idealistic", "innovative", "friendly", "progressive"],
    "venus_in_house_12": ["mystical", "dreamy", "romantic", "artistic", "unconscious", "compassionate"]
}
mars_in_house = {
    "mars_in_house_1": ["energetic", "assertive", "courageous", "pioneering", "self-reliant", "adventurous"],
    "mars_in_house_2": ["driven", "ambitious", "materialistic", "resourceful", "determined", "competitive"],
    "mars_in_house_3": ["communicative", "energetic", "argumentative", "restless", "inquisitive", "assertive"],
    "mars_in_house_4": ["emotional", "protective", "aggressive", "defensive", "patriotic", "territorial"],
    "mars_in_house_5": ["creative", "passionate", "dramatic", "fiery", "romantic", "competitive"],
    "mars_in_house_6": ["hard-working", "efficient", "productive", "critical", "health-conscious", "analytical"],
    "mars_in_house_7": ["assertive", "independent", "competitive", "energetic", "adventurous", "aggressive"],
    "mars_in_house_8": ["intense", "transformative", "sexual", "powerful", "mysterious", "obsessive"],
    "mars_in_house_9": ["adventurous", "philosophical", "optimistic", "energetic", "expansive", "fiery"],
    "mars_in_house_10": ["ambitious", "competitive", "driven", "powerful", "determined", "authoritative"],
    "mars_in_house_11": ["innovative", "unconventional", "rebellious", "energetic", "original", "impulsive"],
    "mars_in_house_12": ["introspective", "emotional", "secretive", "withdrawn", "spiritual", "mysterious"]
}
jupiter_in_house = {
    "jupiter_in_house_1": ["optimistic", "confident", "expansive", "generous", "philosophical", "adventurous"],
    "jupiter_in_house_2": ["prosperous", "abundant", "optimistic", "generous", "indulgent", "expansive"],
    "jupiter_in_house_3": ["intellectual", "curious", "communicative", "expansive", "insightful", "philosophical"],
    "jupiter_in_house_4": ["home-loving", "family-oriented", "generous", "protective", "nurturing", "prosperous"],
    "jupiter_in_house_5": ["creative", "romantic", "generous", "dramatic", "fun-loving", "optimistic"],
    "jupiter_in_house_6": ["health-conscious", "efficient", "productive", "helpful", "analytical", "generous"],
    "jupiter_in_house_7": ["diplomatic", "harmonious", "just", "generous", "optimistic", "expansive"],
    "jupiter_in_house_8": ["transformative", "intense", "mysterious", "prosperous", "regenerative", "generous"],
    "jupiter_in_house_9": ["adventurous", "expansive", "philosophical", "optimistic", "cultural", "generous"],
    "jupiter_in_house_10": ["professional", "career-oriented", "ambitious", "generous", "authoritative", "prosperous"],
    "jupiter_in_house_11": ["friendly", "optimistic", "innovative", "philanthropic", "expansive", "generous"],
    "jupiter_in_house_12": ["mystical", "introspective", "generous", "compassionate", "spiritual", "philanthropic"]
}
saturn_in_house = {
    "saturn_in_house_1": ["disciplined", "responsible", "hard-working", "serious", "practical", "self-critical"],
    "saturn_in_house_2": ["practical", "realistic", "disciplined", "patient", "responsible", "cautious"],
    "saturn_in_house_3": ["thoughtful", "analytical", "serious", "practical", "realistic", "cautious"],
    "saturn_in_house_4": ["family-oriented", "traditional", "dutiful", "responsible", "serious", "cautious"],
    "saturn_in_house_5": ["disciplined", "reserved", "serious", "practical", "cautious", "self-critical"],
    "saturn_in_house_6": ["efficient", "productive", "hard-working", "serious", "responsible", "self-critical"],
    "saturn_in_house_7": ["committed", "serious", "reliable", "responsible", "practical", "cautious"],
    "saturn_in_house_8": ["intense", "transformative", "mysterious", "responsible", "serious", "cautious"],
    "saturn_in_house_9": ["philosophical", "serious", "disciplined", "responsible", "practical", "cautious"],
    "saturn_in_house_10": ["professional", "ambitious", "disciplined", "responsible", "serious", "cautious"],
    "saturn_in_house_11": ["serious", "responsible", "cautious", "disciplined", "reliable", "thoughtful"],
    "saturn_in_house_12": ["introspective", "self-reflective", "serious", "responsible", "practical", "cautious"]
}
uranus_in_house = {
    "uranus_in_house_1": ["independent", "unique", "unconventional", "rebellious", "innovative", "progressive"],
    "uranus_in_house_2": ["unorthodox", "unconventional", "original", "radical", "innovative", "progressive"],
    "uranus_in_house_3": ["innovative", "inquisitive", "original", "unconventional", "independent", "eccentric"],
    "uranus_in_house_4": ["non-traditional", "unconventional", "rebellious", "eccentric", "innovative", "progressive"],
    "uranus_in_house_5": ["creative", "original", "unconventional", "eccentric", "innovative", "progressive"],
    "uranus_in_house_6": ["unpredictable", "unconventional", "original", "independent", "innovative", "eccentric"],
    "uranus_in_house_7": ["unconventional", "original", "independent", "eccentric", "innovative", "progressive"],
    "uranus_in_house_8": ["transformative", "unconventional", "original", "eccentric", "innovative", "progressive"],
    "uranus_in_house_9": ["unconventional", "independent", "progressive", "original", "innovative", "eccentric"],
    "uranus_in_house_10": ["unconventional", "original", "independent", "innovative", "progressive", "eccentric"],
    "uranus_in_house_11": ["progressive", "innovative", "unconventional", "independent", "eccentric", "original"],
    "uranus_in_house_12": ["original", "intuitive", "unconventional", "eccentric", "innovative", "progressive"]
}
neptune_in_house = {
    "neptune_in_house_1": ["mystical", "dreamy", "sensitive", "creative", "idealistic", "intuitive"],
    "neptune_in_house_2": ["dreamy", "imaginative", "romantic", "artistic", "sensitive", "idealistic"],
    "neptune_in_house_3": ["intuitive", "spiritual", "psychic", "dreamy", "imaginative", "artistic"],
    "neptune_in_house_4": ["sensitive", "psychic", "dreamy", "imaginative", "spiritual", "intuitive"],
    "neptune_in_house_5": ["creative", "artistic", "sensitive", "romantic", "dreamy", "idealistic"],
    "neptune_in_house_6": ["compassionate", "healing", "spiritual", "psychic", "sensitive", "intuitive"],
    "neptune_in_house_7": ["harmonious", "compassionate", "spiritual", "romantic", "sensitive", "intuitive"],
    "neptune_in_house_8": ["mysterious", "psychic", "transformational", "spiritual", "intuitive", "sensitive"],
    "neptune_in_house_9": ["philosophical", "spiritual", "mystical", "intuitive", "idealistic", "compassionate"],
    "neptune_in_house_10": ["inspirational", "visionary", "spiritual", "intuitive", "creative", "artistic"],
    "neptune_in_house_11": ["idealistic", "compassionate", "spiritual", "intuitive", "creative", "imaginative"],
    "neptune_in_house_12": ["intuitive", "psychic", "spiritual", "sensitive", "dreamy", "mystical"]
}
pluto_in_house = {
    "pluto_in_house_1": ["powerful", "intense", "transformative", "renewal", "rebirth", "regeneration"],
    "pluto_in_house_2": ["resourceful", "self-reliant", "determined", "persistent", "financially savvy", "intense"],
    "pluto_in_house_3": ["penetrating", "investigative", "research-oriented", "perceptive", "intense", "transformative"],
    "pluto_in_house_4": ["deeply emotional", "transformative", "renewal", "rebirth", "regeneration", "intense"],
    "pluto_in_house_5": ["creative", "passionate", "dramatic", "intense", "transformative", "regenerative"],
    "pluto_in_house_6": ["healing", "transformational", "intense", "purifying", "regenerative", "self-improvement"],
    "pluto_in_house_7": ["intense", "powerful", "transformative", "regenerative", "renewal", "rebirth"],
    "pluto_in_house_8": ["transformational", "regenerative", "intense", "mystical", "renewal", "rebirth"],
    "pluto_in_house_9": ["transformative", "expansive", "renewal", "rebirth", "regeneration", "intense"],
    "pluto_in_house_10": ["intense", "powerful", "transformative", "regenerative", "renewal", "rebirth"],
    "pluto_in_house_11": ["intense", "transformative", "regenerative", "renewal", "rebirth", "spiritual"],
    "pluto_in_house_12": ["intuitive", "psychic", "transformative", "regenerative", "renewal", "rebirth"]
}
### ASPECTS
aspect_dict = {
    'conjunction': ['unity', 'intensity', 'merging', 'fusion', 'amplification', 'synchronicity', 'shared goals', 'joint creativity'],
    'square': ['challenges', 'obstacles', 'frustration', 'conflict', 'crisis', 'growth', 'change', 'self-reflection'],
    'sextile': ['harmony', 'opportunity', 'cooperation', 'balance', 'mutual support', 'creativity', 'new beginnings', 'growth'],
    'trine': ['ease', 'flow', 'support', 'harmony', 'alignment', 'blessings', 'opportunities', 'manifestation'],
    'opposition': ['duality', 'polarization', 'projection', 'awareness', 'balance', 'integration', 'reconciliation', 'compromise']
}
### RETROGRADRE PLANET
retrograde_dict = {
    'mercury_retrograde': ['miscommunication', 'delays', 'revisiting', 'reflection', 're-evaluation', 'clarity', 'technology', 'frustration'],
    'venus_retrograde': ['re-evaluation', 'self-worth', 'healing', 'reconnecting', 'creativity', 'artistry', 'finances', 'relationships'],
    'mars_retrograde': ['frustration', 'introspection', 'patience', 'repressed', 'revisiting', 'strategy', 'energy', 'motivation'],
    'jupiter_retrograde': ['self-examination', 'opportunities', 'spiritual', 'progress', 'philosophy', 'growth', 'travel', 'beliefs'],
    'saturn_retrograde': ['accountability', 'limitations', 'challenges', 'resilience', 'lessons', 'maturity', 'fears', 'responsibility'],
    'uranus_retrograde': ['rebellion', 'disruption', 'innovation', 'independence', 'awakening', 'change', 'freedom', 'inspiration']
}
