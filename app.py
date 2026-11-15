from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Database of 15 Rural Artisan & Skill Categories (English, Hindi, Telugu)
JOB_PROFILES = [
    {
        "keywords": ["tailor", "tailoring", "stitch", "suit", "blouse", "silai", "darzi", "kapde", "కుట్టుపని", "రవికె", "బట్టలు"],
        "craft_category": "Tailoring & Garment Making (సంప్రదాయ కుట్టుపని)",
        "item_name": "Custom Blouses, Suits & School Uniforms",
        "suggested_hourly_wage": 65,
        "recommended_complexity": 1.4,
        "target_buyers": "Local Boutiques, Schools & Retail Customers"
    },
    {
        "keywords": ["embroidery", "kadhai", "zardosi", "maggam", "aari", "mirror work", "అద్దకం", "మగ్గం", "కడాయి"],
        "craft_category": "Hand Embroidery & Maggam Work (మగ్గం & ఎంబ్రాయిడరీ)",
        "item_name": "Bridal Blouses, Saree Borders & Embroidered Dupattas",
        "suggested_hourly_wage": 85,
        "recommended_complexity": 1.8,
        "target_buyers": "Fashion Designers, Wedding Boutiques & Export Houses"
    },
    {
        "keywords": ["cook", "cooking", "chef", "kitchen", "food", "meal", "khana", "rasoi", "tiffin", "వంట", "వంటలు", "భోజనం"],
        "craft_category": "Home-Cooked Meals & Catering (గృహ వంటకాలు & క్యాటరింగ్)",
        "item_name": "Daily Tiffin Boxes, Millet Meals & Festive Catering",
        "suggested_hourly_wage": 60,
        "recommended_complexity": 1.3,
        "target_buyers": "Students, Working Professionals & Local Offices"
    },
    {
        "keywords": ["pickle", "papad", "achar", "pachadi", "snack", "sweet", "laddu", "pindi vantalu", "పచ్చడి", "పిండివంటలు", "అప్పడాలు"],
        "craft_category": "Pickles, Papads & Traditional Snacks (పచ్చళ్లు & పిండివంటలు)",
        "item_name": "Sun-Dried Papads, Mango/Gongura Pickles & Festive Sweets",
        "suggested_hourly_wage": 60,
        "recommended_complexity": 1.4,
        "target_buyers": "Organic Stores, Supermarkets & Bulk Corporate Gifting"
    },
    {
        "keywords": ["weave", "weaving", "handloom", "saree", "loom", "bunkar", "bunai", "నేత", "చేనేత", "చీర"],
        "craft_category": "Handloom & Textile Weaving (చేనేత వస్త్రాలు)",
        "item_name": "Pochampally Ikat, Handloom Cotton Sarees & Stoles",
        "suggested_hourly_wage": 80,
        "recommended_complexity": 1.7,
        "target_buyers": "Handloom Emporiums, Ethical Fashion Brands & Online Buyers"
    },
    {
        "keywords": ["pottery", "clay", "pot", "terracotta", "diya", "kumhar", "mitti", "కుండలు", "మట్టి", "దీపాలు"],
        "craft_category": "Pottery & Terracotta Crafts (కుమ్మరి & మట్టి కళాఖండాలు)",
        "item_name": "Earthen Water Pots, Festive Diyas & Terracotta Planters",
        "suggested_hourly_wage": 65,
        "recommended_complexity": 1.5,
        "target_buyers": "Nurseries, Eco-Friendly Home Decor Stores & Event Planners"
    },
    {
        "keywords": ["bamboo", "basket", "cane", "mat", "chatai", "bans", "tokri", "వెదురు", "బుట్టలు", "చాపలు"],
        "craft_category": "Bamboo & Cane Weaving (వెదురు & పేము కళలు)",
        "item_name": "Handwoven Storage Baskets, Bamboo Lamps & Floor Mats",
        "suggested_hourly_wage": 60,
        "recommended_complexity": 1.4,
        "target_buyers": "Eco-Resorts, Interior Designers & Zero-Waste Stores"
    },
    {
        "keywords": ["wood", "carpenter", "carving", "toy", "wooden", "lakdi", "badhai", "చెక్క", "బొమ్మలు", "వడ్రంగి"],
        "craft_category": "Wood Carving & Wooden Toys (చెక్క బొమ్మలు & శిల్పకళ)",
        "item_name": "Etikoppaka Lacquer Toys, Carved Wall Panels & Kitchen Utensils",
        "suggested_hourly_wage": 80,
        "recommended_complexity": 1.7,
        "target_buyers": "Toy Stores, Cultural Museums & Corporate Gift Buyers"
    },
    {
        "keywords": ["jewelry", "jewellery", "bangle", "bead", "terracotta jewelry", "gahu", "chudi", "గాజులు", "ఆభరణాలు"],
        "craft_category": "Handmade & Terracotta Jewelry (చేతితో చేసిన ఆభరణాలు)",
        "item_name": "Hand-Painted Terracotta Necklaces, Lac Bangles & Thread Earrings",
        "suggested_hourly_wage": 70,
        "recommended_complexity": 1.5,
        "target_buyers": "College Boutiques, Festive Pop-ups & E-Commerce Marketplaces"
    },
    {
        "keywords": ["paint", "painting", "kalamkari", "madhubani", "warli", "art", "chitrakari", "కలంకారీ", "చిత్రలేఖనం"],
        "craft_category": "Traditional Folk Painting (సంప్రదాయ చిత్రలేఖనం - కలంకారీ)",
        "item_name": "Kalamkari Hand-Painted Dupattas, Wall Hangings & Canvas Art",
        "suggested_hourly_wage": 85,
        "recommended_complexity": 1.8,
        "target_buyers": "Art Galleries, Hotels & Apparel Brands"
    },
    {
        "keywords": ["soap", "candle", "agarbatti", "incense", "herbal", "oil", "dhoop", "sabun", "సబ్బులు", "అగరబత్తులు"],
        "craft_category": "Herbal Soaps, Candles & Incense (హెర్బల్ సబ్బులు & అగరబత్తులు)",
        "item_name": "Neem & Turmeric Handmade Soaps, Bamboo-less Agarbatti & Soy Candles",
        "suggested_hourly_wage": 55,
        "recommended_complexity": 1.2,
        "target_buyers": "Wellness Stores, Temples & Subscription Gift Boxes"
    },
    {
        "keywords": ["jute", "bag", "crochet", "knitting", "macrame", "buna", "thaila", "జనపనార", "సంచులు", "అల్లిక"],
        "craft_category": "Jute Bags, Crochet & Macrame (జనపనార సంచులు & అల్లికలు)",
        "item_name": "Printed Jute Tote Bags, Crochet Toys & Macrame Plant Hangers",
        "suggested_hourly_wage": 60,
        "recommended_complexity": 1.3,
        "target_buyers": "Conference Organizers, Retail Chains & Home Decor Shops"
    },
    {
        "keywords": ["leather", "chappal", "footwear", "sandal", "kolhapuri", "chamda", "joota", "చెప్పులు", "తోలు"],
        "craft_category": "Handcrafted Leather Footwear (చేతితో చేసిన చెప్పులు)",
        "item_name": "Traditional Kolhapuri Sandals & Embroidered Leather Mojris",
        "suggested_hourly_wage": 75,
        "recommended_complexity": 1.6,
        "target_buyers": "Ethnic Footwear Brands & Online Fashion Stores"
    },
    {
        "keywords": ["farm", "farming", "honey", "mushroom", "spice", "turmeric", "organic", "kheti", "shahad", "తేనె", "పుట్టగొడుగులు", "పసుపు"],
        "craft_category": "Organic Farming & Agro-Processing (సేంద్రీయ వ్యవసాయ ఉత్పత్తులు)",
        "item_name": "Raw Forest Honey, Oyster Mushrooms & Cold-Ground Turmeric Powder",
        "suggested_hourly_wage": 60,
        "recommended_complexity": 1.3,
        "target_buyers": "Organic Grocery Chains, Restaurants & Direct-to-Home Buyers"
    },
    {
        "keywords": ["beauty", "mehendi", "henna", "parlour", "makeup", "bridal", "మెహందీ", "బ్యూటీ"],
        "craft_category": "Mehendi Art & Rural Beauty Services (మెహందీ & బ్యూటీ సేవలు)",
        "item_name": "Organic Bridal Mehendi Cones & Festive Henna Application",
        "suggested_hourly_wage": 75,
        "recommended_complexity": 1.5,
        "target_buyers": "Wedding Families, Event Organizers & Local Salons"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calculate-price', methods=['POST'])
def calculate_price():
    data = request.json
    try:
        material_cost = float(data.get('material_cost', 0))
        labor_hours = float(data.get('labor_hours', 0))
        complexity = float(data.get('complexity', 1.0))
        base_hourly_wage = float(data.get('hourly_wage', 60.0))

        labor_compensation = labor_hours * base_hourly_wage * complexity
        artisan_payout = material_cost + labor_compensation
        retail_price = artisan_payout * 1.05  # 5% platform upkeep fee
        platform_fee = retail_price - artisan_payout
        margin = (labor_compensation / artisan_payout) * 100 if artisan_payout > 0 else 0

        return jsonify({
            "status": "success",
            "material_cost_inr": round(material_cost, 2),
            "labor_compensation_inr": round(labor_compensation, 2),
            "artisan_payout_inr": round(artisan_payout, 2),
            "platform_fee_inr": round(platform_fee, 2),
            "retail_price_inr": round(retail_price, 2),
            "artisan_margin_percentage": round(margin, 1)
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/api/parse-voice', methods=['POST'])
def parse_voice():
    data = request.json
    transcript = data.get('transcript', '').lower()

    matched_job = None
    for job in JOB_PROFILES:
        if any(word in transcript for word in job["keywords"]):
            matched_job = job
            break

    if not matched_job:
        matched_job = {
            "craft_category": "General Village Handicrafts (గ్రామీణ హస్తకళలు)",
            "item_name": "Custom Handmade Artisan Product",
            "suggested_hourly_wage": 60,
            "recommended_complexity": 1.3,
            "target_buyers": "Local Markets & Online Craft Buyers"
        }

    return jsonify({
        "status": "success",
        "parsed_profile": {
            "spoken_text": data.get('transcript', ''),
            "craft_category": matched_job["craft_category"],
            "item_name": matched_job["item_name"],
            "suggested_hourly_wage": matched_job["suggested_hourly_wage"],
            "recommended_complexity": matched_job["recommended_complexity"],
            "target_buyers": matched_job["target_buyers"],
            "verified": True
        }
    })

if __name__ == '__main__':
    app.run(debug=True)