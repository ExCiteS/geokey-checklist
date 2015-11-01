from model_utils import Choices

TYPE = Choices(
    ('Home', 'Home'),
    ('Work', 'Work'),
    ('School', 'School'),
    ('PlaceOfWorship', 'Place of Worship'),
    ('Vehicle', 'Vehicle'),
    ('Blank', 'Blank')
)

ITEM_TYPE = Choices(
    ('Essential', 'Essential'),
    ('Useful', 'Useful'),
    ('Personal', 'Personal'),
    ('Fixit', 'Fix It'),
    ('Children', 'Children'),
    ('Toddlers', 'Toddlers'),
    ('Infants', 'Infants'),
    ('Pets', 'Pets'),
    ('Custom', 'Custom')
)

EXPIRY_FACTOR = Choices(
    ('-1', 'Yesterday'),
    ('30', 'One Month'),
    ('60', 'Two Months'),
    ('90', 'Three Months'),
    ('180', 'Six Months'),
    ('270', 'Nine Months'),
    ('365', 'One Year'),
    ('730', 'Two Years'),
    ('1825', 'Five Years'),
    ('999999', 'Never')
)

PER_TYPE = Choices(
    ('individual', 'Per Individual'),
    ('location', 'Per Location')
)

FREQUENCY_EXPIRED_REMINDER = Choices(
    ('once', 'once'),
    ('twice', 'twice'),
    ('never', 'never')
)

REMINDER_BEFORE_EXPIRATION = Choices(
    (180, 'six_months', 'six months'),
    (90, 'three_months', 'three months'),
    (30, 'one_month', 'one month'),
    (7, 'one_week', 'one week'),
    (1, 'one_day', 'one day'),
    (999999, 'never', 'never')
)

