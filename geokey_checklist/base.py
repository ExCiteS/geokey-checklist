from model_utils import Choices

TYPE = Choices('Home', 'Work', 'School', 'PlaceOfWorship', 'Vehicle', 'Blank')
ITEM_TYPE = Choices('Essential', 'Useful', 'Personal', 'Fixit' 'Children', 'Toddlers', 'Infants', 'Pets', 'Custom')
FREQUENCY_EXPIRED_REMINDER = Choices('once', 'twice', 'never')
REMINDER_BEFORE_EXPIRATION = Choices('one_week', 'one_day', 'never')
