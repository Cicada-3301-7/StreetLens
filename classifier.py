from utils import logger

class ShopClassifier:
    def __init__(self):
        logger.info("Initializing Shop Classifier...")
        
        # Enhanced category keywords - more specific
        self.category_map = {
            "real_estate": [
                "real estate", "sale", "purchase", "renting", "rental",
                "residential", "commercial", "industrial", "group housing",
                "property", "land", "plot", "apartment", "flat", "house",
                "builder", "developer", "estate", "realty", "broker",
                "housing", "construction", "project", "societies"
            ],
            "medical": [
                "medical", "pharmacy", "clinic", "chemist", "drugs", "hospital",
                "doctor", "health", "medicine", "diagnostic", "lab", "ayurveda",
                "homeopathy", "physiotherapy", "dental", "optician", "nursing",
                "nursing home", "healthcare", "pathology", "x-ray", "scan"
            ],
            "restaurant": [
                "restaurant", "hotel", "cafe", "bhojanalaya", "dhaba", "food",
                "kitchen", "bar", "pub", "diner", "eatery", "pizzeria",
                "fast food", "chinese", "indian", "continental", "snacks", "juice",
                "bakery cafe", "coffee shop", "tea stall", "canteen"
            ],
            "electronics": [
                "electronics", "mobile", "computer", "gadgets", "appliances",
                "phone", "laptop", "tablet", "camera", "tv", "refrigerator",
                "washing machine", "microwave", "console", "gaming", "store",
                "repair", "service center", "showroom"
            ],
            "bakery": [
                "bakery", "cake", "sweets", "confectionery", "bread", "pastry",
                "donut", "cookie", "biscuit", "dessert", "ice cream", "sweet",
                "bakehouse", "sweet shop", "panjabi", "mithai"
            ],
            "salon": [
                "salon", "beauty", "parlour", "hair", "spa", "unisex", "barber",
                "haircut", "massage", "cosmetics", "makeup", "threading", "waxing",
                "beauty parlor", "hair salon", "wellness"
            ],
            "clothing": [
                "clothing", "apparel", "garments", "dress", "boutique",
                "mens wear", "womens wear", "kids wear", "fashion", "footwear",
                "saree", "suit", "shirt", "fabric", "tailor", "store"
            ],
            "grocery": [
                "grocery", "supermarket", "mart", "store", "provision",
                "fruits", "vegetables", "dairy", "general store", "shop",
                "kirana", "bazaar", "market"
            ],
            "auto_parts": [
                "auto parts", "motor starter", "starter", "panel board",
                "auto start", "control panel", "capacitor", "mex", "mieco",
                "bentex", "keltron", "sunny", "jayki", "neuton", "supplier",
                "dealer", "distributor", "spares", "ignition"
                 ],
            "jewelry": [
                "jewelry", "jewellery", "jeweler", "goldsmith", "ornament",
                "diamond", "gold", "silver", "precious", "store", "shop",
                "sona", "sonaar"
            ],
            "hardware": [
                "hardware", "tools", "equipment", "plumbing", "electrical",
                "paint", "cement", "steel", "iron", "bolt", "nut",
                "construction materials", "supplies"
            ],
            "automotive": [
                "automotive", "car", "bike", "motorcycle", "vehicle", "garage","service", "repair", "showroom", "dealer", "mechanic"
            ],
            "education": [
                "school", "college", "university", "coaching", "classes",
                "academy", "institute", "center", "tutorial", "education",
                "training", "course"
            ],
            "banking": [
                "bank", "banking", "atm", "branch", "finance", "loan",
                "credit", "deposit", "insurance", "financial", "services"
            ],
            "entertainment": [
                "cinema", "theatre", "theater", "movie", "films", "multiplex",
                "gaming", "arcade", "games", "club", "nightclub", "lounge"
            ],
            "fitness": [
                "gym", "fitness", "yoga", "wellness", "sports", "workout",
                "trainer", "aerobics", "zumba", "dance", "health club"
            ],
            "beauty_products": [
                "cosmetics", "skincare", "makeup", "beauty products", "perfume",
                "fragrance", "shampoo", "soap", "cream", "lotion"
            ],
            "stationery": [
                "stationery", "books", "paper", "pen", "notebook", "office",
                "supplies", "printing", "photocopy", "xerox"
            ],
            "furniture": [
                "furniture", "sofa", "bed", "chair", "table", "wardrobe",
                "wooden", "interior", "decor", "home furnish"
            ],
            "toys": [
                "toys", "toy store", "games", "hobby", "collectibles",
                "dolls", "action figures"
            ],
            "travel": [
                "travel", "agency", "tour", "tourism", "airline", "ticket",
                "booking", "vacation", "holiday"
            ],
            "tuition": [
                "tuition", "coaching", "classes", "education", "academy",
                "center", "institute", "training"
            ],
            "restaurant_fast_food": [
                "fast food", "burger", "pizza", "kfc", "dominos", "mcdonalds",
                "quick service", "takeaway", "delivery"
            ],
            "restaurant_chinese": [
                "chinese", "noodles", "chow mein", "momos", "dumpling"
            ],
            "restaurant_north_indian": [
                "north indian", "tandoori", "curry", "paratha", "tandoor",
                "biryani", "kebab"
            ],
            "restaurant_south_indian": [
                "south indian", "dosa", "idli", "sambar", "filter coffee",
                "uttapam"
            ],
            "restaurant_pizza": [
                "pizza", "pizzeria", "italian", "pasta", "cheese"
            ],
            "cafe": [
                "cafe", "coffee", "cafe", "tea", "espresso", "latte",
                "cappuccino", "beverage"
            ],
            "laundry": [
                "laundry", "dry clean", "drycleaning", "wash", "ironing",
                "pressing"
            ],
            "photography": [
                "photography", "studio", "photographer", "photo", "portrait",
                "wedding"
            ],
            "printing": [
                "printing", "print", "press", "newspaper", "magazine",
                "publishing", "photostat"
            ],
            "internet_cafe": [
                "internet cafe", "cyber cafe", "computer center", "broadband",
                "wi-fi"
            ]
        }

    def classify(self, text_lines):
        """Classify shop category using keyword matching with scoring"""
        try:
            full_text = " ".join(text_lines).lower()
            
            logger.info(f"Classifying with text: {full_text[:100]}...")
            
            # Score each category
            category_scores = {}
            
            for category, keywords in self.category_map.items():
                matches = 0
                matched_keywords = []
                
                for keyword in keywords:
                    if keyword in full_text:
                        matches += 1
                        matched_keywords.append(keyword)
                
                if matches > 0:
                    category_scores[category] = {
                        'score': matches,
                        'keywords': matched_keywords
                    }
            
            # If categories found, pick the one with highest matches
            if category_scores:
                best_category = max(category_scores, key=lambda x: category_scores[x]['score'])
                
                logger.info(f"Category scores: {category_scores}")
                logger.info(f"Best category: {best_category} with score {category_scores[best_category]['score']}")
                
                # Format category name
                category_names = {
                    "real_estate": "Real Estate",
                    "medical": "Medical Store",
                    "restaurant": "Restaurant",
                    "electronics": "Electronics Store",
                    "bakery": "Bakery",
                    "salon": "Salon",
                    "auto_parts": "Auto Parts Dealer",
                    "clothing": "Clothing Store",
                    "grocery": "Grocery Store",
                    "jewelry": "Jewelry Store",
                    "hardware": "Hardware Store",
                    "automotive": "Automotive",
                    "education": "Education",
                    "banking": "Banking",
                    "entertainment": "Entertainment",
                    "fitness": "Fitness Center",
                    "beauty_products": "Beauty Products",
                    "stationery": "Stationery Store",
                    "furniture": "Furniture Store",
                    "toys": "Toys Store",
                    "travel": "Travel Agency",
                    "tuition": "Tuition Center",
                    "restaurant_fast_food": "Fast Food",
                    "restaurant_chinese": "Chinese Restaurant",
                    "restaurant_north_indian": "North Indian Restaurant",
                    "restaurant_south_indian": "South Indian Restaurant",
                    "restaurant_pizza": "Pizza Restaurant",
                    "cafe": "Cafe",
                    "laundry": "Laundry",
                    "photography": "Photography Studio",
                    "printing": "Printing Press",
                    "internet_cafe": "Internet Cafe"
                }
                
                return category_names.get(best_category, "General Store")
            
            logger.warning("No category matched, returning General Store")
            return "General Store"

        except Exception as e:
            logger.error(f"Classification failed: {e}")
            return "General Store"