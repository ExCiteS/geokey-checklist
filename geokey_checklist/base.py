from model_utils import Choices

TYPE = Choices('Home', 'Work', 'School', 'PlaceOfWorship', 'Vehicle', 'Blank')
ITEM_TYPE = Choices('Essential', 'Useful', 'Personal', 'Fixit' 'Children', 'Toddlers', 'Infants', 'Pets', 'Custom')

EXPIRY_FACTOR = Choices(
    ('30', 'One Month'),
    ('60', 'Two Months'),
    ('90', 'Three Months'),
    ('180', 'Six Months'),
    ('210', 'Seven Months'),
    ('240', 'Eight Months'),
    ('270', 'Nine Months'),
    ('300', 'Ten Months'),
    ('330', 'Eleven Months'),
    ('360', 'One Year'),
    ('390', 'One Year, One Month'),
    ('420', 'One Year, Two Months'),
    ('450', 'One Year, Three Months'),
    ('480', 'One Year, Four Months'),
    ('510', 'One Year, Five Months'),
    ('720', 'Two Years')
)

FREQUENCY_EXPIRED_REMINDER = Choices('once', 'twice', 'never')
REMINDER_BEFORE_EXPIRATION = Choices('one_week', 'one_day', 'never')
