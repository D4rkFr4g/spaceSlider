PROJECT TITLE: spaceSlider
PURPOSE OF PROJECT: Kivy Python Hackathon
VERSION or DATE: 12/27/13
HOW TO START THIS PROJECT: Sideload apk on android device and run Space Slider
AUTHORS: Zane Melcho
USER INSTRUCTIONS:

Swipe Left, Right, Up, or Down to move tile piece
Click Reshuffle to shuffle the puzzle
Click Instant Win to see completed puzzle



Known issues:	
?	Instant Win button closes the app instead of revealing the full image
?	Tile piece can be swiped further then the empty square. Does not however effect where the tile ends up
?	Overall layout sizes isn't scaling appropriately to different screen sizes
?	Dynamic image to tiles function isn't working correctly so feature was disable for the time being
?	Move count doesn't reset when shuffle button is pressed
? Some permutations are unsolvable since it is using a random sort, a better method would be to start from
  the image and shuffle by randomly moving pieces to the empty spot guaranteeing solvability