DEFAULT_ITEMS = [

{'checklisttype':'Home','name':'Toys (Children)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Children','quantityfactor':'1','pertype':'individual','quantityunit':'toy','expiryfactor':'365'},
{'checklisttype':'Home','name':'Snacks (Children)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Children','quantityfactor':'7','pertype':'individual','quantityunit':'snacks','expiryfactor':'180'},
{'checklisttype':'Home','name':'Warm Clothes (Children)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Children','quantityfactor':'7','pertype':'individual','quantityunit':'clothes','expiryfactor':'180'},
{'checklisttype':'Home','name':'Sturdy Shoes (Adults)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Children','quantityfactor':'1','pertype':'individual','quantityunit':'pair','expiryfactor':'180'},
{'checklisttype':'Home','name':'Coats (Children)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Children','quantityfactor':'1','pertype':'individual','quantityunit':'coat','expiryfactor':'180'},
{'checklisttype':'Home','name':'Comfort Items (Children)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Children','quantityfactor':'1','pertype':'individual','quantityunit':'item(s)','expiryfactor':'180'},
{'checklisttype':'Home','name':'Warm Blanket (Adults)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Children','quantityfactor':'1','pertype':'individual','quantityunit':'blanket(s)','expiryfactor':'180'},
{'checklisttype':'Home','name':'Non-perishable food','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'7','pertype':'individual','quantityunit':'days','expiryfactor':'180'},
{'checklisttype':'Home','name':'Water','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'7','pertype':'individual','quantityunit':'gallons','expiryfactor':'180'},
{'checklisttype':'Home','name':'First Aid Kit - Large','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'location','quantityunit':'large kit','expiryfactor':'180'},
{'checklisttype':'Home','name':'Flashlight & batteries (unless wind-up)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'individual','quantityunit':'flashlight','expiryfactor':'180'},
{'checklisttype':'Home','name':'Lantern ','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'location','quantityunit':'lantern','expiryfactor':'180'},
{'checklisttype':'Home','name':'Camping Stove / Propane BBQ','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'location','quantityunit':'stove','expiryfactor':'180'},
{'checklisttype':'Home','name':'Radio (wind-up or with extra batteries)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'radio','expiryfactor':'180'},
{'checklisttype':'Home','name':'Emergency Phone Number List','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'location','quantityunit':'list','expiryfactor':'180'},
{'checklisttype':'Home','name':'Bar soap','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'individual','quantityunit':'bar','expiryfactor':'365'},
{'checklisttype':'Home','name':'Hand Sanitizer','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'individual','quantityunit':'large pump bottle','expiryfactor':'365'},
{'checklisttype':'Home','name':'Paper Towels','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'individual','quantityunit':'roll','expiryfactor':'730'},
{'checklisttype':'Home','name':'Make it Through List','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'location','quantityunit':'list','expiryfactor':'365'},
{'checklisttype':'Home','name':'Manual Can Opener','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'location','quantityunit':'opener','expiryfactor':'365'},
{'checklisttype':'Home','name':'Fire Extinguisher','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'location','quantityunit':'extinguisher','expiryfactor':'365'},
{'checklisttype':'Home','name':'Wrench or Gas Shut-Off tool','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'location','quantityunit':'tool','expiryfactor':'365'},
{'checklisttype':'Home','name':'Waterproof Matches or Magnesium Fire Starter','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'location','quantityunit':'box','expiryfactor':'365'},
{'checklisttype':'Home','name':'Formula','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'7','pertype':'individual','quantityunit':'days','expiryfactor':'180'},
{'checklisttype':'Home','name':'Diapers','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'42','pertype':'individual','quantityunit':'diapers','expiryfactor':'180'},
{'checklisttype':'Home','name':'Baby Wipes (Infants)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'2','pertype':'individual','quantityunit':'packs','expiryfactor':'180'},
{'checklisttype':'Home','name':'Baby Food','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'7','pertype':'individual','quantityunit':'days','expiryfactor':'180'},
{'checklisttype':'Home','name':'Diaper Rash Ointment (Infants)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'1','pertype':'individual','quantityunit':'tube','expiryfactor':'180'},
{'checklisttype':'Home','name':'Toys (Infants)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'1','pertype':'individual','quantityunit':'toy','expiryfactor':'180'},
{'checklisttype':'Home','name':'Warm Clothes (Infants)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'7','pertype':'individual','quantityunit':'pieces of clothing','expiryfactor':'180'},
{'checklisttype':'Home','name':'Sturdy Shoes (Infants)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'1','pertype':'individual','quantityunit':'pair','expiryfactor':'180'},
{'checklisttype':'Home','name':'Coats (Infants)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'1','pertype':'individual','quantityunit':'coat','expiryfactor':'180'},
{'checklisttype':'Home','name':'Comfort Items (Infants)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'1','pertype':'individual','quantityunit':'item','expiryfactor':'180'},
{'checklisttype':'Home','name':'Pacifier','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'2','pertype':'individual','quantityunit':'pacifiers','expiryfactor':'180'},
{'checklisttype':'Home','name':'Bottles','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'1','pertype':'individual','quantityunit':'bottles','expiryfactor':'180'},
{'checklisttype':'Home','name':'Warm Blanket (Infants)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'1','pertype':'individual','quantityunit':'blanket(s)','expiryfactor':'180'},
{'checklisttype':'Home','name':'Nursing Items (e.g. nursing pads, nipple cream/shield)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Infants','quantityfactor':'1','pertype':'location','quantityunit':'item','expiryfactor':'180'},
{'checklisttype':'Home','name':'Feminine Hygiene Products','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Personal','quantityfactor':'1','pertype':'individual','quantityunit':'box','expiryfactor':'180'},
{'checklisttype':'Home','name':'Birth Control','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Personal','quantityfactor':'1','pertype':'individual','quantityunit':'month supply','expiryfactor':'365'},
{'checklisttype':'Home','name':'Prescription Medication & Glasses','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Personal','quantityfactor':'1','pertype':'individual','quantityunit':'month supply','expiryfactor':'365'},
{'checklisttype':'Home','name':'Games','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Personal','quantityfactor':'1','pertype':'individual','quantityunit':'game','expiryfactor':'365'},
{'checklisttype':'Home','name':'Personal Documents','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Personal','quantityfactor':'1','pertype':'individual','quantityunit':'file','expiryfactor':'365'},
{'checklisttype':'Home','name':'Books','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Personal','quantityfactor':'1','pertype':'individual','quantityunit':'book','expiryfactor':'365'},
{'checklisttype':'Home','name':'Litter box, litter, litter scoop and garbage bags','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Pets','quantityfactor':'1','pertype':'individual','quantityunit':'clean-up supply','expiryfactor':'365'},
{'checklisttype':'Home','name':'Sturdy leashes, harnesses and carriers','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Pets','quantityfactor':'1','pertype':'individual','quantityunit':'leash & carrier','expiryfactor':'365'},
{'checklisttype':'Home','name':'Collar and Licensing Tags','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Pets','quantityfactor':'1','pertype':'individual','quantityunit':'item','expiryfactor':'365'},
{'checklisttype':'Home','name':'Toys (Pets)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Pets','quantityfactor':'1','pertype':'individual','quantityunit':'toy','expiryfactor':'365'},
{'checklisttype':'Home','name':'Pet Food','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Pets','quantityfactor':'7','pertype':'individual','quantityunit':'days','expiryfactor':'365'},
{'checklisttype':'Home','name':'Water (Pets)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Pets','quantityfactor':'1','pertype':'individual','quantityunit':'gallon(s)','expiryfactor':'365'},
{'checklisttype':'Home','name':'Medication, medical records and veterinarian\'s details','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Pets','quantityfactor':'1','pertype':'individual','quantityunit':'month supply','expiryfactor':'365'},
{'checklisttype':'Home','name':'Current photo & description of your pets','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Pets','quantityfactor':'1','pertype':'individual','quantityunit':'photo/description','expiryfactor':'365'},
{'checklisttype':'Home','name':'Diapers / Pull-ups','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Toddlers','quantityfactor':'21','pertype':'individual','quantityunit':'diapers','expiryfactor':'180'},
{'checklisttype':'Home','name':'Baby Wipes (Toddlers)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Toddlers','quantityfactor':'1','pertype':'individual','quantityunit':'pack(s)','expiryfactor':'180'},
{'checklisttype':'Home','name':'Diaper Rash Ointment (Toddlers)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Toddlers','quantityfactor':'1','pertype':'individual','quantityunit':'tube','expiryfactor':'180'},
{'checklisttype':'Home','name':'Toys (Toddlers)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Toddlers','quantityfactor':'1','pertype':'individual','quantityunit':'toy','expiryfactor':'180'},
{'checklisttype':'Home','name':'Snacks (Toddlers)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Toddlers','quantityfactor':'14','pertype':'individual','quantityunit':'snack','expiryfactor':'180'},
{'checklisttype':'Home','name':'Warm Clothes (Toddlers)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Toddlers','quantityfactor':'7','pertype':'individual','quantityunit':'outfits','expiryfactor':'180'},
{'checklisttype':'Home','name':'Sturdy Shoes (Toddlers)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Toddlers','quantityfactor':'1','pertype':'individual','quantityunit':'pair','expiryfactor':'180'},
{'checklisttype':'Home','name':'Coats (Toddlers)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Toddlers','quantityfactor':'1','pertype':'individual','quantityunit':'coat','expiryfactor':'180'},
{'checklisttype':'Home','name':'Comfort Items (Toddlers)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Toddlers','quantityfactor':'1','pertype':'individual','quantityunit':'item','expiryfactor':'180'},
{'checklisttype':'Home','name':'Warm Blanket (Toddlers)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Toddlers','quantityfactor':'1','pertype':'individual','quantityunit':'blanket(s)','expiryfactor':'180'},
{'checklisttype':'Home','name':'Wood','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':' month supply','expiryfactor':'365'},
{'checklisttype':'Home','name':'Cash','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'100','pertype':'location','quantityunit':'dollars','expiryfactor':'180'},
{'checklisttype':'Home','name':'Tent','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'item','expiryfactor':'365'},
{'checklisttype':'Home','name':'Tarp','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'item','expiryfactor':'365'},
{'checklisttype':'Home','name':'Warm Clothes (Adults)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'2','pertype':'individual','quantityunit':'outfit','expiryfactor':'365'},
{'checklisttype':'Home','name':'Tools','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'toolbox','expiryfactor':'365'},
{'checklisttype':'Home','name':'Phone Charger (including USB)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'individual','quantityunit':'charger','expiryfactor':'365'},
{'checklisttype':'Home','name':'Underwear','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'individual','quantityunit':'pack','expiryfactor':'365'},
{'checklisttype':'Home','name':'Batteries','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'variety pack','expiryfactor':'365'},
{'checklisttype':'Vehicle','name':'Jumper Cables','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'set','expiryfactor':'730'},
{'checklisttype':'Vehicle','name':'Seat Belt Cutter','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'tool','expiryfactor':'730'},
{'checklisttype':'Vehicle','name':'Power Inverter','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'tool','expiryfactor':'365'},
{'checklisttype':'Vehicle','name':'Window Breaker','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'tool','expiryfactor':'730'},
{'checklisttype':'Vehicle','name':'Snacks (Vehicle)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'7','pertype':'individual','quantityunit':'snacks','expiryfactor':'180'},
{'checklisttype':'Vehicle','name':'Warm Blanket (Vehicle)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'individual','quantityunit':'blanket(s)','expiryfactor':'180'},
{'checklisttype':'Vehicle','name':'Coats (Vehicle)','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'individual','quantityunit':'jacket','expiryfactor':'180'},
{'checklisttype':'Vehicle','name':'Paper Map','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'map','expiryfactor':'365'},
{'checklisttype':'Vehicle','name':'Flares','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'set','expiryfactor':'365'},
{'checklisttype':'Home','name':'Whistle','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'individual','quantityunit':'whistle','expiryfactor':'365'},
{'checklisttype':'Home','name':'Shovel','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'shovel','expiryfactor':'365'},
{'checklisttype':'Home','name':'Bucket','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'bucket','expiryfactor':'365'},
{'checklisttype':'Home','name':'Heavy Duty Trashbags','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Useful','quantityfactor':'1','pertype':'location','quantityunit':'box','expiryfactor':'365'},
{'checklisttype':'Home','name':'Toilet Paper','checklistitemdescription':'','checklistitemurl':'','checklistitemtype':'Essential','quantityfactor':'1','pertype':'individual','quantityunit':'roll','expiryfactor':'365'}

]
