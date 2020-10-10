# Foodler(name subject to change)
 - Store recips
 - Store food-stuffs in sql
 - See what can be made out of stuff from home
 - See what needs to be bought to cook a recepie
 - Add/remove recipes
 - Add/remove goods
  
## SQL Tables
- Dry storage
- Fridge
- Freezer
- Spices
- Snacks

## What can I put into classes?
- Kitchen (mother class for all tableclasses)
    - Have functions for calling sql (used by child classes)
- All sql-tables
- cli-loop (CMD)

### Notes for menue loop
- MainMenue
    - Check what you have home
    - Check what you can make
    - Add remove things from storage
    - Add/Check/Remove recipes
    - Make a food (Remove goods from storage)
    - Add things from shopping to storage
- ModifyFoods
    - Add/remove things from storage
    - Exit loop when done to go back to main menue
- ModifyRecipes
    - View/Add/Remove recepies from database
    - Exit loop when done to go back to main menue
